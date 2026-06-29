"""
Event Streams module for Falcon MCP Server.

Provides discovery and session-refresh tools for the Falcon Event Streams (datafeed)
API. This module deliberately does NOT hold a long-lived streaming connection — it only
lists the available datafeed streams and refreshes an active stream session so that an
external consumer can keep its feed alive.
"""

from typing import Any

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule

logger = get_logger(__name__)

# Refresh mutates the server-side session lease but is not destructive and is idempotent.
REFRESH_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=False, idempotentHint=True, openWorldHint=True,
)


class EventStreamsModule(BaseModule):
    """Module for CrowdStrike Falcon Event Streams discovery and session refresh."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.list_available_streams, name="list_available_streams")
        self._add_tool(
            server=server, method=self.refresh_active_stream_session,
            name="refresh_active_stream_session", annotations=REFRESH_ANNOTATIONS,
        )

    def register_resources(self, server: FastMCP) -> None:
        pass

    def list_available_streams(
        self,
        app_id: str = Field(
            description="Label identifying this connection (1-32 alphanumeric chars), e.g. 'mcp-soc-feed'.",
        ),
        format: str | None = Field(
            default=None,
            description="Event format for the stream: 'json' or 'flatjson'.",
        ),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Discover the available event streams (datafeeds) for this tenant.

        Returns datafeed URLs, session tokens, refresh intervals, and partition info. An
        external consumer uses the returned `dataFeedURL` + token to open the stream; this
        tool does not open or hold the stream itself.
        """
        params: dict[str, Any] = {"appId": app_id}
        if format is not None:
            params["format"] = format
        return self._base_search_api_call(
            operation="listAvailableStreamsOAuth2",
            search_params=params,
            error_message="Failed to list available event streams",
            member_cid=member_cid,
        )

    def refresh_active_stream_session(
        self,
        app_id: str = Field(description="The same connection label used to open the stream."),
        partition: int = Field(default=0, description="Stream partition to refresh (from the discovery response)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Refresh an active event stream session to keep its lease from expiring.

        Re-arms the session before the refresh interval elapses. Idempotent: refreshing an
        already-valid session simply extends it.
        """
        params = {
            "action_name": "refresh_active_stream_session",
            "appId": app_id,
            "partition": partition,
        }
        return self._base_query_api_call(
            operation="refreshActiveStreamSession",
            query_params=params,
            error_message="Failed to refresh active stream session",
            member_cid=member_cid,
        )
