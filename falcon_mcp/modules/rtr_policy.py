"""
RTR Response Policy module for Falcon MCP Server.

Provides tools for managing CrowdStrike Real Time Response policies and host group
assignments. Pairs with the existing `rtr` module which handles live RTR sessions.
"""

from typing import Any

from mcp.server import FastMCP
from mcp.server.fastmcp.resources import TextResource
from mcp.types import ToolAnnotations
from pydantic import AnyUrl, Field

from falcon_mcp.common.errors import _format_error_response
from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule
from falcon_mcp.resources.policies import POLICY_FQL_DOCUMENTATION

logger = get_logger(__name__)

WRITE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True,
)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True,
)


class RtrPolicyModule(BaseModule):
    """Module for CrowdStrike Falcon RTR response policy management."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.search_rtr_policies, name="search_rtr_policies")
        self._add_tool(server=server, method=self.get_rtr_policy_members, name="get_rtr_policy_members")
        self._add_tool(
            server=server, method=self.create_rtr_policy, name="create_rtr_policy",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.update_rtr_policy, name="update_rtr_policy",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.delete_rtr_policies, name="delete_rtr_policies",
            annotations=DESTRUCTIVE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.assign_rtr_policy_host_groups,
            name="assign_rtr_policy_host_groups", annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.unassign_rtr_policy_host_groups,
            name="unassign_rtr_policy_host_groups", annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.set_rtr_policies_state,
            name="set_rtr_policies_state", annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.set_rtr_policies_precedence,
            name="set_rtr_policies_precedence", annotations=WRITE_ANNOTATIONS,
        )

    def register_resources(self, server: FastMCP) -> None:
        self._add_resource(server, TextResource(
            uri=AnyUrl("falcon://policies/rtr/fql-guide"),
            name="falcon_rtr_policies_fql_guide",
            description="FQL filter guide for RTR response policy search.",
            text=POLICY_FQL_DOCUMENTATION,
        ))

    def search_rtr_policies(
        self,
        filter: str | None = Field(default=None, description="FQL filter; see `falcon://policies/rtr/fql-guide`."),
        limit: int = Field(default=10, ge=1, le=5000, description="Max records."),
        offset: int | None = Field(default=None, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search RTR response policies and return full policy details."""
        result = self._base_search_api_call(
            operation="queryCombinedRTResponsePolicies",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search RTR policies",
        )
        if self._is_error(result):
            if filter:
                return self._format_fql_error_response([result], filter, POLICY_FQL_DOCUMENTATION)
            return [result]
        if not result and filter:
            return self._format_fql_error_response([], filter, POLICY_FQL_DOCUMENTATION)
        return result

    def get_rtr_policy_members(
        self,
        id: str = Field(description="RTR policy ID."),
        filter: str | None = Field(default=None, description="Optional FQL filter on members."),
        limit: int = Field(default=100, ge=1, le=5000, description="Max members."),
        offset: int | None = Field(default=None, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List host details for hosts that have a given RTR policy applied."""
        result = self._base_search_api_call(
            operation="queryCombinedRTResponsePolicyMembers",
            search_params={"id": id, "filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to list RTR policy members",
        )
        if self._is_error(result):
            return [result]
        return result

    def create_rtr_policy(
        self,
        name: str = Field(description="Policy name (must be unique within the CID)."),
        platform_name: str = Field(description="'Windows', 'Mac', or 'Linux'."),
        description: str | None = Field(default=None, description="Policy description."),
        clone_id: str | None = Field(default=None, description="Existing policy ID to clone."),
        settings: list[dict[str, Any]] | None = Field(default=None, description="Setting overrides."),
    ) -> list[dict[str, Any]]:
        """Create an RTR response policy."""
        if platform_name not in ("Windows", "Mac", "Linux"):
            return [_format_error_response(
                "`platform_name` must be 'Windows', 'Mac', or 'Linux'.",
                operation="createRTResponsePolicies",
            )]
        resource: dict[str, Any] = {"name": name, "platform_name": platform_name}
        if description:
            resource["description"] = description
        if clone_id:
            resource["clone_id"] = clone_id
        if settings:
            resource["settings"] = settings
        result = self._base_query_api_call(
            operation="createRTResponsePolicies",
            body_params={"resources": [resource]},
            error_message="Failed to create RTR policy",
        )
        if self._is_error(result):
            return [result]
        return result

    def update_rtr_policy(
        self,
        id: str = Field(description="Policy ID to update."),
        name: str | None = Field(default=None, description="New name."),
        description: str | None = Field(default=None, description="New description."),
        settings: list[dict[str, Any]] | None = Field(default=None, description="Updated settings."),
    ) -> list[dict[str, Any]]:
        """Update an RTR response policy."""
        if name is None and description is None and settings is None:
            return [_format_error_response(
                "Provide at least one of `name`, `description`, or `settings`.",
                operation="updateRTResponsePolicies",
            )]
        resource: dict[str, Any] = {"id": id}
        if name is not None:
            resource["name"] = name
        if description is not None:
            resource["description"] = description
        if settings is not None:
            resource["settings"] = settings
        result = self._base_query_api_call(
            operation="updateRTResponsePolicies",
            body_params={"resources": [resource]},
            error_message="Failed to update RTR policy",
        )
        if self._is_error(result):
            return [result]
        return result

    def delete_rtr_policies(
        self,
        ids: list[str] = Field(description="Policy IDs to delete."),
    ) -> list[dict[str, Any]]:
        """Delete RTR response policies by ID."""
        if not ids:
            return [_format_error_response("`ids` is required.", operation="deleteRTResponsePolicies")]
        result = self._base_query_api_call(
            operation="deleteRTResponsePolicies",
            query_params={"ids": ids},
            error_message="Failed to delete RTR policies",
        )
        if self._is_error(result):
            return [result]
        return result

    def assign_rtr_policy_host_groups(
        self,
        id: str = Field(description="RTR policy ID."),
        host_group_ids: list[str] = Field(description="Host group IDs to assign."),
    ) -> list[dict[str, Any]]:
        """Add host groups to an RTR policy."""
        return self._policy_action("add-host-group", id, host_group_ids)

    def unassign_rtr_policy_host_groups(
        self,
        id: str = Field(description="RTR policy ID."),
        host_group_ids: list[str] = Field(description="Host group IDs to remove."),
    ) -> list[dict[str, Any]]:
        """Remove host groups from an RTR policy."""
        return self._policy_action("remove-host-group", id, host_group_ids)

    def set_rtr_policies_state(
        self,
        ids: list[str] = Field(description="Policy IDs."),
        enabled: bool = Field(description="True to enable, False to disable."),
    ) -> list[dict[str, Any]]:
        """Enable or disable RTR policies."""
        action = "enable" if enabled else "disable"
        result = self._base_query_api_call(
            operation="performRTResponsePoliciesAction",
            query_params={"action_name": action},
            body_params={"ids": ids},
            error_message=f"Failed to {action} RTR policies",
        )
        if self._is_error(result):
            return [result]
        return result

    def set_rtr_policies_precedence(
        self,
        ids: list[str] = Field(description="Policy IDs in desired precedence order (highest first)."),
        platform_name: str = Field(description="'Windows', 'Mac', or 'Linux'."),
    ) -> list[dict[str, Any]]:
        """Set RTR policy precedence for a platform."""
        result = self._base_query_api_call(
            operation="setRTResponsePoliciesPrecedence",
            body_params={"ids": ids, "platform_name": platform_name},
            error_message="Failed to set RTR policy precedence",
        )
        if self._is_error(result):
            return [result]
        return result

    def _policy_action(self, action_name: str, policy_id: str, group_ids: list[str]) -> list[dict[str, Any]]:
        if not group_ids:
            return [_format_error_response(
                "`host_group_ids` is required.",
                operation=f"performRTResponsePoliciesAction:{action_name}",
            )]
        body = {
            "action_parameters": [{"name": "group_id", "value": gid} for gid in group_ids],
            "ids": [policy_id],
        }
        result = self._base_query_api_call(
            operation="performRTResponsePoliciesAction",
            query_params={"action_name": action_name},
            body_params=body,
            error_message=f"Failed to {action_name}",
        )
        if self._is_error(result):
            return [result]
        return result
