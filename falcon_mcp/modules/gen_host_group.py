"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `host_group` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenHostGroupModule(GeneratedModuleBase):
    """Generated tools for the Falcon `host_group` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.query_combined_host_groups, name="query_combined_host_groups")
        self._add_tool(server=server, method=self.query_group_members, name="query_group_members")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def query_combined_host_groups(
        self,
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results"),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        limit: int | None = Field(default=None, description="The maximum records to return. [1-5000]"),
        sort: str | None = Field(default=None, description="The property to sort by"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for Host Groups in your environment by providing an FQL filter and paging details. Returns a set of Host Groups which match the filter criteria"""
        return self._call(operation="queryCombinedHostGroups", query_params={"filter": filter, "offset": offset, "limit": limit, "sort": sort}, error_message="queryCombinedHostGroups failed", member_cid=member_cid)

    def query_group_members(
        self,
        id: str | None = Field(default=None, description="The ID of the Host Group to search for members of"),
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results"),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        limit: int | None = Field(default=None, description="The maximum records to return. [1-5000]"),
        sort: str | None = Field(default=None, description="The property to sort by"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for members of a Host Group in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria"""
        return self._call(operation="queryGroupMembers", query_params={"id": id, "filter": filter, "offset": offset, "limit": limit, "sort": sort}, error_message="queryGroupMembers failed", member_cid=member_cid)
