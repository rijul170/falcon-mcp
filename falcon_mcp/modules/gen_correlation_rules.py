"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `correlation_rules` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenCorrelationRulesModule(GeneratedModuleBase):
    """Generated tools for the Falcon `correlation_rules` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.combined_rules_get_v2, name="combined_rules_get_v2")
        self._add_tool(server=server, method=self.entities_latest_rules_get_v1, name="entities_latest_rules_get_v1")
        self._add_tool(server=server, method=self.entities_templates_get_v1_mixin0, name="entities_templates_get_v1_mixin0")
        self._add_tool(server=server, method=self.queries_rules_get_v2, name="queries_rules_get_v2")
        self._add_tool(server=server, method=self.queries_templates_get_v1_mixin0, name="queries_templates_get_v1_mixin0")
        self._add_tool(server=server, method=self.entities_rule_versions_export_post_v1, name="entities_rule_versions_export_post_v1", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_rule_versions_import_post_v1, name="entities_rule_versions_import_post_v1", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_rule_versions_publish_patch_v1, name="entities_rule_versions_publish_patch_v1", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_templates_rules_post_v1, name="entities_templates_rules_post_v1", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_rule_versions_delete_v1, name="entities_rule_versions_delete_v1", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def combined_rules_get_v2(
        self,
        filter: str | None = Field(default=None, description="FQL query specifying the filter parameters"),
        q: str | None = Field(default=None, description="Match query criteria, which includes all the filter string fields"),
        sort: str | None = Field(default=None, description="Rule property to sort on"),
        offset: int | None = Field(default=None, description="Starting index of overall result set from which to return IDs"),
        limit: int | None = Field(default=None, description="Number of IDs to return"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Find all rules matching the query and filter. Supported filters: customer_id,user_id,user_uuid,status,name,created_on,last_updated_on Supported range filters: created_on,last_updated_on"""
        return self._call(operation="combined_rules_get_v2", query_params={"filter": filter, "q": q, "sort": sort, "offset": offset, "limit": limit}, error_message="combined_rules_get_v2 failed", member_cid=member_cid)

    def entities_latest_rules_get_v1(
        self,
        rule_ids: list[str] = Field(description="The rule IDs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve latest rule versions by rule IDs"""
        return self._call(operation="entities_latest_rules_get_v1", query_params={"rule_ids": rule_ids}, error_message="entities_latest_rules_get_v1 failed", member_cid=member_cid)

    def entities_rule_versions_delete_v1(
        self,
        ids: list[str] = Field(description="The IDs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete versions by IDs"""
        return self._call(operation="entities_rule_versions_delete_v1", query_params={"ids": ids}, error_message="entities_rule_versions_delete_v1 failed", member_cid=member_cid)

    def entities_rule_versions_export_post_v1(
        self,
        body: dict = Field(description="Request JSON body for `entities_rule_versions_export_post_v1` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Export rule versions"""
        return self._call(operation="entities_rule_versions_export_post_v1", query_params=None, body_params=body, error_message="entities_rule_versions_export_post_v1 failed", member_cid=member_cid)

    def entities_rule_versions_import_post_v1(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Import rule versions"""
        return self._call(operation="entities_rule_versions_import_post_v1", query_params=None, error_message="entities_rule_versions_import_post_v1 failed", member_cid=member_cid)

    def entities_rule_versions_publish_patch_v1(
        self,
        body: dict = Field(description="Request JSON body for `entities_rule_versions_publish_patch_v1` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Publish existing rule version"""
        return self._call(operation="entities_rule_versions_publish_patch_v1", query_params=None, body_params=body, error_message="entities_rule_versions_publish_patch_v1 failed", member_cid=member_cid)

    def entities_templates_get_v1_mixin0(
        self,
        ids: list[str] = Field(description="The IDs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve rule templates by IDs"""
        return self._call(operation="entities_templates_get_v1Mixin0", query_params={"ids": ids}, error_message="entities_templates_get_v1Mixin0 failed", member_cid=member_cid)

    def entities_templates_rules_post_v1(
        self,
        body: dict = Field(description="Request JSON body for `entities_templates_rules_post_v1` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create rule from template"""
        return self._call(operation="entities_templates_rules_post_v1", query_params=None, body_params=body, error_message="entities_templates_rules_post_v1 failed", member_cid=member_cid)

    def queries_rules_get_v2(
        self,
        filter: str | None = Field(default=None, description="FQL query specifying the filter parameters"),
        q: str | None = Field(default=None, description="Match query criteria, which includes all the filter string fields"),
        sort: str | None = Field(default=None, description="Rule property to sort on"),
        offset: int | None = Field(default=None, description="Starting index of overall result set from which to return IDs"),
        limit: int | None = Field(default=None, description="Number of IDs to return"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Find all rule version IDs matching the query and filter. Supported filters: customer_id,user_id,user_uui d,status,name,created_on,last_updated_on,state,version,rule_id,executor_rule_id Supported range filters: created_on,last_updated_on"""
        return self._call(operation="queries_rules_get_v2", query_params={"filter": filter, "q": q, "sort": sort, "offset": offset, "limit": limit}, error_message="queries_rules_get_v2 failed", member_cid=member_cid)

    def queries_templates_get_v1_mixin0(
        self,
        filter: str | None = Field(default=None, description="FQL query specifying the filter parameters"),
        sort: str | None = Field(default=None, description="Rule property to sort on"),
        offset: int | None = Field(default=None, description="Starting index of overall result set from which to return IDs"),
        limit: int | None = Field(default=None, description="Number of IDs to return"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search rule template IDs matching the filter. Supported filters: name,description,vendor,outcome,mitre_attack.tactic_id,mitre_attack.technique_id,type Supported range filters: created_on,last_updated_on"""
        return self._call(operation="queries_templates_get_v1Mixin0", query_params={"filter": filter, "sort": sort, "offset": offset, "limit": limit}, error_message="queries_templates_get_v1Mixin0 failed", member_cid=member_cid)
