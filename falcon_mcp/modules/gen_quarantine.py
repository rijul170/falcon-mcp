"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `quarantine` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenQuarantineModule(GeneratedModuleBase):
    """Generated tools for the Falcon `quarantine` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.action_update_count, name="action_update_count")
        self._add_tool(server=server, method=self.get_aggregate_files, name="get_aggregate_files")
        self._add_tool(server=server, method=self.update_qf_by_query, name="update_qf_by_query", annotations=WRITE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def action_update_count(
        self,
        filter: str = Field(description="FQL specifying filter parameters."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns count of potentially affected quarantined files for each action."""
        return self._call(operation="ActionUpdateCount", query_params={"filter": filter}, error_message="ActionUpdateCount failed", member_cid=member_cid)

    def get_aggregate_files(
        self,
        body: dict = Field(description="Request JSON body for `GetAggregateFiles` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get quarantine file aggregates as specified via json in request body."""
        return self._call(operation="GetAggregateFiles", query_params=None, body_params=body, error_message="GetAggregateFiles failed", member_cid=member_cid)

    def update_qf_by_query(
        self,
        body: dict = Field(description="Request JSON body for `UpdateQfByQuery` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Apply quarantine file actions by query."""
        return self._call(operation="UpdateQfByQuery", query_params=None, body_params=body, error_message="UpdateQfByQuery failed", member_cid=member_cid)
