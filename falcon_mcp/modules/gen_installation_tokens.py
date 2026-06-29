"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `installation_tokens` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenInstallationTokensModule(GeneratedModuleBase):
    """Generated tools for the Falcon `installation_tokens` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.customer_settings_update, name="customer_settings_update", annotations=WRITE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def customer_settings_update(
        self,
        body: dict = Field(description="Request JSON body for `customer_settings_update` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update installation token settings."""
        return self._call(operation="customer_settings_update", query_params=None, body_params=body, error_message="customer_settings_update failed", member_cid=member_cid)
