"""
Prevention Policy module for Falcon MCP Server.

Provides tools for managing CrowdStrike Falcon prevention policies and their host group
assignments.
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


class PreventionPolicyModule(BaseModule):
    """Module for CrowdStrike Falcon prevention policy management."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.search_prevention_policies, name="search_prevention_policies")
        self._add_tool(server=server, method=self.get_prevention_policy_members, name="get_prevention_policy_members")
        self._add_tool(
            server=server, method=self.create_prevention_policy, name="create_prevention_policy",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.update_prevention_policy, name="update_prevention_policy",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.delete_prevention_policies, name="delete_prevention_policies",
            annotations=DESTRUCTIVE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.assign_prevention_policy_host_groups,
            name="assign_prevention_policy_host_groups", annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.unassign_prevention_policy_host_groups,
            name="unassign_prevention_policy_host_groups", annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.set_prevention_policies_state,
            name="set_prevention_policies_state", annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.set_prevention_policies_precedence,
            name="set_prevention_policies_precedence", annotations=WRITE_ANNOTATIONS,
        )

    def register_resources(self, server: FastMCP) -> None:
        self._add_resource(server, TextResource(
            uri=AnyUrl("falcon://policies/prevention/fql-guide"),
            name="falcon_prevention_policies_fql_guide",
            description="FQL filter guide for prevention policy search.",
            text=POLICY_FQL_DOCUMENTATION,
        ))

    def search_prevention_policies(
        self,
        filter: str | None = Field(default=None, description="FQL filter; see `falcon://policies/prevention/fql-guide`."),
        limit: int = Field(default=10, ge=1, le=5000, description="Max records."),
        offset: int | None = Field(default=None, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression (e.g. precedence.asc)."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search prevention policies and return full policy details."""
        result = self._base_search_api_call(
            operation="queryCombinedPreventionPolicies",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search prevention policies",
        )
        if self._is_error(result):
            if filter:
                return self._format_fql_error_response([result], filter, POLICY_FQL_DOCUMENTATION)
            return [result]
        if not result and filter:
            return self._format_fql_error_response([], filter, POLICY_FQL_DOCUMENTATION)
        return result

    def get_prevention_policy_members(
        self,
        id: str = Field(description="Prevention policy ID."),
        filter: str | None = Field(default=None, description="Optional FQL filter on members."),
        limit: int = Field(default=100, ge=1, le=5000, description="Max members."),
        offset: int | None = Field(default=None, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List host details for hosts that have a given prevention policy applied."""
        result = self._base_search_api_call(
            operation="queryCombinedPreventionPolicyMembers",
            search_params={"id": id, "filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to list prevention policy members",
        )
        if self._is_error(result):
            return [result]
        return result

    def create_prevention_policy(
        self,
        name: str = Field(description="Policy name (must be unique within the CID)."),
        platform_name: str = Field(description="'Windows', 'Mac', 'Linux', 'Android', or 'iOS'."),
        description: str | None = Field(default=None, description="Policy description."),
        clone_id: str | None = Field(default=None, description="Existing policy ID to clone."),
        settings: list[dict[str, Any]] | None = Field(
            default=None,
            description="List of policy setting overrides ({'id': str, 'value': {...}}). Optional when cloning.",
        ),
    ) -> list[dict[str, Any]]:
        """Create a prevention policy."""
        if platform_name not in ("Windows", "Mac", "Linux", "Android", "iOS"):
            return [_format_error_response(
                "`platform_name` must be one of Windows, Mac, Linux, Android, iOS.",
                operation="createPreventionPolicies",
            )]
        resource: dict[str, Any] = {"name": name, "platform_name": platform_name}
        if description:
            resource["description"] = description
        if clone_id:
            resource["clone_id"] = clone_id
        if settings:
            resource["settings"] = settings

        result = self._base_query_api_call(
            operation="createPreventionPolicies",
            body_params={"resources": [resource]},
            error_message="Failed to create prevention policy",
        )
        if self._is_error(result):
            return [result]
        return result

    def update_prevention_policy(
        self,
        id: str = Field(description="Policy ID to update."),
        name: str | None = Field(default=None, description="New name."),
        description: str | None = Field(default=None, description="New description."),
        settings: list[dict[str, Any]] | None = Field(default=None, description="Updated settings."),
    ) -> list[dict[str, Any]]:
        """Update a prevention policy's name, description, or settings."""
        if name is None and description is None and settings is None:
            return [_format_error_response(
                "Provide at least one of `name`, `description`, or `settings`.",
                operation="updatePreventionPolicies",
            )]
        resource: dict[str, Any] = {"id": id}
        if name is not None:
            resource["name"] = name
        if description is not None:
            resource["description"] = description
        if settings is not None:
            resource["settings"] = settings
        result = self._base_query_api_call(
            operation="updatePreventionPolicies",
            body_params={"resources": [resource]},
            error_message="Failed to update prevention policy",
        )
        if self._is_error(result):
            return [result]
        return result

    def delete_prevention_policies(
        self,
        ids: list[str] = Field(description="Policy IDs to delete."),
    ) -> list[dict[str, Any]]:
        """Delete prevention policies by ID."""
        if not ids:
            return [_format_error_response("`ids` is required.", operation="deletePreventionPolicies")]
        result = self._base_query_api_call(
            operation="deletePreventionPolicies",
            query_params={"ids": ids},
            error_message="Failed to delete prevention policies",
        )
        if self._is_error(result):
            return [result]
        return result

    def assign_prevention_policy_host_groups(
        self,
        id: str = Field(description="Prevention policy ID."),
        host_group_ids: list[str] = Field(description="Host group IDs to assign."),
    ) -> list[dict[str, Any]]:
        """Add host groups to a prevention policy."""
        return self._policy_action("add-host-group", id, host_group_ids)

    def unassign_prevention_policy_host_groups(
        self,
        id: str = Field(description="Prevention policy ID."),
        host_group_ids: list[str] = Field(description="Host group IDs to remove."),
    ) -> list[dict[str, Any]]:
        """Remove host groups from a prevention policy."""
        return self._policy_action("remove-host-group", id, host_group_ids)

    def set_prevention_policies_state(
        self,
        ids: list[str] = Field(description="Prevention policy IDs."),
        enabled: bool = Field(description="True to enable, False to disable."),
    ) -> list[dict[str, Any]]:
        """Enable or disable prevention policies."""
        action = "enable" if enabled else "disable"
        body = {"ids": ids}
        result = self._base_query_api_call(
            operation="performPreventionPoliciesAction",
            query_params={"action_name": action},
            body_params=body,
            error_message=f"Failed to {action} prevention policies",
        )
        if self._is_error(result):
            return [result]
        return result

    def set_prevention_policies_precedence(
        self,
        ids: list[str] = Field(description="Policy IDs in desired precedence order (highest first)."),
        platform_name: str = Field(description="'Windows', 'Mac', 'Linux', 'Android', or 'iOS'."),
    ) -> list[dict[str, Any]]:
        """Set prevention policy precedence for a platform."""
        result = self._base_query_api_call(
            operation="setPreventionPoliciesPrecedence",
            body_params={"ids": ids, "platform_name": platform_name},
            error_message="Failed to set prevention policy precedence",
        )
        if self._is_error(result):
            return [result]
        return result

    def _policy_action(self, action_name: str, policy_id: str, group_ids: list[str]) -> list[dict[str, Any]]:
        if not group_ids:
            return [_format_error_response(
                "`host_group_ids` is required.",
                operation=f"performPreventionPoliciesAction:{action_name}",
            )]
        body = {
            "action_parameters": [{"name": "group_id", "value": gid} for gid in group_ids],
            "ids": [policy_id],
        }
        result = self._base_query_api_call(
            operation="performPreventionPoliciesAction",
            query_params={"action_name": action_name},
            body_params=body,
            error_message=f"Failed to {action_name}",
        )
        if self._is_error(result):
            return [result]
        return result
