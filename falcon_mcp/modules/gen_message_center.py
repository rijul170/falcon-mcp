"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `message_center` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenMessageCenterModule(GeneratedModuleBase):
    """Generated tools for the Falcon `message_center` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.case_download_attachment, name="case_download_attachment")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def case_download_attachment(
        self,
        id: str = Field(description="attachment ID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """retrieves an attachment for the case, given the attachment id"""
        return self._call(operation="CaseDownloadAttachment", query_params={"id": id}, error_message="CaseDownloadAttachment failed", member_cid=member_cid)
