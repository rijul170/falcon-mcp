"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `netscan` zones
API service collection.

NOTE: FalconPy 1.6.1 does not yet include netscan operation IDs in its endpoint registry.
All methods therefore use the Uber-class `override` keyword to call the raw REST paths
directly, bypassing FalconPy's operation dispatch table.

Required API scope: Network scanning: READ (GET/POST-aggregates/combined) / WRITE (POST/PATCH/DELETE).
API base paths:
  /netscan/aggregates/zones/GET/v1   POST   aggregate_zones
  /netscan/combined/zones/v1         GET    combined_zones
  /netscan/entities/zones/v1         GET    get_zones
  /netscan/entities/zones/v1         POST   create_zones
  /netscan/entities/zones/v1         DELETE delete_zones
  /netscan/entities/zones/v1         PATCH  update_zones
  /netscan/queries/zones/v1          GET    query_zones
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

_AGGREGATE_PATH = "/netscan/aggregates/zones/GET/v1"
_COMBINED_PATH = "/netscan/combined/zones/v1"
_ENTITIES_PATH = "/netscan/entities/zones/v1"
_QUERIES_PATH = "/netscan/queries/zones/v1"


class GenNetscanZonesModule(GeneratedModuleBase):
    """Generated tools for the Falcon `netscan` zones collection.

    Covers:
      - aggregate_zones   POST   /netscan/aggregates/zones/GET/v1
      - combined_zones    GET    /netscan/combined/zones/v1
      - get_zones         GET    /netscan/entities/zones/v1
      - create_zones      POST   /netscan/entities/zones/v1
      - delete_zones      DELETE /netscan/entities/zones/v1
      - update_zones      PATCH  /netscan/entities/zones/v1
      - query_zones       GET    /netscan/queries/zones/v1
    """

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.aggregate_zones, name="aggregate_zones")
        self._add_tool(server=server, method=self.combined_zones, name="combined_zones")
        self._add_tool(server=server, method=self.get_zones, name="get_zones")
        self._add_tool(server=server, method=self.create_zones, name="create_zones", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_zones, name="delete_zones", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_zones, name="update_zones", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.query_zones, name="query_zones")

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

    def aggregate_zones(
        self,
        body: dict = Field(
            description=(
                "Request JSON body for `aggregate_zones` per the CrowdStrike API schema (required). "
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
        """Return aggregated metrics for zone entities.

        Accepts a standard CrowdStrike aggregation request body and returns bucketed
        counts or statistics over the netscan zones data set.

        Required scope: Network scanning: READ
        """
        return self._raw_call(
            http_method="POST",
            path=_AGGREGATE_PATH,
            body_params=body,
            error_message="aggregate_zones failed",
            member_cid=member_cid,
        )

    def combined_zones(
        self,
        offset: int | None = Field(default=None, description="Pagination offset. Omit on first call; use the previous call's offset + limit for subsequent pages."),
        limit: int | None = Field(default=None, description="Maximum number of zone entities to return. Min: 1, Max: 100, Default: 100."),
        sort: str | None = Field(default=None, description="Sort zones by a single property (e.g. 'name.asc' or 'created_at.desc')."),
        filter: str | None = Field(default=None, description="FQL filter expression to narrow results (e.g. `name:'DMZ'`)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get full zone entities matching the filter — returns complete records rather than IDs.

        This is the combined (search + fetch) variant: use it when you want full zone
        detail records without a separate `get_zones` call. For ID-only results with
        subsequent fetching, use `query_zones` + `get_zones`.

        Required scope: Network scanning: READ
        """
        return self._raw_call(
            http_method="GET",
            path=_COMBINED_PATH,
            query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter},
            error_message="combined_zones failed",
            member_cid=member_cid,
        )

    def get_zones(
        self,
        ids: list[str] = Field(description="Zone IDs to retrieve. Min: 1, Max: 100."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get zone entities by their IDs.

        Required scope: Network scanning: READ
        """
        return self._raw_call(
            http_method="GET",
            path=_ENTITIES_PATH,
            query_params={"ids": ids},
            error_message="get_zones failed",
            member_cid=member_cid,
        )

    def create_zones(
        self,
        body: dict = Field(
            description=(
                "Request JSON body for `create_zones` per the CrowdStrike API schema (required). "
                "Supported top-level keys: "
                "name (string) — zone display name; "
                "scanners (array of strings) — scanner AIDs to assign to this zone."
            )
        ),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create one or more zone entities using the provided specifications.

        Zones group networks and their associated scanners into logical segments
        (e.g. by site, geography, or security boundary).

        Required scope: Network scanning: WRITE
        """
        return self._raw_call(
            http_method="POST",
            path=_ENTITIES_PATH,
            body_params=body,
            error_message="create_zones failed",
            member_cid=member_cid,
        )

    def delete_zones(
        self,
        ids: list[str] = Field(description="Zone IDs to delete. Min: 1, Max: 100."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete zone entities by their IDs.

        Required scope: Network scanning: WRITE
        """
        return self._raw_call(
            http_method="DELETE",
            path=_ENTITIES_PATH,
            query_params={"ids": ids},
            error_message="delete_zones failed",
            member_cid=member_cid,
        )

    def update_zones(
        self,
        body: dict = Field(
            description=(
                "Request JSON body for `update_zones` per the CrowdStrike API schema (required). "
                "Supported top-level keys: "
                "id (string) — unique zone identifier to update; "
                "name (string) — updated zone display name; "
                "scanners_to_add (array of strings) — scanner AIDs to add to this zone; "
                "scanners_to_remove (array of strings) — scanner AIDs to remove from this zone."
            )
        ),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update zone entities using the provided specifications.

        Use `scanners_to_add` / `scanners_to_remove` for incremental scanner membership
        changes without having to specify the full scanner list.

        Required scope: Network scanning: WRITE
        """
        return self._raw_call(
            http_method="PATCH",
            path=_ENTITIES_PATH,
            body_params=body,
            error_message="update_zones failed",
            member_cid=member_cid,
        )

    def query_zones(
        self,
        offset: int | None = Field(default=None, description="Pagination offset. Omit on first call; use the previous call's offset + limit for subsequent pages."),
        limit: int | None = Field(default=None, description="Maximum number of zone IDs to return. Min: 1, Max: 100, Default: 100."),
        sort: str | None = Field(default=None, description="Sort zones by a single property (e.g. 'name.asc' or 'created_at.desc')."),
        filter: str | None = Field(default=None, description="FQL filter expression to narrow results (e.g. `name:'DMZ'`)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get zone IDs matching the specified filter criteria.

        Returns a list of zone IDs that can be passed to `get_zones` to retrieve
        full entity details. For full records in a single call, use `combined_zones`.

        Required scope: Network scanning: READ
        """
        return self._raw_call(
            http_method="GET",
            path=_QUERIES_PATH,
            query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter},
            error_message="query_zones failed",
            member_cid=member_cid,
        )
