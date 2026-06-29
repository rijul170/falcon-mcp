"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `image_assessment_policies` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenImageAssessmentPoliciesModule(GeneratedModuleBase):
    """Generated tools for the Falcon `image_assessment_policies` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.read_policies, name="read_policies")
        self._add_tool(server=server, method=self.read_policy_exclusions, name="read_policy_exclusions")
        self._add_tool(server=server, method=self.read_policy_groups, name="read_policy_groups")
        self._add_tool(server=server, method=self.create_policies, name="create_policies", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.create_policy_groups, name="create_policy_groups", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_policies, name="update_policies", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_policy_exclusions, name="update_policy_exclusions", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_policy_groups, name="update_policy_groups", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_policy_precedence, name="update_policy_precedence", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_policy, name="delete_policy", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_policy_group, name="delete_policy_group", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def create_policies(
        self,
        body: dict = Field(description="Request JSON body for `CreatePolicies` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create Image Assessment policies"""
        return self._call(operation="CreatePolicies", query_params=None, body_params=body, error_message="CreatePolicies failed", member_cid=member_cid)

    def create_policy_groups(
        self,
        body: dict = Field(description="Request JSON body for `CreatePolicyGroups` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create Image Assessment Policy Group entities"""
        return self._call(operation="CreatePolicyGroups", query_params=None, body_params=body, error_message="CreatePolicyGroups failed", member_cid=member_cid)

    def delete_policy(
        self,
        id: str = Field(description="Image Assessment Policy entity UUID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete Image Assessment Policy by policy UUID"""
        return self._call(operation="DeletePolicy", query_params={"id": id}, error_message="DeletePolicy failed", member_cid=member_cid)

    def delete_policy_group(
        self,
        id: str = Field(description="Policy Image Group entity UUID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete Image Assessment Policy Group entities"""
        return self._call(operation="DeletePolicyGroup", query_params={"id": id}, error_message="DeletePolicyGroup failed", member_cid=member_cid)

    def read_policies(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get all Image Assessment policies"""
        return self._call(operation="ReadPolicies", query_params=None, error_message="ReadPolicies failed", member_cid=member_cid)

    def read_policy_exclusions(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve Image Assessment Policy Exclusion entities"""
        return self._call(operation="ReadPolicyExclusions", query_params=None, error_message="ReadPolicyExclusions failed", member_cid=member_cid)

    def read_policy_groups(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve Image Assessment Policy Group entities"""
        return self._call(operation="ReadPolicyGroups", query_params=None, error_message="ReadPolicyGroups failed", member_cid=member_cid)

    def update_policies(
        self,
        id: str = Field(description="Image Assessment Policy entity UUID"),
        body: dict = Field(description="Request JSON body for `UpdatePolicies` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update Image Assessment Policy entities"""
        return self._call(operation="UpdatePolicies", query_params={"id": id}, body_params=body, error_message="UpdatePolicies failed", member_cid=member_cid)

    def update_policy_exclusions(
        self,
        body: dict = Field(description="Request JSON body for `UpdatePolicyExclusions` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update Image Assessment Policy Exclusion entities"""
        return self._call(operation="UpdatePolicyExclusions", query_params=None, body_params=body, error_message="UpdatePolicyExclusions failed", member_cid=member_cid)

    def update_policy_groups(
        self,
        id: str = Field(description="Policy Image Group entity UUID"),
        body: dict = Field(description="Request JSON body for `UpdatePolicyGroups` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update Image Assessment Policy Group entities"""
        return self._call(operation="UpdatePolicyGroups", query_params={"id": id}, body_params=body, error_message="UpdatePolicyGroups failed", member_cid=member_cid)

    def update_policy_precedence(
        self,
        body: dict = Field(description="Request JSON body for `UpdatePolicyPrecedence` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update Image Assessment Policy precedence"""
        return self._call(operation="UpdatePolicyPrecedence", query_params=None, body_params=body, error_message="UpdatePolicyPrecedence failed", member_cid=member_cid)
