"""
Content Update Policy module for Falcon MCP Server.

Provides tools for managing CrowdStrike Falcon sensor content update policies —
controlling which Falcon content version (Raptor/Channel Files) is pinned on hosts.
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


class ContentUpdatePolicyModule(BaseModule):
    """Module for CrowdStrike Falcon content update policy management."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.search_content_update_policies, name="search_content_update_policies")
        self._add_tool(server=server, method=self.get_content_update_policy_members, name="get_content_update_policy_members")
        self._add_tool(server=server, method=self.list_pinnable_content_versions, name="list_pinnable_content_versions")
        self._add_tool(
            server=server, method=self.create_content_update_policy, name="create_content_update_policy",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.update_content_update_policy, name="update_content_update_policy",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.delete_content_update_policies, name="delete_content_update_policies",
            annotations=DESTRUCTIVE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.set_content_update_policy_state, name="set_content_update_policy_state",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.set_content_update_policy_precedence, name="set_content_update_policy_precedence",
            annotations=WRITE_ANNOTATIONS,
        )

    def register_resources(self, server: FastMCP) -> None:
        pass

    def search_content_update_policies(
        self,
        filter: str | None = Field(default=None, description="FQL filter. Supported fields: id, name, platform_name, enabled."),
        limit: int = Field(default=10, ge=1, le=5000, description="Max records."),
        offset: int | None = Field(default=None, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search content update policies and return full policy details.

        Content update policies control which version of Falcon sensor content
        (channel files / Raptor content) is deployed to hosts in the assigned group.
        Use this to audit or compare content versions across host groups.
        """
        result = self._base_search_api_call(
            operation="queryCombinedContentUpdatePolicies",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search content update policies",
        )
        if self._is_error(result):
            return [result]
        return result

    def get_content_update_policy_members(
        self,
        id: str = Field(description="Content update policy ID."),
        filter: str | None = Field(default=None, description="Optional FQL filter on member hosts."),
        limit: int = Field(default=100, ge=1, le=5000, description="Max members."),
        offset: int | None = Field(default=None, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List host details for hosts assigned to a content update policy."""
        result = self._base_search_api_call(
            operation="queryCombinedContentUpdatePolicyMembers",
            search_params={"id": id, "filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to list content update policy members",
        )
        if self._is_error(result):
            return [result]
        return result

    def list_pinnable_content_versions(
        self,
        filter: str | None = Field(default=None, description="FQL filter. Supported fields: platform, content_type, version."),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int | None = Field(default=None, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List available Falcon content versions that can be pinned in a policy.

        Returns the content versions (Raptor channel file sets) available to pin.
        Use the `version` value when creating or updating a content update policy.
        """
        result = self._base_search_api_call(
            operation="queryPinnableContentVersions",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to list pinnable content versions",
        )
        if self._is_error(result):
            return [result]
        return result

    def create_content_update_policy(
        self,
        name: str = Field(description="Policy name."),
        platform_name: str = Field(description="'Windows', 'Mac', or 'Linux'."),
        description: str | None = Field(default=None, description="Policy description."),
        settings: dict[str, Any] | None = Field(
            default=None,
            description=(
                "Policy settings. Typically includes `content_ring` (e.g. 'n-2') or "
                "`pinned_version` to pin a specific content version from `falcon_list_pinnable_content_versions`."
            ),
        ),
    ) -> list[dict[str, Any]]:
        """Create a content update policy."""
        if platform_name not in ("Windows", "Mac", "Linux"):
            return [_format_error_response(
                "`platform_name` must be 'Windows', 'Mac', or 'Linux'.",
                operation="createContentUpdatePolicies",
            )]
        resource: dict[str, Any] = {"name": name, "platform_name": platform_name}
        if description:
            resource["description"] = description
        if settings is not None:
            resource["settings"] = settings
        result = self._base_query_api_call(
            operation="createContentUpdatePolicies",
            body_params={"resources": [resource]},
            error_message="Failed to create content update policy",
        )
        if self._is_error(result):
            return [result]
        return result

    def update_content_update_policy(
        self,
        id: str = Field(description="Policy ID to update."),
        name: str | None = Field(default=None, description="New name."),
        description: str | None = Field(default=None, description="New description."),
        settings: dict[str, Any] | None = Field(default=None, description="Updated settings object."),
    ) -> list[dict[str, Any]]:
        """Update a content update policy."""
        if name is None and description is None and settings is None:
            return [_format_error_response(
                "Provide at least one of `name`, `description`, or `settings`.",
                operation="updateContentUpdatePolicies",
            )]
        resource: dict[str, Any] = {"id": id}
        if name is not None:
            resource["name"] = name
        if description is not None:
            resource["description"] = description
        if settings is not None:
            resource["settings"] = settings
        result = self._base_query_api_call(
            operation="updateContentUpdatePolicies",
            body_params={"resources": [resource]},
            error_message="Failed to update content update policy",
        )
        if self._is_error(result):
            return [result]
        return result

    def delete_content_update_policies(
        self,
        ids: list[str] = Field(description="Policy IDs to delete."),
    ) -> list[dict[str, Any]]:
        """Delete content update policies by ID."""
        if not ids:
            return [_format_error_response("`ids` is required.", operation="deleteContentUpdatePolicies")]
        result = self._base_query_api_call(
            operation="deleteContentUpdatePolicies",
            query_params={"ids": ids},
            error_message="Failed to delete content update policies",
        )
        if self._is_error(result):
            return [result]
        return result

    def set_content_update_policy_state(
        self,
        id: str = Field(description="Policy ID."),
        enabled: bool = Field(description="True to enable, False to disable."),
    ) -> list[dict[str, Any]]:
        """Enable or disable a content update policy."""
        action = "enable" if enabled else "disable"
        result = self._base_query_api_call(
            operation="performContentUpdatePoliciesAction",
            query_params={"action_name": action},
            body_params={"ids": [id]},
            error_message=f"Failed to {action} content update policy",
        )
        if self._is_error(result):
            return [result]
        return result

    def set_content_update_policy_precedence(
        self,
        ids: list[str] = Field(description="Policy IDs in desired precedence order (highest priority first)."),
        platform_name: str = Field(description="'Windows', 'Mac', or 'Linux'."),
    ) -> list[dict[str, Any]]:
        """Set content update policy precedence for a platform."""
        result = self._base_query_api_call(
            operation="setContentUpdatePoliciesPrecedence",
            body_params={"ids": ids, "platform_name": platform_name},
            error_message="Failed to set content update policy precedence",
        )
        if self._is_error(result):
            return [result]
        return result
