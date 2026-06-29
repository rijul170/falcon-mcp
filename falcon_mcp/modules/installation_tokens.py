"""
Installation Tokens module for Falcon MCP Server.

Provides tools for managing CrowdStrike sensor installation tokens.
"""

from typing import Any

from mcp.server import FastMCP
from mcp.server.fastmcp.resources import TextResource
from mcp.types import ToolAnnotations
from pydantic import AnyUrl, Field

from falcon_mcp.common.errors import _format_error_response
from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule
from falcon_mcp.resources.installation_tokens import SEARCH_INSTALLATION_TOKENS_FQL_DOCUMENTATION

logger = get_logger(__name__)

WRITE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True,
)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True,
)


class InstallationTokensModule(BaseModule):
    """Module for CrowdStrike Falcon installation token management."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.search_installation_tokens, name="search_installation_tokens")
        self._add_tool(server=server, method=self.get_installation_token_details, name="get_installation_token_details")
        self._add_tool(server=server, method=self.get_installation_token_settings, name="get_installation_token_settings")
        self._add_tool(
            server=server, method=self.create_installation_token, name="create_installation_token",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.update_installation_token, name="update_installation_token",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.delete_installation_tokens, name="delete_installation_tokens",
            annotations=DESTRUCTIVE_ANNOTATIONS,
        )
        self._add_tool(server=server, method=self.search_token_audit_events, name="search_token_audit_events")
        self._add_tool(server=server, method=self.get_token_audit_event_details, name="get_token_audit_event_details")

    def register_resources(self, server: FastMCP) -> None:
        self._add_resource(server, TextResource(
            uri=AnyUrl("falcon://installation-tokens/search/fql-guide"),
            name="falcon_search_installation_tokens_fql_guide",
            description="FQL filter guide for `falcon_search_installation_tokens`.",
            text=SEARCH_INSTALLATION_TOKENS_FQL_DOCUMENTATION,
        ))

    def search_installation_tokens(
        self,
        filter: str | None = Field(default=None, description="FQL filter; see `falcon://installation-tokens/search/fql-guide`."),
        limit: int = Field(default=100, ge=1, le=1000, description="Max records."),
        offset: int | None = Field(default=None, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression (e.g. expires_timestamp.asc)."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search installation tokens and return their details."""
        ids = self._base_search_api_call(
            operation="tokens_query",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search installation tokens",
        )
        if self._is_error(ids):
            if filter:
                return self._format_fql_error_response([ids], filter, SEARCH_INSTALLATION_TOKENS_FQL_DOCUMENTATION)
            return [ids]
        if not ids:
            if filter:
                return self._format_fql_error_response([], filter, SEARCH_INSTALLATION_TOKENS_FQL_DOCUMENTATION)
            return []
        details = self._base_get_by_ids(operation="tokens_read", ids=ids, use_params=True)
        if self._is_error(details):
            return [details]
        return details

    def get_installation_token_details(
        self,
        ids: list[str] = Field(description="Installation token IDs."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Retrieve full details for the given installation token IDs."""
        if not ids:
            return []
        return self._base_get_by_ids(operation="tokens_read", ids=ids, use_params=True)

    def get_installation_token_settings(self) -> list[dict[str, Any]] | dict[str, Any]:
        """Read CID-wide installation token settings (default expiration, max_active_tokens, etc.)."""
        result = self._base_search_api_call(
            operation="customer_settings_read",
            search_params={},
            error_message="Failed to read installation token settings",
        )
        if self._is_error(result):
            return [result]
        return result

    def create_installation_token(
        self,
        label: str = Field(description="Human-readable label for the new token."),
        expires_timestamp: str | None = Field(
            default=None,
            description="ISO 8601 expiration timestamp (UTC). Omit to use the CID default.",
            examples=["2026-12-31T23:59:59Z"],
        ),
    ) -> list[dict[str, Any]]:
        """Create a new installation token."""
        body: dict[str, Any] = {"label": label}
        if expires_timestamp is not None:
            body["expires_timestamp"] = expires_timestamp
        result = self._base_query_api_call(
            operation="tokens_create",
            body_params=body,
            error_message="Failed to create installation token",
        )
        if self._is_error(result):
            return [result]
        return result

    def update_installation_token(
        self,
        ids: list[str] = Field(description="Installation token IDs to update."),
        label: str | None = Field(default=None, description="New label."),
        revoked: bool | None = Field(default=None, description="True to revoke, False to re-enable."),
        expires_timestamp: str | None = Field(default=None, description="New ISO 8601 expiration timestamp."),
    ) -> list[dict[str, Any]]:
        """Update one or more installation tokens (label / revoked state / expiration)."""
        if not ids:
            return [_format_error_response("`ids` is required.", operation="tokens_update")]
        body: dict[str, Any] = {}
        if label is not None:
            body["label"] = label
        if revoked is not None:
            body["revoked"] = revoked
        if expires_timestamp is not None:
            body["expires_timestamp"] = expires_timestamp
        if not body:
            return [_format_error_response(
                "Provide at least one of `label`, `revoked`, or `expires_timestamp`.",
                operation="tokens_update",
            )]
        result = self._base_query_api_call(
            operation="tokens_update",
            query_params={"ids": ids},
            body_params=body,
            error_message="Failed to update installation token",
        )
        if self._is_error(result):
            return [result]
        return result

    def delete_installation_tokens(
        self,
        ids: list[str] = Field(description="Installation token IDs to delete."),
    ) -> list[dict[str, Any]]:
        """Delete installation tokens by ID."""
        if not ids:
            return [_format_error_response("`ids` is required.", operation="tokens_delete")]
        result = self._base_query_api_call(
            operation="tokens_delete",
            query_params={"ids": ids},
            error_message="Failed to delete installation tokens",
        )
        if self._is_error(result):
            return [result]
        return result

    def search_token_audit_events(
        self,
        filter: str | None = Field(
            default=None,
            description="FQL filter for audit events. Supported fields: action, token_id, user_id, created_at, updated_at.",
        ),
        limit: int = Field(default=20, ge=1, le=1000, description="Maximum audit events to return."),
        offset: int | None = Field(default=None, description="Pagination offset."),
        sort: str | None = Field(default=None, description="Sort expression. Example: `created_at|desc`."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search installation token audit events.

        Returns audit event IDs that record token creation, updates, deletions, and use events.
        Use to track token lifecycle and investigate suspicious token activity.
        """
        ids = self._base_search_api_call(
            operation="audit_events_query",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search token audit events",
        )
        if self._is_error(ids):
            return [ids]
        if not ids:
            return []
        details = self._base_get_by_ids(
            operation="audit_events_read",
            ids=ids,
            id_key="ids",
            use_params=True,
        )
        if self._is_error(details):
            return [details]
        return details

    def get_token_audit_event_details(
        self,
        ids: list[str] = Field(description="Audit event IDs to retrieve. Obtain from `falcon_search_token_audit_events`."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Retrieve full details for installation token audit events by ID."""
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="audit_events_read",
            ids=ids,
            id_key="ids",
            use_params=True,
        )
