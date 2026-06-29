"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `container_alerts` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenContainerAlertsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `container_alerts` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.read_container_alerts_count, name="read_container_alerts_count")
        self._add_tool(server=server, method=self.read_container_alerts_count_by_severity, name="read_container_alerts_count_by_severity")
        self._add_tool(server=server, method=self.search_and_read_container_alerts, name="search_and_read_container_alerts")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def read_container_alerts_count(
        self,
        filter: str | None = Field(default=None, description="Search Container Alerts using a query in Falcon Query Language (FQL). Supported filter fields: cid container_id last_seen"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search Container Alerts by the provided search criteria"""
        return self._call(operation="ReadContainerAlertsCount", query_params={"filter": filter}, error_message="ReadContainerAlertsCount failed", member_cid=member_cid)

    def read_container_alerts_count_by_severity(
        self,
        filter: str | None = Field(default=None, description="Search Container Alerts using a query in Falcon Query Language (FQL). Supported filter fields: cid container_id last_seen"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get Container Alerts counts by severity"""
        return self._call(operation="ReadContainerAlertsCountBySeverity", query_params={"filter": filter}, error_message="ReadContainerAlertsCountBySeverity failed", member_cid=member_cid)

    def search_and_read_container_alerts(
        self,
        filter: str | None = Field(default=None, description="Search Container Alerts using a query in Falcon Query Language (FQL). Supported filter fields: cid container_id last_seen name severity"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        sort: str | None = Field(default=None, description="The fields to sort the records on."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search Container Alerts by the provided search criteria"""
        return self._call(operation="SearchAndReadContainerAlerts", query_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort}, error_message="SearchAndReadContainerAlerts failed", member_cid=member_cid)
