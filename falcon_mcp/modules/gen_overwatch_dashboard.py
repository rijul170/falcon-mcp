"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `overwatch_dashboard` API service collection.

DEPRECATION NOTICE: The Overwatch Dashboard service collection is marked deprecated
by CrowdStrike. Tools are registered but callers should plan for future removal.

NOTE: This service collection is NOT present in FalconPy's endpoint registry.
All operations therefore use the APIHarnessV2 ``override`` kwarg
(format: 'METHOD,/path') to bypass the registry lookup.

API docs: https://developer.crowdstrike.com/api-reference/collections/overwatch-dashboard/
Required scope: Overwatch Dashboard: READ (all five operations)
"""

from typing import Any

from mcp.server import FastMCP
from pydantic import Field

from falcon_mcp.common.errors import handle_api_response
from falcon_mcp.common.logging import get_logger
from falcon_mcp.common.utils import prepare_api_parameters
from falcon_mcp.common.generated_base import GeneratedModuleBase

logger = get_logger(__name__)

# Endpoint paths (all under /overwatch-dashboards/)
_EP_DETECTIONS_GLOBAL_COUNTS = "/overwatch-dashboards/aggregates/detections-global-counts/v1"
_EP_EVENTS_COLLECTIONS = "/overwatch-dashboards/aggregates/events-collections/GET/v1"
_EP_EVENTS = "/overwatch-dashboards/aggregates/events/GET/v1"
_EP_INCIDENTS_GLOBAL_COUNTS = "/overwatch-dashboards/aggregates/incidents-global-counts/v1"
_EP_OW_EVENTS_GLOBAL_COUNTS = "/overwatch-dashboards/aggregates/ow-events-global-counts/v1"


class GenOverwatchDashboardModule(GeneratedModuleBase):
    """Generated tools for the Falcon ``overwatch_dashboard`` collection (deprecated).

    Because FalconPy's endpoint registry does not include this service collection,
    calls go through the Uber class ``override`` mechanism.
    """

    # ------------------------------------------------------------------
    # Internal helper — uses the Uber class override to bypass the
    # FalconPy operation registry for endpoints not yet (or no longer)
    # bundled in the installed FalconPy release.
    # ------------------------------------------------------------------
    def _override_call(
        self,
        method: str,
        path: str,
        *,
        query_params: dict[str, Any] | None = None,
        body_params: dict[str, Any] | None = None,
        operation_label: str = "operation",
        member_cid: str | None = None,
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Issue an API call via the Uber class ``override`` kwarg.

        Args:
            method: HTTP method string (GET, POST, …).
            path: Absolute API path.
            query_params: Dict of query-string parameters (None values stripped).
            body_params: Dict of body parameters (None values stripped).
            operation_label: Human-readable label used in error messages.
            member_cid: Optional child CID for MSSP tenant scoping.

        Returns:
            Parsed API response resources list, or an error dict.
        """
        call_args: dict[str, Any] = {"override": f"{method.upper()},{path}"}

        if query_params:
            call_args["parameters"] = prepare_api_parameters(query_params)

        if body_params:
            call_args["body"] = prepare_api_parameters(body_params)

        logger.debug("override_call %s %s member_cid=%s args=%s", method, path, member_cid, call_args)

        response = self.client.command_for(operation_label, member_cid=member_cid, **call_args)

        return handle_api_response(
            response,
            operation=operation_label,
            error_message=f"{operation_label} failed",
            default_result=[],
        )

    # ------------------------------------------------------------------
    # Tool registration
    # ------------------------------------------------------------------
    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.aggregates_detections_global_counts, name="aggregates_detections_global_counts")
        self._add_tool(server=server, method=self.aggregates_events_collections, name="aggregates_events_collections")
        self._add_tool(server=server, method=self.aggregates_events, name="aggregates_events")
        self._add_tool(server=server, method=self.aggregates_incidents_global_counts, name="aggregates_incidents_global_counts")
        self._add_tool(server=server, method=self.aggregates_events_global_counts, name="aggregates_events_global_counts")

    def register_resources(self, server: FastMCP) -> None:
        pass

    # ------------------------------------------------------------------
    # Operations
    # ------------------------------------------------------------------
    def aggregates_detections_global_counts(
        self,
        filter: str | None = Field(default=None, description="FQL query expression to limit results. Example: \"timestamp:>'now-7d'\"."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get the total number of OverWatch detections pushed across all customers. (DEPRECATED)

        Endpoint: GET /overwatch-dashboards/aggregates/detections-global-counts/v1
        Required scope: Overwatch Dashboard: READ
        """
        return self._override_call(
            "GET",
            _EP_DETECTIONS_GLOBAL_COUNTS,
            query_params={"filter": filter},
            operation_label="AggregatesDetectionsGlobalCounts",
            member_cid=member_cid,
        )

    def aggregates_events_collections(
        self,
        body: dict = Field(description=(
            "Aggregate query body. Supported keys: date_ranges (list), exclude (str), "
            "field (str), filter (str, FQL), from (int), include (str), interval (str), "
            "max_doc_count (int), min_doc_count (int), missing (str), name (str), q (str), "
            "ranges (list), size (int), sub_aggregates (list), sort (str), time_zone (str), "
            "type (str — one of: date_histogram, date_range, terms, range, cardinality, "
            "max, min, avg, sum, percentiles)."
        )),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get OverWatch detection event collection info by providing an aggregate query. (DEPRECATED)

        Endpoint: POST /overwatch-dashboards/aggregates/events-collections/GET/v1
        Required scope: Overwatch Dashboard: READ
        """
        return self._override_call(
            "POST",
            _EP_EVENTS_COLLECTIONS,
            body_params=body,
            operation_label="AggregatesEventsCollections",
            member_cid=member_cid,
        )

    def aggregates_events(
        self,
        body: dict = Field(description=(
            "Aggregate query body. Supported keys: date_ranges (list), exclude (str), "
            "field (str), filter (str, FQL), from (int), include (str), interval (str), "
            "max_doc_count (int), min_doc_count (int), missing (str), name (str), q (str), "
            "ranges (list), size (int), sub_aggregates (list), sort (str), time_zone (str), "
            "type (str — one of: date_histogram, date_range, terms, range, cardinality, "
            "max, min, avg, sum, percentiles)."
        )),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get aggregate OverWatch detection event info by providing an aggregate query. (DEPRECATED)

        Endpoint: POST /overwatch-dashboards/aggregates/events/GET/v1
        Required scope: Overwatch Dashboard: READ
        """
        return self._override_call(
            "POST",
            _EP_EVENTS,
            body_params=body,
            operation_label="AggregatesEvents",
            member_cid=member_cid,
        )

    def aggregates_incidents_global_counts(
        self,
        filter: str | None = Field(default=None, description="FQL query expression to limit results. Example: \"timestamp:>'now-7d'\"."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get the total number of OverWatch incidents pushed across all customers. (DEPRECATED)

        Endpoint: GET /overwatch-dashboards/aggregates/incidents-global-counts/v1
        Required scope: Overwatch Dashboard: READ
        """
        return self._override_call(
            "GET",
            _EP_INCIDENTS_GLOBAL_COUNTS,
            query_params={"filter": filter},
            operation_label="AggregatesIncidentsGlobalCounts",
            member_cid=member_cid,
        )

    def aggregates_events_global_counts(
        self,
        filter: str | None = Field(default=None, description="FQL query expression to limit results. Example: \"timestamp:>'now-7d'\"."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get the total number of OverWatch events across all customers. (DEPRECATED)

        Endpoint: GET /overwatch-dashboards/aggregates/ow-events-global-counts/v1
        Required scope: Overwatch Dashboard: READ
        """
        return self._override_call(
            "GET",
            _EP_OW_EVENTS_GLOBAL_COUNTS,
            query_params={"filter": filter},
            operation_label="AggregatesOWEventsGlobalCounts",
            member_cid=member_cid,
        )
