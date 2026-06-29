"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `serverless_exports` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenServerlessExportsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `serverless_exports` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.download_export_file_mixin0, name="download_export_file_mixin0")
        self._add_tool(server=server, method=self.query_export_jobs_mixin0, name="query_export_jobs_mixin0")
        self._add_tool(server=server, method=self.read_export_jobs_mixin0, name="read_export_jobs_mixin0")
        self._add_tool(server=server, method=self.launch_export_job_mixin0, name="launch_export_job_mixin0", annotations=WRITE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def download_export_file_mixin0(
        self,
        id: str = Field(description="Export job ID."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Download an export file"""
        return self._call(operation="DownloadExportFileMixin0", query_params={"id": id}, error_message="DownloadExportFileMixin0 failed", member_cid=member_cid)

    def launch_export_job_mixin0(
        self,
        body: dict = Field(description="Request JSON body for `LaunchExportJobMixin0` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Launch an export job of a Lambda Security resource. Maximum of 1 job in progress per resource. Use expand_vulnerabilities=true to get detailed vulnerability information."""
        return self._call(operation="LaunchExportJobMixin0", query_params=None, body_params=body, error_message="LaunchExportJobMixin0 failed", member_cid=member_cid)

    def query_export_jobs_mixin0(
        self,
        filter: str | None = Field(default=None, description="Filter exports using a query in Falcon Query Language (FQL). Only the last 100 jobs are returned. Supported filter fields: resource status"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Query export jobs entities"""
        return self._call(operation="QueryExportJobsMixin0", query_params={"filter": filter}, error_message="QueryExportJobsMixin0 failed", member_cid=member_cid)

    def read_export_jobs_mixin0(
        self,
        ids: list[str] = Field(description="Export Job IDs to read. Allowed up to 100 IDs per request."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Read export jobs entities"""
        return self._call(operation="ReadExportJobsMixin0", query_params={"ids": ids}, error_message="ReadExportJobsMixin0 failed", member_cid=member_cid)
