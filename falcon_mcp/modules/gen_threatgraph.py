"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `threatgraph` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenThreatgraphModule(GeneratedModuleBase):
    """Generated tools for the Falcon `threatgraph` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.entities_vertices_get, name="entities_vertices_get")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def entities_vertices_get(
        self,
        vertex_type: str = Field(description="`vertex_type` path parameter (required)."),
        ids: list[str] = Field(description="Vertex ID to get details for"),
        scope: str | None = Field(default=None, description="Scope of the request"),
        nano: bool | None = Field(default=None, description="Return nano-precision entity timestamps"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve metadata for a given vertex ID. Note: This is a legacy endpoint used by CrowdStrike Store partners prior to release of the ThreatGraph OAuth 2.0 APIs. If you’re not currently using this endpoint, use the /v2 endpoint instead."""
        return self._call(operation="entities_vertices_get", query_params={"ids": ids, "scope": scope, "nano": nano}, path_params={"vertex_type": vertex_type}, error_message="entities_vertices_get failed", member_cid=member_cid)
