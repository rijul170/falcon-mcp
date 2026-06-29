"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `cloud_azure_registration` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenCloudAzureRegistrationModule(GeneratedModuleBase):
    """Generated tools for the Falcon `cloud_azure_registration` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.cloud_registration_azure_get_registration, name="cloud_registration_azure_get_registration")
        self._add_tool(server=server, method=self.download_azure_script, name="download_azure_script")
        self._add_tool(server=server, method=self.cloud_registration_azure_create_registration, name="cloud_registration_azure_create_registration", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.cloud_registration_azure_update_registration, name="cloud_registration_azure_update_registration", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.cloud_registration_azure_validate_registration, name="cloud_registration_azure_validate_registration", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.cloud_registration_azure_delete_legacy_subscription, name="cloud_registration_azure_delete_legacy_subscription", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.cloud_registration_azure_delete_registration, name="cloud_registration_azure_delete_registration", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.cloud_registration_azure_download_script, name="cloud_registration_azure_download_script", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.cloud_registration_azure_trigger_health_check, name="cloud_registration_azure_trigger_health_check", annotations=WRITE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def cloud_registration_azure_create_registration(
        self,
        body: dict = Field(description="Request JSON body for `cloud_registration_azure_create_registration` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create an Azure registration for a tenant."""
        return self._call(operation="cloud_registration_azure_create_registration", query_params=None, body_params=body, error_message="cloud_registration_azure_create_registration failed", member_cid=member_cid)

    def cloud_registration_azure_delete_legacy_subscription(
        self,
        body: dict = Field(description="Request JSON body for `cloud_registration_azure_delete_legacy_subscription` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete existing legacy Azure subscriptions."""
        return self._call(operation="cloud_registration_azure_delete_legacy_subscription", query_params=None, body_params=body, error_message="cloud_registration_azure_delete_legacy_subscription failed", member_cid=member_cid)

    def cloud_registration_azure_delete_registration(
        self,
        tenant_ids: list[str] = Field(description="Azure tenant IDs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deletes existing Azure registrations."""
        return self._call(operation="cloud_registration_azure_delete_registration", query_params={"tenant_ids": tenant_ids}, error_message="cloud_registration_azure_delete_registration failed", member_cid=member_cid)

    def cloud_registration_azure_download_script(
        self,
        body: dict = Field(description="Request JSON body for `cloud_registration_azure_download_script` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve script to create resources"""
        return self._call(operation="cloud_registration_azure_download_script", query_params=None, body_params=body, error_message="cloud_registration_azure_download_script failed", member_cid=member_cid)

    def cloud_registration_azure_get_registration(
        self,
        tenant_id: str = Field(description="Tenant ID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve existing Azure registration for a tenant."""
        return self._call(operation="cloud_registration_azure_get_registration", query_params={"tenant_id": tenant_id}, error_message="cloud_registration_azure_get_registration failed", member_cid=member_cid)

    def cloud_registration_azure_trigger_health_check(
        self,
        tenant_ids: list[str] | None = Field(default=None, description="Azure tenant IDs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Trigger health check scan for Azure registrations"""
        return self._call(operation="cloud_registration_azure_trigger_health_check", query_params={"tenant_ids": tenant_ids}, error_message="cloud_registration_azure_trigger_health_check failed", member_cid=member_cid)

    def cloud_registration_azure_update_registration(
        self,
        body: dict = Field(description="Request JSON body for `cloud_registration_azure_update_registration` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update an existing Azure registration for a tenant."""
        return self._call(operation="cloud_registration_azure_update_registration", query_params=None, body_params=body, error_message="cloud_registration_azure_update_registration failed", member_cid=member_cid)

    def cloud_registration_azure_validate_registration(
        self,
        tenant_id: str = Field(description="Azure tenant ID to be validated"),
        stack_name: str | None = Field(default=None, description="Azure deployment stack name to be validated"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Validate an Azure registration by checking service principal, role assignments and deployment stack (if the deployment method is Bicep)"""
        return self._call(operation="cloud_registration_azure_validate_registration", query_params={"tenant_id": tenant_id, "stack_name": stack_name}, error_message="cloud_registration_azure_validate_registration failed", member_cid=member_cid)

    def download_azure_script(
        self,
        tenant_id: str = Field(description="Azure tenant ID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Download Azure deployment script (Terraform or Bicep)"""
        return self._call(operation="download_azure_script", query_params={"tenant_id": tenant_id}, error_message="download_azure_script failed", member_cid=member_cid)
