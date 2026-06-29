"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `spotlight_evaluation_logic` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenSpotlightEvaluationLogicModule(GeneratedModuleBase):
    """Generated tools for the Falcon `spotlight_evaluation_logic` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.combined_query_evaluation_logic, name="combined_query_evaluation_logic")
        self._add_tool(server=server, method=self.combined_supported_evaluation_ext, name="combined_supported_evaluation_ext")
        self._add_tool(server=server, method=self.get_evaluation_logic, name="get_evaluation_logic")
        self._add_tool(server=server, method=self.query_evaluation_logic, name="query_evaluation_logic")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def combined_query_evaluation_logic(
        self,
        filter: str = Field(description="FQL query specifying the filter parameters."),
        after: str | None = Field(default=None, description="A pagination token used with the limit parameter to manage pagination of results. On your first request, don't provide an after token. On subsequent requests, provide the after token from the previous response to continue from that place in the results."),
        limit: int | None = Field(default=None, description="Maximum number of entities to return."),
        sort: str | None = Field(default=None, description="Sort evaluation logic by their properties."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for evaluation logic in your environment by providing a FQL filter and paging details. Returns a set of evaluation logic entities which match the filter criteria."""
        return self._call(operation="combinedQueryEvaluationLogic", query_params={"after": after, "limit": limit, "filter": filter, "sort": sort}, error_message="combinedQueryEvaluationLogic failed", member_cid=member_cid)

    def combined_supported_evaluation_ext(
        self,
        filter: str = Field(description="Filter items using a query in Falcon Query Language (FQL). Wildcards * and empty filter values are unsupported. Available filter fields that supports match (~): N/A Available filter fields that supports exact match: id, risk_id, risk_provider, finding_provider, platform Available filter fields that supports wildcard (*): N/A Available filter fields that supports range comparisons (>, <, >=, <=): created_timestamp, updated_timestamp"),
        after: str | None = Field(default=None, description="A pagination token used with the limit parameter to manage pagination of results. On your first request, don't provide an after token. On subsequent requests, provide the after token from the previous response to continue from that place in the results."),
        offset: str | None = Field(default=None, description="Starting index of overall result set from which to return ids."),
        limit: int | None = Field(default=None, description="The number of items to return in this response (default: 100, max: 400). Use with the after parameter to manage pagination of results."),
        sort: str | None = Field(default=None, description="Sort vulnerabilities by their properties. Available sort options: <ul><li>created_timestamp|asc/desc</li><li>updated_timestamp|asc/desc</li></ul>. Can be used in a format <field>|asc for ascending order or <field>|desc for descending order."),
        risk_provider: list[str] | None = Field(default=None, description="zero or more risk providers - zero means all. Supported values: <ul><li>S for Falcon sensor</li><li>See RiskProvider for all values.</li></ul>"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Performs a combined query and get operation for retrieving RiskSupportedEvaluation entities."""
        return self._call(operation="combinedSupportedEvaluationExt", query_params={"after": after, "offset": offset, "limit": limit, "sort": sort, "filter": filter, "risk_provider": risk_provider}, error_message="combinedSupportedEvaluationExt failed", member_cid=member_cid)

    def get_evaluation_logic(
        self,
        ids: list[str] = Field(description="One or more evaluation logic IDs."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get details on evaluation logic items by providing one or more IDs."""
        return self._call(operation="getEvaluationLogic", query_params={"ids": ids}, error_message="getEvaluationLogic failed", member_cid=member_cid)

    def query_evaluation_logic(
        self,
        filter: str = Field(description="FQL query specifying the filter parameters."),
        after: str | None = Field(default=None, description="A pagination token used with the limit parameter to manage pagination of results. On your first request, don't provide an after token. On subsequent requests, provide the after token from the previous response to continue from that place in the results."),
        limit: int | None = Field(default=None, description="Maximum number of entities to return."),
        sort: str | None = Field(default=None, description="Sort evaluation logic by their properties."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for evaluation logic in your environment by providing a FQL filter and paging details. Returns a set of evaluation logic IDs which match the filter criteria."""
        return self._call(operation="queryEvaluationLogic", query_params={"after": after, "limit": limit, "filter": filter, "sort": sort}, error_message="queryEvaluationLogic failed", member_cid=member_cid)
