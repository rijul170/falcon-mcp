"""
IOA Exclusions module for Falcon MCP Server.

Provides tools for managing Indicator of Attack (IOA) exclusions — behavioral pattern
exclusions that suppress specific IOA-based detections for matching processes.
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


class IOAExclusionsModule(BaseModule):
    """Module for CrowdStrike Falcon Indicator of Attack (IOA) Exclusions management."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.search_ioa_exclusions, name="search_ioa_exclusions")
        self._add_tool(server=server, method=self.get_ioa_exclusion_details, name="get_ioa_exclusion_details")
        self._add_tool(
            server=server, method=self.create_ioa_exclusion, name="create_ioa_exclusion",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.update_ioa_exclusion, name="update_ioa_exclusion",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.delete_ioa_exclusions, name="delete_ioa_exclusions",
            annotations=DESTRUCTIVE_ANNOTATIONS,
        )

    def register_resources(self, server: FastMCP) -> None:
        pass

    def search_ioa_exclusions(
        self,
        filter: str | None = Field(
            default=None,
            description=(
                "FQL filter. Supported fields: `name`, `pattern_id`, `pattern_name`, "
                "`created_by`, `created_on`, `last_modified`, `modified_by`, `applied_globally`."
            ),
        ),
        limit: int = Field(default=100, ge=1, le=500, description="Max records."),
        offset: int | None = Field(default=None, description="Offset for pagination."),
        sort: str | None = Field(
            default=None,
            description="Sort expression. Examples: `name.asc`, `created_on.desc`, `last_modified.desc`.",
        ),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search IOA exclusions and return full exclusion details.

        IOA exclusions suppress behavioral (Indicator of Attack) detections for a specific
        pattern matched against a command-line and/or image-file-name regex. Audit these to
        ensure attacker behaviors are not being unintentionally suppressed.
        """
        ids = self._base_search_api_call(
            operation="queryIOAExclusionsV1",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search IOA exclusions",
            member_cid=member_cid,
        )
        if self._is_error(ids):
            return [ids]
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="getIOAExclusionsV1", ids=ids, use_params=True, member_cid=member_cid,
        )

    def get_ioa_exclusion_details(
        self,
        ids: list[str] = Field(description="IOA exclusion IDs. Obtain from `falcon_search_ioa_exclusions`."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get full details for specific IOA exclusions by ID."""
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="getIOAExclusionsV1", ids=ids, use_params=True, member_cid=member_cid,
        )

    def create_ioa_exclusion(
        self,
        name: str = Field(description="Name for the IOA exclusion."),
        pattern_id: str = Field(description="IOA pattern ID this exclusion targets."),
        pattern_name: str | None = Field(default=None, description="Human-readable IOA pattern name."),
        cl_regex: str | None = Field(default=None, description="Command-line regex the exclusion matches against."),
        ifn_regex: str | None = Field(default=None, description="Image-file-name regex the exclusion matches against."),
        groups: list[str] | None = Field(
            default=None,
            description="Host group IDs to scope the exclusion to. Use ['all'] to apply globally.",
        ),
        description: str | None = Field(default=None, description="Description of the exclusion."),
        detection_json: str | None = Field(default=None, description="Optional detection JSON payload."),
        comment: str | None = Field(default=None, description="Audit log comment."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Create an IOA exclusion.

        Suppresses an IOA-based behavioral detection for matching processes. Use carefully —
        overly broad regexes can mask genuine attacker behavior. Prefer group-scoped over
        global (`groups=['all']`) exclusions.
        """
        body: dict[str, Any] = {"name": name, "pattern_id": pattern_id}
        body["groups"] = groups if groups else ["all"]
        if pattern_name is not None:
            body["pattern_name"] = pattern_name
        if cl_regex is not None:
            body["cl_regex"] = cl_regex
        if ifn_regex is not None:
            body["ifn_regex"] = ifn_regex
        if description is not None:
            body["description"] = description
        if detection_json is not None:
            body["detection_json"] = detection_json
        if comment is not None:
            body["comment"] = comment
        result = self._base_query_api_call(
            operation="createIOAExclusionsV1",
            body_params=body,
            error_message="Failed to create IOA exclusion",
            member_cid=member_cid,
        )
        if self._is_error(result):
            return [result]
        return result

    def update_ioa_exclusion(
        self,
        id: str = Field(description="IOA exclusion ID to update. Obtain from `falcon_search_ioa_exclusions`."),
        name: str | None = Field(default=None, description="Updated name."),
        cl_regex: str | None = Field(default=None, description="Updated command-line regex."),
        ifn_regex: str | None = Field(default=None, description="Updated image-file-name regex."),
        groups: list[str] | None = Field(
            default=None, description="Updated host group IDs. Replaces the current list.",
        ),
        description: str | None = Field(default=None, description="Updated description."),
        comment: str | None = Field(default=None, description="Audit log comment."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Update an existing IOA exclusion."""
        if name is None and cl_regex is None and ifn_regex is None and groups is None and description is None:
            return [_format_error_response(
                "Provide at least one of `name`, `cl_regex`, `ifn_regex`, `groups`, or `description` to update.",
                operation="updateIOAExclusionsV1",
            )]
        body: dict[str, Any] = {"id": id}
        if name is not None:
            body["name"] = name
        if cl_regex is not None:
            body["cl_regex"] = cl_regex
        if ifn_regex is not None:
            body["ifn_regex"] = ifn_regex
        if groups is not None:
            body["groups"] = groups
        if description is not None:
            body["description"] = description
        if comment is not None:
            body["comment"] = comment
        result = self._base_query_api_call(
            operation="updateIOAExclusionsV1",
            body_params=body,
            error_message="Failed to update IOA exclusion",
            member_cid=member_cid,
        )
        if self._is_error(result):
            return [result]
        return result

    def delete_ioa_exclusions(
        self,
        ids: list[str] = Field(description="IOA exclusion IDs to delete."),
        comment: str | None = Field(default=None, description="Audit log comment explaining the deletion."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Delete IOA exclusions by ID."""
        if not ids:
            return [_format_error_response("`ids` is required.", operation="deleteIOAExclusionsV1")]
        from falcon_mcp.common.utils import prepare_api_parameters
        params = prepare_api_parameters({"ids": ids, "comment": comment})
        result = self._base_query_api_call(
            operation="deleteIOAExclusionsV1",
            query_params=params,
            error_message="Failed to delete IOA exclusions",
            member_cid=member_cid,
        )
        if self._is_error(result):
            return [result]
        return result
