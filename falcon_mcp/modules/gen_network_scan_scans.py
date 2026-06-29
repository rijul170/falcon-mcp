"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `network_scan_scans` API service collection.

FalconPy note: FalconPy 1.6.1 does not include a dedicated NetworkScan service class.
These tools call the /netscan/ endpoints via the APIHarnessV2 uber-class using operation IDs
sourced directly from the CrowdStrike API reference:
  https://developer.crowdstrike.com/api-reference/collections/network-scan-scans/
Required OAuth2 scope: Network scanning: READ (reads) / WRITE (creates, updates, deletes).
"""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenNetworkScanScansModule(GeneratedModuleBase):
    """Generated tools for the Falcon `network_scan_scans` collection.

    Covers the /netscan/aggregates/scans, /netscan/entities/scans, and
    /netscan/queries/scans endpoints.
    """

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.aggregate_scans, name="aggregate_scans")
        self._add_tool(server=server, method=self.get_scans, name="get_scans")
        self._add_tool(server=server, method=self.query_scans, name="query_scans")
        self._add_tool(server=server, method=self.create_scans, name="create_scans", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_scans, name="update_scans", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_scans, name="delete_scans", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def aggregate_scans(
        self,
        body: dict = Field(description="Request JSON body for `aggregate_scans` per the CrowdStrike API schema. Supports fields: date_ranges, exclude, extended_bounds, field, filter, filters_spec, from, include, interval, max_doc_count, min_doc_count, missing, name, percents, q, ranges, size, sort, sub_aggregates, time_zone, type."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns 'scans' aggregations. POSTs to /netscan/aggregates/scans/GET/v1.
        Requires OAuth2 scope: Network scanning: READ."""
        return self._call(operation="aggregate_scansMixin0", query_params=None, body_params=body, error_message="aggregate_scans failed", member_cid=member_cid)

    def get_scans(
        self,
        ids: list[str] = Field(description="IDs of 'scans' to be retrieved (Min: 1, Max: 100)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get 'scans' by their IDs. GETs /netscan/entities/scans/v1.
        Requires OAuth2 scope: Network scanning: READ."""
        return self._call(operation="get_scans", query_params={"ids": ids}, error_message="get_scans failed", member_cid=member_cid)

    def create_scans(
        self,
        body: dict = Field(description="Request JSON body for `create_scans` per the CrowdStrike API schema. Supported fields: block_windows (object), credentialed (bool), credentials (object), description (str), fragile_device_detection (bool), name (str), scheduling (object), target_asset (object), target_asset_filter (object), target_external_ip (object), target_ip (object), target_type (str), template_id (str)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create 'scans' using provided specifications. POSTs to /netscan/entities/scans/v1.
        Requires OAuth2 scope: Network scanning: WRITE."""
        return self._call(operation="create_scans", query_params=None, body_params=body, error_message="create_scans failed", member_cid=member_cid)

    def delete_scans(
        self,
        ids: list[str] = Field(description="IDs of 'scans' to be deleted (Min: 1, Max: 100)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete 'scans' by their IDs. DELETEs /netscan/entities/scans/v1.
        Requires OAuth2 scope: Network scanning: WRITE."""
        return self._call(operation="delete_scans", query_params={"ids": ids}, error_message="delete_scans failed", member_cid=member_cid)

    def update_scans(
        self,
        body: dict = Field(description="Request JSON body for `update_scans` per the CrowdStrike API schema. Supported fields: id (str, required — the scan to update), block_windows (object), credentialed (bool), credentials (object), description (str), fragile_device_detection (bool), name (str), scheduling (object), target_asset (object), target_asset_filter (object), target_external_ip (object), target_ip (object), target_type (str), template_id (str)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update 'scans' using provided specifications. PATCHes /netscan/entities/scans/v1.
        Requires OAuth2 scope: Network scanning: WRITE."""
        return self._call(operation="update_scans", query_params=None, body_params=body, error_message="update_scans failed", member_cid=member_cid)

    def query_scans(
        self,
        offset: int | None = Field(default=None, description="Starting index for pagination. Do not provide on the first request."),
        limit: int | None = Field(default=None, description="Number of scan IDs to return (Min: 1, Max: 100, Default: 100)."),
        sort: str | None = Field(default=None, description="Sort 'scans' by their properties. A single sort field is allowed."),
        filter: str | None = Field(default=None, description="FQL filter to search for 'scans'. Example: `name:'my-scan'`"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get 'scan IDs' by filter. GETs /netscan/queries/scans/v1.
        Requires OAuth2 scope: Network scanning: READ."""
        return self._call(operation="query_scansMixin0", query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter}, error_message="query_scans failed", member_cid=member_cid)
