"""
Correlation Rules module for Falcon MCP Server.

Provides tools for managing NGSIEM correlation/detection rules that trigger
alerts based on log and event patterns.
"""

from typing import Any

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.errors import handle_api_response
from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule

logger = get_logger(__name__)

WRITE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True,
)

DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True,
)


class CorrelationRulesModule(BaseModule):
    """Module for managing CrowdStrike NGSIEM correlation rules."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.search_correlation_rules, name="search_correlation_rules")
        self._add_tool(server=server, method=self.get_correlation_rule_details, name="get_correlation_rule_details")
        self._add_tool(
            server=server, method=self.create_correlation_rule, name="create_correlation_rule",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.update_correlation_rule, name="update_correlation_rule",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.delete_correlation_rules, name="delete_correlation_rules",
            annotations=DESTRUCTIVE_ANNOTATIONS,
        )

    def search_correlation_rules(
        self,
        filter: str | None = Field(
            default=None,
            description="FQL filter. Supported fields: customer_id, user_id, user_uuid, status, name, created_on, last_updated_on. Example: \"status:'enabled'\".",
        ),
        q: str | None = Field(
            default=None,
            description="Full-text search across all rule metadata.",
        ),
        sort: str | None = Field(
            default=None,
            description="Sort expression: `created_on`, `created_on|desc`, `last_updated_on`, `last_updated_on|desc`.",
            examples=["created_on|desc", "last_updated_on|desc"],
        ),
        limit: int = Field(
            default=20, ge=1, le=500,
            description="Maximum number of rules to return.",
        ),
        offset: int | None = Field(default=None, description="Pagination offset."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search NGSIEM correlation rules and return full rule details.

        Use `filter` to narrow by status or name, `q` for free-text search across rule content.
        Returns full rule objects including trigger conditions, severity, and MITRE mappings.
        """
        ids = self._base_search_api_call(
            operation="queries_rules_get_v1",
            search_params={"filter": filter, "q": q, "sort": sort, "limit": limit, "offset": offset},
            error_message="Failed to search correlation rules",
        )
        if self._is_error(ids):
            return [ids]
        if not ids:
            return []

        details = self._base_get_by_ids(
            operation="entities_rules_get_v2",
            ids=ids,
            id_key="ids",
            use_params=True,
        )
        if self._is_error(details):
            return [details]
        return details

    def get_correlation_rule_details(
        self,
        ids: list[str] = Field(
            description="Correlation rule IDs to retrieve. Obtain from `falcon_search_correlation_rules`.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Retrieve full details for one or more correlation rules by ID."""
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="entities_rules_get_v2",
            ids=ids,
            id_key="ids",
            use_params=True,
        )

    def create_correlation_rule(
        self,
        name: str = Field(description="Name for the new correlation rule."),
        rule_body: dict[str, Any] = Field(
            description=(
                "Full rule definition as a JSON object. Must include at minimum `name` and the "
                "trigger/query configuration. Key fields: `description`, `severity` (1-100), "
                "`status` (enabled/disabled), `triggers` (list of trigger objects), "
                "`notifications` (alert routing), `mitre_attack` (list of {tactic_id, technique_id}). "
                "The `name` in this body overrides the `name` parameter if both are provided."
            ),
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Create a new NGSIEM correlation rule.

        Provide the full rule definition in `rule_body`. At minimum include the trigger/query
        configuration — a rule with no triggers will never fire. Use `falcon_get_correlation_rule_details`
        on an existing rule to understand the expected body structure.
        """
        body = {"name": name, **rule_body}
        return self._base_query_api_call(
            operation="entities_rules_post_v1",
            body_params=body,
            error_message="Failed to create correlation rule",
        )

    def update_correlation_rule(
        self,
        rule_id: str = Field(
            description="ID of the rule to update. Obtain from `falcon_search_correlation_rules`.",
        ),
        rule_body: dict[str, Any] = Field(
            description=(
                "Updated rule definition as a JSON object. Include `id` in the body or it will "
                "be set from `rule_id`. Fields you omit are not changed. Common update fields: "
                "`name`, `description`, `status` (enabled/disabled), `severity`, `triggers`, `notifications`."
            ),
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Update an existing NGSIEM correlation rule.

        Pass only the fields you want to change in `rule_body`. The rule ID from `rule_id`
        is automatically injected into the body.
        """
        body = {"id": rule_id, **rule_body}
        return self._base_query_api_call(
            operation="entities_rules_patch_v1",
            body_params=body,
            error_message="Failed to update correlation rule",
        )

    def delete_correlation_rules(
        self,
        ids: list[str] = Field(
            description="Correlation rule IDs to permanently delete. Obtain from `falcon_search_correlation_rules`.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Permanently delete one or more correlation rules.

        IMPORTANT: Deleted rules cannot be recovered. Active rules stop firing immediately.
        """
        response = self.client.command_for(
            "entities_rules_delete_v1",
            parameters={"ids": ids},
        )
        return handle_api_response(
            response,
            operation="entities_rules_delete_v1",
            error_message="Failed to delete correlation rules",
            default_result=[],
        )
