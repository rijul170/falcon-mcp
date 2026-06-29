"""
Falcon Complete Dashboard module for Falcon MCP Server.

Provides tools for accessing Falcon Complete (MDR) SOC metrics, aggregated device counts,
incidents, escalations, remediations, allow/block lists, and support issues.
"""

from typing import Any

from mcp.server import FastMCP
from pydantic import Field

from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule

logger = get_logger(__name__)


class FalconCompleteModule(BaseModule):
    """Module for CrowdStrike Falcon Complete Dashboard (MDR SOC metrics)."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.aggregate_fc_alerts, name="aggregate_fc_alerts")
        self._add_tool(server=server, method=self.aggregate_fc_allow_list, name="aggregate_fc_allow_list")
        self._add_tool(server=server, method=self.aggregate_fc_block_list, name="aggregate_fc_block_list")
        self._add_tool(server=server, method=self.aggregate_fc_device_count_collection, name="aggregate_fc_device_count_collection")
        self._add_tool(server=server, method=self.aggregate_fc_total_device_counts, name="aggregate_fc_total_device_counts")
        self._add_tool(server=server, method=self.aggregate_fc_escalations, name="aggregate_fc_escalations")
        self._add_tool(server=server, method=self.aggregate_fc_incidents, name="aggregate_fc_incidents")
        self._add_tool(server=server, method=self.aggregate_fc_prevention_policy, name="aggregate_fc_prevention_policy")
        self._add_tool(server=server, method=self.aggregate_fc_remediations, name="aggregate_fc_remediations")
        self._add_tool(server=server, method=self.aggregate_fc_sensor_update_policy, name="aggregate_fc_sensor_update_policy")
        self._add_tool(server=server, method=self.aggregate_fc_support_issues, name="aggregate_fc_support_issues")
        self._add_tool(server=server, method=self.query_fc_alert_ids, name="query_fc_alert_ids")
        self._add_tool(server=server, method=self.query_fc_allow_list, name="query_fc_allow_list")
        self._add_tool(server=server, method=self.query_fc_block_list, name="query_fc_block_list")
        self._add_tool(server=server, method=self.query_fc_device_count_collections, name="query_fc_device_count_collections")
        self._add_tool(server=server, method=self.query_fc_escalation_ids, name="query_fc_escalation_ids")
        self._add_tool(server=server, method=self.query_fc_incident_ids, name="query_fc_incident_ids")
        self._add_tool(server=server, method=self.query_fc_remediation_ids, name="query_fc_remediation_ids")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def _fc_aggregate(self, operation: str, filter_body: dict[str, Any]) -> list[dict[str, Any]] | dict[str, Any]:
        result = self._base_query_api_call(
            operation=operation,
            body_params=filter_body,
            error_message=f"Failed to get Falcon Complete aggregate: {operation}",
        )
        if self._is_error(result):
            return [result]
        return result

    def _fc_query(self, operation: str, filter: str | None, limit: int, offset: int, sort: str | None) -> list[dict[str, Any]] | dict[str, Any]:
        result = self._base_search_api_call(
            operation=operation,
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message=f"Failed to query Falcon Complete: {operation}",
        )
        if self._is_error(result):
            return [result]
        return result

    def aggregate_fc_alerts(
        self,
        filter_body: dict[str, Any] = Field(
            default_factory=dict,
            description=(
                "Aggregate filter body. Optional fields: `filter` (FQL string), "
                "`date_range_filter` ({\"from\": \"ISO8601\", \"to\": \"ISO8601\"}), "
                "`limit` (int), `offset` (int)."
            ),
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get aggregated Falcon Complete alert metrics.

        Returns alert counts and trends for the Falcon Complete SOC dashboard.
        Requires Falcon Complete (MDR) subscription.
        """
        return self._fc_aggregate("AggregateAlerts", filter_body)

    def aggregate_fc_allow_list(
        self,
        filter_body: dict[str, Any] = Field(
            default_factory=dict,
            description="Aggregate filter body (see `falcon_aggregate_fc_alerts` for body structure).",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get aggregated Falcon Complete allow-list metrics."""
        return self._fc_aggregate("AggregateAllowList", filter_body)

    def aggregate_fc_block_list(
        self,
        filter_body: dict[str, Any] = Field(
            default_factory=dict,
            description="Aggregate filter body (see `falcon_aggregate_fc_alerts` for body structure).",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get aggregated Falcon Complete block-list metrics."""
        return self._fc_aggregate("AggregateBlockList", filter_body)

    def aggregate_fc_device_count_collection(
        self,
        filter_body: dict[str, Any] = Field(
            default_factory=dict,
            description="Aggregate filter body (see `falcon_aggregate_fc_alerts` for body structure).",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get aggregated Falcon Complete device count collection metrics."""
        return self._fc_aggregate("AggregateDeviceCountCollection", filter_body)

    def aggregate_fc_total_device_counts(
        self,
        filter_body: dict[str, Any] = Field(
            default_factory=dict,
            description="Aggregate filter body (see `falcon_aggregate_fc_alerts` for body structure).",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get total device counts from the Falcon Complete Dashboard."""
        return self._fc_aggregate("AggregateTotalDeviceCounts", filter_body)

    def aggregate_fc_escalations(
        self,
        filter_body: dict[str, Any] = Field(
            default_factory=dict,
            description="Aggregate filter body (see `falcon_aggregate_fc_alerts` for body structure).",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get aggregated Falcon Complete case escalation metrics."""
        return self._fc_aggregate("AggregateEscalations", filter_body)

    def aggregate_fc_incidents(
        self,
        filter_body: dict[str, Any] = Field(
            default_factory=dict,
            description="Aggregate filter body (see `falcon_aggregate_fc_alerts` for body structure).",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get aggregated Falcon Complete incident metrics."""
        return self._fc_aggregate("AggregateFCIncidents", filter_body)

    def aggregate_fc_prevention_policy(
        self,
        filter_body: dict[str, Any] = Field(
            default_factory=dict,
            description="Aggregate filter body (see `falcon_aggregate_fc_alerts` for body structure).",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get aggregated Falcon Complete prevention policy metrics."""
        return self._fc_aggregate("AggregatePreventionPolicy", filter_body)

    def aggregate_fc_remediations(
        self,
        filter_body: dict[str, Any] = Field(
            default_factory=dict,
            description="Aggregate filter body (see `falcon_aggregate_fc_alerts` for body structure).",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get aggregated Falcon Complete remediation metrics."""
        return self._fc_aggregate("AggregateRemediations", filter_body)

    def aggregate_fc_sensor_update_policy(
        self,
        filter_body: dict[str, Any] = Field(
            default_factory=dict,
            description="Aggregate filter body (see `falcon_aggregate_fc_alerts` for body structure).",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get aggregated Falcon Complete sensor update policy metrics."""
        return self._fc_aggregate("AggregateSensorUpdatePolicy", filter_body)

    def aggregate_fc_support_issues(
        self,
        filter_body: dict[str, Any] = Field(
            default_factory=dict,
            description="Aggregate filter body (see `falcon_aggregate_fc_alerts` for body structure).",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get aggregated Falcon Complete support issue metrics."""
        return self._fc_aggregate("AggregateSupportIssues", filter_body)

    def query_fc_alert_ids(
        self,
        filter: str | None = Field(default=None, description="FQL filter for alerts."),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Query Falcon Complete alert IDs by FQL filter.

        Returns alert IDs which can be resolved via `falcon_get_detection_details`.
        """
        return self._fc_query("QueryAlertIdsByFilterV2", filter, limit, offset, sort)

    def query_fc_allow_list(
        self,
        filter: str | None = Field(default=None, description="FQL filter."),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Query Falcon Complete allow-list entries by FQL filter."""
        return self._fc_query("QueryAllowListFilter", filter, limit, offset, sort)

    def query_fc_block_list(
        self,
        filter: str | None = Field(default=None, description="FQL filter."),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Query Falcon Complete block-list entries by FQL filter."""
        return self._fc_query("QueryBlockListFilter", filter, limit, offset, sort)

    def query_fc_device_count_collections(
        self,
        filter: str | None = Field(default=None, description="FQL filter."),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Query Falcon Complete device count collection IDs by FQL filter."""
        return self._fc_query("GetDeviceCountCollectionQueriesByFilter", filter, limit, offset, sort)

    def query_fc_escalation_ids(
        self,
        filter: str | None = Field(default=None, description="FQL filter."),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Query Falcon Complete escalation IDs by FQL filter."""
        return self._fc_query("QueryEscalationsFilter", filter, limit, offset, sort)

    def query_fc_incident_ids(
        self,
        filter: str | None = Field(default=None, description="FQL filter."),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Query Falcon Complete incident IDs by FQL filter.

        Returns IDs resolvable via `falcon_get_incident_details`.
        """
        return self._fc_query("QueryIncidentIdsByFilter", filter, limit, offset, sort)

    def query_fc_remediation_ids(
        self,
        filter: str | None = Field(default=None, description="FQL filter."),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Query Falcon Complete remediation IDs by FQL filter."""
        return self._fc_query("QueryRemediationsFilter", filter, limit, offset, sort)
