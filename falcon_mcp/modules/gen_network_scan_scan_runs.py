"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `network_scan_scan_runs` API service collection.

FalconPy note: FalconPy 1.6.1 does not include a dedicated NetworkScan service class.
These tools call the /netscan/ endpoints via the APIHarnessV2 uber-class using operation IDs
sourced directly from the CrowdStrike API reference:
  https://developer.crowdstrike.com/api-reference/collections/network-scan-scan-runs/
Required OAuth2 scope: Network scanning: READ (reads) / WRITE (creates, updates).
"""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenNetworkScanScanRunsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `network_scan_scan_runs` collection.

    Covers the /netscan/aggregates/scan-runs, /netscan/entities/scan-runs, and
    /netscan/queries/scan-runs endpoints.
    """

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.aggregate_scan_runs, name="aggregate_scan_runs")
        self._add_tool(server=server, method=self.get_scan_runs, name="get_scan_runs")
        self._add_tool(server=server, method=self.query_scan_runs, name="query_scan_runs")
        self._add_tool(server=server, method=self.create_scan_runs, name="create_scan_runs", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_scan_runs, name="update_scan_runs", annotations=WRITE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def aggregate_scan_runs(
        self,
        body: dict = Field(description="Request JSON body for `aggregate_scan_runs` per the CrowdStrike API schema. Supports fields: date_ranges, exclude, extended_bounds, field, filter, filters_spec, from, include, interval, max_doc_count, min_doc_count, missing, name, percents, q, ranges, size, sort, sub_aggregates, time_zone, type."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns 'scan-runs' aggregations. POSTs to /netscan/aggregates/scan-runs/GET/v1.
        Requires OAuth2 scope: Network scanning: READ."""
        return self._call(operation="aggregate_scan_runs", query_params=None, body_params=body, error_message="aggregate_scan_runs failed", member_cid=member_cid)

    def get_scan_runs(
        self,
        ids: list[str] = Field(description="IDs of 'scan-runs' to be retrieved (Min: 1, Max: 100)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get 'scan-runs' by their IDs. GETs /netscan/entities/scan-runs/v1.
        Requires OAuth2 scope: Network scanning: READ."""
        return self._call(operation="get_scan_runs", query_params={"ids": ids}, error_message="get_scan_runs failed", member_cid=member_cid)

    def create_scan_runs(
        self,
        body: dict = Field(description="Request JSON body for `create_scan_runs` per the CrowdStrike API schema. Supported fields: scan_id (str — the scan ID based on which to create a scan run), config (object — the scan run configuration)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create 'scan-runs' using provided specifications. POSTs to /netscan/entities/scan-runs/v1.
        Requires OAuth2 scope: Network scanning: WRITE."""
        return self._call(operation="create_scan_runs", query_params=None, body_params=body, error_message="create_scan_runs failed", member_cid=member_cid)

    def update_scan_runs(
        self,
        body: dict = Field(description="Request JSON body for `update_scan_runs` per the CrowdStrike API schema. Supported fields: id (str — the ID of the scan run to update), action (str — the action to be performed for the scan run, e.g. 'pause', 'resume', 'cancel')."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update 'scan-runs' using provided specifications (e.g. pause, resume, cancel a run).
        PATCHes /netscan/entities/scan-runs/v1.
        Requires OAuth2 scope: Network scanning: WRITE."""
        return self._call(operation="update_scan_runs", query_params=None, body_params=body, error_message="update_scan_runs failed", member_cid=member_cid)

    def query_scan_runs(
        self,
        offset: int | None = Field(default=None, description="Starting index for pagination. Do not provide on the first request."),
        limit: int | None = Field(default=None, description="Number of scan-run IDs to return (Min: 1, Max: 100, Default: 100)."),
        sort: str | None = Field(default=None, description="Sort 'scan-runs' by their properties. A single sort field is allowed."),
        filter: str | None = Field(default=None, description="FQL filter to search for 'scan-runs'. Example: `scan_id:'<id>'`"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get 'scan-run IDs' by filter. GETs /netscan/queries/scan-runs/v1.
        Requires OAuth2 scope: Network scanning: READ."""
        return self._call(operation="query_scan_runs", query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter}, error_message="query_scan_runs failed", member_cid=member_cid)
