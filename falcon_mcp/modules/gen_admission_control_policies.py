"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `admission_control_policies` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenAdmissionControlPoliciesModule(GeneratedModuleBase):
    """Generated tools for the Falcon `admission_control_policies` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.admission_control_get_policies, name="admission_control_get_policies")
        self._add_tool(server=server, method=self.admission_control_query_policies, name="admission_control_query_policies")
        self._add_tool(server=server, method=self.admission_control_add_host_groups, name="admission_control_add_host_groups", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.admission_control_add_rule_group_custom_rule, name="admission_control_add_rule_group_custom_rule", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.admission_control_create_policy, name="admission_control_create_policy", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.admission_control_create_rule_groups, name="admission_control_create_rule_groups", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.admission_control_set_rule_group_precedence, name="admission_control_set_rule_group_precedence", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.admission_control_update_policy, name="admission_control_update_policy", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.admission_control_update_policy_precedence, name="admission_control_update_policy_precedence", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.admission_control_update_rule_groups, name="admission_control_update_rule_groups", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.admission_control_delete_policies, name="admission_control_delete_policies", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.admission_control_delete_rule_groups, name="admission_control_delete_rule_groups", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.admission_control_remove_host_groups, name="admission_control_remove_host_groups", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.admission_control_remove_rule_group_custom_rule, name="admission_control_remove_rule_group_custom_rule", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.admission_control_replace_rule_group_selectors, name="admission_control_replace_rule_group_selectors", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def admission_control_add_host_groups(
        self,
        body: dict = Field(description="Request JSON body for `admission_control_add_host_groups` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Add one or more host groups to an admission control policy."""
        return self._call(operation="admission_control_add_host_groups", query_params=None, body_params=body, error_message="admission_control_add_host_groups failed", member_cid=member_cid)

    def admission_control_add_rule_group_custom_rule(
        self,
        body: dict = Field(description="Request JSON body for `admission_control_add_rule_group_custom_rule` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Add one or more custom Rego rules to a rule group in an admission control policy. The requested custom rules are also added to all other unspecified rule groups in the policy with action 'Disabled'."""
        return self._call(operation="admission_control_add_rule_group_custom_rule", query_params=None, body_params=body, error_message="admission_control_add_rule_group_custom_rule failed", member_cid=member_cid)

    def admission_control_create_policy(
        self,
        body: dict = Field(description="Request JSON body for `admission_control_create_policy` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create an admission control policy."""
        return self._call(operation="admission_control_create_policy", query_params=None, body_params=body, error_message="admission_control_create_policy failed", member_cid=member_cid)

    def admission_control_create_rule_groups(
        self,
        body: dict = Field(description="Request JSON body for `admission_control_create_rule_groups` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create one or more rule groups and add them to an existing admission control policy. The list of new rule groups will be created with the last rule group having highest precedence, second to last with second highest precedence, and so on."""
        return self._call(operation="admission_control_create_rule_groups", query_params=None, body_params=body, error_message="admission_control_create_rule_groups failed", member_cid=member_cid)

    def admission_control_delete_policies(
        self,
        ids: list[str] = Field(description="The ids of the policies to delete (maximum 100 IDs allowed)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete an admission control policy."""
        return self._call(operation="admission_control_delete_policies", query_params={"ids": ids}, error_message="admission_control_delete_policies failed", member_cid=member_cid)

    def admission_control_delete_rule_groups(
        self,
        policy_id: str = Field(description="The id of the policy to modify."),
        rule_group_ids: list[str] = Field(description="The ids of the rule groups to delete (maximum 100 IDs allowed)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete rule groups."""
        return self._call(operation="admission_control_delete_rule_groups", query_params={"policy_id": policy_id, "rule_group_ids": rule_group_ids}, error_message="admission_control_delete_rule_groups failed", member_cid=member_cid)

    def admission_control_get_policies(
        self,
        ids: list[str] = Field(description="The list of policies to return (maximum 100 IDs allowed)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get admission control policies."""
        return self._call(operation="admission_control_get_policies", query_params={"ids": ids}, error_message="admission_control_get_policies failed", member_cid=member_cid)

    def admission_control_query_policies(
        self,
        filter: str | None = Field(default=None, description="FQL filter, allowed properties: precedence created_timestamp modified_timestamp name description"),
        limit: int | None = Field(default=None, description="The maximum number of resources to return. The maximum allowed is 500."),
        offset: int | None = Field(default=None, description="The number of results to skip before starting to return results."),
        sort: str | None = Field(default=None, description="Field to sort on. Sortable fields: precedence created_timestamp modified_timestamp Use the |asc or |desc suffix to specify sort direction."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search admission control policies."""
        return self._call(operation="admission_control_query_policies", query_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort}, error_message="admission_control_query_policies failed", member_cid=member_cid)

    def admission_control_remove_host_groups(
        self,
        policy_id: str = Field(description="The id of the policy to modify."),
        host_group_ids: list[str] = Field(description="The ids of the host groups to remove (maximum 100 IDs allowed)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Remove one or more host groups from an admission control policy."""
        return self._call(operation="admission_control_remove_host_groups", query_params={"policy_id": policy_id, "host_group_ids": host_group_ids}, error_message="admission_control_remove_host_groups failed", member_cid=member_cid)

    def admission_control_remove_rule_group_custom_rule(
        self,
        policy_id: str = Field(description="The id of the policy to modify."),
        custom_rule_ids: list[str] = Field(description="The ids of the custom Rego rules to delete (maximum 100 IDs allowed)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete one or more custom Rego rules from all rule groups in an admission control policy."""
        return self._call(operation="admission_control_remove_rule_group_custom_rule", query_params={"policy_id": policy_id, "custom_rule_ids": custom_rule_ids}, error_message="admission_control_remove_rule_group_custom_rule failed", member_cid=member_cid)

    def admission_control_replace_rule_group_selectors(
        self,
        body: dict = Field(description="Request JSON body for `admission_control_replace_rule_group_selectors` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Replace labels and/or namespaces of a rule group within an admission control policy."""
        return self._call(operation="admission_control_replace_rule_group_selectors", query_params=None, body_params=body, error_message="admission_control_replace_rule_group_selectors failed", member_cid=member_cid)

    def admission_control_set_rule_group_precedence(
        self,
        body: dict = Field(description="Request JSON body for `admission_control_set_rule_group_precedence` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Change precedence of rule groups within an admission control policy."""
        return self._call(operation="admission_control_set_rule_group_precedence", query_params=None, body_params=body, error_message="admission_control_set_rule_group_precedence failed", member_cid=member_cid)

    def admission_control_update_policy(
        self,
        ids: str = Field(description="The id of the admission control policy to update."),
        body: dict = Field(description="Request JSON body for `admission_control_update_policy` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update an admission control policy."""
        return self._call(operation="admission_control_update_policy", query_params={"ids": ids}, body_params=body, error_message="admission_control_update_policy failed", member_cid=member_cid)

    def admission_control_update_policy_precedence(
        self,
        body: dict = Field(description="Request JSON body for `admission_control_update_policy_precedence` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update admission control policy precedence."""
        return self._call(operation="admission_control_update_policy_precedence", query_params=None, body_params=body, error_message="admission_control_update_policy_precedence failed", member_cid=member_cid)

    def admission_control_update_rule_groups(
        self,
        body: dict = Field(description="Request JSON body for `admission_control_update_rule_groups` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update a rule group. Change rule group name, description, deny on error, Image Assessment settings, default rule actions, and custom rule actions."""
        return self._call(operation="admission_control_update_rule_groups", query_params=None, body_params=body, error_message="admission_control_update_rule_groups failed", member_cid=member_cid)
