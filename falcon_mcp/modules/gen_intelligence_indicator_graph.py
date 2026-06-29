"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `intelligence_indicator_graph` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenIntelligenceIndicatorGraphModule(GeneratedModuleBase):
    """Generated tools for the Falcon `intelligence_indicator_graph` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.lookup_indicators, name="lookup_indicators")
        self._add_tool(server=server, method=self.search_indicators_intelligence_indicator_graph, name="search_indicators_intelligence_indicator_graph", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def lookup_indicators(
        self,
        body: dict = Field(description="Request JSON body for `LookupIndicators` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get indicators based on their value."""
        return self._call(operation="LookupIndicators", query_params=None, body_params=body, error_message="LookupIndicators failed", member_cid=member_cid)

    def search_indicators_intelligence_indicator_graph(
        self,
        body: dict = Field(description="Request JSON body for `SearchIndicators` per the CrowdStrike API schema (required)."),
        sort: str | None = Field(default=None, description="Parameter to specify the order(field examples: FileDetails.SHA256, URLDetails.URL, PublishDate, MaliciousConfidence) Ex: 'PublishDate|asc'."),
        filter: str | None = Field(default=None, description="FQL query specifying the filter parameters. **Filter parameters include:** Type, LastUpdated, KillChain, MaliciousConfidence, MaliciousConfidenceValidatedTime, FirstSeen, LastSeen, Adversaries.Name, Adversaries.Slug, Reports.Title, Reports.Slug, Threats.FamilyName, Vulnerabilities.CVE, Sectors.Name, FileDetails.SHA256, FileDetails.SHA1, FileDetails.MD5, DomainDetails.Detail, IPv4Details.IPv4, IPv6Details.IPv6, URLDetails.URL and others"),
        limit: int | None = Field(default=None, description="Limit"),
        offset: str | None = Field(default=None, description="Offset"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search indicators based on FQL filter."""
        return self._call(operation="SearchIndicators", query_params={"sort": sort, "filter": filter, "limit": limit, "offset": offset}, body_params=body, error_message="SearchIndicators failed", member_cid=member_cid)
