"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `cloud_google_cloud_registration` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenCloudGoogleCloudRegistrationModule(GeneratedModuleBase):
    """Generated tools for the Falcon `cloud_google_cloud_registration` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.cloud_registration_gcp_get_entities, name="cloud_registration_gcp_get_entities")
        self._add_tool(server=server, method=self.cloud_registration_gcp_get_registration, name="cloud_registration_gcp_get_registration")
        self._add_tool(server=server, method=self.cloud_registration_gcp_create_registration, name="cloud_registration_gcp_create_registration", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.cloud_registration_gcp_put_registration, name="cloud_registration_gcp_put_registration", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.cloud_registration_gcp_update_registration, name="cloud_registration_gcp_update_registration", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.cloud_registration_gcp_delete_registration, name="cloud_registration_gcp_delete_registration", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.cloud_registration_gcp_trigger_health_check, name="cloud_registration_gcp_trigger_health_check", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def cloud_registration_gcp_create_registration(
        self,
        body: dict = Field(description="Request JSON body for `cloud_registration_gcp_create_registration` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create a Google Cloud Registration."""
        return self._call(operation="cloud_registration_gcp_create_registration", query_params=None, body_params=body, error_message="cloud_registration_gcp_create_registration failed", member_cid=member_cid)

    def cloud_registration_gcp_delete_registration(
        self,
        ids: str = Field(description="Google Cloud Registration ID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deletes a Google Cloud Registration and returns the deleted registration in the response body."""
        return self._call(operation="cloud_registration_gcp_delete_registration", query_params={"ids": ids}, error_message="cloud_registration_gcp_delete_registration failed", member_cid=member_cid)

    def cloud_registration_gcp_get_entities(
        self,
        ids: list[str] | None = Field(default=None, description="Google Cloud Registration IDs to filter by"),
        filter: str | None = Field(default=None, description="FQL (Falcon Query Language) string for filtering results. Allowed filters are entity_type, entity_id, entity_name, registration_id, registration_name, registration_scope, parent_id, ioa_status, iom_status, created, updated"),
        sort: str | None = Field(default=None, description="Field and direction for sorting results (e.g., 'created|desc'). Sorting applies across all entity types before grouping."),
        limit: int | None = Field(default=None, description="Maximum number of records to return (default: 100, max: 500). Limit applies across all entity types."),
        offset: int | None = Field(default=None, description="Starting index of result"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve all GCP entities (organizations, folders, projects) grouped by type with support for FQL filtering, sorting, and pagination."""
        return self._call(operation="cloud_registration_gcp_get_entities", query_params={"ids": ids, "filter": filter, "sort": sort, "limit": limit, "offset": offset}, error_message="cloud_registration_gcp_get_entities failed", member_cid=member_cid)

    def cloud_registration_gcp_get_registration(
        self,
        ids: str = Field(description="Google Cloud Registration ID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve a Google Cloud Registration."""
        return self._call(operation="cloud_registration_gcp_get_registration", query_params={"ids": ids}, error_message="cloud_registration_gcp_get_registration failed", member_cid=member_cid)

    def cloud_registration_gcp_put_registration(
        self,
        body: dict = Field(description="Request JSON body for `cloud_registration_gcp_put_registration` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Creates/Updates a Google Cloud Registration."""
        return self._call(operation="cloud_registration_gcp_put_registration", query_params=None, body_params=body, error_message="cloud_registration_gcp_put_registration failed", member_cid=member_cid)

    def cloud_registration_gcp_trigger_health_check(
        self,
        ids: list[str] | None = Field(default=None, description="GCP Registration IDs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Trigger health check scan for GCP registrations"""
        return self._call(operation="cloud_registration_gcp_trigger_health_check", query_params={"ids": ids}, error_message="cloud_registration_gcp_trigger_health_check failed", member_cid=member_cid)

    def cloud_registration_gcp_update_registration(
        self,
        ids: str = Field(description="Google Cloud Registration ID"),
        body: dict = Field(description="Request JSON body for `cloud_registration_gcp_update_registration` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update a Google Cloud Registration."""
        return self._call(operation="cloud_registration_gcp_update_registration", query_params={"ids": ids}, body_params=body, error_message="cloud_registration_gcp_update_registration failed", member_cid=member_cid)
