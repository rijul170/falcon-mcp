"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `real_time_response_admin` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenRealTimeResponseAdminModule(GeneratedModuleBase):
    """Generated tools for the Falcon `real_time_response_admin` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.rtr_check_admin_command_status, name="rtr_check_admin_command_status")
        self._add_tool(server=server, method=self.rtr_get_put_file_contents, name="rtr_get_put_file_contents")
        self._add_tool(server=server, method=self.rtr_execute_admin_command, name="rtr_execute_admin_command", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def rtr_check_admin_command_status(
        self,
        cloud_request_id: str = Field(description="Cloud Request ID of the executed command to query"),
        sequence_id: int = Field(description="Sequence ID that we want to retrieve. Command responses are chunked across sequences"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get status of an executed RTR administrator command on a single host."""
        return self._call(operation="RTR_CheckAdminCommandStatus", query_params={"cloud_request_id": cloud_request_id, "sequence_id": sequence_id}, error_message="RTR_CheckAdminCommandStatus failed", member_cid=member_cid)

    def rtr_execute_admin_command(
        self,
        body: dict = Field(description="Request JSON body for `RTR_ExecuteAdminCommand` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Execute a RTR administrator command on a single host."""
        return self._call(operation="RTR_ExecuteAdminCommand", query_params=None, body_params=body, error_message="RTR_ExecuteAdminCommand failed", member_cid=member_cid)

    def rtr_get_put_file_contents(
        self,
        id: str = Field(description="put file ID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get RTR put file contents for a given file ID"""
        return self._call(operation="RTR_GetPutFileContents", query_params={"id": id}, error_message="RTR_GetPutFileContents failed", member_cid=member_cid)
