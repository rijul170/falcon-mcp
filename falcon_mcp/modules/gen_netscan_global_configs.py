"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `netscan` global-configs
API service collection.

NOTE: FalconPy 1.6.1 does not yet include netscan operation IDs in its endpoint registry.
All methods therefore use the Uber-class `override` keyword to call the raw REST paths
directly, bypassing FalconPy's operation dispatch table.

Required API scope: Network scanning: READ (GET operations) / WRITE (PATCH operations).
API base path: /netscan/entities/global-configs/v1
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

_BASE_PATH = "/netscan/entities/global-configs/v1"


class GenNetscanGlobalConfigsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `netscan` global-configs collection.

    Covers:
      - get_global_configs   GET  /netscan/entities/global-configs/v1
      - update_global_configs PATCH /netscan/entities/global-configs/v1
    """

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_global_configs, name="get_global_configs")
        self._add_tool(server=server, method=self.update_global_configs, name="update_global_configs", annotations=WRITE_ANNOTATIONS)

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
            # operation string is unused when override is set but must be non-empty
            "override",
            member_cid=member_cid,
            **call_args,
        )

        return handle_api_response(response, operation=f"{http_method} {path}", error_message=error_message)

    # ------------------------------------------------------------------
    # Operations
    # ------------------------------------------------------------------

    def get_global_configs(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get the network-scanning global configuration for the CID.

        Returns the current global-config entity including settings such as whether
        network scanning is enabled, maximum concurrent scan tasks, scan exclusions,
        and scanner asset lists.

        Required scope: Network scanning: READ
        """
        return self._raw_call(
            http_method="GET",
            path=_BASE_PATH,
            error_message="get_global_configs failed",
            member_cid=member_cid,
        )

    def update_global_configs(
        self,
        body: dict = Field(
            description=(
                "Request JSON body for `update_global_configs` per the CrowdStrike API schema (required). "
                "Supported top-level keys: "
                "auto_confirm_ownership (object) — settings for auto-confirmation of network ownership; "
                "max_concurrent_tasks (integer) — maximum scan tasks to run in parallel; "
                "network_scanning_enabled (boolean) — set to false to stop ongoing scans and disable future execution; "
                "scan_exclusion (object) — IP ranges / CIDRs to exclude from scanning; "
                "scanners (array) — asset AIDs eligible as scanners; "
                "scanners_exclusion (array) — asset AIDs excluded from scanner selection."
            )
        ),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update the network-scanning global configuration using the provided specification.

        Required scope: Network scanning: WRITE
        """
        return self._raw_call(
            http_method="PATCH",
            path=_BASE_PATH,
            body_params=body,
            error_message="update_global_configs failed",
            member_cid=member_cid,
        )
