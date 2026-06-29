"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `real_time_response_audit` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenRealTimeResponseAuditModule(GeneratedModuleBase):
    """Generated tools for the Falcon `real_time_response_audit` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.rtr_audit_sessions, name="rtr_audit_sessions")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def rtr_audit_sessions(
        self,
        filter: str | None = Field(default=None, description="Optional filter criteria in the form of an FQL query. For more information about FQL queries, see our [FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide)."),
        sort: str | None = Field(default=None, description="how to sort the session IDs. e.g. sort=created_at|desc will sort the results based on createdAt in descending order"),
        limit: int | None = Field(default=None, description="number of sessions to be returned"),
        offset: int | None = Field(default=None, description="offset value to be used for paginated results"),
        with_command_info: bool | None = Field(default=None, description="get sessions with command info included; by default sessions are returned without command info which include cloud_request_ids and logs fields"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get all the RTR sessions created for a customer in a specified duration"""
        return self._call(operation="RTRAuditSessions", query_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset, "with_command_info": with_command_info}, error_message="RTRAuditSessions failed", member_cid=member_cid)
