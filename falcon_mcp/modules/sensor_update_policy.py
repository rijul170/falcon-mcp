"""
Sensor Update Policy module for Falcon MCP Server.

Provides tools for managing CrowdStrike Falcon sensor update policies, host group
assignments, and uninstall tokens.
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


class SensorUpdatePolicyModule(BaseModule):
    """Module for CrowdStrike Falcon sensor update policy management."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.search_sensor_update_policies, name="search_sensor_update_policies")
        self._add_tool(server=server, method=self.get_sensor_update_policy_members, name="get_sensor_update_policy_members")
        self._add_tool(server=server, method=self.list_sensor_builds, name="list_sensor_builds")
        self._add_tool(
            server=server, method=self.create_sensor_update_policy, name="create_sensor_update_policy",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.update_sensor_update_policy, name="update_sensor_update_policy",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.delete_sensor_update_policies, name="delete_sensor_update_policies",
            annotations=DESTRUCTIVE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.assign_sensor_update_policy_host_groups,
            name="assign_sensor_update_policy_host_groups", annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.unassign_sensor_update_policy_host_groups,
            name="unassign_sensor_update_policy_host_groups", annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.set_sensor_update_policies_state,
            name="set_sensor_update_policies_state", annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.set_sensor_update_policies_precedence,
            name="set_sensor_update_policies_precedence", annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.reveal_uninstall_token, name="reveal_uninstall_token",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(server=server, method=self.list_sensor_update_kernels, name="list_sensor_update_kernels")
        self._add_tool(server=server, method=self.get_sensor_update_kernel_field_values, name="get_sensor_update_kernel_field_values")

    def register_resources(self, server: FastMCP) -> None:
        self._add_resource(server, TextResource(
            uri=AnyUrl("falcon://policies/sensor-update/fql-guide"),
            name="falcon_sensor_update_policies_fql_guide",
            description="FQL filter guide for sensor update policy search.",
            text=POLICY_FQL_DOCUMENTATION,
        ))

    def search_sensor_update_policies(
        self,
        filter: str | None = Field(default=None, description="FQL filter; see `falcon://policies/sensor-update/fql-guide`."),
        limit: int = Field(default=10, ge=1, le=5000, description="Max records."),
        offset: int | None = Field(default=None, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search sensor update policies (V2 endpoint, includes uninstall protection settings)."""
        result = self._base_search_api_call(
            operation="queryCombinedSensorUpdatePoliciesV2",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search sensor update policies",
        )
        if self._is_error(result):
            if filter:
                return self._format_fql_error_response([result], filter, POLICY_FQL_DOCUMENTATION)
            return [result]
        if not result and filter:
            return self._format_fql_error_response([], filter, POLICY_FQL_DOCUMENTATION)
        return result

    def get_sensor_update_policy_members(
        self,
        id: str = Field(description="Sensor update policy ID."),
        filter: str | None = Field(default=None, description="Optional FQL filter on members."),
        limit: int = Field(default=100, ge=1, le=5000, description="Max members."),
        offset: int | None = Field(default=None, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List host details for hosts that have a given sensor update policy applied."""
        result = self._base_search_api_call(
            operation="queryCombinedSensorUpdatePolicyMembers",
            search_params={"id": id, "filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to list sensor update policy members",
        )
        if self._is_error(result):
            return [result]
        return result

    def list_sensor_builds(
        self,
        platform: str | None = Field(
            default=None,
            description="Optional FQL filter on platform (windows / mac / linux).",
            examples=["platform:'windows'"],
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List available sensor builds you can pin a policy to."""
        result = self._base_search_api_call(
            operation="queryCombinedSensorUpdateBuilds",
            search_params={"platform": platform} if platform else {},
            error_message="Failed to list sensor builds",
        )
        if self._is_error(result):
            return [result]
        return result

    def create_sensor_update_policy(
        self,
        name: str = Field(description="Policy name (must be unique within the CID)."),
        platform_name: str = Field(description="'Windows', 'Mac', or 'Linux'."),
        build: str | None = Field(
            default=None,
            description="Sensor build to pin (e.g. 'n-1', '7.20.18313'). Use list_sensor_builds.",
        ),
        description: str | None = Field(default=None, description="Policy description."),
        uninstall_protection: str | None = Field(
            default=None,
            description="'ENABLED', 'DISABLED', or 'MAINTENANCE_MODE'.",
        ),
        settings: dict[str, Any] | None = Field(
            default=None,
            description="Full settings object (overrides convenience fields if provided).",
        ),
    ) -> list[dict[str, Any]]:
        """Create a sensor update policy (V2)."""
        if platform_name not in ("Windows", "Mac", "Linux"):
            return [_format_error_response(
                "`platform_name` must be 'Windows', 'Mac', or 'Linux'.",
                operation="createSensorUpdatePoliciesV2",
            )]
        resource: dict[str, Any] = {"name": name, "platform_name": platform_name}
        if description:
            resource["description"] = description
        if settings is not None:
            resource["settings"] = settings
        else:
            policy_settings: dict[str, Any] = {}
            if build is not None:
                policy_settings["build"] = build
            if uninstall_protection is not None:
                policy_settings["uninstall_protection"] = uninstall_protection
            if policy_settings:
                resource["settings"] = policy_settings

        result = self._base_query_api_call(
            operation="createSensorUpdatePoliciesV2",
            body_params={"resources": [resource]},
            error_message="Failed to create sensor update policy",
        )
        if self._is_error(result):
            return [result]
        return result

    def update_sensor_update_policy(
        self,
        id: str = Field(description="Policy ID to update."),
        name: str | None = Field(default=None, description="New name."),
        description: str | None = Field(default=None, description="New description."),
        settings: dict[str, Any] | None = Field(default=None, description="Updated settings object."),
    ) -> list[dict[str, Any]]:
        """Update a sensor update policy."""
        if name is None and description is None and settings is None:
            return [_format_error_response(
                "Provide at least one of `name`, `description`, or `settings`.",
                operation="updateSensorUpdatePoliciesV2",
            )]
        resource: dict[str, Any] = {"id": id}
        if name is not None:
            resource["name"] = name
        if description is not None:
            resource["description"] = description
        if settings is not None:
            resource["settings"] = settings
        result = self._base_query_api_call(
            operation="updateSensorUpdatePoliciesV2",
            body_params={"resources": [resource]},
            error_message="Failed to update sensor update policy",
        )
        if self._is_error(result):
            return [result]
        return result

    def delete_sensor_update_policies(
        self,
        ids: list[str] = Field(description="Policy IDs to delete."),
    ) -> list[dict[str, Any]]:
        """Delete sensor update policies by ID."""
        if not ids:
            return [_format_error_response("`ids` is required.", operation="deleteSensorUpdatePolicies")]
        result = self._base_query_api_call(
            operation="deleteSensorUpdatePolicies",
            query_params={"ids": ids},
            error_message="Failed to delete sensor update policies",
        )
        if self._is_error(result):
            return [result]
        return result

    def assign_sensor_update_policy_host_groups(
        self,
        id: str = Field(description="Sensor update policy ID."),
        host_group_ids: list[str] = Field(description="Host group IDs to assign."),
    ) -> list[dict[str, Any]]:
        """Add host groups to a sensor update policy."""
        return self._policy_action("add-host-group", id, host_group_ids)

    def unassign_sensor_update_policy_host_groups(
        self,
        id: str = Field(description="Sensor update policy ID."),
        host_group_ids: list[str] = Field(description="Host group IDs to remove."),
    ) -> list[dict[str, Any]]:
        """Remove host groups from a sensor update policy."""
        return self._policy_action("remove-host-group", id, host_group_ids)

    def set_sensor_update_policies_state(
        self,
        ids: list[str] = Field(description="Policy IDs."),
        enabled: bool = Field(description="True to enable, False to disable."),
    ) -> list[dict[str, Any]]:
        """Enable or disable sensor update policies."""
        action = "enable" if enabled else "disable"
        result = self._base_query_api_call(
            operation="performSensorUpdatePoliciesAction",
            query_params={"action_name": action},
            body_params={"ids": ids},
            error_message=f"Failed to {action} sensor update policies",
        )
        if self._is_error(result):
            return [result]
        return result

    def set_sensor_update_policies_precedence(
        self,
        ids: list[str] = Field(description="Policy IDs in desired precedence order (highest first)."),
        platform_name: str = Field(description="'Windows', 'Mac', or 'Linux'."),
    ) -> list[dict[str, Any]]:
        """Set sensor update policy precedence for a platform."""
        result = self._base_query_api_call(
            operation="setSensorUpdatePoliciesPrecedence",
            body_params={"ids": ids, "platform_name": platform_name},
            error_message="Failed to set sensor update policy precedence",
        )
        if self._is_error(result):
            return [result]
        return result

    def reveal_uninstall_token(
        self,
        device_id: str = Field(description="Host AID, or 'MAINTENANCE' to fetch the maintenance token."),
        audit_message: str | None = Field(default=None, description="Reason logged in the audit trail."),
    ) -> list[dict[str, Any]]:
        """Reveal an uninstall token for a host (or the maintenance token)."""
        body: dict[str, Any] = {"device_id": device_id}
        if audit_message:
            body["audit_message"] = audit_message
        result = self._base_query_api_call(
            operation="revealUninstallToken",
            body_params=body,
            error_message="Failed to reveal uninstall token",
        )
        if self._is_error(result):
            return [result]
        return result

    def list_sensor_update_kernels(
        self,
        filter: str | None = Field(default=None, description="FQL filter. Supported fields: distro, distro_version, flavor, release, vendor, version, architecture, tier."),
        limit: int = Field(default=20, ge=1, le=500, description="Maximum kernels to return."),
        offset: int | None = Field(default=None, description="Pagination offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List sensor-compatible Linux kernels with full details.

        Returns kernel metadata including distro, version, architecture, and compatibility tier.
        Use this to verify kernel compatibility before deploying sensor updates to Linux hosts.
        """
        result = self._base_search_api_call(
            operation="queryCombinedSensorUpdateKernels",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to list sensor update kernels",
        )
        if self._is_error(result):
            return [result]
        return result

    def get_sensor_update_kernel_field_values(
        self,
        field_name: str = Field(
            description="Kernel field to get distinct values for. Supported: distro, distro_version, flavor, release, vendor, version, architecture, tier.",
            examples=["distro", "architecture", "tier"],
        ),
        filter: str | None = Field(default=None, description="FQL filter to narrow results."),
        limit: int = Field(default=50, ge=1, le=500, description="Maximum distinct values to return."),
        offset: int | None = Field(default=None, description="Pagination offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get distinct values for a specific sensor kernel field.

        Use to discover all supported distros, architectures, or tiers in your sensor update scope.
        """
        result = self._base_search_api_call(
            operation="querySensorUpdateKernelsDistinct",
            search_params={"field_name": field_name, "filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to get kernel field values",
        )
        if self._is_error(result):
            return [result]
        return result

    def _policy_action(self, action_name: str, policy_id: str, group_ids: list[str]) -> list[dict[str, Any]]:
        if not group_ids:
            return [_format_error_response(
                "`host_group_ids` is required.",
                operation=f"performSensorUpdatePoliciesAction:{action_name}",
            )]
        body = {
            "action_parameters": [{"name": "group_id", "value": gid} for gid in group_ids],
            "ids": [policy_id],
        }
        result = self._base_query_api_call(
            operation="performSensorUpdatePoliciesAction",
            query_params={"action_name": action_name},
            body_params=body,
            error_message=f"Failed to {action_name}",
        )
        if self._is_error(result):
            return [result]
        return result
