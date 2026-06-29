"""
Recon (Falcon Intelligence Recon) module for Falcon MCP Server.

Provides tools for searching and managing Recon notification rules and the
notifications they generate.
"""

from typing import Any

from mcp.server import FastMCP
from mcp.server.fastmcp.resources import TextResource
from mcp.types import ToolAnnotations
from pydantic import AnyUrl, Field

from falcon_mcp.common.errors import _format_error_response, handle_api_response
from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule
from falcon_mcp.resources.recon import RECON_FQL_DOCUMENTATION

logger = get_logger(__name__)

WRITE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True,
)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True,
)


class ReconModule(BaseModule):
    """Module for CrowdStrike Falcon Intelligence Recon."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.search_recon_notifications, name="search_recon_notifications")
        self._add_tool(server=server, method=self.get_recon_notification_details, name="get_recon_notification_details")
        self._add_tool(server=server, method=self.search_recon_rules, name="search_recon_rules")
        self._add_tool(server=server, method=self.get_recon_rule_details, name="get_recon_rule_details")
        self._add_tool(
            server=server, method=self.update_recon_notifications, name="update_recon_notifications",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.delete_recon_notifications, name="delete_recon_notifications",
            annotations=DESTRUCTIVE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.create_recon_rule, name="create_recon_rule",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.update_recon_rule, name="update_recon_rule",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.delete_recon_rules, name="delete_recon_rules",
            annotations=DESTRUCTIVE_ANNOTATIONS,
        )

    def register_resources(self, server: FastMCP) -> None:
        self._add_resource(server, TextResource(
            uri=AnyUrl("falcon://recon/fql-guide"),
            name="falcon_recon_fql_guide",
            description="FQL filter guide for Recon search tools.",
            text=RECON_FQL_DOCUMENTATION,
        ))

    def search_recon_notifications(
        self,
        filter: str | None = Field(default=None, description="FQL filter; see `falcon://recon/fql-guide`."),
        limit: int = Field(default=10, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression (e.g. created_date.desc)."),
        q: str | None = Field(default=None, description="Free-text query string."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search Recon notifications and return their details."""
        ids = self._base_search_api_call(
            operation="QueryNotificationsV1",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort, "q": q},
            error_message="Failed to search Recon notifications",
        )
        if self._is_error(ids):
            if filter:
                return self._format_fql_error_response([ids], filter, RECON_FQL_DOCUMENTATION)
            return [ids]
        if not ids:
            if filter:
                return self._format_fql_error_response([], filter, RECON_FQL_DOCUMENTATION)
            return []
        details = self._base_get_by_ids(operation="GetNotificationsV1", ids=ids, use_params=True)
        if self._is_error(details):
            return [details]
        return details

    def get_recon_notification_details(
        self,
        ids: list[str] = Field(description="Notification IDs."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get full details for the given Recon notification IDs."""
        if not ids:
            return []
        return self._base_get_by_ids(operation="GetNotificationsV1", ids=ids, use_params=True)

    def search_recon_rules(
        self,
        filter: str | None = Field(default=None, description="FQL filter."),
        limit: int = Field(default=10, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
        q: str | None = Field(default=None, description="Free-text query string."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search Recon monitoring rules."""
        ids = self._base_search_api_call(
            operation="QueryRulesV1",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort, "q": q},
            error_message="Failed to search Recon rules",
        )
        if self._is_error(ids):
            return [ids]
        if not ids:
            return []
        details = self._base_get_by_ids(operation="GetRulesV1", ids=ids, use_params=True)
        if self._is_error(details):
            return [details]
        return details

    def get_recon_rule_details(
        self,
        ids: list[str] = Field(description="Rule IDs."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get full details for Recon rule IDs."""
        if not ids:
            return []
        return self._base_get_by_ids(operation="GetRulesV1", ids=ids, use_params=True)

    def update_recon_notifications(
        self,
        updates: list[dict[str, Any]] = Field(
            description=(
                "List of notification updates. Each item is a dict with `id` and any of "
                "`status` (e.g. 'new', 'in-progress', 'closed-true-positive', 'closed-false-positive') "
                "and `assigned_to_uuid`."
            ),
        ),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID to scope this call to a specific child tenant. Leave unset to use the parent account scope.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Update Recon notifications (status / assignee). Body is a top-level list per the API spec."""
        if not updates:
            return [_format_error_response(
                "`updates` is required.", operation="UpdateNotificationsV1",
            )]
        # Recon's PATCH expects a top-level list as body, not a {"resources": [...]} envelope.
        response = self.client.command_for("UpdateNotificationsV1", member_cid=member_cid, body=updates)
        return handle_api_response(
            response,
            operation="UpdateNotificationsV1",
            error_message="Failed to update Recon notifications",
            default_result=[],
        )

    def delete_recon_notifications(
        self,
        ids: list[str] = Field(description="Notification IDs to delete."),
    ) -> list[dict[str, Any]]:
        """Delete Recon notifications by ID."""
        if not ids:
            return [_format_error_response(
                "`ids` is required.", operation="DeleteNotificationsV1",
            )]
        result = self._base_query_api_call(
            operation="DeleteNotificationsV1",
            query_params={"ids": ids},
            error_message="Failed to delete Recon notifications",
        )
        if self._is_error(result):
            return [result]
        return result

    def create_recon_rule(
        self,
        name: str = Field(description="Rule name."),
        topic: str = Field(
            description="Rule topic (e.g. 'SA_ALIAS', 'SA_AUTHOR', 'SA_BRAND_PRODUCT', 'SA_VIP', 'SA_CVE', etc.).",
        ),
        filter: str = Field(description="Rule FQL filter expression."),
        priority: str = Field(description="'high', 'medium', or 'low'."),
        permissions: str = Field(description="'private' or 'public'."),
        breach_monitoring_enabled: bool = Field(default=False, description="Enable breach monitoring."),
        substring_matching_enabled: bool = Field(default=False, description="Enable substring matching."),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID to scope this call to a specific child tenant. Leave unset to use the parent account scope.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Create a Recon monitoring rule. Body is a top-level list per the API spec."""
        if priority not in ("high", "medium", "low"):
            return [_format_error_response(
                "`priority` must be high/medium/low.", operation="CreateRulesV1",
            )]
        if permissions not in ("private", "public"):
            return [_format_error_response(
                "`permissions` must be private/public.", operation="CreateRulesV1",
            )]
        rule = {
            "name": name,
            "topic": topic,
            "filter": filter,
            "priority": priority,
            "permissions": permissions,
            "breach_monitoring_enabled": breach_monitoring_enabled,
            "substring_matching_enabled": substring_matching_enabled,
        }
        response = self.client.command_for("CreateRulesV1", member_cid=member_cid, body=[rule])
        return handle_api_response(
            response, operation="CreateRulesV1",
            error_message="Failed to create Recon rule", default_result=[],
        )

    def update_recon_rule(
        self,
        id: str = Field(description="Rule ID to update."),
        name: str | None = Field(default=None, description="New name."),
        filter: str | None = Field(default=None, description="New FQL filter."),
        priority: str | None = Field(default=None, description="'high', 'medium', or 'low'."),
        permissions: str | None = Field(default=None, description="'private' or 'public'."),
        breach_monitoring_enabled: bool | None = Field(default=None, description="Enable breach monitoring."),
        substring_matching_enabled: bool | None = Field(default=None, description="Enable substring matching."),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID to scope this call to a specific child tenant. Leave unset to use the parent account scope.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Update a Recon monitoring rule. Body is a top-level list per the API spec."""
        rule: dict[str, Any] = {"id": id}
        if name is not None:
            rule["name"] = name
        if filter is not None:
            rule["filter"] = filter
        if priority is not None:
            rule["priority"] = priority
        if permissions is not None:
            rule["permissions"] = permissions
        if breach_monitoring_enabled is not None:
            rule["breach_monitoring_enabled"] = breach_monitoring_enabled
        if substring_matching_enabled is not None:
            rule["substring_matching_enabled"] = substring_matching_enabled
        if len(rule) == 1:
            return [_format_error_response(
                "Provide at least one field to update.", operation="UpdateRulesV1",
            )]
        response = self.client.command_for("UpdateRulesV1", member_cid=member_cid, body=[rule])
        return handle_api_response(
            response, operation="UpdateRulesV1",
            error_message="Failed to update Recon rule", default_result=[],
        )

    def delete_recon_rules(
        self,
        ids: list[str] = Field(description="Rule IDs to delete."),
        delete_notifications: bool = Field(
            default=False,
            description="If True, also delete notifications generated by these rules.",
        ),
    ) -> list[dict[str, Any]]:
        """Delete Recon monitoring rules."""
        if not ids:
            return [_format_error_response(
                "`ids` is required.", operation="DeleteRulesV1",
            )]
        result = self._base_query_api_call(
            operation="DeleteRulesV1",
            query_params={
                "ids": ids,
                "notificationsDeletionRequested": delete_notifications,
            },
            error_message="Failed to delete Recon rules",
        )
        if self._is_error(result):
            return [result]
        return result
