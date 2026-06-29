"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `faas_execution` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenFaasExecutionModule(GeneratedModuleBase):
    """Generated tools for the Falcon `faas_execution` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.read_request_body, name="read_request_body")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def read_request_body(
        self,
        id: str = Field(description="Execution ID"),
        fn: str = Field(description="function ref; form of $fn_id:$fn_version"),
        filename: str = Field(description="filename to be retrieved"),
        sha256: str = Field(description="sha256 checksum for file to be retrieved"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """retrieve a large request body, such as a file, that has spilled into object storage"""
        return self._call(operation="ReadRequestBody", query_params={"id": id, "fn": fn, "filename": filename, "sha256": sha256}, error_message="ReadRequestBody failed", member_cid=member_cid)
