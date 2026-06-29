"""
Host Groups module for Falcon MCP Server.

Provides tools for managing CrowdStrike Falcon host groups and their membership.
"""

from typing import Any

from mcp.server import FastMCP
from mcp.server.fastmcp.resources import TextResource
from mcp.types import ToolAnnotations
from pydantic import AnyUrl, Field

from falcon_mcp.common.errors import _format_error_response
from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule
from falcon_mcp.resources.host_groups import SEARCH_HOST_GROUPS_FQL_DOCUMENTATION

logger = get_logger(__name__)

WRITE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False,
    destructiveHint=False,
    idempotentHint=False,
    openWorldHint=True,
)

DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False,
    destructiveHint=True,
    idempotentHint=True,
    openWorldHint=True,
)


class HostGroupsModule(BaseModule):
    """Module for CrowdStrike Falcon host group management."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.search_host_groups, name="search_host_groups")
        self._add_tool(server=server, method=self.get_host_group_members, name="get_host_group_members")
        self._add_tool(
            server=server,
            method=self.create_host_group,
            name="create_host_group",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server,
            method=self.update_host_group,
            name="update_host_group",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server,
            method=self.delete_host_groups,
            name="delete_host_groups",
            annotations=DESTRUCTIVE_ANNOTATIONS,
        )
        self._add_tool(
            server=server,
            method=self.add_hosts_to_group,
            name="add_hosts_to_group",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server,
            method=self.remove_hosts_from_group,
            name="remove_hosts_from_group",
            annotations=WRITE_ANNOTATIONS,
        )

    def register_resources(self, server: FastMCP) -> None:
        fql_resource = TextResource(
            uri=AnyUrl("falcon://host-groups/search/fql-guide"),
            name="falcon_search_host_groups_fql_guide",
            description="FQL filter guide for the `falcon_search_host_groups` tool.",
            text=SEARCH_HOST_GROUPS_FQL_DOCUMENTATION,
        )
        self._add_resource(server, fql_resource)

    def search_host_groups(
        self,
        filter: str | None = Field(
            default=None,
            description="FQL filter for host group search. See `falcon://host-groups/search/fql-guide`.",
            examples=["name:'Production*'", "group_type:'static'"],
        ),
        limit: int = Field(default=10, ge=1, le=5000, description="Max records to return."),
        offset: int | None = Field(default=None, description="Offset to start from."),
        sort: str | None = Field(
            default=None,
            description="Sort expression (e.g. name.asc, modified_timestamp.desc).",
            examples=["name.asc", "modified_timestamp.desc"],
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search host groups and return full group details."""
        ids = self._base_search_api_call(
            operation="queryHostGroups",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search host groups",
        )

        if self._is_error(ids):
            if filter:
                return self._format_fql_error_response([ids], filter, SEARCH_HOST_GROUPS_FQL_DOCUMENTATION)
            return [ids]

        if not ids:
            if filter:
                return self._format_fql_error_response([], filter, SEARCH_HOST_GROUPS_FQL_DOCUMENTATION)
            return []

        details = self._base_get_by_ids(operation="getHostGroups", ids=ids, use_params=True)
        if self._is_error(details):
            return [details]
        return details

    def get_host_group_members(
        self,
        id: str = Field(description="Host group ID."),
        filter: str | None = Field(default=None, description="Optional FQL filter applied to members."),
        limit: int = Field(default=100, ge=1, le=5000, description="Max members to return."),
        offset: int | None = Field(default=None, description="Offset to start from."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List full host details for hosts that belong to a host group."""
        result = self._base_search_api_call(
            operation="queryCombinedGroupMembers",
            search_params={
                "id": id,
                "filter": filter,
                "limit": limit,
                "offset": offset,
                "sort": sort,
            },
            error_message="Failed to list host group members",
        )
        if self._is_error(result):
            return [result]
        return result

    def create_host_group(
        self,
        name: str = Field(description="Host group name (must be unique within the CID)."),
        group_type: str = Field(
            description="Group type: 'static' (membership by host IDs) or 'dynamic' (membership by FQL rule).",
            examples=["static", "dynamic"],
        ),
        description: str | None = Field(default=None, description="Group description."),
        assignment_rule: str | None = Field(
            default=None,
            description="FQL assignment rule. Required for dynamic groups; ignored for static groups.",
            examples=["platform_name:'Windows'+tags:'production'"],
        ),
    ) -> list[dict[str, Any]]:
        """Create a host group (static or dynamic)."""
        if group_type not in ("static", "dynamic"):
            return [_format_error_response(
                "`group_type` must be 'static' or 'dynamic'.", operation="createHostGroups"
            )]
        if group_type == "dynamic" and not assignment_rule:
            return [_format_error_response(
                "`assignment_rule` is required when group_type='dynamic'.",
                operation="createHostGroups",
            )]

        resource: dict[str, Any] = {"name": name, "group_type": group_type}
        if description:
            resource["description"] = description
        if assignment_rule and group_type == "dynamic":
            resource["assignment_rule"] = assignment_rule

        result = self._base_query_api_call(
            operation="createHostGroups",
            body_params={"resources": [resource]},
            error_message="Failed to create host group",
        )
        if self._is_error(result):
            return [result]
        return result

    def update_host_group(
        self,
        id: str = Field(description="Host group ID to update."),
        name: str | None = Field(default=None, description="New name."),
        description: str | None = Field(default=None, description="New description."),
        assignment_rule: str | None = Field(
            default=None,
            description="New FQL assignment rule (dynamic groups only).",
        ),
    ) -> list[dict[str, Any]]:
        """Update a host group's name, description, or assignment rule."""
        if name is None and description is None and assignment_rule is None:
            return [_format_error_response(
                "Provide at least one of `name`, `description`, or `assignment_rule`.",
                operation="updateHostGroups",
            )]

        resource: dict[str, Any] = {"id": id}
        if name is not None:
            resource["name"] = name
        if description is not None:
            resource["description"] = description
        if assignment_rule is not None:
            resource["assignment_rule"] = assignment_rule

        result = self._base_query_api_call(
            operation="updateHostGroups",
            body_params={"resources": [resource]},
            error_message="Failed to update host group",
        )
        if self._is_error(result):
            return [result]
        return result

    def delete_host_groups(
        self,
        ids: list[str] = Field(description="Host group IDs to delete."),
    ) -> list[dict[str, Any]]:
        """Delete host groups by ID."""
        if not ids:
            return [_format_error_response(
                "`ids` is required.", operation="deleteHostGroups"
            )]
        result = self._base_query_api_call(
            operation="deleteHostGroups",
            query_params={"ids": ids},
            error_message="Failed to delete host groups",
        )
        if self._is_error(result):
            return [result]
        return result

    def add_hosts_to_group(
        self,
        group_id: str = Field(description="Target host group ID (must be a static group)."),
        host_ids: list[str] = Field(description="Host device IDs (AIDs) to add."),
    ) -> list[dict[str, Any]]:
        """Add hosts to a static host group."""
        return self._perform_group_action("add-hosts", group_id, host_ids)

    def remove_hosts_from_group(
        self,
        group_id: str = Field(description="Source host group ID (must be a static group)."),
        host_ids: list[str] = Field(description="Host device IDs (AIDs) to remove."),
    ) -> list[dict[str, Any]]:
        """Remove hosts from a static host group."""
        return self._perform_group_action("remove-hosts", group_id, host_ids)

    def _perform_group_action(
        self, action_name: str, group_id: str, host_ids: list[str]
    ) -> list[dict[str, Any]]:
        if not host_ids:
            return [_format_error_response(
                "`host_ids` is required.", operation=f"performGroupAction:{action_name}"
            )]
        # The add-hosts / remove-hosts action takes the target host AIDs through an
        # FQL filter on device_id, with the host group ID(s) in `ids`.
        device_filter = "device_id:[" + ",".join(f"'{h}'" for h in host_ids) + "]"
        body = {
            "action_parameters": [{"name": "filter", "value": device_filter}],
            "ids": [group_id],
        }
        result = self._base_query_api_call(
            operation="performGroupAction",
            query_params={"action_name": action_name},
            body_params=body,
            error_message=f"Failed to {action_name}",
        )
        if self._is_error(result):
            return [result]
        return result
