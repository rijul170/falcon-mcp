"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `container_packages` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenContainerPackagesModule(GeneratedModuleBase):
    """Generated tools for the Falcon `container_packages` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.read_packages_by_fixable_vuln_count, name="read_packages_by_fixable_vuln_count")
        self._add_tool(server=server, method=self.read_packages_by_image_count, name="read_packages_by_image_count")
        self._add_tool(server=server, method=self.read_packages_by_vuln_count, name="read_packages_by_vuln_count")
        self._add_tool(server=server, method=self.read_packages_combined_export, name="read_packages_combined_export")
        self._add_tool(server=server, method=self.read_packages_combined_v2, name="read_packages_combined_v2")
        self._add_tool(server=server, method=self.read_packages_count_by_zero_day, name="read_packages_count_by_zero_day")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def read_packages_by_fixable_vuln_count(
        self,
        filter: str | None = Field(default=None, description="Filter packages using a query in Falcon Query Language (FQL). Supported filter fields: ai_related cid container_id cveid fix_status image_digest license package_name_version severity type vulnerability_count"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve top x app packages with the most fixable vulnerabilities"""
        return self._call(operation="ReadPackagesByFixableVulnCount", query_params={"filter": filter, "limit": limit, "offset": offset}, error_message="ReadPackagesByFixableVulnCount failed", member_cid=member_cid)

    def read_packages_by_image_count(
        self,
        filter: str | None = Field(default=None, description="Filter packages using a query in Falcon Query Language (FQL). Supported filter fields:ai_related cveid running_images severity type vulnerability_count"),
        limit: int | None = Field(default=None, description="Maximum number of package results to return"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves the N most frequently used packages across images"""
        return self._call(operation="ReadPackagesByImageCount", query_params={"filter": filter, "limit": limit}, error_message="ReadPackagesByImageCount failed", member_cid=member_cid)

    def read_packages_by_vuln_count(
        self,
        filter: str | None = Field(default=None, description="Filter packages using a query in Falcon Query Language (FQL). Supported filter fields: ai_related cid container_id cveid fix_status image_digest license package_name_version severity type vulnerability_count"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve top x packages with the most vulnerabilities"""
        return self._call(operation="ReadPackagesByVulnCount", query_params={"filter": filter, "limit": limit, "offset": offset}, error_message="ReadPackagesByVulnCount failed", member_cid=member_cid)

    def read_packages_combined_export(
        self,
        filter: str | None = Field(default=None, description="Filter packages using a query in Falcon Query Language (FQL). Supported filter fields: ai_related cid container_id cveid fix_status image_digest license package_name_version severity type vulnerability_count"),
        only_zero_day_affected: bool | None = Field(default=None, description="(true/false) load zero day affected packages"),
        sort: str | None = Field(default=None, description="The fields to sort the records on. Supported columns: license package_name_version type vulnerability_count"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves a paginated list of packages identified by the provided filter criteria,used for export.Maximumpage size: 100. Maximum available packages: 10,000"""
        return self._call(operation="ReadPackagesCombinedExport", query_params={"filter": filter, "only_zero_day_affected": only_zero_day_affected, "sort": sort, "limit": limit, "offset": offset}, error_message="ReadPackagesCombinedExport failed", member_cid=member_cid)

    def read_packages_combined_v2(
        self,
        filter: str | None = Field(default=None, description="Filter packages using a query in Falcon Query Language (FQL). Supported filter fields: ai_related cid container_id cveid fix_status image_digest license package_name_version severity type vulnerability_count"),
        only_zero_day_affected: bool | None = Field(default=None, description="(true/false) load zero day affected packages"),
        sort: str | None = Field(default=None, description="The fields to sort the records on. Supported columns: license package_name_version type vulnerability_count"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve packages identified by the provided filter criteria"""
        return self._call(operation="ReadPackagesCombinedV2", query_params={"filter": filter, "only_zero_day_affected": only_zero_day_affected, "sort": sort, "limit": limit, "offset": offset}, error_message="ReadPackagesCombinedV2 failed", member_cid=member_cid)

    def read_packages_count_by_zero_day(
        self,
        filter: str | None = Field(default=None, description="Filter packages using a query in Falcon Query Language (FQL). Supported filter fields: cid"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve packages count affected by zero day vulnerabilities"""
        return self._call(operation="ReadPackagesCountByZeroDay", query_params={"filter": filter}, error_message="ReadPackagesCountByZeroDay failed", member_cid=member_cid)
