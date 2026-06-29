"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `sample_uploads` API service collection."""

import os
from typing import Any

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.errors import handle_api_response
from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenSampleUploadsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `sample_uploads` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.archive_get_v1, name="archive_get_v1")
        self._add_tool(server=server, method=self.archive_list_v1, name="archive_list_v1")
        self._add_tool(server=server, method=self.extraction_get_v1, name="extraction_get_v1")
        self._add_tool(server=server, method=self.extraction_list_v1, name="extraction_list_v1")
        self._add_tool(server=server, method=self.get_sample_v3, name="get_sample_v3")
        self._add_tool(server=server, method=self.upload_sample_v3, name="upload_sample_v3", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.archive_upload_v2, name="archive_upload_v2", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.extraction_create_v1, name="extraction_create_v1", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.archive_delete_v1, name="archive_delete_v1", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_sample_v3, name="delete_sample_v3", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def upload_sample_v3(
        self,
        file_path: str = Field(description="Absolute path to the local file to upload (e.g. '/tmp/malware.exe'). Accepts executables, Office docs, PDFs, scripts, ELF binaries, and more."),
        file_name: str | None = Field(default=None, description="Filename to register in the Sample Store. Defaults to the basename of file_path."),
        is_confidential: bool = Field(default=True, description="When True (default), prevents distribution to third-party threat intelligence services. Set False to allow CrowdStrike intelligence sharing."),
        comment: str | None = Field(default=None, description="Analyst comment describing origin or context of the sample."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Upload a file to the CrowdStrike Sample Store (POST /samples/entities/samples/v3).

        This is the required first step before sandbox detonation (submit_sandbox_analysis)
        or ML quick-scan (scan_samples). Returns a SHA256 identifier for the uploaded sample.
        Requires: Sample Uploads: WRITE scope. Max file size 256 MB.
        """
        expanded = os.path.expanduser(file_path)
        if not os.path.isfile(expanded):
            return {"status_code": 400, "errors": [{"message": f"File not found: {file_path}"}]}
        name = file_name or os.path.basename(expanded)
        try:
            with open(expanded, "rb") as fh:
                content: bytes = fh.read()
        except OSError as exc:
            return {"status_code": 400, "errors": [{"message": f"Cannot read file: {exc}"}]}
        form_data: dict[str, Any] = {"file_name": name}
        if comment:
            form_data["comment"] = comment
        if is_confidential is not None:
            form_data["is_confidential"] = is_confidential
        response = self.client.command_for(
            "UploadSampleV3",
            member_cid=member_cid,
            files=[("sample", (name, content, "application/octet-stream"))],
            data=form_data,
        )
        return handle_api_response(response, operation="UploadSampleV3", error_message="UploadSampleV3 failed")

    def archive_upload_v2(
        self,
        file_path: str = Field(description="Absolute path to the local archive file to upload (ZIP, 7z, or RAR). Password-protected archives must use the password 'infected'."),
        name: str | None = Field(default=None, description="Archive filename to register. Defaults to the basename of file_path."),
        is_confidential: bool = Field(default=True, description="When True (default), prevents distribution to third-party threat intelligence. Set False to allow CrowdStrike intelligence sharing."),
        comment: str | None = Field(default=None, description="Analyst comment describing the archive origin or context."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Upload an archive file to the Sample Store (POST /archives/entities/archives/v2).

        Use archive_get_v1 to poll status until 'done', then extraction_create_v1 to unpack
        individual files for analysis. Requires: Sample Uploads: WRITE scope.
        """
        expanded = os.path.expanduser(file_path)
        if not os.path.isfile(expanded):
            return {"status_code": 400, "errors": [{"message": f"File not found: {file_path}"}]}
        archive_name = name or os.path.basename(expanded)
        try:
            with open(expanded, "rb") as fh:
                content = fh.read()
        except OSError as exc:
            return {"status_code": 400, "errors": [{"message": f"Cannot read file: {exc}"}]}
        form_data: dict[str, Any] = {"name": archive_name}
        if comment:
            form_data["comment"] = comment
        if is_confidential is not None:
            form_data["is_confidential"] = is_confidential
        response = self.client.command_for(
            "ArchiveUploadV2",
            member_cid=member_cid,
            files=[("file", (archive_name, content, "application/octet-stream"))],
            data=form_data,
        )
        return handle_api_response(response, operation="ArchiveUploadV2", error_message="ArchiveUploadV2 failed")

    def archive_delete_v1(
        self,
        id: str = Field(description="The archive SHA256."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete an archive that was uploaded previously"""
        return self._call(operation="ArchiveDeleteV1", query_params={"id": id}, error_message="ArchiveDeleteV1 failed", member_cid=member_cid)

    def archive_get_v1(
        self,
        id: str = Field(description="The archive SHA256."),
        include_files: bool | None = Field(default=None, description="If true includes processed archive files in response."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves the archives upload operation statuses. Status `done` means that archive was processed successfully. Status `error` means that archive was not processed successfully."""
        return self._call(operation="ArchiveGetV1", query_params={"id": id, "include_files": include_files}, error_message="ArchiveGetV1 failed", member_cid=member_cid)

    def archive_list_v1(
        self,
        id: str = Field(description="The archive SHA256."),
        limit: int | None = Field(default=None, description="Max number of files to retrieve."),
        offset: str | None = Field(default=None, description="Offset from where to get files."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves the archives files in chunks."""
        return self._call(operation="ArchiveListV1", query_params={"id": id, "limit": limit, "offset": offset}, error_message="ArchiveListV1 failed", member_cid=member_cid)

    def delete_sample_v3(
        self,
        ids: str = Field(description="The file SHA256."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Removes a sample, including file, meta and submissions from the collection"""
        return self._call(operation="DeleteSampleV3", query_params={"ids": ids}, error_message="DeleteSampleV3 failed", member_cid=member_cid)

    def extraction_create_v1(
        self,
        body: dict = Field(description="Request JSON body for `ExtractionCreateV1` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Extracts files from an uploaded archive and copies them to internal storage making it available for content analysis."""
        return self._call(operation="ExtractionCreateV1", query_params=None, body_params=body, error_message="ExtractionCreateV1 failed", member_cid=member_cid)

    def extraction_get_v1(
        self,
        id: str = Field(description="The extraction operation ID."),
        include_files: bool | None = Field(default=None, description="If true includes processed archive files in response."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves the files extraction operation statuses. Status `done` means that all files were processed successfully. Status `error` means that at least one of the file could not be processed."""
        return self._call(operation="ExtractionGetV1", query_params={"id": id, "include_files": include_files}, error_message="ExtractionGetV1 failed", member_cid=member_cid)

    def extraction_list_v1(
        self,
        id: str = Field(description="The extraction operation ID."),
        limit: int | None = Field(default=None, description="Max number of file extractions to retrieve."),
        offset: str | None = Field(default=None, description="Offset from where to get file extractions."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves the files extractions in chunks. Status `done` means that all files were processed successfully. Status `error` means that at least one of the file could not be processed."""
        return self._call(operation="ExtractionListV1", query_params={"id": id, "limit": limit, "offset": offset}, error_message="ExtractionListV1 failed", member_cid=member_cid)

    def get_sample_v3(
        self,
        ids: str = Field(description="The file SHA256."),
        password_protected: bool | None = Field(default=None, description="Flag whether the sample should be zipped and password protected with pass='infected'"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves the file associated with the given ID (SHA256)"""
        return self._call(operation="GetSampleV3", query_params={"ids": ids, "password_protected": password_protected}, error_message="GetSampleV3 failed", member_cid=member_cid)
