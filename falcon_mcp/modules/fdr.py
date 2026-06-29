"""
FDR (Falcon Data Replicator) Schema module for Falcon MCP Server.

Provides tools for querying FDR event and field schema definitions.
"""

from typing import Any

from mcp.server import FastMCP
from pydantic import Field

from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule

logger = get_logger(__name__)


class FDRModule(BaseModule):
    """Module for CrowdStrike Falcon Data Replicator (FDR) schema reference."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_fdr_schema, name="get_fdr_schema")
        self._add_tool(server=server, method=self.list_fdr_events, name="list_fdr_events")
        self._add_tool(server=server, method=self.get_fdr_event_details, name="get_fdr_event_details")
        self._add_tool(server=server, method=self.list_fdr_fields, name="list_fdr_fields")
        self._add_tool(server=server, method=self.get_fdr_field_details, name="get_fdr_field_details")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def get_fdr_schema(
        self,
        filter: str | None = Field(default=None, description="FQL filter to narrow event types."),
        limit: int = Field(default=50, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get combined FDR event schema — event types with all their fields in one call.

        Use this to understand the structure of FDR events before writing data pipeline
        transforms or NGSIEM parsers.
        """
        result = self._base_search_api_call(
            operation="fdrschema_combined_event_get",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to get FDR schema",
        )
        if self._is_error(result):
            return [result]
        return result

    def list_fdr_events(
        self,
        filter: str | None = Field(default=None, description="FQL filter."),
        limit: int = Field(default=50, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List FDR event type IDs.

        Returns event type IDs matching the filter. Use `falcon_get_fdr_event_details`
        to get full schema details for specific event types.
        """
        result = self._base_search_api_call(
            operation="fdrschema_queries_event_get",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to list FDR events",
        )
        if self._is_error(result):
            return [result]
        return result

    def get_fdr_event_details(
        self,
        ids: list[str] = Field(description="FDR event type IDs. Obtain from `falcon_list_fdr_events`."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get full schema details for specific FDR event types by ID."""
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="fdrschema_entities_event_get", ids=ids, use_params=True,
        )

    def list_fdr_fields(
        self,
        filter: str | None = Field(default=None, description="FQL filter."),
        limit: int = Field(default=100, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List FDR field IDs.

        Returns individual field definitions used across FDR event types.
        Use `falcon_get_fdr_field_details` for full field metadata.
        """
        result = self._base_search_api_call(
            operation="fdrschema_queries_field_get",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to list FDR fields",
        )
        if self._is_error(result):
            return [result]
        return result

    def get_fdr_field_details(
        self,
        ids: list[str] = Field(description="FDR field IDs. Obtain from `falcon_list_fdr_fields`."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get full metadata for specific FDR fields by ID."""
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="fdrschema_entities_field_get", ids=ids, use_params=True,
        )
