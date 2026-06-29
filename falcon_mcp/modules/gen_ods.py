"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `ods` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenOdsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `ods` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.aggregate_scans, name="aggregate_scans")
        self._add_tool(server=server, method=self.aggregate_scan_host_metadata, name="aggregate_scan_host_metadata")
        self._add_tool(server=server, method=self.aggregate_scheduled_scans, name="aggregate_scheduled_scans")
        self._add_tool(server=server, method=self.delete_scheduled_scans, name="delete_scheduled_scans", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.schedule_scan, name="schedule_scan", annotations=WRITE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def aggregate_scans(
        self,
        body: dict = Field(description="Aggregate query body per the CrowdStrike API schema. Supports fields: date_ranges, exclude, field, filter, from, include, interval, min_doc_count, missing, name, q, ranges, size, sort, sub_aggregates, time_zone, type."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get aggregate scan statistics (POST /ods/aggregates/scans/v1). Use for dashboarding scan counts by status, host, severity, etc."""
        return self._call(operation="aggregate_scans", query_params=None, body_params=body, error_message="aggregate_scans failed", member_cid=member_cid)

    def aggregate_scan_host_metadata(
        self,
        body: dict = Field(description="Aggregate query body per the CrowdStrike API schema."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get aggregate scan host metadata statistics (POST /ods/aggregates/scan-hosts/v1). Useful for coverage reporting across endpoints."""
        return self._call(operation="aggregate_query_scan_host_metadata", query_params=None, body_params=body, error_message="aggregate_query_scan_host_metadata failed", member_cid=member_cid)

    def aggregate_scheduled_scans(
        self,
        body: dict = Field(description="Aggregate query body per the CrowdStrike API schema."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get aggregate scheduled scan statistics (POST /ods/aggregates/scheduled-scans/v1)."""
        return self._call(operation="aggregate_scheduled_scans", query_params=None, body_params=body, error_message="aggregate_scheduled_scans failed", member_cid=member_cid)

    def delete_scheduled_scans(
        self,
        ids: list[str] = Field(description="The scan IDs to retrieve the scan entities"),
        filter: str | None = Field(default=None, description="A FQL compatible query string."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete ODS scheduled-scans for the given scheduled-scan ids."""
        return self._call(operation="delete_scheduled_scans", query_params={"ids": ids, "filter": filter}, error_message="delete_scheduled_scans failed", member_cid=member_cid)

    def schedule_scan(
        self,
        body: dict = Field(description="Request JSON body for `schedule_scan` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create ODS scan and start or schedule scan for the given scan request."""
        return self._call(operation="schedule_scan", query_params=None, body_params=body, error_message="schedule_scan failed", member_cid=member_cid)
