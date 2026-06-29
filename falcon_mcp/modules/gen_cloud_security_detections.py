"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `cloud_security_detections` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenCloudSecurityDetectionsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `cloud_security_detections` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.cspm_evaluations_combined_iom_by_rule, name="cspm_evaluations_combined_iom_by_rule")
        self._add_tool(server=server, method=self.cspm_evaluations_iom_entities, name="cspm_evaluations_iom_entities")
        self._add_tool(server=server, method=self.cspm_evaluations_iom_queries, name="cspm_evaluations_iom_queries")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def cspm_evaluations_combined_iom_by_rule(
        self,
        filter: str | None = Field(default=None, description="FQL string to filter results in Falcon Query Language (FQL). Supported fields: account_id account_name applicable_profile attack_type benchmark_name benchmark_version business_impact cid cloud_group cloud_label cloud_label_id cloud_provider cloud_scope created_at environment extension_status first_detected framework last_detected policy_id policy_name region requirement resource_gcrn resource_id resource_parent resource_status resource_type resource_type_name rule_group rule_id rule_name rule_origin section service service_category severity status suppressed_by tactic_id tactic_name tag_key tag_value tags tags_string technique_id technique_name zone"),
        sort: str | None = Field(default=None, description="The field to sort on. Sortable fields include: assessed_assets cloud_provider misconfigurations rule_id severity Use |asc or |desc suffix to specify sort direction."),
        limit: int | None = Field(default=None, description="The maximum number of items to return. When not specified or 0, 500 is used. When larger than 1000, 1000 is used."),
        offset: int | None = Field(default=None, description="Offset returned assets"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """returns ioms grouped by rule"""
        return self._call(operation="cspm_evaluations_combined_iom_by_rule", query_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset}, error_message="cspm_evaluations_combined_iom_by_rule failed", member_cid=member_cid)

    def cspm_evaluations_iom_entities(
        self,
        ids: list[str] | None = Field(default=None, description="List of IOMs to return (maximum 100 IDs allowed). Use POST method with same path if more entities are required."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Gets IOMs based on the provided IDs"""
        return self._call(operation="cspm_evaluations_iom_entities", query_params={"ids": ids}, error_message="cspm_evaluations_iom_entities failed", member_cid=member_cid)

    def cspm_evaluations_iom_queries(
        self,
        filter: str | None = Field(default=None, description="FQL string to filter results in Falcon Query Language (FQL). Supported fields: account_id account_name applicable_profile attack_type benchmark_name benchmark_version business_impact cid cloud_group cloud_label cloud_label_id cloud_provider cloud_scope created_at environment extension_status first_detected framework last_detected policy_id policy_name policy_uuid region requirement requirement_name resource_gcrn resource_id resource_parent resource_status resource_type resource_type_name rule_group rule_id rule_name rule_origin rule_remediation section service service_category severity status suppressed_by suppression_reason tactic_id tactic_name tag_key tag_value tags tags_string technique_id technique_name"),
        sort: str | None = Field(default=None, description="The field to sort on. Use |asc or |desc suffix to specify sort direction.Supported fields: account_id account_name applicable_profile attack_type benchmark_name benchmark_version business_impact cid cloud_group cloud_label cloud_label_id cloud_provider cloud_scope created_at environment extension_status first_detected framework last_detected policy_id policy_name policy_uuid region requirement requirement_name resource_gcrn resource_id resource_parent resource_status resource_type resource_type_name rule_group rule_id rule_name rule_origin rule_remediation section service service_category severity status suppressed_by suppression_reason tactic_id tactic_name tag_key tag_value tags tags_string technique_id technique_name"),
        limit: int | None = Field(default=None, description="The maximum number of items to return. When not specified or 0, 500 is used. When larger than 1000, 1000 is used."),
        offset: int | None = Field(default=None, description="Offset returned assets"),
        after: str | None = Field(default=None, description="token-based pagination. Use for paginating through an entire result set. Use only one of 'offset' and 'after' parameters for paginating"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Gets a list of IOM IDs for the given parameters, filters and sort criteria."""
        return self._call(operation="cspm_evaluations_iom_queries", query_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset, "after": after}, error_message="cspm_evaluations_iom_queries failed", member_cid=member_cid)
