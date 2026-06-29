"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `device_content` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenDeviceContentModule(GeneratedModuleBase):
    """Generated tools for the Falcon `device_content` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.entities_states_v1, name="entities_states_v1")
        self._add_tool(server=server, method=self.queries_states_v1, name="queries_states_v1")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def entities_states_v1(
        self,
        ids: list[str] = Field(description="The ids of the devices to fetch the content state of."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve the host content state for a number of ids between 1 and 100."""
        return self._call(operation="entities_states_v1", query_params={"ids": ids}, error_message="entities_states_v1 failed", member_cid=member_cid)

    def queries_states_v1(
        self,
        limit: int | None = Field(default=None, description="The max number of resource ids to return."),
        sort: str | None = Field(default=None, description="What field to sort the results on."),
        offset: int | None = Field(default=None, description="The offset token returned from the previous query. If none was returned, there are no more pages to the result set."),
        filter: str | None = Field(default=None, description="The FQL search filter"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Query for the content state of the host."""
        return self._call(operation="queries_states_v1", query_params={"limit": limit, "sort": sort, "offset": offset, "filter": filter}, error_message="queries_states_v1 failed", member_cid=member_cid)
