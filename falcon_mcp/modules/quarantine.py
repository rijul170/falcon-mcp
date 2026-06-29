"""
Quarantine module for Falcon MCP Server.

Provides tools for managing quarantined files: search/list quarantined files, get their
metadata, and take action on them (release, unrelease, delete).
"""

from typing import Any

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.errors import _format_error_response
from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule

logger = get_logger(__name__)

# Releasing/deleting quarantined files changes endpoint state and (delete) cannot be undone.
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True,
)


class QuarantineModule(BaseModule):
    """Module for CrowdStrike Falcon Quarantined Files management."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.search_quarantined_files, name="search_quarantined_files")
        self._add_tool(server=server, method=self.get_quarantine_file_details, name="get_quarantine_file_details")
        self._add_tool(
            server=server, method=self.update_quarantined_files, name="update_quarantined_files",
            annotations=DESTRUCTIVE_ANNOTATIONS,
        )

    def register_resources(self, server: FastMCP) -> None:
        pass

    def search_quarantined_files(
        self,
        filter: str | None = Field(
            default=None,
            description=(
                "FQL filter. Common fields: `aid`, `sha256`, `state` "
                "('quarantined','released','deleted','pending_release','pending_deletion'), "
                "`hostname`, `username`, `paths.path`, `date_created`, `date_updated`. "
                "Example: `state:'quarantined'+sha256:'<hash>'`"
            ),
        ),
        limit: int = Field(default=100, ge=1, le=5000, description="Max records per page."),
        offset: int | None = Field(default=None, description="Offset for pagination."),
        sort: str | None = Field(
            default=None,
            description="Sort expression. Examples: `date_created|desc`, `hostname|asc`.",
        ),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search quarantined files and return full file metadata.

        Queries quarantine file IDs matching the FQL filter, then hydrates them into full
        records (hostname, hash, paths, state, sandbox verdict) in a single call.
        """
        ids = self._base_search_api_call(
            operation="QueryQuarantineFiles",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to query quarantined files",
            member_cid=member_cid,
        )
        if self._is_error(ids):
            return [ids]
        if not ids:
            return []
        return self._base_query_api_call(
            operation="GetQuarantineFiles",
            body_params={"ids": ids},
            error_message="Failed to retrieve quarantined file details",
            member_cid=member_cid,
        )

    def get_quarantine_file_details(
        self,
        ids: list[str] = Field(
            description="Quarantine file IDs to retrieve. Obtain from `falcon_search_quarantined_files`.",
        ),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get full metadata for specific quarantined files by ID."""
        if not ids:
            return []
        return self._base_query_api_call(
            operation="GetQuarantineFiles",
            body_params={"ids": ids},
            error_message="Failed to retrieve quarantined file details",
            member_cid=member_cid,
        )

    def update_quarantined_files(
        self,
        ids: list[str] = Field(
            description="Quarantine file IDs to act on. Obtain from `falcon_search_quarantined_files`.",
        ),
        action: str = Field(
            description=(
                "Action to apply: 'release' (restore the file to the host), "
                "'unrelease' (re-quarantine a released file), or 'delete' (permanently remove). "
                "'delete' is irreversible."
            ),
        ),
        comment: str | None = Field(default=None, description="Audit log comment explaining the action."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Take action on quarantined files: release, unrelease, or delete.

        Releasing restores a file to its original location on the endpoint; delete removes
        it permanently. Confirm intent before releasing or deleting — releasing malware
        re-introduces it to the host.
        """
        if action not in ("release", "unrelease", "delete"):
            return [_format_error_response(
                "`action` must be one of: 'release', 'unrelease', 'delete'.",
                operation="UpdateQuarantinedDetectsByIds",
            )]
        body: dict[str, Any] = {"ids": ids, "action": action}
        if comment is not None:
            body["comment"] = comment
        result = self._base_query_api_call(
            operation="UpdateQuarantinedDetectsByIds",
            body_params=body,
            error_message="Failed to update quarantined files",
            member_cid=member_cid,
        )
        if self._is_error(result):
            return [result]
        return result
