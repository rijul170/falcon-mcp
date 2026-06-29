"""
Falcon Sandbox (Falcon Intelligence Sandbox / FalconX) module for Falcon MCP Server.

Provides detonation and report-retrieval tools: submit a file hash or URL for sandbox
analysis (mutating), query report IDs, and retrieve full reports or summary reports (RO).
"""

from typing import Any

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.errors import _format_error_response
from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule

logger = get_logger(__name__)

# Submitting a detonation creates a new analysis job; not destructive, not idempotent.
SUBMIT_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True,
)


class FalconXSandboxModule(BaseModule):
    """Module for CrowdStrike Falcon Intelligence Sandbox (FalconX)."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.query_sandbox_reports, name="query_sandbox_reports")
        self._add_tool(server=server, method=self.get_sandbox_report, name="get_sandbox_report")
        self._add_tool(server=server, method=self.get_sandbox_report_summary, name="get_sandbox_report_summary")
        self._add_tool(
            server=server, method=self.submit_sandbox_analysis, name="submit_sandbox_analysis",
            annotations=SUBMIT_ANNOTATIONS,
        )

    def register_resources(self, server: FastMCP) -> None:
        pass

    def query_sandbox_reports(
        self,
        filter: str | None = Field(
            default=None,
            description="FQL filter over submissions, e.g. `sandbox.sha256:'<hash>'` or `state:'success'`.",
        ),
        limit: int = Field(default=100, ge=1, le=5000, description="Max report IDs to return."),
        offset: str | None = Field(default=None, description="Offset for pagination."),
        sort: str | None = Field(default=None, description="Sort expression, e.g. `created_timestamp|desc`."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Query Falcon Sandbox report IDs matching an FQL filter.

        Returns report IDs; pass them to `falcon_get_sandbox_report` or
        `falcon_get_sandbox_report_summary` to retrieve the analysis.
        """
        return self._base_search_api_call(
            operation="QueryReports",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to query sandbox reports",
            member_cid=member_cid,
        )

    def get_sandbox_report(
        self,
        ids: list[str] = Field(description="Report IDs. Obtain from `falcon_query_sandbox_reports`."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get full Falcon Sandbox analysis reports by ID (behavioral details, IOCs, verdict)."""
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="GetReports", ids=ids, use_params=True, member_cid=member_cid,
        )

    def get_sandbox_report_summary(
        self,
        ids: list[str] = Field(description="Report IDs. Obtain from `falcon_query_sandbox_reports`."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get condensed Falcon Sandbox summary reports by ID (verdict, threat score, key IOCs)."""
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="GetSummaryReports", ids=ids, use_params=True, member_cid=member_cid,
        )

    def submit_sandbox_analysis(
        self,
        sha256: str | None = Field(
            default=None,
            description="SHA256 of a sample already uploaded to the Sample Store to detonate.",
        ),
        url: str | None = Field(default=None, description="URL to submit for analysis (instead of sha256)."),
        environment_id: int = Field(
            default=160,
            description=(
                "Sandbox environment ID. Common: 160 (Win10 x64), 110 (Win7 x64), "
                "300 (Linux Ubuntu 16.04), 200 (Android). "
            ),
        ),
        action_script: str | None = Field(default=None, description="Runtime action script for the analysis."),
        command_line: str | None = Field(default=None, description="Command line passed to the sample at runtime."),
        document_password: str | None = Field(default=None, description="Password for protected Office/Adobe files."),
        submit_name: str | None = Field(default=None, description="Display name for the submitted sample."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Submit a sample (by SHA256) or URL to the Falcon Intelligence Sandbox for detonation.

        Returns a submission ID; the analysis runs asynchronously. Poll
        `falcon_query_sandbox_reports` / `falcon_get_sandbox_report` for results. Provide
        exactly one of `sha256` or `url`.
        """
        if not sha256 and not url:
            return [_format_error_response("Provide exactly one of `sha256` or `url`.", operation="Submit")]
        if sha256 and url:
            return [_format_error_response("Provide only one of `sha256` or `url`, not both.", operation="Submit")]
        item: dict[str, Any] = {"environment_id": environment_id}
        if sha256:
            item["sha256"] = sha256
        if url:
            item["url"] = url
        if action_script:
            item["action_script"] = action_script
        if command_line:
            item["command_line"] = command_line
        if document_password:
            item["document_password"] = document_password
        if submit_name:
            item["submit_name"] = submit_name
        result = self._base_query_api_call(
            operation="Submit",
            body_params={"sandbox": [item]},
            error_message="Failed to submit sandbox analysis",
            member_cid=member_cid,
        )
        if self._is_error(result):
            return [result]
        return result
