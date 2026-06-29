"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `sensor_usage` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenSensorUsageModule(GeneratedModuleBase):
    """Generated tools for the Falcon `sensor_usage` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_sensor_usage_hourly, name="get_sensor_usage_hourly")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def get_sensor_usage_hourly(
        self,
        filter: str | None = Field(default=None, description="The FQL search filter. Allowed fields: 'event_date' : A specified date that will be final date of the results returned. Specified date cannot be after the default. Format: '2024-06-11' Default: the current date, minus 2 days, in UTC 'period' : An integer surrounded by single quotes representing the number of days to return. Format: '30' Default: '28' Minimum: '1' Maximum: '395' 'selected_cids' : A comma separated list of CIDs to return data for. Caller must be a parent CID or have special access enabled. Format: 'cid_1,cid_2,cid_3' Default: for parent CIDs the default is the parent and all children, otherwise the current CID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Fetches hourly average. Each data point represents the average of how many unique AIDs were seen per hour for the previous 28 days."""
        return self._call(operation="GetSensorUsageHourly", query_params={"filter": filter}, error_message="GetSensorUsageHourly failed", member_cid=member_cid)
