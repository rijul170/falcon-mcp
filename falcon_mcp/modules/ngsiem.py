"""
NGSIEM module for Falcon MCP Server

This module provides tools for running search queries against CrowdStrike's
Next-Gen SIEM via the asynchronous job-based search API.
"""

import asyncio
import os
from datetime import datetime
from typing import Any

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.errors import _format_error_response, handle_api_response
from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule

WRITE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True,
)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True,
)

logger = get_logger(__name__)

# Configurable polling settings
POLL_INTERVAL_SECONDS = int(os.environ.get("FALCON_MCP_NGSIEM_POLL_INTERVAL", "5"))
TIMEOUT_SECONDS = int(os.environ.get("FALCON_MCP_NGSIEM_TIMEOUT", "300"))


def _iso_to_epoch_ms(iso_timestamp: str) -> int:
    """Convert ISO 8601 timestamp to Unix epoch milliseconds.

    Args:
        iso_timestamp: ISO 8601 formatted timestamp (e.g., "2025-01-01T00:00:00Z")

    Returns:
        Unix epoch time in milliseconds
    """
    dt = datetime.fromisoformat(iso_timestamp.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)


class NGSIEMModule(BaseModule):
    """Module for running search queries against CrowdStrike Next-Gen SIEM."""

    def register_tools(self, server: FastMCP) -> None:
        """Register tools with the MCP server.

        Args:
            server: MCP server instance
        """
        self._add_tool(
            server=server,
            method=self.search_ngsiem,
            name="search_ngsiem",
        )
        # Read-only NGSIEM content + data connections
        self._add_tool(server=server, method=self.list_ngsiem_lookup_files, name="list_ngsiem_lookup_files")
        self._add_tool(server=server, method=self.list_ngsiem_parsers, name="list_ngsiem_parsers")
        self._add_tool(server=server, method=self.list_ngsiem_saved_queries, name="list_ngsiem_saved_queries")
        self._add_tool(server=server, method=self.list_ngsiem_dashboards, name="list_ngsiem_dashboards")
        self._add_tool(server=server, method=self.list_ngsiem_data_connections, name="list_ngsiem_data_connections")
        self._add_tool(server=server, method=self.list_ngsiem_data_connectors, name="list_ngsiem_data_connectors")
        self._add_tool(server=server, method=self.get_ngsiem_data_connection_status, name="get_ngsiem_data_connection_status")
        self._add_tool(
            server=server, method=self.create_ngsiem_connection, name="create_ngsiem_connection",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.delete_ngsiem_connection, name="delete_ngsiem_connection",
            annotations=DESTRUCTIVE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.set_ngsiem_connection_state, name="set_ngsiem_connection_state",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(server=server, method=self.get_ngsiem_ingest_token, name="get_ngsiem_ingest_token")
        self._add_tool(
            server=server, method=self.regenerate_ngsiem_ingest_token, name="regenerate_ngsiem_ingest_token",
            annotations=WRITE_ANNOTATIONS,
        )

    async def search_ngsiem(
        self,
        query_string: str = Field(
            description=(
                "The CQL query string to execute. "
                "This tool executes pre-written CQL queries - it does NOT help construct queries. "
                "Users must provide a complete, valid CQL query. "
                "Example: '#event_simpleName=ProcessRollup2' or 'source=firewall | count()'"
            ),
        ),
        start: str = Field(
            description=(
                "Search start time as an ISO 8601 timestamp (REQUIRED format). "
                "Example: start='2025-01-01T00:00:00Z'"
            ),
            examples=["2025-01-01T00:00:00Z"],
        ),
        repository: str = Field(
            default="search-all",
            description=(
                "Repository to search. Valid options: "
                "search-all (default - all event data), "
                "investigate_view (endpoint events), "
                "third-party (third-party source events), "
                "falcon_for_it_view (Falcon for IT data), "
                "forensics_view (Falcon Forensics triage data)"
            ),
        ),
        end: str | None = Field(
            default=None,
            description=(
                "Search end time as an ISO 8601 timestamp. "
                "If not provided, defaults to the current time. "
                "Example: end='2025-02-06T00:00:00Z'"
            ),
            examples=["2025-01-01T00:00:00Z"],
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Execute a CQL query against CrowdStrike Next-Gen SIEM.

        This tool executes pre-written CQL queries provided by the user. It does NOT
        assist with query construction - users must supply complete, valid CQL syntax.

        The tool starts an asynchronous search job, polls for completion (up to the
        configured timeout), and returns matching events.

        Note: Search times out after FALCON_MCP_NGSIEM_TIMEOUT seconds (default: 300).
        Polling interval is controlled by FALCON_MCP_NGSIEM_POLL_INTERVAL (default: 5).

        Args:
            query_string (required): The CQL query to execute. Example: '#event_simpleName=ProcessRollup2'
            start (required): ISO 8601 timestamp for search start. Example: '2025-01-01T00:00:00Z'
            repository (optional): Repository to search. Default: 'search-all'.
                Options: search-all, investigate_view, third-party, falcon_for_it_view, forensics_view
            end (optional): ISO 8601 timestamp for search end. Defaults to current time.
        """
        # Step 1: Start the search job
        # Note: FalconPy uber class passes body unchanged; API expects camelCase keys
        body_params: dict[str, Any] = {
            "queryString": query_string,
            "start": _iso_to_epoch_ms(start),
        }
        if isinstance(end, str):
            body_params["end"] = _iso_to_epoch_ms(end)

        logger.debug("Starting NGSIEM search with query: %s", query_string)

        start_response = self.client.command(
            operation="StartSearchV1",
            repository=repository,
            body=body_params,
        )

        start_status = start_response.get("status_code")
        if start_status != 200:
            return handle_api_response(
                start_response,
                operation="StartSearchV1",
                error_message="Failed to start NGSIEM search",
                default_result=[],
            )

        job_id = start_response.get("body", {}).get("id")
        if not job_id:
            return _format_error_response(
                message="Failed to start NGSIEM search: no job ID returned",
                details=start_response.get("body", {}),
                operation="StartSearchV1",
            )

        logger.debug("NGSIEM search job started: %s", job_id)

        # Step 2: Poll for completion
        elapsed = 0.0
        while elapsed < TIMEOUT_SECONDS:
            await asyncio.sleep(POLL_INTERVAL_SECONDS)
            elapsed += POLL_INTERVAL_SECONDS

            poll_response = self.client.command(
                operation="GetSearchStatusV1",
                repository=repository,
                search_id=job_id,
            )

            poll_status = poll_response.get("status_code")
            if poll_status != 200:
                return handle_api_response(
                    poll_response,
                    operation="GetSearchStatusV1",
                    error_message="Failed to poll NGSIEM search status",
                    default_result=[],
                )

            body = poll_response.get("body", {})
            if body.get("done"):
                logger.debug("NGSIEM search job completed: %s", job_id)
                return body.get("events", [])

        # Step 3: Timeout — attempt cleanup
        logger.warning("NGSIEM search job timed out: %s", job_id)
        self.client.command(
            operation="StopSearchV1",
            repository=repository,
            id=job_id,
        )

        return _format_error_response(
            message=f"NGSIEM search timed out after {TIMEOUT_SECONDS} seconds. "
            "Try narrowing your query or reducing the time range.",
            details={"job_id": job_id, "timeout_seconds": TIMEOUT_SECONDS},
            operation="GetSearchStatusV1",
        )

    # --- NGSIEM content (read-only) ----------------------------------------

    def list_ngsiem_lookup_files(
        self,
        repository: str | None = Field(default=None, description="Optional repository name filter."),
        limit: int = Field(default=100, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List NGSIEM lookup files (used by saved searches and dashboards)."""
        params: dict[str, Any] = {"limit": limit, "offset": offset}
        if repository:
            params["repository"] = repository
        result = self._base_search_api_call(
            operation="ListLookupFiles",
            search_params=params,
            error_message="Failed to list NGSIEM lookup files",
        )
        if self._is_error(result):
            return [result]
        return result

    def list_ngsiem_parsers(
        self,
        repository: str | None = Field(default=None, description="Optional repository name filter."),
        limit: int = Field(default=100, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List NGSIEM parsers."""
        params: dict[str, Any] = {"limit": limit, "offset": offset}
        if repository:
            params["repository"] = repository
        result = self._base_search_api_call(
            operation="ListParsers",
            search_params=params,
            error_message="Failed to list NGSIEM parsers",
        )
        if self._is_error(result):
            return [result]
        return result

    def list_ngsiem_saved_queries(
        self,
        repository: str | None = Field(default=None, description="Optional repository name filter."),
        limit: int = Field(default=100, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List NGSIEM saved queries."""
        params: dict[str, Any] = {"limit": limit, "offset": offset}
        if repository:
            params["repository"] = repository
        result = self._base_search_api_call(
            operation="ListSavedQueries",
            search_params=params,
            error_message="Failed to list NGSIEM saved queries",
        )
        if self._is_error(result):
            return [result]
        return result

    def list_ngsiem_dashboards(
        self,
        repository: str | None = Field(default=None, description="Optional repository name filter."),
        limit: int = Field(default=100, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List NGSIEM dashboards."""
        params: dict[str, Any] = {"limit": limit, "offset": offset}
        if repository:
            params["repository"] = repository
        result = self._base_search_api_call(
            operation="ListDashboards",
            search_params=params,
            error_message="Failed to list NGSIEM dashboards",
        )
        if self._is_error(result):
            return [result]
        return result

    def list_ngsiem_data_connections(
        self,
        filter: str | None = Field(default=None, description="Optional FQL filter."),
        limit: int = Field(default=100, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List NGSIEM data connections (sources feeding data into NGSIEM)."""
        result = self._base_search_api_call(
            operation="ExternalListDataConnections",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to list NGSIEM data connections",
        )
        if self._is_error(result):
            return [result]
        return result

    def list_ngsiem_data_connectors(
        self,
        filter: str | None = Field(default=None, description="Optional FQL filter."),
        limit: int = Field(default=100, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List NGSIEM data connector types."""
        result = self._base_search_api_call(
            operation="ExternalListDataConnectors",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to list NGSIEM data connectors",
        )
        if self._is_error(result):
            return [result]
        return result

    def get_ngsiem_data_connection_status(
        self,
        ids: list[str] = Field(description="Data connection IDs."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get the live status of one or more NGSIEM data connections."""
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="ExternalGetDataConnectionStatus", ids=ids, use_params=True,
        )

    # --- NGSIEM data connection write operations ----------------------------

    def create_ngsiem_connection(
        self,
        connection_body: dict[str, Any] = Field(
            description=(
                "Data connection configuration object. Required fields vary by connector type. "
                "Typical fields: `name` (str), `connector_type` (str from `falcon_list_ngsiem_data_connectors`), "
                "`settings` (dict — connector-specific config). "
                "Example: {\"name\": \"My Syslog\", \"connector_type\": \"syslog\", \"settings\": {}}"
            ),
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Create a new NGSIEM data connection.

        A data connection is a configured ingest source that streams events into NGSIEM.
        Retrieve supported connector types with `falcon_list_ngsiem_data_connectors` first.
        After creation, retrieve the ingest token with `falcon_get_ngsiem_ingest_token`.
        """
        result = self._base_query_api_call(
            operation="ExternalCreateDataConnection",
            body_params=connection_body,
            error_message="Failed to create NGSIEM data connection",
        )
        if self._is_error(result):
            return [result]
        return result

    def delete_ngsiem_connection(
        self,
        ids: list[str] = Field(description="Data connection IDs to delete. Obtain from `falcon_list_ngsiem_data_connections`."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Delete NGSIEM data connections.

        WARNING: Deleting a connection stops all ingestion from that source immediately
        and cannot be undone. The ingest token becomes invalid.
        """
        if not ids:
            return [_format_error_response("`ids` is required.", operation="ExternalDeleteDataConnection")]
        result = self._base_query_api_call(
            operation="ExternalDeleteDataConnection",
            query_params={"ids": ids},
            error_message="Failed to delete NGSIEM data connection",
        )
        if self._is_error(result):
            return [result]
        return result

    def set_ngsiem_connection_state(
        self,
        ids: list[str] = Field(description="Data connection IDs. Obtain from `falcon_list_ngsiem_data_connections`."),
        action: str = Field(
            description="State to apply: `pause` to suspend ingestion, `resume` to re-activate ingestion.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Pause or resume NGSIEM data connections.

        Pausing a connection suspends ingestion without deleting the connection or token.
        Use this for maintenance windows or when temporarily disabling a source.
        """
        if action not in ("pause", "resume"):
            return [_format_error_response(
                "`action` must be 'pause' or 'resume'.", operation="ExternalUpdateDataConnectionStatus",
            )]
        result = self._base_query_api_call(
            operation="ExternalUpdateDataConnectionStatus",
            body_params={"ids": ids, "action": action},
            error_message=f"Failed to {action} NGSIEM data connection",
        )
        if self._is_error(result):
            return [result]
        return result

    def get_ngsiem_ingest_token(
        self,
        id: str = Field(description="Data connection ID. Obtain from `falcon_list_ngsiem_data_connections`."),
    ) -> dict[str, Any]:
        """Retrieve the ingest token for a NGSIEM data connection.

        The token is used to authenticate log shippers (e.g., Fluentd, Logstash) when
        sending events to this connection's NGSIEM endpoint.
        """
        response = self.client.command_for("ExternalGetDataConnectionToken", parameters={"id": id})
        return handle_api_response(
            response, operation="ExternalGetDataConnectionToken",
            error_message="Failed to retrieve NGSIEM ingest token", default_result={},
        )

    def regenerate_ngsiem_ingest_token(
        self,
        id: str = Field(description="Data connection ID. Obtain from `falcon_list_ngsiem_data_connections`."),
    ) -> dict[str, Any]:
        """Regenerate the ingest token for a NGSIEM data connection.

        Invalidates the current token and issues a new one. Update all log shippers
        with the new token immediately after regeneration to avoid ingestion gaps.
        """
        result = self._base_query_api_call(
            operation="ExternalRegenerateDataConnectionToken",
            query_params={"id": id},
            error_message="Failed to regenerate NGSIEM ingest token",
        )
        if self._is_error(result):
            return result
        return result[0] if isinstance(result, list) and result else result
