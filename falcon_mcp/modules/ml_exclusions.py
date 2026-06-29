"""
ML Exclusions module for Falcon MCP Server.

Provides tools for managing Machine Learning (ML) exclusions — file path patterns that
are excluded from Falcon's on-sensor and cloud ML detection.
"""

from typing import Any

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.errors import _format_error_response
from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule

logger = get_logger(__name__)

WRITE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True,
)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True,
)


class MLExclusionsModule(BaseModule):
    """Module for CrowdStrike Falcon Machine Learning Exclusions management."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.search_ml_exclusions, name="search_ml_exclusions")
        self._add_tool(server=server, method=self.get_ml_exclusion_details, name="get_ml_exclusion_details")
        self._add_tool(
            server=server, method=self.create_ml_exclusion, name="create_ml_exclusion",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.update_ml_exclusion, name="update_ml_exclusion",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.delete_ml_exclusions, name="delete_ml_exclusions",
            annotations=DESTRUCTIVE_ANNOTATIONS,
        )

    def register_resources(self, server: FastMCP) -> None:
        pass

    def search_ml_exclusions(
        self,
        filter: str | None = Field(
            default=None,
            description=(
                "FQL filter. Supported fields: `value` (path/pattern), `created_by`, "
                "`created_on`, `last_modified`, `modified_by`, `applied_globally`."
            ),
        ),
        limit: int = Field(default=100, ge=1, le=500, description="Max records."),
        offset: int | None = Field(default=None, description="Offset for pagination."),
        sort: str | None = Field(
            default=None,
            description="Sort expression. Examples: `value.asc`, `created_on.desc`, `last_modified.desc`.",
        ),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search ML exclusions and return full exclusion details.

        ML exclusions tell the ML detection engine to skip specific file paths/patterns.
        Use to audit exclusions and confirm none are overly broad (which would create
        detection blind spots).
        """
        ids = self._base_search_api_call(
            operation="queryMLExclusionsV1",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search ML exclusions",
            member_cid=member_cid,
        )
        if self._is_error(ids):
            return [ids]
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="getMLExclusionsV1", ids=ids, use_params=True, member_cid=member_cid,
        )

    def get_ml_exclusion_details(
        self,
        ids: list[str] = Field(description="ML exclusion IDs. Obtain from `falcon_search_ml_exclusions`."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get full details for specific ML exclusions by ID."""
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="getMLExclusionsV1", ids=ids, use_params=True, member_cid=member_cid,
        )

    def create_ml_exclusion(
        self,
        value: str = Field(description="File path/pattern to exclude from ML detection. Supports wildcards."),
        excluded_from: list[str] | None = Field(
            default=None,
            description="ML detection sources to exclude from, e.g. ['blocking','extraction']. Defaults to both.",
        ),
        groups: list[str] | None = Field(
            default=None,
            description="Host group IDs to scope the exclusion to. Use ['all'] to apply globally.",
        ),
        comment: str | None = Field(default=None, description="Audit log comment."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Create an ML exclusion.

        Use sparingly — broad ML exclusions can suppress malware detections. Prefer
        group-scoped exclusions over global (`groups=['all']`) ones.
        """
        body: dict[str, Any] = {"value": value}
        body["groups"] = groups if groups else ["all"]
        if excluded_from:
            body["excluded_from"] = excluded_from
        if comment is not None:
            body["comment"] = comment
        result = self._base_query_api_call(
            operation="createMLExclusionsV1",
            body_params=body,
            error_message="Failed to create ML exclusion",
            member_cid=member_cid,
        )
        if self._is_error(result):
            return [result]
        return result

    def update_ml_exclusion(
        self,
        id: str = Field(description="ML exclusion ID to update. Obtain from `falcon_search_ml_exclusions`."),
        value: str | None = Field(default=None, description="Updated file path/pattern."),
        groups: list[str] | None = Field(
            default=None, description="Updated host group IDs. Replaces the current list.",
        ),
        comment: str | None = Field(default=None, description="Audit log comment."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Update an existing ML exclusion."""
        if value is None and groups is None:
            return [_format_error_response(
                "Provide at least one of `value` or `groups` to update.",
                operation="updateMLExclusionsV1",
            )]
        body: dict[str, Any] = {"id": id}
        if value is not None:
            body["value"] = value
        if groups is not None:
            body["groups"] = groups
        if comment is not None:
            body["comment"] = comment
        result = self._base_query_api_call(
            operation="updateMLExclusionsV1",
            body_params=body,
            error_message="Failed to update ML exclusion",
            member_cid=member_cid,
        )
        if self._is_error(result):
            return [result]
        return result

    def delete_ml_exclusions(
        self,
        ids: list[str] = Field(description="ML exclusion IDs to delete."),
        comment: str | None = Field(default=None, description="Audit log comment explaining the deletion."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Delete ML exclusions by ID."""
        if not ids:
            return [_format_error_response("`ids` is required.", operation="deleteMLExclusionsV1")]
        from falcon_mcp.common.utils import prepare_api_parameters
        params = prepare_api_parameters({"ids": ids, "comment": comment})
        result = self._base_query_api_call(
            operation="deleteMLExclusionsV1",
            query_params=params,
            error_message="Failed to delete ML exclusions",
            member_cid=member_cid,
        )
        if self._is_error(result):
            return [result]
        return result
