"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `real_time_response` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenRealTimeResponseModule(GeneratedModuleBase):
    """Generated tools for the Falcon `real_time_response` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.batch_get_cmd_status, name="batch_get_cmd_status")
        self._add_tool(server=server, method=self.rtr_check_active_responder_command_status, name="rtr_check_active_responder_command_status")
        self._add_tool(server=server, method=self.rtr_get_extracted_file_contents, name="rtr_get_extracted_file_contents")
        self._add_tool(server=server, method=self.rtr_delete_file_v2, name="rtr_delete_file_v2", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.rtr_delete_queued_session, name="rtr_delete_queued_session", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.rtr_execute_active_responder_command, name="rtr_execute_active_responder_command", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.rtr_list_queued_sessions, name="rtr_list_queued_sessions", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def batch_get_cmd_status(
        self,
        batch_get_cmd_req_id: str = Field(description="Batch Get Command Request ID received from /real-time-response/combined/get-command/v1"),
        timeout: int | None = Field(default=None, description="Timeout for how long to wait for the request in seconds, default timeout is 30 seconds. Maximum is 5 minutes."),
        timeout_duration: str | None = Field(default=None, description="Timeout duration for how long to wait for the request in duration syntax. Example, 10s. Valid units: ns, us, ms, s, m, h. Maximum is 5 minutes."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves the status of the specified batch get command. Will return successful files when they are finished processing."""
        return self._call(operation="BatchGetCmdStatus", query_params={"timeout": timeout, "timeout_duration": timeout_duration, "batch_get_cmd_req_id": batch_get_cmd_req_id}, error_message="BatchGetCmdStatus failed", member_cid=member_cid)

    def rtr_check_active_responder_command_status(
        self,
        cloud_request_id: str = Field(description="Cloud Request ID of the executed command to query"),
        sequence_id: int = Field(description="Sequence ID that we want to retrieve. Command responses are chunked across sequences"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get status of an executed active-responder command on a single host."""
        return self._call(operation="RTR_CheckActiveResponderCommandStatus", query_params={"cloud_request_id": cloud_request_id, "sequence_id": sequence_id}, error_message="RTR_CheckActiveResponderCommandStatus failed", member_cid=member_cid)

    def rtr_delete_file_v2(
        self,
        ids: str = Field(description="RTR Session file id"),
        session_id: str = Field(description="RTR Session id"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete a RTR session file."""
        return self._call(operation="RTR_DeleteFileV2", query_params={"ids": ids, "session_id": session_id}, error_message="RTR_DeleteFileV2 failed", member_cid=member_cid)

    def rtr_delete_queued_session(
        self,
        session_id: str = Field(description="RTR Session id"),
        cloud_request_id: str = Field(description="Cloud Request ID of the executed command to query"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete a queued session command"""
        return self._call(operation="RTR_DeleteQueuedSession", query_params={"session_id": session_id, "cloud_request_id": cloud_request_id}, error_message="RTR_DeleteQueuedSession failed", member_cid=member_cid)

    def rtr_execute_active_responder_command(
        self,
        body: dict = Field(description="Request JSON body for `RTR_ExecuteActiveResponderCommand` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Execute an active responder command on a single host."""
        return self._call(operation="RTR_ExecuteActiveResponderCommand", query_params=None, body_params=body, error_message="RTR_ExecuteActiveResponderCommand failed", member_cid=member_cid)

    def rtr_get_extracted_file_contents(
        self,
        session_id: str = Field(description="RTR Session id"),
        sha256: str = Field(description="Extracted SHA256 (e.g. 'efa256a96af3b556cd3fc9d8b1cf587d72807d7805ced441e8149fc279db422b')"),
        filename: str | None = Field(default=None, description="Filename to use for the archive name and the file within the archive."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get RTR extracted file contents for specified session and sha256."""
        return self._call(operation="RTR_GetExtractedFileContents", query_params={"session_id": session_id, "sha256": sha256, "filename": filename}, error_message="RTR_GetExtractedFileContents failed", member_cid=member_cid)

    def rtr_list_queued_sessions(
        self,
        body: dict = Field(description="Request JSON body for `RTR_ListQueuedSessions` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get queued session metadata by session ID."""
        return self._call(operation="RTR_ListQueuedSessions", query_params=None, body_params=body, error_message="RTR_ListQueuedSessions failed", member_cid=member_cid)
