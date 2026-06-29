"""
Tailored Intelligence module for Falcon MCP Server.

Read-only access to CrowdStrike Tailored Intelligence events and rules (indicators):
query event/rule IDs by FQL and hydrate the full entities.
"""

from typing import Any

from mcp.server import FastMCP
from pydantic import Field

from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule

logger = get_logger(__name__)


class TailoredIntelligenceModule(BaseModule):
    """Module for CrowdStrike Falcon Tailored Intelligence (events and rules)."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.search_tailored_intel_events, name="search_tailored_intel_events")
        self._add_tool(server=server, method=self.get_tailored_intel_event_details, name="get_tailored_intel_event_details")
        self._add_tool(server=server, method=self.search_tailored_intel_rules, name="search_tailored_intel_rules")
        self._add_tool(server=server, method=self.get_tailored_intel_rule_details, name="get_tailored_intel_rule_details")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def search_tailored_intel_events(
        self,
        filter: str | None = Field(
            default=None,
            description="FQL filter over tailored intel events, e.g. `created_date:>'2024-01-01'`.",
        ),
        limit: int = Field(default=100, ge=1, le=5000, description="Max event IDs to query."),
        offset: str | None = Field(default=None, description="Offset for pagination."),
        sort: str | None = Field(default=None, description="Sort expression, e.g. `updated_date|desc`."),
        q: str | None = Field(default=None, description="Free-text phrase_prefix match across indexed fields."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search Tailored Intelligence event IDs by FQL filter.

        Returns event IDs; pass them to `falcon_get_tailored_intel_event_details`.
        """
        return self._base_search_api_call(
            operation="QueryEvents",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort, "q": q},
            error_message="Failed to query tailored intelligence events",
            member_cid=member_cid,
        )

    def get_tailored_intel_event_details(
        self,
        ids: list[str] = Field(description="Event IDs. Obtain from `falcon_search_tailored_intel_events`."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get full Tailored Intelligence event entities by ID."""
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="GetEventsEntities", ids=ids, member_cid=member_cid,
        )

    def search_tailored_intel_rules(
        self,
        filter: str | None = Field(
            default=None,
            description="FQL filter over tailored intel rules, e.g. `type:'snort-suricata-master'`.",
        ),
        limit: int = Field(default=100, ge=1, le=5000, description="Max rule IDs to query."),
        offset: str | None = Field(default=None, description="Offset for pagination."),
        sort: str | None = Field(default=None, description="Sort expression, e.g. `updated_date|desc`."),
        q: str | None = Field(default=None, description="Free-text phrase_prefix match across indexed fields."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search Tailored Intelligence rule IDs by FQL filter.

        Returns rule IDs; pass them to `falcon_get_tailored_intel_rule_details`.
        """
        return self._base_search_api_call(
            operation="QueryRules",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort, "q": q},
            error_message="Failed to query tailored intelligence rules",
            member_cid=member_cid,
        )

    def get_tailored_intel_rule_details(
        self,
        ids: list[str] = Field(description="Rule IDs. Obtain from `falcon_search_tailored_intel_rules`."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get full Tailored Intelligence rule entities by ID."""
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="GetRulesEntities", ids=ids, member_cid=member_cid,
        )
