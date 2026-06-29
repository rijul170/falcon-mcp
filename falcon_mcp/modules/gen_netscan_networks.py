"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `netscan` networks
API service collection.

NOTE: FalconPy 1.6.1 does not yet include netscan operation IDs in its endpoint registry.
All methods therefore use the Uber-class `override` keyword to call the raw REST paths
directly, bypassing FalconPy's operation dispatch table.

Required API scope: Network scanning: READ (GET/POST-aggregates) / WRITE (POST/PATCH/DELETE).
API base paths:
  /netscan/aggregates/networks/GET/v1   POST  aggregate_networks
  /netscan/entities/networks/v1         GET   get_networks
  /netscan/entities/networks/v1         POST  create_networks
  /netscan/entities/networks/v1         DELETE delete_networks
  /netscan/entities/networks/v1         PATCH  update_networks
  /netscan/queries/networks/v1          GET   query_networks
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

_AGGREGATE_PATH = "/netscan/aggregates/networks/GET/v1"
_ENTITIES_PATH = "/netscan/entities/networks/v1"
_QUERIES_PATH = "/netscan/queries/networks/v1"


class GenNetscanNetworksModule(GeneratedModuleBase):
    """Generated tools for the Falcon `netscan` networks collection.

    Covers:
      - aggregate_networks   POST   /netscan/aggregates/networks/GET/v1
      - get_networks         GET    /netscan/entities/networks/v1
      - create_networks      POST   /netscan/entities/networks/v1
      - delete_networks      DELETE /netscan/entities/networks/v1
      - update_networks      PATCH  /netscan/entities/networks/v1
      - query_networks       GET    /netscan/queries/networks/v1
    """

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.aggregate_networks, name="aggregate_networks")
        self._add_tool(server=server, method=self.get_networks, name="get_networks")
        self._add_tool(server=server, method=self.create_networks, name="create_networks", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_networks, name="delete_networks", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_networks, name="update_networks", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.query_networks, name="query_networks")

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

    def aggregate_networks(
        self,
        body: dict = Field(
            description=(
                "Request JSON body for `aggregate_networks` per the CrowdStrike API schema (required). "
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
        """Return aggregated metrics for network entities.

        Accepts a standard CrowdStrike aggregation request body (same schema used by
        Discover, Spotlight, etc.) and returns bucketed counts or statistics over the
        netscan networks data set.

        Required scope: Network scanning: READ
        """
        return self._raw_call(
            http_method="POST",
            path=_AGGREGATE_PATH,
            body_params=body,
            error_message="aggregate_networks failed",
            member_cid=member_cid,
        )

    def get_networks(
        self,
        ids: list[str] = Field(description="Network IDs to retrieve. Min: 1, Max: 100."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get network entities by their IDs.

        Required scope: Network scanning: READ
        """
        return self._raw_call(
            http_method="GET",
            path=_ENTITIES_PATH,
            query_params={"ids": ids},
            error_message="get_networks failed",
            member_cid=member_cid,
        )

    def create_networks(
        self,
        body: dict = Field(
            description=(
                "Request JSON body for `create_networks` per the CrowdStrike API schema (required). "
                "Supported top-level keys: "
                "name (string) — network display name; "
                "scanner_aids (array of strings) — scanner asset IDs to assign; "
                "scanner_assignment_type (string) — assignment mode for scanners; "
                "subnet (string) — network subnet in CIDR notation; "
                "zone_id (string) — zone this network belongs to."
            )
        ),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create one or more network entities using the provided specifications.

        Required scope: Network scanning: WRITE
        """
        return self._raw_call(
            http_method="POST",
            path=_ENTITIES_PATH,
            body_params=body,
            error_message="create_networks failed",
            member_cid=member_cid,
        )

    def delete_networks(
        self,
        ids: list[str] = Field(description="Network IDs to delete. Min: 1, Max: 100."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete network entities by their IDs.

        Required scope: Network scanning: WRITE
        """
        return self._raw_call(
            http_method="DELETE",
            path=_ENTITIES_PATH,
            query_params={"ids": ids},
            error_message="delete_networks failed",
            member_cid=member_cid,
        )

    def update_networks(
        self,
        body: dict = Field(
            description=(
                "Request JSON body for `update_networks` per the CrowdStrike API schema (required). "
                "Supported top-level keys: "
                "id (string) — unique network identifier to update; "
                "name (string) — updated network display name; "
                "ownership (string) — network ownership indicator; "
                "scanner_aids (array of strings) — updated list of scanner AIDs; "
                "scanner_assignment_type (string) — updated assignment mode; "
                "zone_id (string) — updated zone association."
            )
        ),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update network entities using the provided specifications.

        Required scope: Network scanning: WRITE
        """
        return self._raw_call(
            http_method="PATCH",
            path=_ENTITIES_PATH,
            body_params=body,
            error_message="update_networks failed",
            member_cid=member_cid,
        )

    def query_networks(
        self,
        offset: int | None = Field(default=None, description="Pagination offset. Omit on first call; use the previous call's offset + limit for subsequent pages."),
        limit: int | None = Field(default=None, description="Maximum number of network IDs to return. Min: 1, Max: 100, Default: 100."),
        sort: str | None = Field(default=None, description="Sort networks by a single property (e.g. 'name.asc' or 'created_at.desc')."),
        filter: str | None = Field(default=None, description="FQL filter expression to narrow results (e.g. `subnet:'10.0.0.0/8'`)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get network IDs matching the specified filter criteria.

        Returns a list of network IDs that can be passed to `get_networks` to retrieve
        full entity details.

        Required scope: Network scanning: READ
        """
        return self._raw_call(
            http_method="GET",
            path=_QUERIES_PATH,
            query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter},
            error_message="query_networks failed",
            member_cid=member_cid,
        )
