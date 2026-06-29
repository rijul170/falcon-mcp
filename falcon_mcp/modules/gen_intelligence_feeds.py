"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `intelligence_feeds` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenIntelligenceFeedsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `intelligence_feeds` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.download_feed_archive, name="download_feed_archive")
        self._add_tool(server=server, method=self.list_feed_types, name="list_feed_types")
        self._add_tool(server=server, method=self.query_feed_archives, name="query_feed_archives")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def download_feed_archive(
        self,
        feed_item_id: str = Field(description="Feed ID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Downloads the content as a zip archive for a given feed item ID"""
        return self._call(operation="DownloadFeedArchive", query_params={"feed_item_id": feed_item_id}, error_message="DownloadFeedArchive failed", member_cid=member_cid)

    def list_feed_types(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Lists the accessible feed types for a given customer"""
        return self._call(operation="ListFeedTypes", query_params=None, error_message="ListFeedTypes failed", member_cid=member_cid)

    def query_feed_archives(
        self,
        feed_name: str = Field(description="Feed Name"),
        feed_interval: str | None = Field(default=None, description="Feed interval must be one of: dump: Complete historical data snapshot daily: Daily aggregated updates hourly: Hourly incremental updates minutely: Minute-by-minute updates any: Automatically combines the appropriate intervals to provide complete, up-to-date data with minimal overlap Defaults to 'any' if not specified."),
        since: str | None = Field(default=None, description="Since is a valid timestamp in RFC3399 format. Restrictions: minutely: now()-2h, hourly: now()-2d, daily: now()-5d; dump: now()-7d"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Queries the accessible feed types for a customer. Returns a list of feed item IDs which can be later downloaded"""
        return self._call(operation="QueryFeedArchives", query_params={"feed_name": feed_name, "feed_interval": feed_interval, "since": since}, error_message="QueryFeedArchives failed", member_cid=member_cid)
