"""
Sensor Visibility Exclusions module for Falcon MCP Server.

Provides tools for managing Sensor Visibility (SV) exclusions — process/path patterns
that are excluded from Falcon sensor visibility monitoring.
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


class SensorVisibilityExclusionsModule(BaseModule):
    """Module for CrowdStrike Falcon Sensor Visibility Exclusions management."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.search_sv_exclusions, name="search_sv_exclusions")
        self._add_tool(server=server, method=self.get_sv_exclusion_details, name="get_sv_exclusion_details")
        self._add_tool(
            server=server, method=self.create_sv_exclusion, name="create_sv_exclusion",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.update_sv_exclusion, name="update_sv_exclusion",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.delete_sv_exclusions, name="delete_sv_exclusions",
            annotations=DESTRUCTIVE_ANNOTATIONS,
        )

    def register_resources(self, server: FastMCP) -> None:
        pass

    def search_sv_exclusions(
        self,
        filter: str | None = Field(
            default=None,
            description=(
                "FQL filter. Supported fields: `value` (path/process pattern), "
                "`created_by`, `created_on`, `last_modified`, `modified_by`, `applied_globally`."
            ),
        ),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int | None = Field(default=None, description="Offset for pagination."),
        sort: str | None = Field(
            default=None,
            description=(
                "Sort expression. Supported: `value.asc`, `value.desc`, "
                "`created_on.asc`, `created_on.desc`, `last_modified.asc`, `last_modified.desc`."
            ),
        ),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search Sensor Visibility exclusions and return full exclusion details.

        SV exclusions define process paths or patterns that the Falcon sensor skips
        during visibility monitoring. Use to audit which processes are excluded and
        verify exclusions are not overly broad.
        """
        ids = self._base_search_api_call(
            operation="querySensorVisibilityExclusionsV1",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search sensor visibility exclusions",
            member_cid=member_cid,
        )
        if self._is_error(ids):
            return [ids]
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="getSensorVisibilityExclusionsV1", ids=ids, use_params=True, member_cid=member_cid,
        )

    def get_sv_exclusion_details(
        self,
        ids: list[str] = Field(description="SV exclusion IDs to retrieve. Obtain from `falcon_search_sv_exclusions`."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get full details for specific Sensor Visibility exclusions by ID."""
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="getSensorVisibilityExclusionsV1", ids=ids, use_params=True, member_cid=member_cid,
        )

    def create_sv_exclusion(
        self,
        value: str = Field(
            description="Process/path pattern to exclude. Supports wildcards, e.g. `C:\\\\Program Files\\\\MyApp\\\\*`.",
        ),
        groups: list[str] | None = Field(
            default=None,
            description=(
                "Host group IDs to scope this exclusion to. "
                "Leave unset (or set `applied_globally=true`) to apply to all hosts."
            ),
        ),
        applied_globally: bool = Field(
            default=False,
            description="If true, applies to all hosts regardless of group assignment.",
        ),
        description: str | None = Field(default=None, description="Optional description."),
        comment: str | None = Field(default=None, description="Audit log comment."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Create a Sensor Visibility exclusion.

        Excludes a process path pattern from sensor visibility monitoring. Use sparingly —
        overly broad exclusions (e.g., `*`) can create blind spots in threat detection.
        Prefer group-scoped exclusions over globally applied ones.
        """
        body: dict[str, Any] = {
            "value": value,
            "applied_globally": applied_globally,
        }
        if groups:
            body["groups"] = [{"id": gid} for gid in groups]
        if description:
            body["description"] = description
        if comment:
            body["comment"] = comment
        result = self._base_query_api_call(
            operation="createSVExclusionsV1",
            body_params=body,
            error_message="Failed to create sensor visibility exclusion",
            member_cid=member_cid,
        )
        if self._is_error(result):
            return [result]
        return result

    def update_sv_exclusion(
        self,
        id: str = Field(description="SV exclusion ID to update. Obtain from `falcon_search_sv_exclusions`."),
        value: str | None = Field(default=None, description="Updated path/process pattern."),
        groups: list[str] | None = Field(
            default=None,
            description="Updated host group IDs. Replaces the current group list.",
        ),
        applied_globally: bool | None = Field(default=None, description="Update global application flag."),
        description: str | None = Field(default=None, description="Updated description."),
        comment: str | None = Field(default=None, description="Audit log comment."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Update an existing Sensor Visibility exclusion."""
        if value is None and groups is None and applied_globally is None and description is None:
            return [_format_error_response(
                "Provide at least one of `value`, `groups`, `applied_globally`, or `description` to update.",
                operation="updateSensorVisibilityExclusionsV1",
            )]
        body: dict[str, Any] = {"id": id}
        if value is not None:
            body["value"] = value
        if groups is not None:
            body["groups"] = [{"id": gid} for gid in groups]
        if applied_globally is not None:
            body["applied_globally"] = applied_globally
        if description is not None:
            body["description"] = description
        if comment is not None:
            body["comment"] = comment
        result = self._base_query_api_call(
            operation="updateSensorVisibilityExclusionsV1",
            body_params=body,
            error_message="Failed to update sensor visibility exclusion",
            member_cid=member_cid,
        )
        if self._is_error(result):
            return [result]
        return result

    def delete_sv_exclusions(
        self,
        ids: list[str] = Field(description="SV exclusion IDs to delete."),
        comment: str | None = Field(default=None, description="Audit log comment explaining the deletion."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Delete Sensor Visibility exclusions by ID."""
        if not ids:
            return [_format_error_response("`ids` is required.", operation="deleteSensorVisibilityExclusionsV1")]
        from falcon_mcp.common.utils import prepare_api_parameters
        params = prepare_api_parameters({"ids": ids, "comment": comment})
        result = self._base_query_api_call(
            operation="deleteSensorVisibilityExclusionsV1",
            query_params=params,
            error_message="Failed to delete sensor visibility exclusions",
            member_cid=member_cid,
        )
        if self._is_error(result):
            return [result]
        return result
