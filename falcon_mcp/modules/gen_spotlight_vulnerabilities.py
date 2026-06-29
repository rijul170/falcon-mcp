"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `spotlight_vulnerabilities` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenSpotlightVulnerabilitiesModule(GeneratedModuleBase):
    """Generated tools for the Falcon `spotlight_vulnerabilities` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_remediations_v2, name="get_remediations_v2")
        self._add_tool(server=server, method=self.get_vulnerabilities_spotlight_vulnerabilities, name="get_vulnerabilities_spotlight_vulnerabilities")
        self._add_tool(server=server, method=self.query_vulnerabilities_spotlight_vulnerabilities, name="query_vulnerabilities_spotlight_vulnerabilities")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def get_remediations_v2(
        self,
        ids: list[str] = Field(description="One or more remediation IDs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get details on remediation by providing one or more IDs"""
        return self._call(operation="getRemediationsV2", query_params={"ids": ids}, error_message="getRemediationsV2 failed", member_cid=member_cid)

    def get_vulnerabilities_spotlight_vulnerabilities(
        self,
        ids: list[str] = Field(description="One or more vulnerability IDs (max: 400). Find vulnerability IDs with GET /spotlight/queries/vulnerabilities/v1"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get details on vulnerabilities by providing one or more IDs"""
        return self._call(operation="getVulnerabilities", query_params={"ids": ids}, error_message="getVulnerabilities failed", member_cid=member_cid)

    def query_vulnerabilities_spotlight_vulnerabilities(
        self,
        filter: str = Field(description="Filter items using a query in Falcon Query Language (FQL). Wildcards * and empty filter values are unsupported. Available filter fields that supports match (~): N/A Available filter fields that supports exact match: aid, cid, last_seen_within, status, cve.id, cve.is_cisa_kev, cve.remediation_level, cve.cps_rating, cve.exprt_rating, cve.exploit_status_to_include, cve.severity, cve.base_score, cve.types, host_info.asset_criticality, host_info.asset_roles, host_info.internet_exposure, host_info.tags, host_info.groups, host_info.product_type_desc, host_info.platform_name, suppression_info.is_suppressed, suppression_info.reason, host_info.instance_state Available filter fields that supports wildcard (*): N/A Available filter fields that supports range comparisons (>, <, >=, <=): created_timestamp, closed_timestamp, updated_timestamp, cve.base_score"),
        after: str | None = Field(default=None, description="A pagination token used with the limit parameter to manage pagination of results. On your first request, don't provide an after token. On subsequent requests, provide the after token from the previous response to continue from that place in the results."),
        limit: int | None = Field(default=None, description="The number of items to return in this response (default: 100, max: 400). Use with the after parameter to manage pagination of results."),
        sort: str | None = Field(default=None, description="Sort vulnerabilities by their properties. Available sort options: <ul><li>updated_timestamp|asc/desc</li><li>closed_timestamp|asc</li><li>updated_timestamp|asc/desc</li></ul>. Can be used in a format <field>|asc for ascending order or <field>|desc for descending order."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for Vulnerabilities in your environment by providing an FQL filter and paging details. Returns a set of Vulnerability IDs which match the filter criteria"""
        return self._call(operation="queryVulnerabilities", query_params={"after": after, "limit": limit, "sort": sort, "filter": filter}, error_message="queryVulnerabilities failed", member_cid=member_cid)
