"""
Zero Trust Assessment module for Falcon MCP Server.

Provides tools for reading CrowdStrike Zero Trust Assessment scores and the audit trail.
"""

from typing import Any

from mcp.server import FastMCP
from mcp.server.fastmcp.resources import TextResource
from pydantic import AnyUrl, Field

from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule
from falcon_mcp.resources.zero_trust import ZTA_FQL_DOCUMENTATION

logger = get_logger(__name__)


class ZeroTrustModule(BaseModule):
    """Module for CrowdStrike Falcon Zero Trust Assessment."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_zta_assessments, name="get_zta_assessments")
        self._add_tool(server=server, method=self.search_zta_assessments, name="search_zta_assessments")
        self._add_tool(server=server, method=self.get_zta_assessments_by_score, name="get_zta_assessments_by_score")
        self._add_tool(server=server, method=self.get_zta_audit, name="get_zta_audit")

    def register_resources(self, server: FastMCP) -> None:
        self._add_resource(server, TextResource(
            uri=AnyUrl("falcon://zero-trust/fql-guide"),
            name="falcon_zta_fql_guide",
            description="FQL filter guide for Zero Trust Assessment search tools.",
            text=ZTA_FQL_DOCUMENTATION,
        ))

    def get_zta_assessments(
        self,
        ids: list[str] = Field(description="Host AIDs to fetch ZTA scores for. Maximum 100 per request."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get the latest Zero Trust Assessment for a list of host AIDs."""
        if not ids:
            return []
        return self._base_get_by_ids(operation="getAssessmentV1", ids=ids, use_params=True)

    def search_zta_assessments(
        self,
        filter: str | None = Field(default=None, description="FQL filter; see `falcon://zero-trust/fql-guide`."),
        limit: int = Field(default=100, ge=1, le=1000, description="Max records."),
        offset: str | None = Field(default=None, description="Pagination token from previous response (`after`)."),
        sort: str | None = Field(default=None, description="Sort expression (e.g. score.asc)."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search Zero Trust Assessments across hosts (combined query)."""
        result = self._base_search_api_call(
            operation="getCombinedAssessmentsQuery",
            search_params={"filter": filter, "limit": limit, "after": offset, "sort": sort},
            error_message="Failed to query ZTA assessments",
        )
        if self._is_error(result):
            if filter:
                return self._format_fql_error_response([result], filter, ZTA_FQL_DOCUMENTATION)
            return [result]
        if not result and filter:
            return self._format_fql_error_response([], filter, ZTA_FQL_DOCUMENTATION)
        return result

    def get_zta_assessments_by_score(
        self,
        filter: str | None = Field(default=None, description="FQL filter (e.g. `score:<50`)."),
        limit: int = Field(default=100, ge=1, le=1000, description="Max records."),
        offset: str | None = Field(default=None, description="Pagination token (`after`)."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List ZTA assessments ordered/filtered by score (find lowest-scoring hosts)."""
        result = self._base_search_api_call(
            operation="getAssessmentsByScoreV1",
            search_params={"filter": filter, "limit": limit, "after": offset, "sort": sort},
            error_message="Failed to query ZTA assessments by score",
        )
        if self._is_error(result):
            if filter:
                return self._format_fql_error_response([result], filter, ZTA_FQL_DOCUMENTATION)
            return [result]
        return result

    def get_zta_audit(self) -> list[dict[str, Any]] | dict[str, Any]:
        """Get the ZTA audit/aggregate scores for the CID (sensor coverage, OS coverage, etc.)."""
        result = self._base_search_api_call(
            operation="getAuditV1",
            search_params={},
            error_message="Failed to fetch ZTA audit",
        )
        if self._is_error(result):
            return [result]
        return result
