"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `response_policies` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenResponsePoliciesModule(GeneratedModuleBase):
    """Generated tools for the Falcon `response_policies` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_rt_response_policies, name="get_rt_response_policies")
        self._add_tool(server=server, method=self.query_rt_response_policies, name="query_rt_response_policies")
        self._add_tool(server=server, method=self.query_rt_response_policy_members, name="query_rt_response_policy_members")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def get_rt_response_policies(
        self,
        ids: list[str] = Field(description="The IDs of the RTR Policies to return"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve a set of Response Policies by specifying their IDs"""
        return self._call(operation="getRTResponsePolicies", query_params={"ids": ids}, error_message="getRTResponsePolicies failed", member_cid=member_cid)

    def query_rt_response_policies(
        self,
        filter: str | None = Field(default=None, description="The filter expression that should be used to determine the results."),
        offset: int | None = Field(default=None, description="The offset of the first record to retrieve from"),
        limit: int | None = Field(default=None, description="The maximum number of records to return [1-5000]"),
        sort: str | None = Field(default=None, description="The property to sort results by"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for Response Policies in your environment by providing an FQL filter with sort and/or paging details. This returns a set of Response Policy IDs that match the given criteria."""
        return self._call(operation="queryRTResponsePolicies", query_params={"filter": filter, "offset": offset, "limit": limit, "sort": sort}, error_message="queryRTResponsePolicies failed", member_cid=member_cid)

    def query_rt_response_policy_members(
        self,
        id: str | None = Field(default=None, description="The ID of the Response policy to search for members of"),
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results"),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        limit: int | None = Field(default=None, description="The maximum records to return. [1-5000]"),
        sort: str | None = Field(default=None, description="The property to sort by"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for members of a Response policy in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria"""
        return self._call(operation="queryRTResponsePolicyMembers", query_params={"id": id, "filter": filter, "offset": offset, "limit": limit, "sort": sort}, error_message="queryRTResponsePolicyMembers failed", member_cid=member_cid)
