"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `foundry_logscale` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenFoundryLogscaleModule(GeneratedModuleBase):
    """Generated tools for the Falcon `foundry_logscale` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_saved_searches_execute_v1, name="get_saved_searches_execute_v1")
        self._add_tool(server=server, method=self.get_saved_searches_job_results_download_v1, name="get_saved_searches_job_results_download_v1")
        self._add_tool(server=server, method=self.list_repos_v1, name="list_repos_v1")
        self._add_tool(server=server, method=self.list_view_v1, name="list_view_v1")
        self._add_tool(server=server, method=self.create_saved_searches_ingest_v1, name="create_saved_searches_ingest_v1", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.create_saved_searches_dynamic_execute_v1, name="create_saved_searches_dynamic_execute_v1", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.create_saved_searches_execute_v1, name="create_saved_searches_execute_v1", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def create_saved_searches_dynamic_execute_v1(
        self,
        body: dict = Field(description="Request JSON body for `CreateSavedSearchesDynamicExecuteV1` per the CrowdStrike API schema (required)."),
        app_id: str | None = Field(default=None, description="Application ID."),
        include_schema_generation: bool | None = Field(default=None, description="Include generated schemas in the response"),
        include_test_data: bool | None = Field(default=None, description="Include test data when executing searches"),
        infer_json_types: bool | None = Field(default=None, description="Whether to try to infer data types in json event response instead of returning map[string]string"),
        match_response_schema: bool | None = Field(default=None, description="Whether to validate search results against their schema"),
        metadata: bool | None = Field(default=None, description="Whether to include metadata in the response"),
        mode: str | None = Field(default=None, description="Mode to execute the query under."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Execute a dynamic saved search"""
        return self._call(operation="CreateSavedSearchesDynamicExecuteV1", query_params={"app_id": app_id, "include_schema_generation": include_schema_generation, "include_test_data": include_test_data, "infer_json_types": infer_json_types, "match_response_schema": match_response_schema, "metadata": metadata, "mode": mode}, body_params=body, error_message="CreateSavedSearchesDynamicExecuteV1 failed", member_cid=member_cid)

    def create_saved_searches_execute_v1(
        self,
        body: dict = Field(description="Request JSON body for `CreateSavedSearchesExecuteV1` per the CrowdStrike API schema (required)."),
        app_id: str | None = Field(default=None, description="Application ID."),
        detailed: bool | None = Field(default=None, description="Whether to include search field details"),
        include_test_data: bool | None = Field(default=None, description="Include test data when executing searches"),
        infer_json_types: bool | None = Field(default=None, description="Whether to try to infer data types in json event response instead of returning map[string]string"),
        match_response_schema: bool | None = Field(default=None, description="Whether to validate search results against their schema"),
        metadata: bool | None = Field(default=None, description="Whether to include metadata in the response"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Execute a saved search"""
        return self._call(operation="CreateSavedSearchesExecuteV1", query_params={"app_id": app_id, "detailed": detailed, "include_test_data": include_test_data, "infer_json_types": infer_json_types, "match_response_schema": match_response_schema, "metadata": metadata}, body_params=body, error_message="CreateSavedSearchesExecuteV1 failed", member_cid=member_cid)

    def create_saved_searches_ingest_v1(
        self,
        app_id: str | None = Field(default=None, description="Application ID."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Populate a saved search"""
        return self._call(operation="CreateSavedSearchesIngestV1", query_params={"app_id": app_id}, error_message="CreateSavedSearchesIngestV1 failed", member_cid=member_cid)

    def get_saved_searches_execute_v1(
        self,
        job_id: str = Field(description="Job ID for a previously executed async query"),
        app_id: str | None = Field(default=None, description="Application ID."),
        infer_json_types: bool | None = Field(default=None, description="Whether to try to infer data types in json event response instead of returning map[string]string"),
        job_status_only: bool | None = Field(default=None, description="If set to true, result rows are dropped from the response and only the job status is returned"),
        limit: str | None = Field(default=None, description="Maximum number of records to return."),
        match_response_schema: bool | None = Field(default=None, description="Whether to validate search results against their schema"),
        metadata: bool | None = Field(default=None, description="Whether to include metadata in the response"),
        offset: str | None = Field(default=None, description="Starting pagination offset of records to return."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get the results of a saved search"""
        return self._call(operation="GetSavedSearchesExecuteV1", query_params={"job_id": job_id, "app_id": app_id, "infer_json_types": infer_json_types, "job_status_only": job_status_only, "limit": limit, "match_response_schema": match_response_schema, "metadata": metadata, "offset": offset}, error_message="GetSavedSearchesExecuteV1 failed", member_cid=member_cid)

    def get_saved_searches_job_results_download_v1(
        self,
        job_id: str = Field(description="Job ID for a previously executed async query"),
        infer_json_types: bool | None = Field(default=None, description="Whether to try to infer data types in json event response instead of returning map[string]string"),
        result_format: str | None = Field(default=None, description="Result Format"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get the results of a saved search as a file"""
        return self._call(operation="GetSavedSearchesJobResultsDownloadV1", query_params={"job_id": job_id, "infer_json_types": infer_json_types, "result_format": result_format}, error_message="GetSavedSearchesJobResultsDownloadV1 failed", member_cid=member_cid)

    def list_repos_v1(
        self,
        check_test_data: bool | None = Field(default=None, description="Include whether test data is present in the application repository"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Lists available repositories and views"""
        return self._call(operation="ListReposV1", query_params={"check_test_data": check_test_data}, error_message="ListReposV1 failed", member_cid=member_cid)

    def list_view_v1(
        self,
        check_test_data: bool | None = Field(default=None, description="Include whether test data is present in the application repository"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """List views"""
        return self._call(operation="ListViewV1", query_params={"check_test_data": check_test_data}, error_message="ListViewV1 failed", member_cid=member_cid)
