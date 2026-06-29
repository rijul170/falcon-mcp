"""
Configuration Assessment module for Falcon MCP Server.

Provides tools for querying Falcon Configuration Assessment findings (host-level
benchmark compliance checks) and their underlying rule definitions.
"""

from typing import Any

from mcp.server import FastMCP
from pydantic import Field

from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule

logger = get_logger(__name__)


class ConfigurationAssessmentModule(BaseModule):
    """Module for CrowdStrike Falcon Configuration Assessment findings."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.search_configuration_assessments, name="search_configuration_assessments")
        self._add_tool(server=server, method=self.get_configuration_assessment_rule_details, name="get_configuration_assessment_rule_details")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def search_configuration_assessments(
        self,
        filter: str = Field(
            description=(
                "FQL filter (required). Common fields: "
                "`aid` (host AID), `created_timestamp`, `updated_timestamp`, "
                "`finding.severity` ('low','medium','high','critical'), "
                "`status` ('new','in_progress','closed'). "
                "Example: `aid:'abc123'+finding.severity:'critical'`"
            ),
        ),
        limit: int = Field(default=100, ge=1, le=5000, description="Max records per page."),
        after: str | None = Field(
            default=None,
            description="Cursor token from a previous response for pagination. Omit for first page.",
        ),
        sort: str | None = Field(
            default=None,
            description="Sort expression. Examples: `created_timestamp|desc`, `updated_timestamp|asc`.",
        ),
        facet: list[str] | None = Field(
            default=None,
            description=(
                "Detail blocks to include. Values: `host`, `finding.rule`, `finding.evaluation_logic`. "
                "Default (no facet) returns summary data only."
            ),
        ),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID for MSSP child tenant scoping.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search configuration assessment findings across hosts.

        Returns HostFinding entities — benchmark compliance check results per host.
        Each finding links a host (via AID) to a specific rule and its pass/fail status.

        Use `facet=['host','finding.rule']` to get enriched results with host metadata
        and rule details in a single call.

        Uses cursor-based pagination: pass the `after` token from the previous response
        to get the next page.
        """
        from falcon_mcp.common.utils import prepare_api_parameters
        params = prepare_api_parameters({
            "filter": filter,
            "limit": limit,
            "after": after,
            "sort": sort,
            "facet": facet,
        })
        response = self.client.command_for("getCombinedAssessmentsQuery", member_cid=member_cid, parameters=params)
        if not isinstance(response, dict) or response.get("status_code") not in (200, None):
            from falcon_mcp.common.errors import handle_api_response
            return handle_api_response(
                response,
                operation="getCombinedAssessmentsQuery",
                error_message="Failed to search configuration assessments",
                default_result=[],
            )
        body = response.get("body", {})
        resources = body.get("resources", []) if isinstance(body, dict) else []
        return resources if isinstance(resources, list) else [resources]

    def get_configuration_assessment_rule_details(
        self,
        ids: list[str] = Field(description="Rule IDs to retrieve (max 400). Obtain from assessment findings."),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID for MSSP child tenant scoping.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get full rule definitions for configuration assessment rules by ID.

        Returns rule metadata including title, description, rationale, remediation steps,
        benchmark references, and severity. Use this to understand what a failing check
        requires before building remediation workflows.
        """
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="getRuleDetails", ids=ids, use_params=True, member_cid=member_cid,
        )
