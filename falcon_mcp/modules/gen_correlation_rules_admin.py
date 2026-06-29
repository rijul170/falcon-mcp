"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `correlation_rules_admin` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenCorrelationRulesAdminModule(GeneratedModuleBase):
    """Generated tools for the Falcon `correlation_rules_admin` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.entities_rules_ownership_put_v1, name="entities_rules_ownership_put_v1", annotations=WRITE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def entities_rules_ownership_put_v1(
        self,
        body: dict = Field(description="Request JSON body for `entities_rules_ownership_put_v1` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Change the owner of an existing Correlation Rule"""
        return self._call(operation="entities_rules_ownership_put_v1", query_params=None, body_params=body, error_message="entities_rules_ownership_put_v1 failed", member_cid=member_cid)
