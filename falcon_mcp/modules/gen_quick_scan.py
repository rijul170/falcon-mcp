"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `quick_scan` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenQuickScanModule(GeneratedModuleBase):
    """Generated tools for the Falcon `quick_scan` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_scans, name="get_scans")
        self._add_tool(server=server, method=self.query_submissions_mixin0, name="query_submissions_mixin0")
        self._add_tool(server=server, method=self.scan_samples, name="scan_samples", annotations=WRITE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def get_scans(
        self,
        ids: list[str] = Field(description="ID of a submitted scan"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Check the status of a volume scan. Time required for analysis increases with the number of samples in a volume but usually it should take less than 1 minute"""
        return self._call(operation="GetScans", query_params={"ids": ids}, error_message="GetScans failed", member_cid=member_cid)

    def query_submissions_mixin0(
        self,
        filter: str | None = Field(default=None, description="Optional filter and sort criteria in the form of an FQL query. For more information about FQL queries, see [our FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide)."),
        offset: str | None = Field(default=None, description="The offset to start retrieving submissions from."),
        limit: int | None = Field(default=None, description="Maximum number of volume IDs to return. Max: 5000."),
        sort: str | None = Field(default=None, description="Sort order: asc or desc."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Find IDs for submitted scans by providing an FQL filter and paging details. Returns a set of volume IDs that match your criteria."""
        return self._call(operation="QuerySubmissionsMixin0", query_params={"filter": filter, "offset": offset, "limit": limit, "sort": sort}, error_message="QuerySubmissionsMixin0 failed", member_cid=member_cid)

    def scan_samples(
        self,
        body: dict = Field(description="Request JSON body for `ScanSamples` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Submit a volume of files for ml scanning. Time required for analysis increases with the number of samples in a volume but usually it should take less than 1 minute"""
        return self._call(operation="ScanSamples", query_params=None, body_params=body, error_message="ScanSamples failed", member_cid=member_cid)
