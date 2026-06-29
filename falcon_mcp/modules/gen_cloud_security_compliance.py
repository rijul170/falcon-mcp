"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `cloud_security_compliance` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenCloudSecurityComplianceModule(GeneratedModuleBase):
    """Generated tools for the Falcon `cloud_security_compliance` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.cloud_compliance_framework_posture_summaries, name="cloud_compliance_framework_posture_summaries")
        self._add_tool(server=server, method=self.cloud_compliance_rule_posture_summaries, name="cloud_compliance_rule_posture_summaries")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def cloud_compliance_framework_posture_summaries(
        self,
        ids: list[str] = Field(description="The uuids of compliance frameworks to retrieve (maximum 20 IDs allowed)."),
        filter: str | None = Field(default=None, description="FQL filter, supported properties: - account_id account_name business_impact cloud_label cloud_label_id cloud_provider environment groups region resource_type resource_type_name tag_key tag_value tags_string"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get sections and requirements with scores for benchmarks."""
        return self._call(operation="cloud_compliance_framework_posture_summaries", query_params={"ids": ids, "filter": filter}, error_message="cloud_compliance_framework_posture_summaries failed", member_cid=member_cid)

    def cloud_compliance_rule_posture_summaries(
        self,
        ids: list[str] = Field(description="The uuids of compliance rules to retrieve (maximum 350 IDs allowed)."),
        filter: str | None = Field(default=None, description="FQL filter, supported properties: - account_id account_name business_impact cloud_label cloud_label_id cloud_provider environment groups region resource_type resource_type_name tag_key tag_value tags_string"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get compliance score and counts for rules."""
        return self._call(operation="cloud_compliance_rule_posture_summaries", query_params={"ids": ids, "filter": filter}, error_message="cloud_compliance_rule_posture_summaries failed", member_cid=member_cid)
