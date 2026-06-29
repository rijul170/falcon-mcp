"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `tailored_intelligence` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenTailoredIntelligenceModule(GeneratedModuleBase):
    """Generated tools for the Falcon `tailored_intelligence` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_events_body, name="get_events_body")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def get_events_body(
        self,
        id: str = Field(description="Return the event body for event id."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get event body for the provided event ID"""
        return self._call(operation="GetEventsBody", query_params={"id": id}, error_message="GetEventsBody failed", member_cid=member_cid)
