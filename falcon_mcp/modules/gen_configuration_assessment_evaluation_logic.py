"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `configuration_assessment_evaluation_logic` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenConfigurationAssessmentEvaluationLogicModule(GeneratedModuleBase):
    """Generated tools for the Falcon `configuration_assessment_evaluation_logic` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_evaluation_logic_mixin0, name="get_evaluation_logic_mixin0")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def get_evaluation_logic_mixin0(
        self,
        ids: list[str] = Field(description="One or more evaluation logic finding IDs."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get details on evaluation logic items by providing one or more finding IDs."""
        return self._call(operation="getEvaluationLogicMixin0", query_params={"ids": ids}, error_message="getEvaluationLogicMixin0 failed", member_cid=member_cid)
