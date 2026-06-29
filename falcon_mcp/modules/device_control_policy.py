"""
Device Control Policy module for Falcon MCP Server.

Provides tools for managing CrowdStrike Falcon Device Control (USB/peripheral) policies
and host group assignments.
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


class DeviceControlPolicyModule(BaseModule):
    """Module for CrowdStrike Falcon Device Control policy management."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.search_device_control_policies, name="search_device_control_policies")
        self._add_tool(server=server, method=self.get_device_control_policy_members, name="get_device_control_policy_members")
        self._add_tool(
            server=server, method=self.create_device_control_policy, name="create_device_control_policy",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.update_device_control_policy, name="update_device_control_policy",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.delete_device_control_policies, name="delete_device_control_policies",
            annotations=DESTRUCTIVE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.assign_device_control_policy_host_groups,
            name="assign_device_control_policy_host_groups", annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.unassign_device_control_policy_host_groups,
            name="unassign_device_control_policy_host_groups", annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.set_device_control_policies_state,
            name="set_device_control_policies_state", annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.set_device_control_policies_precedence,
            name="set_device_control_policies_precedence", annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.configure_device_control_classes,
            name="configure_device_control_classes", annotations=WRITE_ANNOTATIONS,
        )

    def register_resources(self, server: FastMCP) -> None:
        self._add_resource(server, TextResource(
            uri=AnyUrl("falcon://policies/device-control/fql-guide"),
            name="falcon_device_control_policies_fql_guide",
            description="FQL filter guide for device control policy search.",
            text=POLICY_FQL_DOCUMENTATION,
        ))

    def search_device_control_policies(
        self,
        filter: str | None = Field(default=None, description="FQL filter; see `falcon://policies/device-control/fql-guide`."),
        limit: int = Field(default=10, ge=1, le=5000, description="Max records."),
        offset: int | None = Field(default=None, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search device control policies and return full policy details."""
        result = self._base_search_api_call(
            operation="queryCombinedDeviceControlPolicies",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search device control policies",
        )
        if self._is_error(result):
            if filter:
                return self._format_fql_error_response([result], filter, POLICY_FQL_DOCUMENTATION)
            return [result]
        if not result and filter:
            return self._format_fql_error_response([], filter, POLICY_FQL_DOCUMENTATION)
        return result

    def get_device_control_policy_members(
        self,
        id: str = Field(description="Device control policy ID."),
        filter: str | None = Field(default=None, description="Optional FQL filter on members."),
        limit: int = Field(default=100, ge=1, le=5000, description="Max members."),
        offset: int | None = Field(default=None, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List host details for hosts that have a given device control policy applied."""
        result = self._base_search_api_call(
            operation="queryCombinedDeviceControlPolicyMembers",
            search_params={"id": id, "filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to list device control policy members",
        )
        if self._is_error(result):
            return [result]
        return result

    def create_device_control_policy(
        self,
        name: str = Field(description="Policy name."),
        platform_name: str = Field(description="'Windows' or 'Mac'."),
        description: str | None = Field(default=None, description="Policy description."),
        clone_id: str | None = Field(default=None, description="Existing policy ID to clone."),
        settings: dict[str, Any] | None = Field(default=None, description="Setting overrides."),
    ) -> list[dict[str, Any]]:
        """Create a device control policy."""
        if platform_name not in ("Windows", "Mac"):
            return [_format_error_response(
                "`platform_name` must be 'Windows' or 'Mac'.",
                operation="createDeviceControlPolicies",
            )]
        resource: dict[str, Any] = {"name": name, "platform_name": platform_name}
        if description:
            resource["description"] = description
        if clone_id:
            resource["clone_id"] = clone_id
        if settings:
            resource["settings"] = settings
        result = self._base_query_api_call(
            operation="createDeviceControlPolicies",
            body_params={"resources": [resource]},
            error_message="Failed to create device control policy",
        )
        if self._is_error(result):
            return [result]
        return result

    def update_device_control_policy(
        self,
        id: str = Field(description="Policy ID to update."),
        name: str | None = Field(default=None, description="New name."),
        description: str | None = Field(default=None, description="New description."),
        settings: dict[str, Any] | None = Field(default=None, description="Updated settings object."),
    ) -> list[dict[str, Any]]:
        """Update a device control policy."""
        if name is None and description is None and settings is None:
            return [_format_error_response(
                "Provide at least one of `name`, `description`, or `settings`.",
                operation="updateDeviceControlPolicies",
            )]
        resource: dict[str, Any] = {"id": id}
        if name is not None:
            resource["name"] = name
        if description is not None:
            resource["description"] = description
        if settings is not None:
            resource["settings"] = settings
        result = self._base_query_api_call(
            operation="updateDeviceControlPolicies",
            body_params={"resources": [resource]},
            error_message="Failed to update device control policy",
        )
        if self._is_error(result):
            return [result]
        return result

    def delete_device_control_policies(
        self,
        ids: list[str] = Field(description="Policy IDs to delete."),
    ) -> list[dict[str, Any]]:
        """Delete device control policies by ID."""
        if not ids:
            return [_format_error_response("`ids` is required.", operation="deleteDeviceControlPolicies")]
        result = self._base_query_api_call(
            operation="deleteDeviceControlPolicies",
            query_params={"ids": ids},
            error_message="Failed to delete device control policies",
        )
        if self._is_error(result):
            return [result]
        return result

    def assign_device_control_policy_host_groups(
        self,
        id: str = Field(description="Device control policy ID."),
        host_group_ids: list[str] = Field(description="Host group IDs to assign."),
    ) -> list[dict[str, Any]]:
        """Add host groups to a device control policy."""
        return self._policy_action("add-host-group", id, host_group_ids)

    def unassign_device_control_policy_host_groups(
        self,
        id: str = Field(description="Device control policy ID."),
        host_group_ids: list[str] = Field(description="Host group IDs to remove."),
    ) -> list[dict[str, Any]]:
        """Remove host groups from a device control policy."""
        return self._policy_action("remove-host-group", id, host_group_ids)

    def set_device_control_policies_state(
        self,
        ids: list[str] = Field(description="Policy IDs."),
        enabled: bool = Field(description="True to enable, False to disable."),
    ) -> list[dict[str, Any]]:
        """Enable or disable device control policies."""
        action = "enable" if enabled else "disable"
        result = self._base_query_api_call(
            operation="performDeviceControlPoliciesAction",
            query_params={"action_name": action},
            body_params={"ids": ids},
            error_message=f"Failed to {action} device control policies",
        )
        if self._is_error(result):
            return [result]
        return result

    def set_device_control_policies_precedence(
        self,
        ids: list[str] = Field(description="Policy IDs in desired precedence order (highest first)."),
        platform_name: str = Field(description="'Windows' or 'Mac'."),
    ) -> list[dict[str, Any]]:
        """Set device control policy precedence for a platform."""
        result = self._base_query_api_call(
            operation="setDeviceControlPoliciesPrecedence",
            body_params={"ids": ids, "platform_name": platform_name},
            error_message="Failed to set device control policy precedence",
        )
        if self._is_error(result):
            return [result]
        return result

    def configure_device_control_classes(
        self,
        policy_id: str = Field(
            description="Device control policy ID to configure classes for. Obtain from `falcon_search_device_control_policies`.",
        ),
        classes: list[dict[str, Any]] = Field(
            description=(
                "List of device class configurations. Each entry is a dict with: "
                "`id` (class ID e.g. 'USB'), `action` (FULL_ACCESS, READ_ONLY, NO_ACCESS, BLOCK_EXECUTION), "
                "`exceptions` (optional list of exception dicts). "
                "Example: [{\"id\": \"USB\", \"action\": \"READ_ONLY\"}]"
            ),
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Configure device class rules within a device control policy.

        Use this to set USB, storage, and other device class permissions within a policy.
        Each class can be set to FULL_ACCESS, READ_ONLY, NO_ACCESS, or BLOCK_EXECUTION.
        """
        result = self._base_query_api_call(
            operation="patchDeviceControlPoliciesClassesV1",
            body_params={"id": policy_id, "settings": {"classes": classes}},
            error_message="Failed to configure device control classes",
        )
        if self._is_error(result):
            return [result]
        return result

    def _policy_action(self, action_name: str, policy_id: str, group_ids: list[str]) -> list[dict[str, Any]]:
        if not group_ids:
            return [_format_error_response(
                "`host_group_ids` is required.",
                operation=f"performDeviceControlPoliciesAction:{action_name}",
            )]
        body = {
            "action_parameters": [{"name": "group_id", "value": gid} for gid in group_ids],
            "ids": [policy_id],
        }
        result = self._base_query_api_call(
            operation="performDeviceControlPoliciesAction",
            query_params={"action_name": action_name},
            body_params=body,
            error_message=f"Failed to {action_name}",
        )
        if self._is_error(result):
            return [result]
        return result
