"""
Alerts module for Falcon MCP Server.

Provides tools for the unified Falcon Alerts API (the "Epp" unified alerts surface):
search/query alerts with details, retrieve full alert entities, take actions on alerts
(update status, assign, tag, comment), and run aggregations.
"""

from typing import Any

from mcp.server import FastMCP
from mcp.server.fastmcp.resources import TextResource
from mcp.types import ToolAnnotations
from pydantic import AnyUrl, Field

from falcon_mcp.common.errors import _format_error_response
from falcon_mcp.common.logging import get_logger
from falcon_mcp.common.utils import prepare_api_parameters
from falcon_mcp.modules.base import BaseModule
from falcon_mcp.resources.alerts import SEARCH_ALERTS_FQL_DOCUMENTATION

logger = get_logger(__name__)

# update_alerts mutates state but is not destructive (no deletion). Re-applying the
# same action yields the same end state, so idempotentHint=True.
UPDATE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=False, idempotentHint=True, openWorldHint=True,
)


class AlertsModule(BaseModule):
    """Module for CrowdStrike Falcon unified Alerts."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.search_alerts, name="search_alerts")
        self._add_tool(server=server, method=self.get_alert_details, name="get_alert_details")
        self._add_tool(server=server, method=self.aggregate_alerts, name="aggregate_alerts")
        self._add_tool(
            server=server, method=self.update_alerts, name="update_alerts",
            annotations=UPDATE_ANNOTATIONS,
        )

    def register_resources(self, server: FastMCP) -> None:
        search_alerts_fql_resource = TextResource(
            uri=AnyUrl("falcon://alerts/fql-guide"),
            name="falcon_search_alerts_fql_guide",
            description="Contains the guide for the `filter` param of the `falcon_search_alerts` tool.",
            text=SEARCH_ALERTS_FQL_DOCUMENTATION,
        )
        self._add_resource(server, search_alerts_fql_resource)

    def search_alerts(
        self,
        filter: str | None = Field(
            default=None,
            description=(
                "FQL filter. Common fields: `status` ('new','in_progress','closed','reopened'), "
                "`severity` (1-100 integer), `assigned_to_name`, `product`, `pattern_id`, "
                "`tactic`, `technique`, `aggregate_id`, `composite_id`, `created_timestamp`, "
                "`timestamp`, `tags`. Example: `status:'new'+severity:>=50`"
            ),
        ),
        limit: int = Field(default=100, ge=1, le=10000, description="Max alert IDs to query."),
        offset: int | None = Field(default=None, description="Offset for pagination."),
        sort: str | None = Field(
            default=None,
            description="Sort expression. Examples: `created_timestamp|desc`, `severity|desc`.",
        ),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search unified Falcon alerts and return full alert entities.

        Queries alert IDs (composite_ids) matching the FQL filter, then hydrates them
        into full alert objects in a single call. Covers EDR/NGAV, identity, mobile,
        and other detection sources surfaced through the unified Alerts API.
        """
        id_response = self._base_query_api_call(
            operation="GetQueriesAlertsV2",
            query_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to query alerts",
            member_cid=member_cid,
        )
        if self._is_error(id_response):
            return self._format_fql_error_response([id_response], filter, SEARCH_ALERTS_FQL_DOCUMENTATION)
        if not id_response:
            return self._format_fql_error_response([], filter, SEARCH_ALERTS_FQL_DOCUMENTATION)
        return self._base_query_api_call(
            operation="PostEntitiesAlertsV2",
            body_params={"composite_ids": id_response},
            error_message="Failed to retrieve alert details",
            member_cid=member_cid,
        )

    def get_alert_details(
        self,
        composite_ids: list[str] = Field(
            description="Alert composite IDs to retrieve. Obtain from `falcon_search_alerts`.",
        ),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get full details for specific unified alerts by composite ID."""
        if not composite_ids:
            return []
        return self._base_query_api_call(
            operation="PostEntitiesAlertsV2",
            body_params={"composite_ids": composite_ids},
            error_message="Failed to retrieve alert details",
            member_cid=member_cid,
        )

    def aggregate_alerts(
        self,
        date_ranges: list[dict[str, str]] | None = Field(
            default=None,
            description="Date range buckets, e.g. `[{'from':'2024-01-01T00:00:00Z','to':'2024-02-01T00:00:00Z'}]`.",
        ),
        field: str | None = Field(
            default=None,
            description="Field to aggregate on, e.g. `severity`, `status`, `tactic`, `product`.",
        ),
        filter: str | None = Field(default=None, description="FQL filter to scope the aggregation."),
        type: str | None = Field(
            default=None,
            description="Aggregation type, e.g. `terms`, `date_range`, `count`. Default `terms`.",
        ),
        interval: str | None = Field(default=None, description="Interval for date_histogram (e.g. `day`, `week`)."),
        size: int | None = Field(default=None, description="Max number of buckets to return."),
        name: str = Field(default="alerts_aggregate", description="Label for this aggregation."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Run an aggregation over unified alerts.

        Useful for dashboards: counts by severity/status/tactic, alert volume over time, etc.
        """
        agg: dict[str, Any] = {"name": name, "type": type or "terms"}
        if field is not None:
            agg["field"] = field
        if filter is not None:
            agg["filter"] = filter
        if date_ranges is not None:
            agg["date_ranges"] = date_ranges
        if interval is not None:
            agg["interval"] = interval
        if size is not None:
            agg["size"] = size
        # PostAggregatesAlertsV2 expects a JSON list body; prepare_api_parameters only
        # accepts dicts, so call the client directly with the list body.
        from falcon_mcp.common.errors import handle_api_response
        response = self.client.command_for(
            "PostAggregatesAlertsV2", member_cid=member_cid, body=[agg],
        )
        return handle_api_response(
            response,
            operation="PostAggregatesAlertsV2",
            error_message="Failed to aggregate alerts",
            default_result=[],
        )

    def update_alerts(
        self,
        composite_ids: list[str] = Field(
            description="Alert composite IDs to act on. Obtain from `falcon_search_alerts`.",
        ),
        update_status: str | None = Field(
            default=None,
            description="New status: 'new', 'in_progress', 'closed', or 'reopened'.",
        ),
        assign_to_uuid: str | None = Field(default=None, description="User UUID to assign the alerts to."),
        assign_to_name: str | None = Field(default=None, description="User display name to assign the alerts to."),
        unassign: bool = Field(default=False, description="If true, remove any current assignee."),
        add_tag: str | None = Field(default=None, description="Tag to add to the alerts."),
        remove_tag: str | None = Field(default=None, description="Tag to remove from the alerts."),
        append_comment: str | None = Field(default=None, description="Comment to append to the alerts."),
        show_in_ui: bool | None = Field(default=None, description="Set the show_in_ui flag."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Take action on unified alerts: set status, assign/unassign, tag, or comment.

        Builds the v3 PATCH action_parameters payload from the supplied options. At least
        one action must be specified. Multiple actions are applied in a single request.
        """
        actions: list[dict[str, str]] = []
        if update_status is not None:
            actions.append({"name": "update_status", "value": update_status})
        if assign_to_uuid is not None:
            actions.append({"name": "assign_to_uuid", "value": assign_to_uuid})
        if assign_to_name is not None:
            actions.append({"name": "assign_to_name", "value": assign_to_name})
        if unassign:
            actions.append({"name": "unassign", "value": ""})
        if add_tag is not None:
            actions.append({"name": "add_tag", "value": add_tag})
        if remove_tag is not None:
            actions.append({"name": "remove_tag", "value": remove_tag})
        if append_comment is not None:
            actions.append({"name": "append_comment", "value": append_comment})
        if show_in_ui is not None:
            actions.append({"name": "show_in_ui", "value": "true" if show_in_ui else "false"})

        if not actions:
            return [_format_error_response(
                "Specify at least one action (update_status, assign_to_uuid, assign_to_name, "
                "unassign, add_tag, remove_tag, append_comment, or show_in_ui).",
                operation="PatchEntitiesAlertsV3",
            )]

        body = prepare_api_parameters({
            "composite_ids": composite_ids,
            "action_parameters": actions,
        })
        result = self._base_query_api_call(
            operation="PatchEntitiesAlertsV3",
            body_params=body,
            error_message="Failed to update alerts",
            member_cid=member_cid,
        )
        if self._is_error(result):
            return [result]
        return result
