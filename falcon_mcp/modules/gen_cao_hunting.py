"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `cao_hunting` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenCaoHuntingModule(GeneratedModuleBase):
    """Generated tools for the Falcon `cao_hunting` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_archive_export, name="get_archive_export")
        self._add_tool(server=server, method=self.get_hunting_guides, name="get_hunting_guides")
        self._add_tool(server=server, method=self.get_intelligence_queries, name="get_intelligence_queries")
        self._add_tool(server=server, method=self.search_hunting_guides, name="search_hunting_guides")
        self._add_tool(server=server, method=self.search_intelligence_queries, name="search_intelligence_queries")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def get_archive_export(
        self,
        language: str = Field(description="The Query Language. Accepted Values: <li>cql</li><li>snort</li><li>suricata</li><li>yara</li><li>SPL <i>AI translated (Beta)</i></li><li>__all__ <i>returns a single archive with queries in all the languages</i></li>"),
        filter: str | None = Field(default=None, description="The FQL Filter"),
        archive_type: str | None = Field(default=None, description="The Archive Type can be one of 'zip' and 'gzip'"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Creates an Archive Export"""
        return self._call(operation="GetArchiveExport", query_params={"language": language, "filter": filter, "archive_type": archive_type}, error_message="GetArchiveExport failed", member_cid=member_cid)

    def get_hunting_guides(
        self,
        ids: list[str] = Field(description="Hunting Guides IDs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves a list of Hunting Guides"""
        return self._call(operation="GetHuntingGuides", query_params={"ids": ids}, error_message="GetHuntingGuides failed", member_cid=member_cid)

    def get_intelligence_queries(
        self,
        ids: list[str] = Field(description="Intelligence queries IDs"),
        include_translated_content: list[str] | None = Field(default=None, description="The AI translated language that should be returned if it exists<br>Accepted values are: <li>SPL</li><li>__all__</li>"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves the details of a list of Intelligence queries IDs"""
        return self._call(operation="GetIntelligenceQueries", query_params={"ids": ids, "include_translated_content": include_translated_content}, error_message="GetIntelligenceQueries failed", member_cid=member_cid)

    def search_hunting_guides(
        self,
        offset: str | None = Field(default=None, description="Starting index of result set from which to return IDs."),
        limit: int | None = Field(default=None, description="Number of IDs to return."),
        sort: str | None = Field(default=None, description="Order by fields."),
        filter: str | None = Field(default=None, description="FQL query specifying the filter parameters."),
        q: str | None = Field(default=None, description="Match phrase_prefix query criteria; included fields: _all (all filter string fields indexed)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for Hunting Guides that match the provided conditions"""
        return self._call(operation="SearchHuntingGuides", query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter, "q": q}, error_message="SearchHuntingGuides failed", member_cid=member_cid)

    def search_intelligence_queries(
        self,
        offset: str | None = Field(default=None, description="Starting index of result set from which to return IDs."),
        limit: int | None = Field(default=None, description="Number of IDs to return."),
        sort: str | None = Field(default=None, description="Order by fields."),
        filter: str | None = Field(default=None, description="FQL query specifying the filter parameters."),
        q: str | None = Field(default=None, description="Match phrase_prefix query criteria; included fields: _all (all filter string fields indexed)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for a list of intelligence queries IDs that match the provided conditions"""
        return self._call(operation="SearchIntelligenceQueries", query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter, "q": q}, error_message="SearchIntelligenceQueries failed", member_cid=member_cid)
