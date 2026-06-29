"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `saas_security` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenSaasSecurityModule(GeneratedModuleBase):
    """Generated tools for the Falcon `saas_security` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_activity_monitor_v3, name="get_activity_monitor_v3")
        self._add_tool(server=server, method=self.get_alerts_v3, name="get_alerts_v3")
        self._add_tool(server=server, method=self.get_app_inventory, name="get_app_inventory")
        self._add_tool(server=server, method=self.get_app_inventory_users, name="get_app_inventory_users")
        self._add_tool(server=server, method=self.get_asset_inventory_v3, name="get_asset_inventory_v3")
        self._add_tool(server=server, method=self.get_device_inventory_v3, name="get_device_inventory_v3")
        self._add_tool(server=server, method=self.get_integrations_v3, name="get_integrations_v3")
        self._add_tool(server=server, method=self.get_metrics_v3, name="get_metrics_v3")
        self._add_tool(server=server, method=self.get_security_check_affected_v3, name="get_security_check_affected_v3")
        self._add_tool(server=server, method=self.get_security_check_compliance_v3, name="get_security_check_compliance_v3")
        self._add_tool(server=server, method=self.get_security_checks_v3, name="get_security_checks_v3")
        self._add_tool(server=server, method=self.get_supported_saas_v3, name="get_supported_saas_v3")
        self._add_tool(server=server, method=self.get_system_logs_v3, name="get_system_logs_v3")
        self._add_tool(server=server, method=self.get_system_users_v3, name="get_system_users_v3")
        self._add_tool(server=server, method=self.get_user_inventory_v3, name="get_user_inventory_v3")
        self._add_tool(server=server, method=self.integration_builder_get_status_v3, name="integration_builder_get_status_v3")
        self._add_tool(server=server, method=self.integration_builder_end_transaction_v3, name="integration_builder_end_transaction_v3", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.integration_builder_upload_v3, name="integration_builder_upload_v3", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.integration_builder_reset_v3, name="integration_builder_reset_v3", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def get_activity_monitor_v3(
        self,
        integration_id: str | None = Field(default=None, description="Integration ID"),
        actor: str | None = Field(default=None, description="Actor"),
        category: str | None = Field(default=None, description="Comma separated list of categories"),
        projection: str | None = Field(default=None, description="Comma separated list of projections"),
        from_date: str | None = Field(default=None, description="From Date"),
        to_date: str | None = Field(default=None, description="To Date"),
        limit: int | None = Field(default=None, description="Max number of logs to fetch"),
        skip: int | None = Field(default=None, description="Number of logs to skip"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """GET Activity Monitor"""
        return self._call(operation="GetActivityMonitorV3", query_params={"integration_id": integration_id, "actor": actor, "category": category, "projection": projection, "from_date": from_date, "to_date": to_date, "limit": limit, "skip": skip}, error_message="GetActivityMonitorV3 failed", member_cid=member_cid)

    def get_alerts_v3(
        self,
        id: str | None = Field(default=None, description="Alert ID"),
        limit: int | None = Field(default=None, description="The maximum number of objects to return"),
        offset: int | None = Field(default=None, description="The starting index of the results"),
        last_id: str | None = Field(default=None, description="The last id of the alert you want to get"),
        type: str | None = Field(default=None, description="The type of alert you want to get"),
        integration_id: str | None = Field(default=None, description="Comma separated list of integration ID's of the alert you want to get"),
        from_date: str | None = Field(default=None, description="The start date of the alert you want to get (in YYYY-MM-DD format)"),
        to_date: str | None = Field(default=None, description="The end date of the alert you want to get (in YYYY-MM-DD format)"),
        ascending: bool | None = Field(default=None, description="`ascending` query parameter."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """GET Alert by ID or GET Alerts"""
        return self._call(operation="GetAlertsV3", query_params={"id": id, "limit": limit, "offset": offset, "last_id": last_id, "type": type, "integration_id": integration_id, "from_date": from_date, "to_date": to_date, "ascending": ascending}, error_message="GetAlertsV3 failed", member_cid=member_cid)

    def get_app_inventory(
        self,
        type: str | None = Field(default=None, description="Comma separated list of app types"),
        limit: int | None = Field(default=None, description="The maximum number of objects to return"),
        offset: int | None = Field(default=None, description="The starting index of the results"),
        status: str | None = Field(default=None, description="Comma separated list of application statuses (approved, in review, rejected, unclassified)"),
        access_level: str | None = Field(default=None, description="Comma separated list of access levels"),
        scopes: str | None = Field(default=None, description="Comma separated list of scopes"),
        users: str | None = Field(default=None, description="Users. Format: 'is equal value' or 'contains value' or 'value' (implies 'is equal value')"),
        groups: str | None = Field(default=None, description="Comma separated list of groups"),
        last_activity: str | None = Field(default=None, description="Last activity was within or was not within the last 'value' days. Format: 'was value' or 'was not value' or 'value' (implies 'was value'). 'value' is an integer"),
        integration_id: str | None = Field(default=None, description="Comma separated list of integration IDs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """GET Applications Inventory"""
        return self._call(operation="GetAppInventory", query_params={"type": type, "limit": limit, "offset": offset, "status": status, "access_level": access_level, "scopes": scopes, "users": users, "groups": groups, "last_activity": last_activity, "integration_id": integration_id}, error_message="GetAppInventory failed", member_cid=member_cid)

    def get_app_inventory_users(
        self,
        item_id: str = Field(description="Item ID in format: 'integration_id|||app_id' (item_id)"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """GET Application Users"""
        return self._call(operation="GetAppInventoryUsers", query_params={"item_id": item_id}, error_message="GetAppInventoryUsers failed", member_cid=member_cid)

    def get_asset_inventory_v3(
        self,
        integration_id: str | None = Field(default=None, description="Comma separated list of integration IDs"),
        limit: int | None = Field(default=None, description="The maximum number of objects to return"),
        offset: int | None = Field(default=None, description="The starting index of the results"),
        resource_type: str | None = Field(default=None, description="Comma separated list of resource types"),
        access_level: str | None = Field(default=None, description="Comma separated list of access levels"),
        last_accessed: str | None = Field(default=None, description="Last accessed date was within or was not within the last 'value' days. Format: 'was value' or 'was not value' or 'value' (implies 'was value'). 'value' is an integer"),
        last_modified: str | None = Field(default=None, description="Last modified date was within or was not within the last 'value' days. Format: 'was value' or 'was not value' or 'value' (implies 'was value'). 'value' is an integer"),
        resource_name: str | None = Field(default=None, description="Resource name contains 'value' (case insensitive)"),
        password_protected: bool | None = Field(default=None, description="Password protected"),
        resource_owner: str | None = Field(default=None, description="Resource owner contains 'value' (case insensitive)"),
        resource_owner_enabled: bool | None = Field(default=None, description="Resource owner enabled"),
        unmanaged_domain: str | None = Field(default=None, description="Comma separated list of unmanaged domains"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """GET Data Inventory"""
        return self._call(operation="GetAssetInventoryV3", query_params={"integration_id": integration_id, "limit": limit, "offset": offset, "resource_type": resource_type, "access_level": access_level, "last_accessed": last_accessed, "last_modified": last_modified, "resource_name": resource_name, "password_protected": password_protected, "resource_owner": resource_owner, "resource_owner_enabled": resource_owner_enabled, "unmanaged_domain": unmanaged_domain}, error_message="GetAssetInventoryV3 failed", member_cid=member_cid)

    def get_device_inventory_v3(
        self,
        integration_id: str | None = Field(default=None, description="Comma separated integration ID's"),
        limit: int | None = Field(default=None, description="The maximum number of objects to return"),
        offset: int | None = Field(default=None, description="The starting index of the results"),
        email: str | None = Field(default=None, description="Email"),
        privileged_only: bool | None = Field(default=None, description="Privileged Only"),
        unassociated_devices: bool | None = Field(default=None, description="Unassociated Devices"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """GET Device Inventory"""
        return self._call(operation="GetDeviceInventoryV3", query_params={"integration_id": integration_id, "limit": limit, "offset": offset, "email": email, "privileged_only": privileged_only, "unassociated_devices": unassociated_devices}, error_message="GetDeviceInventoryV3 failed", member_cid=member_cid)

    def get_integrations_v3(
        self,
        saas_id: str | None = Field(default=None, description="Comma separated SaaS ID's"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """GET Integrations"""
        return self._call(operation="GetIntegrationsV3", query_params={"saas_id": saas_id}, error_message="GetIntegrationsV3 failed", member_cid=member_cid)

    def get_metrics_v3(
        self,
        status: str | None = Field(default=None, description="Exposure status"),
        limit: int | None = Field(default=None, description="The maximum number of objects to return"),
        offset: int | None = Field(default=None, description="The starting index of the results"),
        integration_id: str | None = Field(default=None, description="Comma separated list of integration IDs"),
        impact: str | None = Field(default=None, description="Impact"),
        compliance: bool | None = Field(default=None, description="Compliance"),
        check_type: str | None = Field(default=None, description="Check Type"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """GET Metrics"""
        return self._call(operation="GetMetricsV3", query_params={"status": status, "limit": limit, "offset": offset, "integration_id": integration_id, "impact": impact, "compliance": compliance, "check_type": check_type}, error_message="GetMetricsV3 failed", member_cid=member_cid)

    def get_security_check_affected_v3(
        self,
        id: str = Field(description="Security Check ID"),
        limit: int | None = Field(default=None, description="The maximum number of objects to return"),
        offset: int | None = Field(default=None, description="The starting index of the results"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """GET Security Check Affected"""
        return self._call(operation="GetSecurityCheckAffectedV3", query_params={"id": id, "limit": limit, "offset": offset}, error_message="GetSecurityCheckAffectedV3 failed", member_cid=member_cid)

    def get_security_check_compliance_v3(
        self,
        id: str = Field(description="Security Check ID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """GET Compliance"""
        return self._call(operation="GetSecurityCheckComplianceV3", query_params={"id": id}, error_message="GetSecurityCheckComplianceV3 failed", member_cid=member_cid)

    def get_security_checks_v3(
        self,
        id: str | None = Field(default=None, description="Security Check ID"),
        limit: int | None = Field(default=None, description="The maximum number of objects to return"),
        offset: int | None = Field(default=None, description="The starting index of the results"),
        status: str | None = Field(default=None, description="Exposure status"),
        integration_id: str | None = Field(default=None, description="Comma separated list of integration IDs"),
        impact: str | None = Field(default=None, description="Impact"),
        compliance: bool | None = Field(default=None, description="Compliance"),
        check_type: str | None = Field(default=None, description="Check Type"),
        check_tags: str | None = Field(default=None, description="Comma separated list of check tags names or ids"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """GET Security Check by ID or GET List Security Checks"""
        return self._call(operation="GetSecurityChecksV3", query_params={"id": id, "limit": limit, "offset": offset, "status": status, "integration_id": integration_id, "impact": impact, "compliance": compliance, "check_type": check_type, "check_tags": check_tags}, error_message="GetSecurityChecksV3 failed", member_cid=member_cid)

    def get_supported_saas_v3(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """GET Supported SaaS"""
        return self._call(operation="GetSupportedSaasV3", query_params=None, error_message="GetSupportedSaasV3 failed", member_cid=member_cid)

    def get_system_logs_v3(
        self,
        from_date: str | None = Field(default=None, description="From Date (in YYYY-MM-DD format)"),
        limit: int | None = Field(default=None, description="The maximum number of objects to return"),
        offset: int | None = Field(default=None, description="The starting index of the results"),
        to_date: str | None = Field(default=None, description="To Date (in YYYY-MM-DD format)"),
        total_count: bool | None = Field(default=None, description="Fetch Total Count?"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """GET System Logs"""
        return self._call(operation="GetSystemLogsV3", query_params={"from_date": from_date, "limit": limit, "offset": offset, "to_date": to_date, "total_count": total_count}, error_message="GetSystemLogsV3 failed", member_cid=member_cid)

    def get_system_users_v3(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """GET System Users"""
        return self._call(operation="GetSystemUsersV3", query_params=None, error_message="GetSystemUsersV3 failed", member_cid=member_cid)

    def get_user_inventory_v3(
        self,
        integration_id: str | None = Field(default=None, description="Comma separated integration ID's"),
        limit: int | None = Field(default=None, description="The maximum number of objects to return"),
        offset: int | None = Field(default=None, description="The starting index of the results"),
        email: str | None = Field(default=None, description="Email"),
        privileged_only: bool | None = Field(default=None, description="Privileged Only"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """GET User Inventory"""
        return self._call(operation="GetUserInventoryV3", query_params={"integration_id": integration_id, "limit": limit, "offset": offset, "email": email, "privileged_only": privileged_only}, error_message="GetUserInventoryV3 failed", member_cid=member_cid)

    def integration_builder_end_transaction_v3(
        self,
        id: str = Field(description="Integration ID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """POST Data Upload Transaction Completion"""
        return self._call(operation="IntegrationBuilderEndTransactionV3", query_params={"id": id}, error_message="IntegrationBuilderEndTransactionV3 failed", member_cid=member_cid)

    def integration_builder_get_status_v3(
        self,
        id: str = Field(description="Integration ID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """GET Status"""
        return self._call(operation="IntegrationBuilderGetStatusV3", query_params={"id": id}, error_message="IntegrationBuilderGetStatusV3 failed", member_cid=member_cid)

    def integration_builder_reset_v3(
        self,
        id: str = Field(description="Integration ID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Reset"""
        return self._call(operation="IntegrationBuilderResetV3", query_params={"id": id}, error_message="IntegrationBuilderResetV3 failed", member_cid=member_cid)

    def integration_builder_upload_v3(
        self,
        id: str = Field(description="Integration ID"),
        source_id: str = Field(description="Source ID"),
        body: dict = Field(description="Request JSON body for `IntegrationBuilderUploadV3` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """POST Upload"""
        return self._call(operation="IntegrationBuilderUploadV3", query_params={"id": id, "source_id": source_id}, body_params=body, error_message="IntegrationBuilderUploadV3 failed", member_cid=member_cid)
