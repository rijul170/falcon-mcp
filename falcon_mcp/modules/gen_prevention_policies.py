"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `prevention_policies` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenPreventionPoliciesModule(GeneratedModuleBase):
    """Generated tools for the Falcon `prevention_policies` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_prevention_policies, name="get_prevention_policies")
        self._add_tool(server=server, method=self.query_prevention_policies, name="query_prevention_policies")
        self._add_tool(server=server, method=self.query_prevention_policy_members, name="query_prevention_policy_members")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def get_prevention_policies(
        self,
        ids: list[str] = Field(description="The IDs of the Prevention Policies to return"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve a set of Prevention Policies by specifying their IDs"""
        return self._call(operation="getPreventionPolicies", query_params={"ids": ids}, error_message="getPreventionPolicies failed", member_cid=member_cid)

    def query_prevention_policies(
        self,
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results"),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        limit: int | None = Field(default=None, description="The maximum records to return. [1-5000]"),
        sort: str | None = Field(default=None, description="The property to sort by"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for Prevention Policies in your environment by providing an FQL filter and paging details. Returns a set of Prevention Policy IDs which match the filter criteria"""
        return self._call(operation="queryPreventionPolicies", query_params={"filter": filter, "offset": offset, "limit": limit, "sort": sort}, error_message="queryPreventionPolicies failed", member_cid=member_cid)

    def query_prevention_policy_members(
        self,
        id: str | None = Field(default=None, description="The ID of the Prevention Policy to search for members of"),
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results"),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        limit: int | None = Field(default=None, description="The maximum records to return. [1-5000]"),
        sort: str | None = Field(default=None, description="The property to sort by"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for members of a Prevention Policy in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria"""
        return self._call(operation="queryPreventionPolicyMembers", query_params={"id": id, "filter": filter, "offset": offset, "limit": limit, "sort": sort}, error_message="queryPreventionPolicyMembers failed", member_cid=member_cid)
