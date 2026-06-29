"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `container_vulnerabilities` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenContainerVulnerabilitiesModule(GeneratedModuleBase):
    """Generated tools for the Falcon `container_vulnerabilities` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.read_combined_vulnerabilities_details, name="read_combined_vulnerabilities_details")
        self._add_tool(server=server, method=self.read_combined_vulnerabilities_info, name="read_combined_vulnerabilities_info")
        self._add_tool(server=server, method=self.read_vulnerabilities_by_image_count, name="read_vulnerabilities_by_image_count")
        self._add_tool(server=server, method=self.read_vulnerabilities_publication_date, name="read_vulnerabilities_publication_date")
        self._add_tool(server=server, method=self.read_vulnerability_count, name="read_vulnerability_count")
        self._add_tool(server=server, method=self.read_vulnerability_count_by_actively_exploited, name="read_vulnerability_count_by_actively_exploited")
        self._add_tool(server=server, method=self.read_vulnerability_count_by_cps_rating, name="read_vulnerability_count_by_cps_rating")
        self._add_tool(server=server, method=self.read_vulnerability_count_by_cvss_score, name="read_vulnerability_count_by_cvss_score")
        self._add_tool(server=server, method=self.read_vulnerability_count_by_severity, name="read_vulnerability_count_by_severity")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def read_combined_vulnerabilities_details(
        self,
        id: str = Field(description="Image UUID"),
        filter: str | None = Field(default=None, description="Filter the vulnerabilities using a query in Falcon Query Language (FQL). Supported vulnerability filter fields: cid cps_rating cve_id cvss_score exploited_status_name exploited_status include_base_image_vuln is_zero_day remediation_available severity"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 5000."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve vulnerability details related to an image"""
        return self._call(operation="ReadCombinedVulnerabilitiesDetails", query_params={"id": id, "filter": filter, "limit": limit, "offset": offset}, error_message="ReadCombinedVulnerabilitiesDetails failed", member_cid=member_cid)

    def read_combined_vulnerabilities_info(
        self,
        cve_id: str = Field(description="Vulnerability CVE ID"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve vulnerability and package related info for this customer"""
        return self._call(operation="ReadCombinedVulnerabilitiesInfo", query_params={"cve_id": cve_id, "limit": limit, "offset": offset}, error_message="ReadCombinedVulnerabilitiesInfo failed", member_cid=member_cid)

    def read_vulnerabilities_by_image_count(
        self,
        filter: str | None = Field(default=None, description="Filter vulnerabilities using a query in Falcon Query Language (FQL). Supported filter fields: cid cve_id registry repository tag"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve top x vulnerabilities with the most impacted images"""
        return self._call(operation="ReadVulnerabilitiesByImageCount", query_params={"filter": filter, "limit": limit, "offset": offset}, error_message="ReadVulnerabilitiesByImageCount failed", member_cid=member_cid)

    def read_vulnerabilities_publication_date(
        self,
        filter: str | None = Field(default=None, description="Filter vulnerabilities using a query in Falcon Query Language (FQL). Supported filter fields: cid cve_id registry repository tag"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve top x vulnerabilities with the most recent publication date"""
        return self._call(operation="ReadVulnerabilitiesPublicationDate", query_params={"filter": filter, "limit": limit, "offset": offset}, error_message="ReadVulnerabilitiesPublicationDate failed", member_cid=member_cid)

    def read_vulnerability_count(
        self,
        filter: str | None = Field(default=None, description="Filter vulnerabilities using a query in Falcon Query Language (FQL). Supported filter fields: ai_related base_os cid container_id container_running_status containers_impacted_range cps_rating cve_id cvss_score description exploited_status_name exploited_status fix_status image_digest image_id images_impacted_range include_base_image_vuln index_digest package_name_version registry repository severity tag"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Aggregate count of vulnerabilities"""
        return self._call(operation="ReadVulnerabilityCount", query_params={"filter": filter, "limit": limit, "offset": offset}, error_message="ReadVulnerabilityCount failed", member_cid=member_cid)

    def read_vulnerability_count_by_actively_exploited(
        self,
        filter: str | None = Field(default=None, description="Filter vulnerabilities using a query in Falcon Query Language (FQL). Supported filter fields: ai_related base_os cid container_id container_running_status containers_impacted_range cps_rating cve_id cvss_score description exploited_status_name exploited_status fix_status image_digest image_id images_impacted_range include_base_image_vuln index_digest package_name_version registry repository severity tag"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Aggregate count of vulnerabilities grouped by actively exploited"""
        return self._call(operation="ReadVulnerabilityCountByActivelyExploited", query_params={"filter": filter, "limit": limit, "offset": offset}, error_message="ReadVulnerabilityCountByActivelyExploited failed", member_cid=member_cid)

    def read_vulnerability_count_by_cps_rating(
        self,
        filter: str | None = Field(default=None, description="Filter vulnerabilities using a query in Falcon Query Language (FQL). Supported filter fields: ai_related base_os cid container_id container_running_status containers_impacted_range cps_rating cve_id cvss_score description exploited_status_name exploited_status fix_status image_digest image_id images_impacted_range include_base_image_vuln index_digest package_name_version registry repository severity tag"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Aggregate count of vulnerabilities grouped by csp_rating"""
        return self._call(operation="ReadVulnerabilityCountByCPSRating", query_params={"filter": filter, "limit": limit, "offset": offset}, error_message="ReadVulnerabilityCountByCPSRating failed", member_cid=member_cid)

    def read_vulnerability_count_by_cvss_score(
        self,
        filter: str | None = Field(default=None, description="Filter vulnerabilities using a query in Falcon Query Language (FQL). Supported filter fields: ai_related base_os cid container_id container_running_status containers_impacted_range cps_rating cve_id cvss_score description exploited_status_name exploited_status fix_status image_digest image_id images_impacted_range include_base_image_vuln index_digest package_name_version registry repository severity tag"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Aggregate count of vulnerabilities grouped by CVSS score"""
        return self._call(operation="ReadVulnerabilityCountByCVSSScore", query_params={"filter": filter, "limit": limit, "offset": offset}, error_message="ReadVulnerabilityCountByCVSSScore failed", member_cid=member_cid)

    def read_vulnerability_count_by_severity(
        self,
        filter: str | None = Field(default=None, description="Filter vulnerabilities using a query in Falcon Query Language (FQL). Supported filter fields: ai_related base_os cid container_id container_running_status containers_impacted_range cps_rating cve_id cvss_score description exploited_status_name exploited_status fix_status image_digest image_id images_impacted_range include_base_image_vuln index_digest package_name_version registry repository severity tag"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Aggregate count of vulnerabilities grouped by severity"""
        return self._call(operation="ReadVulnerabilityCountBySeverity", query_params={"filter": filter, "limit": limit, "offset": offset}, error_message="ReadVulnerabilityCountBySeverity failed", member_cid=member_cid)
