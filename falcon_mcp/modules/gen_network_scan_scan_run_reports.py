"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `network_scan_scan_run_reports` API service collection.

FalconPy note: FalconPy 1.6.1 does not include a dedicated NetworkScan service class.
These tools call the /netscan/ endpoints via the APIHarnessV2 uber-class using operation IDs
sourced directly from the CrowdStrike API reference:
  https://developer.crowdstrike.com/api-reference/collections/network-scan-scan-run-reports/
Required OAuth2 scope: Network scanning: READ.
"""

from mcp.server import FastMCP
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase


class GenNetworkScanScanRunReportsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `network_scan_scan_run_reports` collection.

    Covers the /netscan/entities/scan-run-reports endpoint.
    """

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_scan_run_reports, name="get_scan_run_reports")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def get_scan_run_reports(
        self,
        id: str = Field(description="Scan run ID for which the report is to be fetched (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Downloads a scan run report in CSV format. GETs /netscan/entities/scan-run-reports/v1.
        Requires OAuth2 scope: Network scanning: READ.

        Note: the API produces CSV content. The raw response will be returned as-is;
        callers should expect a string payload rather than the standard resources/errors envelope."""
        return self._call(operation="get_scan_run_reports", query_params={"id": id}, error_message="get_scan_run_reports failed", member_cid=member_cid)
