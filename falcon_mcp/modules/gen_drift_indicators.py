"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `drift_indicators` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenDriftIndicatorsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `drift_indicators` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_drift_indicators_values_by_date, name="get_drift_indicators_values_by_date")
        self._add_tool(server=server, method=self.read_drift_indicator_entities, name="read_drift_indicator_entities")
        self._add_tool(server=server, method=self.read_drift_indicators_count, name="read_drift_indicators_count")
        self._add_tool(server=server, method=self.search_and_read_drift_indicator_entities, name="search_and_read_drift_indicator_entities")
        self._add_tool(server=server, method=self.search_drift_indicators, name="search_drift_indicators")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def get_drift_indicators_values_by_date(
        self,
        filter: str | None = Field(default=None, description="Filter Drift Indicators using a query in Falcon Query Language (FQL). Supported filter fields: cid cloud_name command_line container_id file_name file_sha256 host_id indicator_process_id namespace occurred_at parent_process_id pod_name prevented scheduler_name severity worker_node_name"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns the count of Drift Indicators by the date. by default it's for 7 days."""
        return self._call(operation="GetDriftIndicatorsValuesByDate", query_params={"filter": filter, "limit": limit}, error_message="GetDriftIndicatorsValuesByDate failed", member_cid=member_cid)

    def read_drift_indicator_entities(
        self,
        ids: list[str] | None = Field(default=None, description="Search Drift Indicators by ids - The maximum amount is 100 IDs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve Drift Indicator entities identified by the provided IDs"""
        return self._call(operation="ReadDriftIndicatorEntities", query_params={"ids": ids}, error_message="ReadDriftIndicatorEntities failed", member_cid=member_cid)

    def read_drift_indicators_count(
        self,
        filter: str | None = Field(default=None, description="Filter Drift Indicators using a query in Falcon Query Language (FQL). Supported filter fields: cid cloud_name command_line container_id file_name file_sha256 host_id indicator_process_id namespace occurred_at parent_process_id pod_name prevented scheduler_name severity worker_node_name"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns the total count of Drift indicators over a time period"""
        return self._call(operation="ReadDriftIndicatorsCount", query_params={"filter": filter}, error_message="ReadDriftIndicatorsCount failed", member_cid=member_cid)

    def search_and_read_drift_indicator_entities(
        self,
        filter: str | None = Field(default=None, description="Filter Drift Indicators using a query in Falcon Query Language (FQL). Supported filter fields: cid cloud_name command_line container_id file_name file_sha256 host_id indicator_process_id namespace occurred_at parent_process_id pod_name prevented scheduler_name severity worker_node_name"),
        sort: str | None = Field(default=None, description="The fields to sort the records on."),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve Drift Indicators by the provided search criteria"""
        return self._call(operation="SearchAndReadDriftIndicatorEntities", query_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset}, error_message="SearchAndReadDriftIndicatorEntities failed", member_cid=member_cid)

    def search_drift_indicators(
        self,
        filter: str | None = Field(default=None, description="Filter Drift Indicators using a query in Falcon Query Language (FQL). Supported filter fields: cid cloud_name command_line container_id file_name file_sha256 host_id indicator_process_id namespace occurred_at parent_process_id pod_name prevented scheduler_name severity worker_node_name"),
        sort: str | None = Field(default=None, description="The fields to sort the records on."),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve all drift indicators that match the given query"""
        return self._call(operation="SearchDriftIndicators", query_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset}, error_message="SearchDriftIndicators failed", member_cid=member_cid)
