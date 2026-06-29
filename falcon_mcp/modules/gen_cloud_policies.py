"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `cloud_policies` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenCloudPoliciesModule(GeneratedModuleBase):
    """Generated tools for the Falcon `cloud_policies` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_compliance_controls, name="get_compliance_controls")
        self._add_tool(server=server, method=self.get_compliance_frameworks, name="get_compliance_frameworks")
        self._add_tool(server=server, method=self.get_enriched_asset, name="get_enriched_asset")
        self._add_tool(server=server, method=self.get_evaluation_result, name="get_evaluation_result")
        self._add_tool(server=server, method=self.get_rule, name="get_rule")
        self._add_tool(server=server, method=self.get_rule_input_schema, name="get_rule_input_schema")
        self._add_tool(server=server, method=self.get_rule_override, name="get_rule_override")
        self._add_tool(server=server, method=self.get_suppression_rules, name="get_suppression_rules")
        self._add_tool(server=server, method=self.query_compliance_controls, name="query_compliance_controls")
        self._add_tool(server=server, method=self.query_compliance_frameworks, name="query_compliance_frameworks")
        self._add_tool(server=server, method=self.query_rule, name="query_rule")
        self._add_tool(server=server, method=self.query_suppression_rules, name="query_suppression_rules")
        self._add_tool(server=server, method=self.create_compliance_control, name="create_compliance_control", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.create_compliance_framework, name="create_compliance_framework", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.create_rule_mixin0, name="create_rule_mixin0", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.create_rule_override, name="create_rule_override", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_compliance_control, name="update_compliance_control", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_compliance_framework, name="update_compliance_framework", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_rule, name="update_rule", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_rule_override, name="update_rule_override", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.create_suppression_rule, name="create_suppression_rule", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_compliance_control, name="delete_compliance_control", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_compliance_framework, name="delete_compliance_framework", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_rule_mixin0, name="delete_rule_mixin0", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_rule_override, name="delete_rule_override", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_suppression_rules, name="delete_suppression_rules", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.rename_section_compliance_framework, name="rename_section_compliance_framework", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.replace_control_rules, name="replace_control_rules", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_suppression_rule, name="update_suppression_rule", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def create_compliance_control(
        self,
        body: dict = Field(description="Request JSON body for `CreateComplianceControl` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create a new custom compliance control"""
        return self._call(operation="CreateComplianceControl", query_params=None, body_params=body, error_message="CreateComplianceControl failed", member_cid=member_cid)

    def create_compliance_framework(
        self,
        body: dict = Field(description="Request JSON body for `CreateComplianceFramework` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create a new custom compliance framework"""
        return self._call(operation="CreateComplianceFramework", query_params=None, body_params=body, error_message="CreateComplianceFramework failed", member_cid=member_cid)

    def create_rule_mixin0(
        self,
        body: dict = Field(description="Request JSON body for `CreateRuleMixin0` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create a new rule"""
        return self._call(operation="CreateRuleMixin0", query_params=None, body_params=body, error_message="CreateRuleMixin0 failed", member_cid=member_cid)

    def create_rule_override(
        self,
        body: dict = Field(description="Request JSON body for `CreateRuleOverride` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create a new rule override"""
        return self._call(operation="CreateRuleOverride", query_params=None, body_params=body, error_message="CreateRuleOverride failed", member_cid=member_cid)

    def create_suppression_rule(
        self,
        body: dict = Field(description="Request JSON body for `CreateSuppressionRule` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create a new suppression rule"""
        return self._call(operation="CreateSuppressionRule", query_params=None, body_params=body, error_message="CreateSuppressionRule failed", member_cid=member_cid)

    def delete_compliance_control(
        self,
        ids: list[str] = Field(description="The uuids of compliance control to delete"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete custom compliance controls"""
        return self._call(operation="DeleteComplianceControl", query_params={"ids": ids}, error_message="DeleteComplianceControl failed", member_cid=member_cid)

    def delete_compliance_framework(
        self,
        ids: str = Field(description="The uuids of compliance framework to delete"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete a custom compliance framework and all associated controls and rule assignments"""
        return self._call(operation="DeleteComplianceFramework", query_params={"ids": ids}, error_message="DeleteComplianceFramework failed", member_cid=member_cid)

    def delete_rule_mixin0(
        self,
        ids: list[str] = Field(description="The uuids of rules to delete"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete a rule"""
        return self._call(operation="DeleteRuleMixin0", query_params={"ids": ids}, error_message="DeleteRuleMixin0 failed", member_cid=member_cid)

    def delete_rule_override(
        self,
        ids: list[str] = Field(description="The uuids of rule overrides to delete"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete a rule override"""
        return self._call(operation="DeleteRuleOverride", query_params={"ids": ids}, error_message="DeleteRuleOverride failed", member_cid=member_cid)

    def delete_suppression_rules(
        self,
        ids: list[str] = Field(description="The uuids of the suppression rules to delete. A maximum of 10 IDs can be provided."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete Suppression Rules by ID"""
        return self._call(operation="DeleteSuppressionRules", query_params={"ids": ids}, error_message="DeleteSuppressionRules failed", member_cid=member_cid)

    def get_compliance_controls(
        self,
        ids: list[str] = Field(description="The uuids of compliance controls to retrieve"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get compliance controls by ID"""
        return self._call(operation="GetComplianceControls", query_params={"ids": ids}, error_message="GetComplianceControls failed", member_cid=member_cid)

    def get_compliance_frameworks(
        self,
        ids: list[str] = Field(description="The uuids of compliance frameworks to retrieve"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get compliance frameworks by ID"""
        return self._call(operation="GetComplianceFrameworks", query_params={"ids": ids}, error_message="GetComplianceFrameworks failed", member_cid=member_cid)

    def get_enriched_asset(
        self,
        ids: list[str] | None = Field(default=None, description="List of asset IDs (maximum 100 IDs allowed)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Gets enriched assets that combine a primary resource with all its related resources"""
        return self._call(operation="GetEnrichedAsset", query_params={"ids": ids}, error_message="GetEnrichedAsset failed", member_cid=member_cid)

    def get_evaluation_result(
        self,
        body: dict = Field(description="Request JSON body for `GetEvaluationResult` per the CrowdStrike API schema (required)."),
        cloud_provider: str | None = Field(default=None, description="Cloud Service Provider of the provided IDs"),
        resource_type: str | None = Field(default=None, description="Resource Type of the provided IDs"),
        ids: list[str] | None = Field(default=None, description="List of assets to evaluate (maximum 100 IDs allowed)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Gets evaluation results based on the provided rule"""
        return self._call(operation="GetEvaluationResult", query_params={"cloud_provider": cloud_provider, "resource_type": resource_type, "ids": ids}, body_params=body, error_message="GetEvaluationResult failed", member_cid=member_cid)

    def get_rule(
        self,
        ids: list[str] = Field(description="The uuids of rules to retrieve"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get a rule by id"""
        return self._call(operation="GetRule", query_params={"ids": ids}, error_message="GetRule failed", member_cid=member_cid)

    def get_rule_input_schema(
        self,
        domain: str = Field(description="domain"),
        subdomain: str = Field(description="subdomain"),
        resource_type: str = Field(description="Selects the resource type for which to retrieve the rule input schema"),
        cloud_provider: str | None = Field(default=None, description="Cloud service provider for the resource type"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get rule input schema for given resource type"""
        return self._call(operation="GetRuleInputSchema", query_params={"domain": domain, "subdomain": subdomain, "cloud_provider": cloud_provider, "resource_type": resource_type}, error_message="GetRuleInputSchema failed", member_cid=member_cid)

    def get_rule_override(
        self,
        ids: list[str] = Field(description="The uuids of rule overrides to retrieve"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get a rule override"""
        return self._call(operation="GetRuleOverride", query_params={"ids": ids}, error_message="GetRuleOverride failed", member_cid=member_cid)

    def get_suppression_rules(
        self,
        ids: list[str] = Field(description="The uuids of the suppression rules to retrieve"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get Suppression Rules by ID"""
        return self._call(operation="GetSuppressionRules", query_params={"ids": ids}, error_message="GetSuppressionRules failed", member_cid=member_cid)

    def query_compliance_controls(
        self,
        filter: str | None = Field(default=None, description="FQL filter, allowed props: *compliance_control_name* *compliance_control_auth ority* *compliance_control_type* *compliance_control_section* *compliance_control_requirement* *co mpliance_control_benchmark_name* *compliance_control_benchmark_version*"),
        limit: int | None = Field(default=None, description="The maximum number of resources to return. The maximum allowed is 500."),
        offset: int | None = Field(default=None, description="The number of results to skip before starting to return results."),
        sort: str | None = Field(default=None, description="Field to sort on. Sortable fields: *compliance_control_name* *compliance_cont rol_authority* *compliance_control_type* *compliance_control_section* *compliance_control_requirement * *compliance_control_benchmark_name* *compliance_control_benchmark_version* Use the |asc or |desc suffix to specify sort direction."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Query for compliance controls by various parameters"""
        return self._call(operation="QueryComplianceControls", query_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort}, error_message="QueryComplianceControls failed", member_cid=member_cid)

    def query_compliance_frameworks(
        self,
        filter: str | None = Field(default=None, description="FQL filter, allowed properties: *compliance_framework_name* *compliance_framework_version* *compliance_framework_authority*"),
        limit: int | None = Field(default=None, description="The maximum number of resources to return. The maximum allowed is 500."),
        offset: int | None = Field(default=None, description="The number of results to skip before starting to return results."),
        sort: str | None = Field(default=None, description="Field to sort on. Sortable fields: *compliance_framework_name* *compliance_framework_version* *compliance_framework_authority* Use the |asc or |desc suffix to specify sort direction."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Query for compliance frameworks by various parameters"""
        return self._call(operation="QueryComplianceFrameworks", query_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort}, error_message="QueryComplianceFrameworks failed", member_cid=member_cid)

    def query_rule(
        self,
        filter: str | None = Field(default=None, description="FQL filter, allowed properties: *rule_auto_remediable* *rule_category* *ru le_cloneable* *rule_compliance_benchmark* *rule_compliance_benchmark_uuid* *rule_compliance_framework * *rule_control_requirement* *rule_control_section* *rule_created_at* *rule_description* *rule_domain* *rule_mitre_tactic* *rule_mitre_technique* *rule_name* *rule_origin* *rule_parent_uuid* *rule_provider* *rule_resource_type* *rule_resource_type_name* *rule_risk_factor* *rule_servic e* *rule_severity* *rule_short_code* *rule_status* *rule_subdomain* *rule_updated_at* *rule_updated_by*"),
        limit: int | None = Field(default=None, description="The maximum number of resources to return. The maximum allowed is 500."),
        offset: int | None = Field(default=None, description="The number of results to skip before starting to return results."),
        sort: str | None = Field(default=None, description="Field to sort on. Sortable fields: *rule_auto_remediable* *rule_category* *rule_cloneable* *rule_compliance_benchmark* *rule_compliance_benchmark_uuid* *rule_compliance_framew ork* *rule_control_requirement* *rule_control_section* *rule_created_at* *rule_description* *ru le_domain* *rule_mitre_tactic* *rule_mitre_technique* *rule_name* *rule_origin* *rule_parent_uu id* *rule_provider* *rule_resource_type* *rule_resource_type_name* *rule_risk_factor* *rule_ser vice* *rule_severity* *rule_short_code* *rule_status* *rule_subdomain* *rule_updated_at* *ru le_updated_by* Use the |asc or |desc suffix to specify sort direction."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Query for rules by various parameters"""
        return self._call(operation="QueryRule", query_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort}, error_message="QueryRule failed", member_cid=member_cid)

    def query_suppression_rules(
        self,
        filter: str | None = Field(default=None, description="FQL expression to filter suppression rules. The allowed properties are: *name* *description* *domain* *subdomain* *suppression_expiration_date* *suppression_reason* *create d_by* *created_at* *last_modified_at* *disabled* *groups*"),
        limit: int | None = Field(default=None, description="The maximum number of resources to return. The maximum allowed is 50."),
        offset: int | None = Field(default=None, description="The number of results to skip before starting to return results."),
        sort: str | None = Field(default=None, description="Field to sort on. Sortable fields: *name* *description* *domain* *subdo main* *suppression_expiration_date* *suppression_reason* *created_by* *created_at* *last_modifi ed_at* *disabled* *groups* Use the .asc or .desc suffix to specify sort direction."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Query suppression rules with filtering, sorting and pagination"""
        return self._call(operation="QuerySuppressionRules", query_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort}, error_message="QuerySuppressionRules failed", member_cid=member_cid)

    def rename_section_compliance_framework(
        self,
        ids: str = Field(description="The uuid of compliance framework containing the section to rename"),
        sectionName: str = Field(description="The current name of the section to rename"),
        body: dict = Field(description="Request JSON body for `RenameSectionComplianceFramework` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Rename a section in a custom compliance framework"""
        return self._call(operation="RenameSectionComplianceFramework", query_params={"ids": ids, "sectionName": sectionName}, body_params=body, error_message="RenameSectionComplianceFramework failed", member_cid=member_cid)

    def replace_control_rules(
        self,
        ids: str = Field(description="The UUID of the compliance control to assign rules to"),
        body: dict = Field(description="Request JSON body for `ReplaceControlRules` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Assign rules to a compliance control (full replace)"""
        return self._call(operation="ReplaceControlRules", query_params={"ids": ids}, body_params=body, error_message="ReplaceControlRules failed", member_cid=member_cid)

    def update_compliance_control(
        self,
        ids: str = Field(description="The uuid of compliance control to update"),
        body: dict = Field(description="Request JSON body for `UpdateComplianceControl` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update a custom compliance control"""
        return self._call(operation="UpdateComplianceControl", query_params={"ids": ids}, body_params=body, error_message="UpdateComplianceControl failed", member_cid=member_cid)

    def update_compliance_framework(
        self,
        ids: str = Field(description="The uuids of compliance framework to update"),
        body: dict = Field(description="Request JSON body for `UpdateComplianceFramework` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update a custom compliance framework"""
        return self._call(operation="UpdateComplianceFramework", query_params={"ids": ids}, body_params=body, error_message="UpdateComplianceFramework failed", member_cid=member_cid)

    def update_rule(
        self,
        body: dict = Field(description="Request JSON body for `UpdateRule` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update a rule"""
        return self._call(operation="UpdateRule", query_params=None, body_params=body, error_message="UpdateRule failed", member_cid=member_cid)

    def update_rule_override(
        self,
        body: dict = Field(description="Request JSON body for `UpdateRuleOverride` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update a rule override"""
        return self._call(operation="UpdateRuleOverride", query_params=None, body_params=body, error_message="UpdateRuleOverride failed", member_cid=member_cid)

    def update_suppression_rule(
        self,
        body: dict = Field(description="Request JSON body for `UpdateSuppressionRule` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update a suppression rule"""
        return self._call(operation="UpdateSuppressionRule", query_params=None, body_params=body, error_message="UpdateSuppressionRule failed", member_cid=member_cid)
