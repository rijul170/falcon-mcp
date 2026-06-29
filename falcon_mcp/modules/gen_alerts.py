"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `alerts` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenAlertsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `alerts` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.post_combined_alerts_v1, name="post_combined_alerts_v1", annotations=WRITE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def post_combined_alerts_v1(
        self,
        body: dict = Field(description="Request JSON body for `PostCombinedAlertsV1` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves all Alerts that match a particular FQL filter. This API is intended for retrieval of large amounts of Alerts(>10k) using a pagination based on a `after` token. If you need to use `offset` pagination, consider using GET /alerts/queries/alerts/* and POST /alerts/entities/alerts/* APIs."""
        return self._call(operation="PostCombinedAlertsV1", query_params=None, body_params=body, error_message="PostCombinedAlertsV1 failed", member_cid=member_cid)
