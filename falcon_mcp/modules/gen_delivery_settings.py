"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `delivery_settings` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenDeliverySettingsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `delivery_settings` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_delivery_settings, name="get_delivery_settings")
        self._add_tool(server=server, method=self.post_delivery_settings, name="post_delivery_settings", annotations=WRITE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def get_delivery_settings(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get Delivery Settings"""
        return self._call(operation="GetDeliverySettings", query_params=None, error_message="GetDeliverySettings failed", member_cid=member_cid)

    def post_delivery_settings(
        self,
        body: dict = Field(description="Request JSON body for `PostDeliverySettings` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create Delivery Settings"""
        return self._call(operation="PostDeliverySettings", query_params=None, body_params=body, error_message="PostDeliverySettings failed", member_cid=member_cid)
