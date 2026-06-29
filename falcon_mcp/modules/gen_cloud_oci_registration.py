"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `cloud_oci_registration` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenCloudOciRegistrationModule(GeneratedModuleBase):
    """Generated tools for the Falcon `cloud_oci_registration` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.cloud_security_registration_oci_get_account, name="cloud_security_registration_oci_get_account")
        self._add_tool(server=server, method=self.cloud_security_registration_oci_create_account, name="cloud_security_registration_oci_create_account", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.cloud_security_registration_oci_update_account, name="cloud_security_registration_oci_update_account", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.cloud_security_registration_oci_validate_tenancy, name="cloud_security_registration_oci_validate_tenancy", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.cloud_security_registration_oci_delete_account, name="cloud_security_registration_oci_delete_account", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.cloud_security_registration_oci_download_script, name="cloud_security_registration_oci_download_script", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.cloud_security_registration_oci_rotate_key, name="cloud_security_registration_oci_rotate_key", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def cloud_security_registration_oci_create_account(
        self,
        body: dict = Field(description="Request JSON body for `cloud_security_registration_oci_create_account` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create OCI tenancy account in CSPM"""
        return self._call(operation="cloud_security_registration_oci_create_account", query_params=None, body_params=body, error_message="cloud_security_registration_oci_create_account failed", member_cid=member_cid)

    def cloud_security_registration_oci_delete_account(
        self,
        ids: list[str] | None = Field(default=None, description="OCI tenancy ocids to remove"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete an existing OCI tenancy in CSPM."""
        return self._call(operation="cloud_security_registration_oci_delete_account", query_params={"ids": ids}, error_message="cloud_security_registration_oci_delete_account failed", member_cid=member_cid)

    def cloud_security_registration_oci_download_script(
        self,
        body: dict = Field(description="Request JSON body for `cloud_security_registration_oci_download_script` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve script to create resources in tenancy OCID"""
        return self._call(operation="cloud_security_registration_oci_download_script", query_params=None, body_params=body, error_message="cloud_security_registration_oci_download_script failed", member_cid=member_cid)

    def cloud_security_registration_oci_get_account(
        self,
        filter: str | None = Field(default=None, description="FQL (Falcon Query Language) string for filtering results. Allowed filters are Set{updated_at, tenancy_ocid, tenancy_name, home_region, key_age, overall_status, created_at}"),
        sort: str | None = Field(default=None, description="Field and direction for sorting results - allowed sort fields are Set{tenancy_name, home_region, key_age, overall_status, created_at, updated_at, tenancy_ocid}"),
        next_token: str | None = Field(default=None, description="Token for cursor-based pagination. Currently unsupported."),
        limit: int | None = Field(default=None, description="Maximum number of records to return (default: 100, max: 10000)"),
        offset: int | None = Field(default=None, description="Starting index of result"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve a list of OCI tenancies with support for FQL filtering, sorting, and pagination"""
        return self._call(operation="cloud_security_registration_oci_get_account", query_params={"filter": filter, "sort": sort, "next_token": next_token, "limit": limit, "offset": offset}, error_message="cloud_security_registration_oci_get_account failed", member_cid=member_cid)

    def cloud_security_registration_oci_rotate_key(
        self,
        body: dict = Field(description="Request JSON body for `cloud_security_registration_oci_rotate_key` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Refresh key for the OCI Tenancy"""
        return self._call(operation="cloud_security_registration_oci_rotate_key", query_params=None, body_params=body, error_message="cloud_security_registration_oci_rotate_key failed", member_cid=member_cid)

    def cloud_security_registration_oci_update_account(
        self,
        body: dict = Field(description="Request JSON body for `cloud_security_registration_oci_update_account` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Patch an existing OCI account in our system for a customer."""
        return self._call(operation="cloud_security_registration_oci_update_account", query_params=None, body_params=body, error_message="cloud_security_registration_oci_update_account failed", member_cid=member_cid)

    def cloud_security_registration_oci_validate_tenancy(
        self,
        body: dict = Field(description="Request JSON body for `cloud_security_registration_oci_validate_tenancy` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Validate the OCI account in CSPM for a provided CID."""
        return self._call(operation="cloud_security_registration_oci_validate_tenancy", query_params=None, body_params=body, error_message="cloud_security_registration_oci_validate_tenancy failed", member_cid=member_cid)
