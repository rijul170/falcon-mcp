"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `malquery` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenMalqueryModule(GeneratedModuleBase):
    """Generated tools for the Falcon `malquery` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_mal_query_download_v1, name="get_mal_query_download_v1")
        self._add_tool(server=server, method=self.get_mal_query_entities_samples_fetch_v1, name="get_mal_query_entities_samples_fetch_v1")
        self._add_tool(server=server, method=self.post_mal_query_entities_samples_multidownload_v1, name="post_mal_query_entities_samples_multidownload_v1", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.post_mal_query_fuzzy_search_v1, name="post_mal_query_fuzzy_search_v1", annotations=WRITE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def get_mal_query_download_v1(
        self,
        ids: list[str] = Field(description="The file SHA256."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Download a file indexed by MalQuery. Specify the file using its SHA256. Only one file is supported at this time"""
        return self._call(operation="GetMalQueryDownloadV1", query_params={"ids": ids}, error_message="GetMalQueryDownloadV1 failed", member_cid=member_cid)

    def get_mal_query_entities_samples_fetch_v1(
        self,
        ids: str = Field(description="Multidownload job id"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Fetch a zip archive with password 'infected' containing the samples. Call this once the /entities/samples-multidownload request has finished processing"""
        return self._call(operation="GetMalQueryEntitiesSamplesFetchV1", query_params={"ids": ids}, error_message="GetMalQueryEntitiesSamplesFetchV1 failed", member_cid=member_cid)

    def post_mal_query_entities_samples_multidownload_v1(
        self,
        body: dict = Field(description="Request JSON body for `PostMalQueryEntitiesSamplesMultidownloadV1` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Schedule samples for download. Use the result id with the /request endpoint to check if the download is ready after which you can call the /entities/samples-fetch to get the zip"""
        return self._call(operation="PostMalQueryEntitiesSamplesMultidownloadV1", query_params=None, body_params=body, error_message="PostMalQueryEntitiesSamplesMultidownloadV1 failed", member_cid=member_cid)

    def post_mal_query_fuzzy_search_v1(
        self,
        body: dict = Field(description="Request JSON body for `PostMalQueryFuzzySearchV1` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search Falcon MalQuery quickly, but with more potential for false positives. Search for a combination of hex patterns and strings in order to identify samples based upon file content at byte level granularity."""
        return self._call(operation="PostMalQueryFuzzySearchV1", query_params=None, body_params=body, error_message="PostMalQueryFuzzySearchV1 failed", member_cid=member_cid)
