"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `netscan` scanners
API service collection.

NOTE: FalconPy 1.6.1 does not yet include netscan operation IDs in its endpoint registry.
All methods therefore use the Uber-class `override` keyword to call the raw REST paths
directly, bypassing FalconPy's operation dispatch table.

Required API scope: Network scanning: READ (GET/POST-aggregates) / WRITE (PATCH).
API base paths:
  /netscan/aggregates/scanners/GET/v1   POST  aggregate_scanners
  /netscan/entities/scanners/v1         GET   get_scanners
  /netscan/entities/scanners/v1         PATCH  update_scanners
  /netscan/queries/scanners/v1          GET   query_scanners
"""

from typing import Any

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.errors import handle_api_response
from falcon_mcp.common.generated_base import GeneratedModuleBase
from falcon_mcp.common.utils import prepare_api_parameters

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)

_AGGREGATE_PATH = "/netscan/aggregates/scanners/GET/v1"
_ENTITIES_PATH = "/netscan/entities/scanners/v1"
_QUERIES_PATH = "/netscan/queries/scanners/v1"


class GenNetscanScannersModule(GeneratedModuleBase):
    """Generated tools for the Falcon `netscan` scanners collection.

    Covers:
      - aggregate_scanners   POST  /netscan/aggregates/scanners/GET/v1
      - get_scanners         GET   /netscan/entities/scanners/v1
      - update_scanners      PATCH /netscan/entities/scanners/v1
      - query_scanners       GET   /netscan/queries/scanners/v1
    """

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.aggregate_scanners, name="aggregate_scanners")
        self._add_tool(server=server, method=self.get_scanners, name="get_scanners")
        self._add_tool(server=server, method=self.update_scanners, name="update_scanners", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.query_scanners, name="query_scanners")

    def register_resources(self, server: FastMCP) -> None:
        pass

    # ------------------------------------------------------------------
    # Internal helper: call via FalconPy Uber-class override
    # ------------------------------------------------------------------

    def _raw_call(
        self,
        http_method: str,
        path: str,
        query_params: dict[str, Any] | None = None,
        body_params: dict[str, Any] | None = None,
        error_message: str = "Operation failed",
        member_cid: str | None = None,
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Execute a netscan API call using the FalconPy Uber-class override mechanism.

        FalconPy's ``APIHarnessV2.command()`` accepts ``override='METHOD,/path'`` to
        bypass the internal operation lookup table and hit any REST endpoint directly.
        This is required for netscan operations because FalconPy 1.6.1 does not yet
        register them in its endpoint dictionary.
        """
        call_args: dict[str, Any] = {"override": f"{http_method},{path}"}

        if query_params:
            call_args["parameters"] = prepare_api_parameters(query_params)

        if body_params:
            call_args["body"] = prepare_api_parameters(body_params)

        response = self.client.command_for(
            "override",
            member_cid=member_cid,
            **call_args,
        )

        return handle_api_response(response, operation=f"{http_method} {path}", error_message=error_message)

    # ------------------------------------------------------------------
    # Operations
    # ------------------------------------------------------------------

    def aggregate_scanners(
        self,
        body: dict = Field(
            description=(
                "Request JSON body for `aggregate_scanners` per the CrowdStrike API schema (required). "
                "Supported top-level keys: "
                "date_ranges (array), exclude (string), extended_bounds (object), field (string), "
                "filter (string — FQL), filters_spec (object), from (integer), include (string), "
                "interval (string), max_doc_count (integer), min_doc_count (integer), missing (string), "
                "name (string), percents (array), q (string), ranges (array), size (integer), "
                "sort (string), sub_aggregates (array), time_zone (string), type (string)."
            )
        ),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Return aggregated metrics for scanner entities.

        Accepts a standard CrowdStrike aggregation request body and returns bucketed
        counts or statistics over the netscan scanners data set.

        Required scope: Network scanning: READ
        """
        return self._raw_call(
            http_method="POST",
            path=_AGGREGATE_PATH,
            body_params=body,
            error_message="aggregate_scanners failed",
            member_cid=member_cid,
        )

    def get_scanners(
        self,
        ids: list[str] = Field(description="Scanner IDs (AIDs) to retrieve. Min: 1, Max: 100."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get scanner entities by their IDs (agent IDs / AIDs).

        Required scope: Network scanning: READ
        """
        return self._raw_call(
            http_method="GET",
            path=_ENTITIES_PATH,
            query_params={"ids": ids},
            error_message="get_scanners failed",
            member_cid=member_cid,
        )

    def update_scanners(
        self,
        body: dict = Field(
            description=(
                "Request JSON body for `update_scanners` per the CrowdStrike API schema (required). "
                "Supported top-level keys: "
                "action (string) — the action to take on the provided set of scanners "
                "(e.g. 'enable', 'disable'); "
                "aids (array of strings) — the AIDs of the scanners to act on."
            )
        ),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update scanner entities — for example, enable or disable specific scanner assets.

        Required scope: Network scanning: WRITE
        """
        return self._raw_call(
            http_method="PATCH",
            path=_ENTITIES_PATH,
            body_params=body,
            error_message="update_scanners failed",
            member_cid=member_cid,
        )

    def query_scanners(
        self,
        offset: int | None = Field(default=None, description="Pagination offset. Omit on first call; use the previous call's offset + limit for subsequent pages."),
        limit: int | None = Field(default=None, description="Maximum number of scanner IDs to return. Min: 1, Max: 100, Default: 100."),
        sort: str | None = Field(default=None, description="Sort scanners by a single property (e.g. 'hostname.asc' or 'last_seen.desc')."),
        filter: str | None = Field(default=None, description="FQL filter expression to narrow results (e.g. `status:'enabled'`)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get scanner IDs matching the specified filter criteria.

        Returns a list of scanner AIDs that can be passed to `get_scanners` to retrieve
        full entity details.

        Required scope: Network scanning: READ
        """
        return self._raw_call(
            http_method="GET",
            path=_QUERIES_PATH,
            query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter},
            error_message="query_scanners failed",
            member_cid=member_cid,
        )
