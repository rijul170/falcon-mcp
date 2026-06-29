"""
MalQuery module for Falcon MCP Server.

Provides malware-hunting enrichment via CrowdStrike MalQuery: exact (hex/ascii/wide)
pattern search, YARA hunt, sample metadata lookup, and quota checks. Search/hunt submit
a request and return a request_id to poll; metadata and quota are read-only.
"""

from typing import Any

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.errors import _format_error_response
from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule

logger = get_logger(__name__)

# Search/hunt create a server-side asynchronous request; not destructive but not idempotent.
SUBMIT_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True,
)


class MalQueryModule(BaseModule):
    """Module for CrowdStrike Falcon MalQuery malware hunting enrichment."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_malquery_quotas, name="get_malquery_quotas")
        self._add_tool(server=server, method=self.get_malquery_sample_metadata, name="get_malquery_sample_metadata")
        self._add_tool(server=server, method=self.get_malquery_request_results, name="get_malquery_request_results")
        self._add_tool(
            server=server, method=self.malquery_exact_search, name="malquery_exact_search",
            annotations=SUBMIT_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.malquery_hunt, name="malquery_hunt",
            annotations=SUBMIT_ANNOTATIONS,
        )

    def register_resources(self, server: FastMCP) -> None:
        pass

    def get_malquery_quotas(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get the MalQuery search/download quota and usage for this tenant."""
        return self._base_query_api_call(
            operation="GetMalQueryQuotasV1",
            error_message="Failed to get MalQuery quotas",
            member_cid=member_cid,
        )

    def get_malquery_sample_metadata(
        self,
        ids: list[str] = Field(description="SHA256 hashes to retrieve MalQuery metadata for."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get MalQuery metadata (file type, size, first/last seen, labels) for SHA256 samples."""
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="GetMalQueryMetadataV1", ids=ids, use_params=True, member_cid=member_cid,
        )

    def get_malquery_request_results(
        self,
        ids: list[str] = Field(
            description="MalQuery request IDs returned by `malquery_exact_search` / `malquery_hunt`.",
        ),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Poll a MalQuery search/hunt request by its request_id and return matches when ready."""
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="GetMalQueryRequestV1", ids=ids, use_params=True, member_cid=member_cid,
        )

    def malquery_exact_search(
        self,
        patterns: list[dict[str, str]] = Field(
            description=(
                "Patterns to match. Each is `{'type': <hex|ascii|wide>, 'value': <pattern>}`. "
                "Example: `[{'type':'ascii','value':'malware-string'}]`"
            ),
        ),
        filter_filetypes: list[str] | None = Field(default=None, description="Restrict to file types, e.g. ['pe32','elf']."),
        filter_meta: list[str] | None = Field(
            default=None,
            description="Metadata fields to return, e.g. ['sha256','type','size','label'].",
        ),
        limit: int | None = Field(default=None, description="Max matches to return."),
        min_size: str | None = Field(default=None, description="Minimum file size in bytes (string)."),
        max_size: str | None = Field(default=None, description="Maximum file size in bytes (string)."),
        min_date: str | None = Field(default=None, description="Earliest first-seen date (UTC string)."),
        max_date: str | None = Field(default=None, description="Latest first-seen date (UTC string)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Submit a MalQuery exact-pattern search across CrowdStrike's malware corpus.

        Returns a request_id; poll it with `falcon_get_malquery_request_results`. Use to find
        samples sharing a byte/string pattern with a suspected artifact (hunting enrichment).
        """
        if not patterns:
            return [_format_error_response("`patterns` is required.", operation="PostMalQueryExactSearchV1")]
        options: dict[str, Any] = {}
        for k, v in (
            ("filter_filetypes", filter_filetypes), ("filter_meta", filter_meta),
            ("limit", limit), ("min_size", min_size), ("max_size", max_size),
            ("min_date", min_date), ("max_date", max_date),
        ):
            if v is not None:
                options[k] = v
        body: dict[str, Any] = {"patterns": patterns}
        if options:
            body["options"] = options
        return self._base_query_api_call(
            operation="PostMalQueryExactSearchV1",
            body_params=body,
            error_message="Failed to submit MalQuery exact search",
            member_cid=member_cid,
        )

    def malquery_hunt(
        self,
        yara_rule: str = Field(description="YARA rule used to hunt across the MalQuery corpus."),
        filter_filetypes: list[str] | None = Field(default=None, description="Restrict to file types."),
        filter_meta: list[str] | None = Field(default=None, description="Metadata fields to return."),
        limit: int | None = Field(default=None, description="Max matches to return."),
        min_size: str | None = Field(default=None, description="Minimum file size in bytes (string)."),
        max_size: str | None = Field(default=None, description="Maximum file size in bytes (string)."),
        min_date: str | None = Field(default=None, description="Earliest first-seen date (UTC string)."),
        max_date: str | None = Field(default=None, description="Latest first-seen date (UTC string)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Submit a MalQuery YARA hunt across CrowdStrike's malware corpus.

        Returns a request_id; poll it with `falcon_get_malquery_request_results`.
        """
        if not yara_rule:
            return [_format_error_response("`yara_rule` is required.", operation="PostMalQueryHuntV1")]
        options: dict[str, Any] = {}
        for k, v in (
            ("filter_filetypes", filter_filetypes), ("filter_meta", filter_meta),
            ("limit", limit), ("min_size", min_size), ("max_size", max_size),
            ("min_date", min_date), ("max_date", max_date),
        ):
            if v is not None:
                options[k] = v
        body: dict[str, Any] = {"yara_rule": yara_rule}
        if options:
            body["options"] = options
        return self._base_query_api_call(
            operation="PostMalQueryHuntV1",
            body_params=body,
            error_message="Failed to submit MalQuery hunt",
            member_cid=member_cid,
        )
