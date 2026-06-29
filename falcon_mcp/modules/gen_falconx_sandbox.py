"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `falconx_sandbox` API service collection."""

import os

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.errors import handle_api_response
from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenFalconxSandboxModule(GeneratedModuleBase):
    """Generated tools for the Falcon `falconx_sandbox` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_artifacts, name="get_artifacts")
        self._add_tool(server=server, method=self.get_memory_dump, name="get_memory_dump")
        self._add_tool(server=server, method=self.get_memory_dump_extracted_strings, name="get_memory_dump_extracted_strings")
        self._add_tool(server=server, method=self.get_memory_dump_hex_dump, name="get_memory_dump_hex_dump")
        self._add_tool(server=server, method=self.get_sample_v2, name="get_sample_v2")
        self._add_tool(server=server, method=self.get_submissions, name="get_submissions")
        self._add_tool(server=server, method=self.query_sample_v1, name="query_sample_v1")
        self._add_tool(server=server, method=self.query_submissions, name="query_submissions")
        self._add_tool(server=server, method=self.upload_sample_v2, name="upload_sample_v2", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_report, name="delete_report", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_sample_v2, name="delete_sample_v2", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def upload_sample_v2(
        self,
        file_path: str = Field(description="Absolute path to the local file to upload for sandbox analysis (e.g. '/tmp/malware.exe'). Supports PE executables, scripts, Office docs, PDFs."),
        file_name: str | None = Field(default=None, description="Filename to register. Defaults to the basename of file_path."),
        is_confidential: bool = Field(default=True, description="When True (default), prevents distribution to third-party services. Set False to allow CrowdStrike intelligence sharing."),
        comment: str | None = Field(default=None, description="Analyst comment describing the sample origin or context."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Upload a file to the sandbox sample store (POST /samples/entities/samples/v2).

        Use the returned SHA256 with submit_sandbox_analysis to detonate. This v2 endpoint is
        specific to the FalconX sandbox collection; prefer upload_sample_v3 in gen_sample_uploads
        for general sample store operations. Requires: Sample Uploads: WRITE scope.
        """
        expanded = os.path.expanduser(file_path)
        if not os.path.isfile(expanded):
            return {"status_code": 400, "errors": [{"message": f"File not found: {file_path}"}]}
        name = file_name or os.path.basename(expanded)
        try:
            with open(expanded, "rb") as fh:
                content = fh.read()
        except OSError as exc:
            return {"status_code": 400, "errors": [{"message": f"Cannot read file: {exc}"}]}
        form_data = {"file_name": name}
        if comment:
            form_data["comment"] = comment
        if is_confidential is not None:
            form_data["is_confidential"] = is_confidential
        response = self.client.command_for(
            "UploadSampleV2",
            member_cid=member_cid,
            files=[("sample", (name, content, "application/octet-stream"))],
            data=form_data,
        )
        return handle_api_response(response, operation="UploadSampleV2", error_message="UploadSampleV2 failed")

    def delete_report(
        self,
        ids: str = Field(description="ID of a report."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete report based on the report ID. Operation can be checked for success by polling for the report ID on the report-summaries endpoint."""
        return self._call(operation="DeleteReport", query_params={"ids": ids}, error_message="DeleteReport failed", member_cid=member_cid)

    def delete_sample_v2(
        self,
        ids: str = Field(description="The file SHA256."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Removes a sample, including file, meta and submissions from the collection"""
        return self._call(operation="DeleteSampleV2", query_params={"ids": ids}, error_message="DeleteSampleV2 failed", member_cid=member_cid)

    def get_artifacts(
        self,
        id: str = Field(description="ID of an artifact, such as an IOC pack, PCAP file, memory dump, or actor image. Find an artifact ID in a report or summary."),
        name: str | None = Field(default=None, description="The name given to your downloaded file."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Download IOC packs, PCAP files, memory dumps, and other analysis artifacts."""
        return self._call(operation="GetArtifacts", query_params={"id": id, "name": name}, error_message="GetArtifacts failed", member_cid=member_cid)

    def get_memory_dump(
        self,
        id: str = Field(description="Memory dump id"),
        name: str | None = Field(default=None, description="The name given to your downloaded file."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get memory dump content, as binary"""
        return self._call(operation="GetMemoryDump", query_params={"id": id, "name": name}, error_message="GetMemoryDump failed", member_cid=member_cid)

    def get_memory_dump_extracted_strings(
        self,
        id: str = Field(description="Extracted strings id"),
        name: str | None = Field(default=None, description="The name given to your downloaded file."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get extracted strings from a memory dump"""
        return self._call(operation="GetMemoryDumpExtractedStrings", query_params={"id": id, "name": name}, error_message="GetMemoryDumpExtractedStrings failed", member_cid=member_cid)

    def get_memory_dump_hex_dump(
        self,
        id: str = Field(description="Hex dump id"),
        name: str | None = Field(default=None, description="The name given to your downloaded file."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get hex view of a memory dump"""
        return self._call(operation="GetMemoryDumpHexDump", query_params={"id": id, "name": name}, error_message="GetMemoryDumpHexDump failed", member_cid=member_cid)

    def get_sample_v2(
        self,
        ids: str = Field(description="The file SHA256."),
        password_protected: bool | None = Field(default=None, description="Flag whether the sample should be zipped and password protected with pass='infected'"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves the file associated with the given ID (SHA256)"""
        return self._call(operation="GetSampleV2", query_params={"ids": ids, "password_protected": password_protected}, error_message="GetSampleV2 failed", member_cid=member_cid)

    def get_submissions(
        self,
        ids: list[str] = Field(description="ID of a submitted malware sample. Find a submission ID from the response when submitting a malware sample or search with /falconx/queries/submissions/v1."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Check the status of a sandbox analysis. Time required for analysis varies but is usually less than 15 minutes."""
        return self._call(operation="GetSubmissions", query_params={"ids": ids}, error_message="GetSubmissions failed", member_cid=member_cid)

    def query_sample_v1(
        self,
        body: dict = Field(description="Request JSON body for `QuerySampleV1` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves a list with sha256 of samples that exist and customer has rights to access them, maximum number of accepted items is 200"""
        return self._call(operation="QuerySampleV1", query_params=None, body_params=body, error_message="QuerySampleV1 failed", member_cid=member_cid)

    def query_submissions(
        self,
        filter: str | None = Field(default=None, description="Optional filter and sort criteria in the form of an FQL query. For more information about FQL queries, see [our FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide)."),
        offset: str | None = Field(default=None, description="The offset to start retrieving submissions from."),
        limit: int | None = Field(default=None, description="Maximum number of submission IDs to return. Max: 5000."),
        sort: str | None = Field(default=None, description="Sort order: asc or desc."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Find submission IDs for uploaded files by providing an FQL filter and paging details. Returns a set of submission IDs that match your criteria."""
        return self._call(operation="QuerySubmissions", query_params={"filter": filter, "offset": offset, "limit": limit, "sort": sort}, error_message="QuerySubmissions failed", member_cid=member_cid)
