"""
Real Time Response module for Falcon MCP Server.

This module provides tools for initiating and inspecting RTR sessions and for
executing read-only RTR commands during host investigations.
"""

from textwrap import dedent
from typing import Any

from mcp.server import FastMCP
from mcp.server.fastmcp.resources import TextResource
from mcp.types import ToolAnnotations
from pydantic import AnyUrl, Field

from falcon_mcp.common.errors import handle_api_response
from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule
from falcon_mcp.resources.rtr import (
    EMBEDDED_FQL_SYNTAX,
    SEARCH_RTR_SESSIONS_FQL_DOCUMENTATION,
)

logger = get_logger(__name__)


class RTRModule(BaseModule):
    """Module for Real Time Response hunt and triage workflows."""

    def register_tools(self, server: FastMCP) -> None:
        """Register tools with the MCP server.

        Args:
            server: MCP server instance
        """
        self._add_tool(
            server=server,
            method=self.search_sessions,
            name="search_rtr_sessions",
        )

        self._add_tool(
            server=server,
            method=self.get_session_details,
            name="get_rtr_session_details",
        )

        self._add_tool(
            server=server,
            method=self.init_session,
            name="init_rtr_session",
            annotations=ToolAnnotations(
                readOnlyHint=False,
                destructiveHint=False,
                idempotentHint=False,
                openWorldHint=True,
            ),
        )

        self._add_tool(
            server=server,
            method=self.pulse_session,
            name="pulse_rtr_session",
            annotations=ToolAnnotations(
                readOnlyHint=False,
                destructiveHint=False,
                idempotentHint=False,
                openWorldHint=True,
            ),
        )

        self._add_tool(
            server=server,
            method=self.execute_read_only_command,
            name="execute_rtr_read_only_command",
            annotations=ToolAnnotations(
                readOnlyHint=False,
                destructiveHint=False,
                idempotentHint=False,
                openWorldHint=True,
            ),
        )

        self._add_tool(
            server=server,
            method=self.check_command_status,
            name="check_rtr_command_status",
        )

        self._add_tool(
            server=server,
            method=self.list_session_files,
            name="list_rtr_session_files",
        )

        self._add_tool(
            server=server,
            method=self.delete_session,
            name="delete_rtr_session",
            annotations=ToolAnnotations(
                readOnlyHint=False,
                destructiveHint=True,
                idempotentHint=True,
                openWorldHint=True,
            ),
        )

        self._add_tool(
            server=server,
            method=self.batch_init_session,
            name="batch_init_rtr_session",
            annotations=ToolAnnotations(
                readOnlyHint=False,
                destructiveHint=False,
                idempotentHint=False,
                openWorldHint=True,
            ),
        )

        self._add_tool(
            server=server,
            method=self.batch_refresh_session,
            name="batch_refresh_rtr_session",
            annotations=ToolAnnotations(
                readOnlyHint=False,
                destructiveHint=False,
                idempotentHint=False,
                openWorldHint=True,
            ),
        )

        self._add_tool(
            server=server,
            method=self.batch_execute_command,
            name="batch_execute_rtr_command",
            annotations=ToolAnnotations(
                readOnlyHint=False,
                destructiveHint=False,
                idempotentHint=False,
                openWorldHint=True,
            ),
        )

        self._add_tool(
            server=server,
            method=self.batch_execute_active_responder_command,
            name="batch_execute_rtr_active_responder_command",
            annotations=ToolAnnotations(
                readOnlyHint=False,
                destructiveHint=True,
                idempotentHint=False,
                openWorldHint=True,
            ),
        )

        self._add_tool(
            server=server,
            method=self.batch_execute_admin_command,
            name="batch_execute_rtr_admin_command",
            annotations=ToolAnnotations(
                readOnlyHint=False,
                destructiveHint=True,
                idempotentHint=False,
                openWorldHint=True,
            ),
        )

        self._add_tool(
            server=server,
            method=self.batch_get_command,
            name="batch_get_rtr_command",
            annotations=ToolAnnotations(
                readOnlyHint=False,
                destructiveHint=False,
                idempotentHint=False,
                openWorldHint=True,
            ),
        )

        # RTR scripts
        self._add_tool(server=server, method=self.search_rtr_scripts, name="search_rtr_scripts")
        self._add_tool(server=server, method=self.get_rtr_script_details, name="get_rtr_script_details")
        self._add_tool(
            server=server, method=self.upload_rtr_script, name="upload_rtr_script",
            annotations=ToolAnnotations(
                readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True,
            ),
        )
        self._add_tool(
            server=server, method=self.update_rtr_script, name="update_rtr_script",
            annotations=ToolAnnotations(
                readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True,
            ),
        )
        self._add_tool(
            server=server, method=self.delete_rtr_scripts, name="delete_rtr_scripts",
            annotations=ToolAnnotations(
                readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True,
            ),
        )

        # Falcon (built-in) scripts
        self._add_tool(server=server, method=self.search_falcon_scripts, name="search_falcon_scripts")
        self._add_tool(server=server, method=self.get_falcon_script_details, name="get_falcon_script_details")

        # RTR put-files
        self._add_tool(server=server, method=self.search_rtr_put_files, name="search_rtr_put_files")
        self._add_tool(server=server, method=self.get_rtr_put_file_details, name="get_rtr_put_file_details")
        self._add_tool(
            server=server, method=self.delete_rtr_put_files, name="delete_rtr_put_files",
            annotations=ToolAnnotations(
                readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True,
            ),
        )

    def register_resources(self, server: FastMCP) -> None:
        """Register resources with the MCP server.

        Args:
            server: MCP server instance
        """
        search_rtr_sessions_fql_resource = TextResource(
            uri=AnyUrl("falcon://rtr/sessions/search/fql-guide"),
            name="falcon_search_rtr_sessions_fql_guide",
            description="Contains the guide for the `filter` param of the `falcon_search_rtr_sessions` tool.",
            text=SEARCH_RTR_SESSIONS_FQL_DOCUMENTATION,
        )

        self._add_resource(
            server,
            search_rtr_sessions_fql_resource,
        )

    def search_sessions(
        self,
        filter: str | None = Field(
            default=None,
            description=EMBEDDED_FQL_SYNTAX,
            examples=["hostname:'BRR-WB-LIB-22'", "aid:'2c5c4e7738...'"],
        ),
        limit: int = Field(
            default=10,
            ge=1,
            le=5000,
            description="Maximum number of RTR session IDs to return. Max: 5000.",
        ),
        offset: int | None = Field(
            default=None,
            description="Starting index of overall result set from which to return IDs.",
        ),
        sort: str | None = Field(
            default=None,
            description=dedent("""
                Sort RTR sessions by a supported session property such as:
                `created_at.asc`, `updated_at.desc`, or `hostname.asc`.
            """).strip(),
            examples=["created_at.desc", "hostname.asc"],
        ),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID to scope this call to a specific child tenant. Obtain child CIDs from `falcon_list_child_accounts`. Leave unset to use the parent account scope.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search RTR sessions and return full session details.

        IMPORTANT: You must use the `falcon://rtr/sessions/search/fql-guide` resource when you need to use the `filter` parameter.
        This resource contains the guide on how to build the FQL `filter` parameter for the `falcon_search_rtr_sessions` tool.

        Returns FQL syntax guide on error or empty results to help refine queries.
        """
        session_ids = self._base_search_api_call(
            operation="RTR_ListAllSessions",
            search_params={
                "filter": filter,
                "limit": limit,
                "offset": offset,
                "sort": sort,
            },
            error_message="Failed to search RTR sessions",
            member_cid=member_cid,
        )

        if self._is_error(session_ids):
            return self._format_fql_error_response(
                [session_ids], filter, SEARCH_RTR_SESSIONS_FQL_DOCUMENTATION
            )

        if not session_ids:
            return self._format_fql_error_response(
                [], filter, SEARCH_RTR_SESSIONS_FQL_DOCUMENTATION
            )

        details = self._base_get_by_ids(
            operation="RTR_ListSessions",
            ids=session_ids,
            id_key="ids",
            use_params=False,
            member_cid=member_cid,
        )

        if self._is_error(details):
            return [details]

        return details

    def get_session_details(
        self,
        ids: list[str] = Field(
            description="RTR session IDs to retrieve details for.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Retrieve detailed metadata for one or more RTR sessions."""
        logger.debug("Getting RTR session details for IDs: %s", ids)

        if not ids:
            return []

        return self._base_get_by_ids(
            operation="RTR_ListSessions",
            ids=ids,
            id_key="ids",
            use_params=False,
        )

    def init_session(
        self,
        device_id: str = Field(
            description="The host agent ID (AID) to open or reuse an RTR session for.",
        ),
        origin: str = Field(
            default="falcon-mcp",
            description="Origin label for the RTR request.",
        ),
        queue_offline: bool = Field(
            default=False,
            description="Queue the request if the host is currently offline.",
        ),
        timeout: int | None = Field(
            default=None,
            ge=1,
            le=600,
            description="How long to wait for the request in seconds. Max: 600.",
        ),
        timeout_duration: str | None = Field(
            default=None,
            description="Alternate duration syntax such as `30s`, `2m`, or `1h`.",
        ),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID to scope this session to a specific child tenant. Required when the target host belongs to a child tenant. Obtain child CIDs from `falcon_list_child_accounts`.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Initialize or reuse an RTR session for a single host."""
        return self._base_query_api_call(
            operation="RTR_InitSession",
            query_params={
                "timeout": timeout,
                "timeout_duration": timeout_duration,
            },
            body_params={
                "device_id": device_id,
                "origin": origin,
                "queue_offline": queue_offline,
            },
            error_message="Failed to initialize RTR session",
            member_cid=member_cid,
        )

    def pulse_session(
        self,
        device_id: str = Field(
            description="The host agent ID (AID) whose RTR session timeout should be refreshed.",
        ),
        origin: str = Field(
            default="falcon-mcp",
            description="Origin label for the RTR request.",
        ),
        queue_offline: bool = Field(
            default=False,
            description="Queue the pulse if the host is currently offline.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Refresh an RTR session timeout for a single host."""
        return self._base_query_api_call(
            operation="RTR_PulseSession",
            body_params={
                "device_id": device_id,
                "origin": origin,
                "queue_offline": queue_offline,
            },
            error_message="Failed to pulse RTR session",
        )

    def execute_read_only_command(
        self,
        session_id: str = Field(
            description="RTR session ID returned from falcon_init_rtr_session or falcon_search_rtr_sessions.",
        ),
        base_command: str = Field(
            description="Read-only RTR base command to execute, such as `ls`, `ps`, `cat`, `filehash`, or `reg`.",
            examples=["ls", "ps", "filehash"],
        ),
        command_string: str | None = Field(
            default=None,
            description="Optional full command line to execute. Example: `cat C:\\Windows\\win.ini`.",
        ),
        persist: bool = Field(
            default=False,
            description="Persist the read-only command in the RTR session history.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Execute a read-only RTR command on a single host.

        This tool is intentionally limited to the read-only RTR endpoint for
        hunt and triage workflows. It does not expose admin or remediation
        command APIs.
        """
        return self._base_query_api_call(
            operation="RTR_ExecuteCommand",
            body_params={
                "session_id": session_id,
                "base_command": base_command,
                "command_string": command_string,
                "persist": persist,
            },
            error_message="Failed to execute RTR read-only command",
        )

    def check_command_status(
        self,
        cloud_request_id: str = Field(
            description="Cloud request ID returned from falcon_execute_rtr_read_only_command.",
        ),
        sequence_id: int = Field(
            default=0,
            ge=0,
            description="Sequence chunk to retrieve for command output. Starts at 0.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get the status and output chunk for an RTR command."""
        return self._base_query_api_call(
            operation="RTR_CheckCommandStatus",
            query_params={
                "cloud_request_id": cloud_request_id,
                "sequence_id": sequence_id,
            },
            error_message="Failed to check RTR command status",
        )

    def list_session_files(
        self,
        session_id: str = Field(
            description="RTR session ID to retrieve extracted session files for.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List files currently associated with an RTR session."""
        return self._base_query_api_call(
            operation="RTR_ListFilesV2",
            query_params={"session_id": session_id},
            error_message="Failed to list RTR session files",
        )

    def delete_session(
        self,
        session_id: str = Field(
            description="RTR session ID to close.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Delete an RTR session."""
        return self._base_query_api_call(
            operation="RTR_DeleteSession",
            query_params={"session_id": session_id},
            error_message="Failed to delete RTR session",
        )

    def batch_init_session(
        self,
        host_ids: list[str] = Field(
            description="Agent IDs (AIDs) of hosts to open batch RTR sessions on.",
        ),
        queue_offline: bool = Field(
            default=False,
            description="Queue sessions for hosts that are currently offline.",
        ),
        existing_batch_id: str | None = Field(
            default=None,
            description="Optional existing batch ID to add hosts to, rather than creating a new batch.",
        ),
        timeout: int | None = Field(
            default=None,
            ge=1,
            le=600,
            description="Seconds to wait for the overall batch request. Max: 600.",
        ),
        timeout_duration: str | None = Field(
            default=None,
            description="Alternate duration syntax for overall timeout, e.g. `30s`, `2m`.",
        ),
        host_timeout_duration: str | None = Field(
            default=None,
            description="Alternate duration syntax for per-host timeout, e.g. `30s`, `1m`.",
        ),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID to scope this call to a specific child tenant. Obtain child CIDs from `falcon_list_child_accounts`. Leave unset to use the parent account scope.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Initialize RTR sessions across multiple hosts simultaneously.

        Returns a batch_id to use with subsequent batch command tools.
        Use this instead of `falcon_init_rtr_session` when targeting more than one host.
        """
        return self._base_query_api_call(
            operation="BatchInitSessions",
            query_params={
                "timeout": timeout,
                "timeout_duration": timeout_duration,
                "host_timeout_duration": host_timeout_duration,
            },
            body_params={
                "host_ids": host_ids,
                "queue_offline": queue_offline,
                "existing_batch_id": existing_batch_id,
            },
            error_message="Failed to initialize batch RTR session",
            member_cid=member_cid,
        )

    def batch_refresh_session(
        self,
        batch_id: str = Field(
            description="Batch ID returned from `falcon_batch_init_rtr_session`.",
        ),
        hosts_to_remove: list[str] | None = Field(
            default=None,
            description="Optional list of host AIDs to remove from the batch before refreshing.",
        ),
        timeout: int | None = Field(
            default=None,
            ge=1,
            le=600,
            description="Seconds to wait for the batch refresh. Max: 600.",
        ),
        timeout_duration: str | None = Field(
            default=None,
            description="Alternate duration syntax for overall timeout, e.g. `30s`, `2m`.",
        ),
        host_timeout_duration: str | None = Field(
            default=None,
            description="Alternate duration syntax for per-host timeout, e.g. `30s`, `1m`.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Refresh a batch RTR session timeout to keep it alive.

        Call this before the 10-minute session idle timeout to maintain batch sessions
        during long-running investigations.
        """
        return self._base_query_api_call(
            operation="BatchRefreshSessions",
            query_params={
                "timeout": timeout,
                "timeout_duration": timeout_duration,
                "host_timeout_duration": host_timeout_duration,
            },
            body_params={
                "batch_id": batch_id,
                "hosts_to_remove": hosts_to_remove,
            },
            error_message="Failed to refresh batch RTR session",
        )

    def batch_execute_command(
        self,
        batch_id: str = Field(
            description="Batch ID returned from `falcon_batch_init_rtr_session`.",
        ),
        base_command: str = Field(
            description="Read-only RTR command to execute across all hosts in the batch. Examples: `ls`, `ps`, `cat`, `filehash`, `netstat`, `reg query`.",
            examples=["ls", "ps", "cat", "filehash", "netstat"],
        ),
        command_string: str | None = Field(
            default=None,
            description="Full command line to execute. Example: `cat C:\\\\Windows\\\\win.ini`.",
        ),
        optional_hosts: list[str] | None = Field(
            default=None,
            description="Subset of host AIDs from the batch to run the command on. Leave unset to target all hosts in the batch.",
        ),
        timeout: int | None = Field(
            default=None,
            ge=1,
            le=600,
            description="Seconds to wait for command completion. Max: 600.",
        ),
        timeout_duration: str | None = Field(
            default=None,
            description="Alternate duration syntax for overall timeout, e.g. `30s`, `2m`.",
        ),
        host_timeout_duration: str | None = Field(
            default=None,
            description="Alternate duration syntax for per-host timeout, e.g. `30s`, `1m`.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Execute a read-only RTR command across all hosts in a batch session.

        This is the batch equivalent of `falcon_execute_rtr_read_only_command`.
        Results are returned per-host. Use for large-scale hunt and triage workflows.
        """
        return self._base_query_api_call(
            operation="BatchCmd",
            query_params={
                "timeout": timeout,
                "timeout_duration": timeout_duration,
                "host_timeout_duration": host_timeout_duration,
            },
            body_params={
                "batch_id": batch_id,
                "base_command": base_command,
                "command_string": command_string,
                "optional_hosts": optional_hosts,
            },
            error_message="Failed to execute batch RTR read-only command",
        )

    def batch_execute_active_responder_command(
        self,
        batch_id: str = Field(
            description="Batch ID returned from `falcon_batch_init_rtr_session`.",
        ),
        base_command: str = Field(
            description="Active-responder RTR command to execute. Examples: `put`, `run`, `rm`, `cp`, `mv`, `mkdir`, `reg set`, `reg delete`, `kill`.",
            examples=["put", "run", "rm", "kill"],
        ),
        command_string: str | None = Field(
            default=None,
            description="Full command line to execute. Example: `run remediation.exe`.",
        ),
        optional_hosts: list[str] | None = Field(
            default=None,
            description="Subset of host AIDs from the batch to run the command on. Leave unset to target all hosts in the batch.",
        ),
        timeout: int | None = Field(
            default=None,
            ge=1,
            le=600,
            description="Seconds to wait for command completion. Max: 600.",
        ),
        timeout_duration: str | None = Field(
            default=None,
            description="Alternate duration syntax for overall timeout, e.g. `30s`, `2m`.",
        ),
        host_timeout_duration: str | None = Field(
            default=None,
            description="Alternate duration syntax for per-host timeout, e.g. `30s`, `1m`.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Execute an active-responder RTR command across all hosts in a batch session.

        IMPORTANT: Active-responder commands can modify host state (write files, kill processes,
        modify registry). Confirm intent before executing. Requires active-responder RTR role.
        """
        return self._base_query_api_call(
            operation="BatchActiveResponderCmd",
            query_params={
                "timeout": timeout,
                "timeout_duration": timeout_duration,
                "host_timeout_duration": host_timeout_duration,
            },
            body_params={
                "batch_id": batch_id,
                "base_command": base_command,
                "command_string": command_string,
                "optional_hosts": optional_hosts,
            },
            error_message="Failed to execute batch active-responder RTR command",
        )

    def batch_execute_admin_command(
        self,
        batch_id: str = Field(
            description="Batch ID returned from `falcon_batch_init_rtr_session`.",
        ),
        base_command: str = Field(
            description="Admin RTR command to execute. Examples: `runscript`, `put-and-run`, `reg load`, `reg unload`, `restart`, `shutdown`.",
            examples=["runscript", "put-and-run", "restart"],
        ),
        command_string: str | None = Field(
            default=None,
            description="Full command line to execute. Example: `runscript -CloudFile=hunt.ps1`.",
        ),
        optional_hosts: list[str] | None = Field(
            default=None,
            description="Subset of host AIDs from the batch to run the command on. Leave unset to target all hosts in the batch.",
        ),
        timeout: int | None = Field(
            default=None,
            ge=1,
            le=600,
            description="Seconds to wait for command completion. Max: 600.",
        ),
        timeout_duration: str | None = Field(
            default=None,
            description="Alternate duration syntax for overall timeout, e.g. `30s`, `2m`.",
        ),
        host_timeout_duration: str | None = Field(
            default=None,
            description="Alternate duration syntax for per-host timeout, e.g. `30s`, `1m`.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Execute an admin RTR command across all hosts in a batch session.

        IMPORTANT: Admin commands include runscript, put-and-run, restart, shutdown.
        These carry the highest risk of host disruption. Confirm intent before executing.
        Requires RTR admin role.
        """
        return self._base_query_api_call(
            operation="BatchAdminCmd",
            query_params={
                "timeout": timeout,
                "timeout_duration": timeout_duration,
                "host_timeout_duration": host_timeout_duration,
            },
            body_params={
                "batch_id": batch_id,
                "base_command": base_command,
                "command_string": command_string,
                "optional_hosts": optional_hosts,
            },
            error_message="Failed to execute batch admin RTR command",
        )

    def batch_get_command(
        self,
        batch_id: str = Field(
            description="Batch ID returned from `falcon_batch_init_rtr_session`.",
        ),
        file_path: str = Field(
            description="Full path of the file to retrieve from all hosts in the batch. Example: `C:\\\\Windows\\\\System32\\\\drivers\\\\etc\\\\hosts`.",
        ),
        optional_hosts: list[str] | None = Field(
            default=None,
            description="Subset of host AIDs from the batch to retrieve the file from. Leave unset to target all hosts in the batch.",
        ),
        timeout: int | None = Field(
            default=None,
            ge=1,
            le=600,
            description="Seconds to wait for the get operation. Max: 600.",
        ),
        timeout_duration: str | None = Field(
            default=None,
            description="Alternate duration syntax for overall timeout, e.g. `30s`, `2m`.",
        ),
        host_timeout_duration: str | None = Field(
            default=None,
            description="Alternate duration syntax for per-host timeout, e.g. `30s`, `1m`.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Retrieve a file from all hosts in a batch RTR session.

        Initiates a batch file retrieval. Returns a batch_get_cmd_req_id that can be used
        to track the operation. Use `falcon_list_rtr_session_files` to access the retrieved files.
        """
        return self._base_query_api_call(
            operation="BatchGetCmd",
            query_params={
                "timeout": timeout,
                "timeout_duration": timeout_duration,
                "host_timeout_duration": host_timeout_duration,
            },
            body_params={
                "batch_id": batch_id,
                "file_path": file_path,
                "optional_hosts": optional_hosts,
            },
            error_message="Failed to initiate batch RTR get command",
        )

    # ── RTR Scripts ────────────────────────────────────────────────────────────

    def search_rtr_scripts(
        self,
        filter: str | None = Field(
            default=None,
            description="FQL filter to narrow results. Example: `platform:'windows'`.",
        ),
        limit: int = Field(default=20, ge=1, le=5000, description="Maximum results to return."),
        offset: int | None = Field(default=None, description="Pagination offset."),
        sort: str | None = Field(default=None, description="Sort expression. Example: `created_at|desc`."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search custom RTR scripts available for the `runscript` command.

        Returns script IDs and then fetches full details. Use to discover available hunt scripts
        or verify a script is available before running it via a batch RTR session.
        """
        ids = self._base_search_api_call(
            operation="RTR_ListScripts",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to list RTR scripts",
        )
        if self._is_error(ids):
            return [ids]
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="RTR_GetScriptsV2", ids=ids, id_key="ids", use_params=True,
        )

    def get_rtr_script_details(
        self,
        ids: list[str] = Field(description="Script IDs to retrieve details for."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Retrieve full details for RTR scripts by ID, including script content."""
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="RTR_GetScriptsV2", ids=ids, id_key="ids", use_params=True,
        )

    def upload_rtr_script(
        self,
        name: str = Field(description="Script file name (e.g. `hunt.ps1`)."),
        content: str = Field(description="Script content as plain text."),
        platform: str = Field(
            default="windows",
            description="Target platform: `windows`, `mac`, or `linux`.",
            examples=["windows", "mac", "linux"],
        ),
        description: str | None = Field(default=None, description="Human-readable description of what the script does."),
        permission_type: str = Field(
            default="group",
            description="Access: `private` (uploader only), `group` (all RTR admins), `public` (all active-responders + admins).",
            examples=["private", "group", "public"],
        ),
        comments_for_audit_log: str | None = Field(
            default=None, description="Optional audit log comment.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Upload a new custom RTR script for use with the `runscript` command.

        Script content is provided as a string (PowerShell, Bash, etc.). The script becomes
        available for use via `falcon_batch_execute_rtr_admin_command` with `runscript -CloudFile=<name>`.
        """
        data: dict[str, Any] = {
            "name": name,
            "content": content,
            "platform": platform,
            "permission_type": permission_type,
        }
        if description:
            data["description"] = description
        if comments_for_audit_log:
            data["comments_for_audit_log"] = comments_for_audit_log

        response = self.client.command_for("RTR_CreateScriptsV2", data=data)
        return handle_api_response(
            response,
            operation="RTR_CreateScriptsV2",
            error_message="Failed to upload RTR script",
            default_result=[],
        )

    def update_rtr_script(
        self,
        script_id: str = Field(description="Script ID to update. Obtain from `falcon_search_rtr_scripts`."),
        content: str | None = Field(default=None, description="New script content. Omit to keep existing."),
        name: str | None = Field(default=None, description="New script name. Omit to keep existing."),
        description: str | None = Field(default=None, description="New description. Omit to keep existing."),
        platform: str | None = Field(default=None, description="New platform target. Omit to keep existing."),
        permission_type: str | None = Field(default=None, description="New permission level. Omit to keep existing."),
        comments_for_audit_log: str | None = Field(default=None, description="Audit log comment."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Update an existing RTR script's content, name, or permissions."""
        data: dict[str, Any] = {"id": script_id}
        if content is not None:
            data["content"] = content
        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        if platform is not None:
            data["platform"] = platform
        if permission_type is not None:
            data["permission_type"] = permission_type
        if comments_for_audit_log is not None:
            data["comments_for_audit_log"] = comments_for_audit_log

        response = self.client.command_for("RTR_UpdateScriptsV2", data=data)
        return handle_api_response(
            response,
            operation="RTR_UpdateScriptsV2",
            error_message="Failed to update RTR script",
            default_result=[],
        )

    def delete_rtr_scripts(
        self,
        ids: list[str] = Field(description="Script IDs to permanently delete."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Permanently delete one or more RTR scripts."""
        response = self.client.command_for("RTR_DeleteScripts", parameters={"ids": ids})
        return handle_api_response(
            response,
            operation="RTR_DeleteScripts",
            error_message="Failed to delete RTR scripts",
            default_result=[],
        )

    # ── Falcon Built-in Scripts ────────────────────────────────────────────────

    def search_falcon_scripts(
        self,
        filter: str | None = Field(default=None, description="FQL filter."),
        limit: int = Field(default=20, ge=1, le=5000, description="Maximum results to return."),
        offset: int | None = Field(default=None, description="Pagination offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List CrowdStrike built-in Falcon RTR scripts.

        These are pre-built scripts provided by CrowdStrike (not custom uploads). Returns
        script IDs and then fetches full details including script description and parameters.
        """
        ids = self._base_search_api_call(
            operation="RTR_ListFalconScripts",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to list Falcon scripts",
        )
        if self._is_error(ids):
            return [ids]
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="RTR_GetFalconScripts", ids=ids, id_key="ids", use_params=True,
        )

    def get_falcon_script_details(
        self,
        ids: list[str] = Field(description="Falcon script IDs to retrieve."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Retrieve full details for built-in Falcon RTR scripts."""
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="RTR_GetFalconScripts", ids=ids, id_key="ids", use_params=True,
        )

    # ── RTR Put-Files ──────────────────────────────────────────────────────────

    def search_rtr_put_files(
        self,
        filter: str | None = Field(default=None, description="FQL filter."),
        limit: int = Field(default=20, ge=1, le=5000, description="Maximum results to return."),
        offset: int | None = Field(default=None, description="Pagination offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List RTR put-files available for the `put` command.

        Put-files are binary files (executables, tools) that can be staged on hosts
        via the RTR `put` command. Use `falcon_batch_execute_rtr_active_responder_command`
        with `base_command='put'` to deploy them.
        """
        ids = self._base_search_api_call(
            operation="RTR_ListPut_Files",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to list RTR put-files",
        )
        if self._is_error(ids):
            return [ids]
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="RTR_GetPut_FilesV2", ids=ids, id_key="ids", use_params=True,
        )

    def get_rtr_put_file_details(
        self,
        ids: list[str] = Field(description="Put-file IDs to retrieve details for."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Retrieve details for RTR put-files by ID."""
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="RTR_GetPut_FilesV2", ids=ids, id_key="ids", use_params=True,
        )

    def delete_rtr_put_files(
        self,
        ids: list[str] = Field(description="Put-file IDs to permanently delete. Only one file can be deleted per API call; this tool will delete them sequentially."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Permanently delete one or more RTR put-files."""
        results = []
        for file_id in ids:
            response = self.client.command_for("RTR_DeletePut_Files", parameters={"ids": file_id})
            result = handle_api_response(
                response,
                operation="RTR_DeletePut_Files",
                error_message=f"Failed to delete put-file {file_id}",
                default_result=[],
            )
            results.append({"id": file_id, "result": result})
        return results
