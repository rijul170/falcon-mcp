"""
SaaS Security (Falcon Shield) module for Falcon MCP Server.

Provides tools for SaaS application security posture management — security checks,
alerts, integrations, and asset/user inventory for connected SaaS apps.
"""

from typing import Any

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule

logger = get_logger(__name__)

WRITE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True,
)


class SaaSSecurityModule(BaseModule):
    """Module for CrowdStrike SaaS Security (Falcon Shield) posture management."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_saas_security_checks, name="get_saas_security_checks")
        self._add_tool(server=server, method=self.get_saas_check_metrics, name="get_saas_check_metrics")
        self._add_tool(server=server, method=self.get_saas_check_affected, name="get_saas_check_affected")
        self._add_tool(server=server, method=self.get_saas_compliance, name="get_saas_compliance")
        self._add_tool(server=server, method=self.get_saas_alerts, name="get_saas_alerts")
        self._add_tool(server=server, method=self.get_saas_integrations, name="get_saas_integrations")
        self._add_tool(server=server, method=self.get_supported_saas, name="get_supported_saas")
        self._add_tool(server=server, method=self.get_saas_app_inventory, name="get_saas_app_inventory")
        self._add_tool(server=server, method=self.get_saas_app_inventory_users, name="get_saas_app_inventory_users")
        self._add_tool(server=server, method=self.get_saas_asset_inventory, name="get_saas_asset_inventory")
        self._add_tool(server=server, method=self.get_saas_device_inventory, name="get_saas_device_inventory")
        self._add_tool(server=server, method=self.get_saas_user_inventory, name="get_saas_user_inventory")
        self._add_tool(server=server, method=self.get_saas_activity_monitor, name="get_saas_activity_monitor")
        self._add_tool(server=server, method=self.get_saas_system_logs, name="get_saas_system_logs")
        self._add_tool(server=server, method=self.get_saas_system_users, name="get_saas_system_users")
        self._add_tool(
            server=server, method=self.dismiss_saas_checks, name="dismiss_saas_checks",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.dismiss_saas_affected_entities, name="dismiss_saas_affected_entities",
            annotations=WRITE_ANNOTATIONS,
        )

    def register_resources(self, server: FastMCP) -> None:
        pass

    def _saas_get(self, operation: str, params: dict[str, Any]) -> list[dict[str, Any]] | dict[str, Any]:
        from falcon_mcp.common.utils import prepare_api_parameters
        prepared = prepare_api_parameters(params)
        response = self.client.command_for(operation, parameters=prepared)
        if not isinstance(response, dict):
            return [{"error": f"Unexpected response format from {operation}"}]
        status = response.get("status_code")
        if status not in (200, None):
            from falcon_mcp.common.errors import handle_api_response
            return handle_api_response(response, operation=operation,
                                       error_message=f"Failed: {operation}", default_result=[])
        body = response.get("body", {})
        resources = body.get("resources") if isinstance(body, dict) else None
        if resources is None:
            return [body] if body else []
        return resources if isinstance(resources, list) else [resources]

    def get_saas_security_checks(
        self,
        check_ids: list[str] | None = Field(default=None, description="Optional check IDs to filter."),
        integration_type: str | None = Field(default=None, description="SaaS integration type (e.g., 'gsuite', 'o365')."),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get SaaS security posture checks.

        Returns security check definitions and their current pass/fail status
        across connected SaaS applications (Google Workspace, M365, etc.).
        """
        return self._saas_get("GetSecurityChecksV3", {
            "ids": check_ids, "integration_type": integration_type,
            "limit": limit, "offset": offset,
        })

    def get_saas_check_metrics(
        self,
        check_ids: list[str] | None = Field(default=None, description="Optional check IDs."),
        integration_type: str | None = Field(default=None, description="SaaS integration type."),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get aggregated SaaS security check metrics (pass/fail counts and trends)."""
        return self._saas_get("GetMetricsV3", {
            "ids": check_ids, "integration_type": integration_type,
            "limit": limit, "offset": offset,
        })

    def get_saas_check_affected(
        self,
        check_id: str = Field(description="Security check ID. Obtain from `falcon_get_saas_security_checks`."),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get entities (users/resources) affected by a specific SaaS security check failure."""
        return self._saas_get("GetSecurityCheckAffectedV3", {
            "id": check_id, "limit": limit, "offset": offset,
        })

    def get_saas_compliance(
        self,
        framework: str | None = Field(default=None, description="Compliance framework filter (e.g., 'SOC2', 'ISO27001')."),
        integration_type: str | None = Field(default=None, description="SaaS integration type."),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get SaaS security compliance status by framework."""
        return self._saas_get("GetSecurityCheckComplianceV3", {
            "framework": framework, "integration_type": integration_type,
            "limit": limit, "offset": offset,
        })

    def get_saas_alerts(
        self,
        alert_ids: list[str] | None = Field(default=None, description="Optional alert IDs."),
        integration_type: str | None = Field(default=None, description="SaaS integration type."),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get SaaS security alerts (anomalous user/app behavior detections)."""
        return self._saas_get("GetAlertsV3", {
            "ids": alert_ids, "integration_type": integration_type,
            "limit": limit, "offset": offset,
        })

    def get_saas_integrations(
        self,
        integration_ids: list[str] | None = Field(default=None, description="Optional integration IDs."),
        integration_type: str | None = Field(default=None, description="SaaS integration type."),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get configured SaaS integrations and their connection status."""
        return self._saas_get("GetIntegrationsV3", {
            "ids": integration_ids, "integration_type": integration_type,
            "limit": limit, "offset": offset,
        })

    def get_supported_saas(
        self,
        limit: int = Field(default=50, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List all SaaS applications supported by Falcon Shield integrations."""
        return self._saas_get("GetSupportedSaasV3", {"limit": limit, "offset": offset})

    def get_saas_app_inventory(
        self,
        integration_type: str | None = Field(default=None, description="SaaS integration type."),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get SaaS application inventory — third-party apps connected to monitored SaaS platforms."""
        return self._saas_get("GetAppInventory", {
            "integration_type": integration_type, "limit": limit, "offset": offset,
        })

    def get_saas_app_inventory_users(
        self,
        app_id: str = Field(description="App ID from `falcon_get_saas_app_inventory`."),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get users who have authorized a specific third-party SaaS application."""
        return self._saas_get("GetAppInventoryUsers", {
            "id": app_id, "limit": limit, "offset": offset,
        })

    def get_saas_asset_inventory(
        self,
        integration_type: str | None = Field(default=None, description="SaaS integration type."),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get SaaS asset inventory (files, documents, resources in monitored SaaS platforms)."""
        return self._saas_get("GetAssetInventoryV3", {
            "integration_type": integration_type, "limit": limit, "offset": offset,
        })

    def get_saas_device_inventory(
        self,
        integration_type: str | None = Field(default=None, description="SaaS integration type."),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get device inventory from SaaS platforms (devices enrolled in MDM/IdP)."""
        return self._saas_get("GetDeviceInventoryV3", {
            "integration_type": integration_type, "limit": limit, "offset": offset,
        })

    def get_saas_user_inventory(
        self,
        integration_type: str | None = Field(default=None, description="SaaS integration type."),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get user inventory from connected SaaS platforms (user accounts, roles, MFA status)."""
        return self._saas_get("GetUserInventoryV3", {
            "integration_type": integration_type, "limit": limit, "offset": offset,
        })

    def get_saas_activity_monitor(
        self,
        integration_type: str | None = Field(default=None, description="SaaS integration type."),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get SaaS activity monitor events (admin actions, sign-ins, permission changes)."""
        return self._saas_get("GetActivityMonitorV3", {
            "integration_type": integration_type, "limit": limit, "offset": offset,
        })

    def get_saas_system_logs(
        self,
        integration_type: str | None = Field(default=None, description="SaaS integration type."),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get SaaS system audit logs from connected SaaS platforms."""
        return self._saas_get("GetSystemLogsV3", {
            "integration_type": integration_type, "limit": limit, "offset": offset,
        })

    def get_saas_system_users(
        self,
        integration_type: str | None = Field(default=None, description="SaaS integration type."),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get Falcon Shield system users (administrators managing SaaS Security)."""
        return self._saas_get("GetSystemUsersV3", {
            "integration_type": integration_type, "limit": limit, "offset": offset,
        })

    def dismiss_saas_checks(
        self,
        check_ids: list[str] = Field(description="Security check IDs to dismiss. Obtain from `falcon_get_saas_security_checks`."),
        reason: str | None = Field(default=None, description="Dismissal reason (recorded in audit log)."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Dismiss SaaS security check findings.

        Marks the specified checks as dismissed so they no longer affect the posture score.
        Use when checks are accepted risks or false positives.
        """
        body: dict[str, Any] = {"ids": check_ids}
        if reason:
            body["reason"] = reason
        result = self._base_query_api_call(
            operation="DismissSecurityCheckV3",
            body_params=body,
            error_message="Failed to dismiss SaaS security checks",
        )
        if self._is_error(result):
            return [result]
        return result

    def dismiss_saas_affected_entities(
        self,
        check_id: str = Field(description="Security check ID."),
        entity_ids: list[str] = Field(description="Affected entity IDs to dismiss."),
        reason: str | None = Field(default=None, description="Dismissal reason."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Dismiss specific entities affected by a SaaS security check finding.

        Dismisses only the specified entities (users/resources) rather than the entire check.
        """
        body: dict[str, Any] = {"id": check_id, "entity_ids": entity_ids}
        if reason:
            body["reason"] = reason
        result = self._base_query_api_call(
            operation="DismissAffectedEntityV3",
            body_params=body,
            error_message="Failed to dismiss SaaS affected entities",
        )
        if self._is_error(result):
            return [result]
        return result
