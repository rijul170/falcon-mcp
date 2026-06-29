"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `quick_scan_pro` API service collection."""

import os

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.errors import handle_api_response
from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenQuickScanProModule(GeneratedModuleBase):
    """Generated tools for the Falcon `quick_scan_pro` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_scan_result, name="get_scan_result")
        self._add_tool(server=server, method=self.query_scan_results, name="query_scan_results")
        self._add_tool(server=server, method=self.upload_file_quick_scan_pro, name="upload_file_quick_scan_pro", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.launch_scan, name="launch_scan", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_file, name="delete_file", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_scan_result, name="delete_scan_result", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def upload_file_quick_scan_pro(
        self,
        file_path: str = Field(description="Absolute path to the local file to upload for QuickScan Pro analysis (e.g. '/tmp/suspicious.exe'). Supports PE, Office docs, PDFs, scripts and more."),
        file_name: str | None = Field(default=None, description="Filename to register. Defaults to the basename of file_path."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Upload a file for QuickScan Pro (POST /quickscanpro/entities/files/v1).

        Required first step before launch_scan. Returns a file ID (SHA256) to pass
        to launch_scan. Requires: QuickScan Pro: WRITE scope.
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
        response = self.client.command_for(
            "UploadFileQuickScanPro",
            member_cid=member_cid,
            files=[("file", (name, content, "application/octet-stream"))],
            data={"file_name": name},
        )
        return handle_api_response(response, operation="UploadFileQuickScanPro", error_message="UploadFileQuickScanPro failed")

    def delete_file(
        self,
        ids: list[str] = Field(description="File's SHA256"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deletes file by its sha256 identifier."""
        return self._call(operation="DeleteFile", query_params={"ids": ids}, error_message="DeleteFile failed", member_cid=member_cid)

    def delete_scan_result(
        self,
        ids: list[str] = Field(description="Scan job IDs previously created by LaunchScan"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deletes the result of an QuickScan Pro scan."""
        return self._call(operation="DeleteScanResult", query_params={"ids": ids}, error_message="DeleteScanResult failed", member_cid=member_cid)

    def get_scan_result(
        self,
        ids: list[str] = Field(description="Scan job IDs previously created by LaunchScan"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Gets the result of an QuickScan Pro scan."""
        return self._call(operation="GetScanResult", query_params={"ids": ids}, error_message="GetScanResult failed", member_cid=member_cid)

    def launch_scan(
        self,
        body: dict = Field(description="Request JSON body for `LaunchScan` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Starts scanning a file uploaded through '/quickscanpro/entities/files/v1'."""
        return self._call(operation="LaunchScan", query_params=None, body_params=body, error_message="LaunchScan failed", member_cid=member_cid)

    def query_scan_results(
        self,
        filter: str = Field(description="Empty value means to not filter on anything Available filter fields that supports match (~): _all, mitre_attacks.description Available filter fields that supports exact match: cid,sha256,id,s tatus,type,entity,executor,verdict,verdict_reason,verdict_source,file_size,file_type_short,artifacts.file_arti facts.sha256,artifacts.file_artifacts.filename,artifacts.file_artifacts.verdict,artifacts.file_artifacts.verdi ct_reasons,artifacts.url_artifacts.url,artifacts.url_artifacts.verdict,artifacts.url_artifacts.verdict_reasons ,mitre_attacks.attack_id,mitre_attacks.attack_id_wiki,mitre_attacks.tactic,mitre_attacks.technique,mitre_attac ks.capec_id,mitre_attacks.parent.attack_id,mitre_attacks.parent.attack_id_wiki,mitre_attacks.parent.technique Available filter fields that supports wildcard (*): mitre_attacks.description Available filter fields that supports range comparisons (>, <, >=, <=): created_timestamp, updated_timestamp, file_size All filter fields and operations supports negation (!). _all field is used to search between all fields."),
        offset: int | None = Field(default=None, description="The offset to start retrieving ids from."),
        limit: int | None = Field(default=None, description="Maximum number of IDs to return. Max: 5000."),
        sort: str | None = Field(default=None, description="Sort order: asc or desc. Sort supported fields created_timestamp"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """FQL query specifying the filter parameters"""
        return self._call(operation="QueryScanResults", query_params={"filter": filter, "offset": offset, "limit": limit, "sort": sort}, error_message="QueryScanResults failed", member_cid=member_cid)
