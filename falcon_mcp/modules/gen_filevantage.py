"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `filevantage` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenFilevantageModule(GeneratedModuleBase):
    """Generated tools for the Falcon `filevantage` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.query_changes, name="query_changes")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def query_changes(
        self,
        offset: int | None = Field(default=None, description="The offset to start retrieving records from. Defaults to 0 if not specified."),
        limit: int | None = Field(default=None, description="The maximum number of ids to return. Defaults to 100 if not specified. The maximum number of results that can be returned in a single call is 500."),
        sort: str | None = Field(default=None, description="Sort results using options like: action_timestamp (timestamp of the change occurrence) Sort either asc (ascending) or desc (descending). For example: action_timestamp|asc. The full list of allowed sorting options can be reviewed in our API documentation."),
        filter: str | None = Field(default=None, description="Filter changes using a query in Falcon Query Language (FQL). Common filter options include: - host.name - action_timestamp The full list of allowed filter parameters can be reviewed in our API documentation."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns 1 or more change ids"""
        return self._call(operation="queryChanges", query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter}, error_message="queryChanges failed", member_cid=member_cid)
