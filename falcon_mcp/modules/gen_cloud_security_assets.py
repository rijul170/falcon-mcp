"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `cloud_security_assets` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenCloudSecurityAssetsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `cloud_security_assets` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.cloud_security_assets_combined_application_findings, name="cloud_security_assets_combined_application_findings")
        self._add_tool(server=server, method=self.cloud_security_assets_combined_compliance_by_account, name="cloud_security_assets_combined_compliance_by_account")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def cloud_security_assets_combined_application_findings(
        self,
        type: str = Field(description="Finding type"),
        crn: str | None = Field(default=None, description="Deprecated: Use 'gcrn' instead. Application CRN"),
        gcrn: str | None = Field(default=None, description="Application GCRN"),
        filter: str | None = Field(default=None, description="FQL string to filter findings"),
        offset: int | None = Field(default=None, description="Pagination offset"),
        limit: int | None = Field(default=None, description="Page size"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get findings for an application resource with pagination"""
        return self._call(operation="cloud_security_assets_combined_application_findings", query_params={"crn": crn, "gcrn": gcrn, "type": type, "filter": filter, "offset": offset, "limit": limit}, error_message="cloud_security_assets_combined_application_findings failed", member_cid=member_cid)

    def cloud_security_assets_combined_compliance_by_account(
        self,
        filter: str | None = Field(default=None, description="FQL string to filter on asset contents. Filterable fields include: account_id account_name assessment_id business_impact cloud_group cloud_label cloud_label_id cloud_provider cloud_scope compliant control.benchmark.name control.benchmark.version control.extension.status control.framework control.name control.type control.version environment last_evaluated region resource_provider resource_type resource_type_name service service_category severities tag_key tag_value tags_string"),
        sort: str | None = Field(default=None, description="Sort expression in format: field|direction (e.g., last_evaluated|desc). Allowed sort fields: account_id account_name assessment_id cloud_provider control.benchmark.name control.benchmark.version control.framework control.name control.type control.version last_evaluated region resource_counts.compliant resource_counts.non_compliant resource_counts.total resource_provider resource_type resource_type_name service service_category"),
        limit: int | None = Field(default=None, description="The maximum number of items to return. When not specified or 0, 20 is used. When larger than 10000, 10000 is used."),
        offset: int | None = Field(default=None, description="Offset returned controls. Use only one of 'offset' and 'after' parameter for paginating. 'offset' can only be used on offsets < 10,000. For paginating through the entire result set, use 'after' parameter"),
        after: str | None = Field(default=None, description="token-based pagination. use for paginating through an entire result set. Use only one of 'offset' and 'after' parameters for paginating"),
        include_failing_iom_severity_counts: bool | None = Field(default=None, description="Include counts of failing IOMs by severity level"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Gets combined compliance data aggregated by account and region. Results can be filtered and sorted."""
        return self._call(operation="cloud_security_assets_combined_compliance_by_account", query_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset, "after": after, "include_failing_iom_severity_counts": include_failing_iom_severity_counts}, error_message="cloud_security_assets_combined_compliance_by_account failed", member_cid=member_cid)
