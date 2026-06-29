"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `downloads` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenDownloadsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `downloads` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.download_file, name="download_file")
        self._add_tool(server=server, method=self.enumerate_file, name="enumerate_file")
        self._add_tool(server=server, method=self.fetch_files_download_info_v2, name="fetch_files_download_info_v2")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def download_file(
        self,
        file_name: str = Field(description="Name of the file to be downloaded"),
        file_version: str = Field(description="Version of the file to be downloaded"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Gets pre-signed URL for the file"""
        return self._call(operation="DownloadFile", query_params={"file_name": file_name, "file_version": file_version}, error_message="DownloadFile failed", member_cid=member_cid)

    def enumerate_file(
        self,
        file_name: str | None = Field(default=None, description="Apply filtering on file name"),
        file_version: str | None = Field(default=None, description="Apply filtering on file version"),
        platform: str | None = Field(default=None, description="Apply filtering on file platform"),
        os: str | None = Field(default=None, description="Apply filtering on operating system"),
        arch: str | None = Field(default=None, description="Apply filtering on architecture"),
        category: str | None = Field(default=None, description="Apply filtering on file category"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Enumerates a list of files available for CID"""
        return self._call(operation="EnumerateFile", query_params={"file_name": file_name, "file_version": file_version, "platform": platform, "os": os, "arch": arch, "category": category}, error_message="EnumerateFile failed", member_cid=member_cid)

    def fetch_files_download_info_v2(
        self,
        filter: str | None = Field(default=None, description="Search files using various filters. Supported filters: arch,category,file_name,file_version,os"),
        sort: str | None = Field(default=None, description="The fields to sort records on. Supported columns: arch category file_name file_version os"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 1000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get cloud security tools info and pre-signed download URLs"""
        return self._call(operation="FetchFilesDownloadInfoV2", query_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset}, error_message="FetchFilesDownloadInfoV2 failed", member_cid=member_cid)
