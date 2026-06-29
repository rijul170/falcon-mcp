"""
Threat Graph module for Falcon MCP Server.

Provides targeted Threat Graph queries: edge listings, vertex hydration, vertex
summaries, and ran-on indicator pivots. Path-parameter `vertex_type` is passed as
a separate kwarg so falconpy's scrub_target substitutes it into the endpoint URL.
"""

from typing import Any

from mcp.server import FastMCP
from mcp.server.fastmcp.resources import TextResource
from pydantic import AnyUrl, Field

from falcon_mcp.common.errors import _format_error_response, handle_api_response
from falcon_mcp.common.logging import get_logger
from falcon_mcp.common.utils import prepare_api_parameters
from falcon_mcp.modules.base import BaseModule
from falcon_mcp.resources.threat_graph import THREAT_GRAPH_GUIDE

logger = get_logger(__name__)

# Subset of the most common Threat Graph vertex types. The full list is large
# (process, file, ipv4, ipv6, domain, hash, indicator, incident, etc.); users can
# pass any string the API accepts.
VERTEX_TYPES_HINT = (
    "Examples: 'device', 'process', 'file', 'ipv4', 'ipv6', 'domain', "
    "'hash_sha256', 'indicator', 'incident', 'detection', 'any-vertex'."
)
EDGE_DIRECTIONS = ("in", "out", "both")
SCOPES = ("device", "customer", "global", "cspm", "cwpp")


class ThreatGraphModule(BaseModule):
    """Module for CrowdStrike Threat Graph queries."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.list_threat_graph_edge_types, name="list_threat_graph_edge_types")
        self._add_tool(server=server, method=self.get_threat_graph_edges, name="get_threat_graph_edges")
        self._add_tool(server=server, method=self.get_threat_graph_vertices, name="get_threat_graph_vertices")
        self._add_tool(server=server, method=self.get_threat_graph_summary, name="get_threat_graph_summary")
        self._add_tool(server=server, method=self.get_threat_graph_ran_on, name="get_threat_graph_ran_on")

    def register_resources(self, server: FastMCP) -> None:
        self._add_resource(server, TextResource(
            uri=AnyUrl("falcon://threat-graph/guide"),
            name="falcon_threat_graph_guide",
            description="Vertex types, edge types, and scopes reference for Threat Graph.",
            text=THREAT_GRAPH_GUIDE,
        ))

    def list_threat_graph_edge_types(self) -> list[dict[str, Any]] | dict[str, Any]:
        """List the edge types available for use with `get_threat_graph_edges`."""
        result = self._base_search_api_call(
            operation="queries_edgetypes_get",
            search_params={},
            error_message="Failed to list edge types",
        )
        if self._is_error(result):
            return [result]
        return result

    def get_threat_graph_edges(
        self,
        ids: str = Field(description="Vertex ID to fetch edges for (single ID supported)."),
        edge_type: str = Field(description="Edge type. Use `list_threat_graph_edge_types` to enumerate."),
        direction: str = Field(default="both", description="'in', 'out', or 'both'."),
        scope: str | None = Field(default=None, description="Scope: 'device', 'customer', 'global', 'cspm', 'cwpp'."),
        limit: int = Field(default=10, ge=1, le=100, description="Max edges to return."),
        offset: str | None = Field(default=None, description="Pagination token."),
        nano: bool = Field(default=False, description="Use nano-precision timestamps."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Fetch edges for a vertex from Threat Graph."""
        if direction not in EDGE_DIRECTIONS:
            return [_format_error_response(
                f"`direction` must be one of {EDGE_DIRECTIONS}.",
                operation="combined_edges_get",
            )]
        if scope is not None and scope not in SCOPES:
            return [_format_error_response(
                f"`scope` must be one of {SCOPES}.",
                operation="combined_edges_get",
            )]
        result = self._base_search_api_call(
            operation="combined_edges_get",
            search_params={
                "ids": ids, "edge_type": edge_type, "direction": direction,
                "scope": scope, "limit": limit, "offset": offset, "nano": nano,
            },
            error_message="Failed to fetch threat graph edges",
        )
        if self._is_error(result):
            return [result]
        return result

    def get_threat_graph_vertices(
        self,
        vertex_type: str = Field(
            description=f"Vertex type (path parameter). {VERTEX_TYPES_HINT}",
        ),
        ids: list[str] = Field(description="Vertex IDs to retrieve metadata for."),
        scope: str | None = Field(default=None, description="Scope: 'device', 'customer', 'global', 'cspm', 'cwpp'."),
        nano: bool = Field(default=False, description="Use nano-precision timestamps."),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID to scope this call to a specific child tenant. Leave unset to use the parent account scope.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get full metadata for vertices of a given type (V2 endpoint)."""
        if not ids:
            return []
        if scope is not None and scope not in SCOPES:
            return [_format_error_response(
                f"`scope` must be one of {SCOPES}.",
                operation="entities_vertices_getv2",
            )]
        # Path param `vertex_type` must be passed as a kwarg, not inside parameters,
        # so falconpy's scrub_target can substitute the URL placeholder.
        params = prepare_api_parameters({"ids": ids, "scope": scope, "nano": nano})
        response = self.client.command_for(
            "entities_vertices_getv2", member_cid=member_cid, parameters=params, vertex_type=vertex_type,
        )
        return handle_api_response(
            response, operation="entities_vertices_getv2",
            error_message="Failed to fetch threat graph vertices", default_result=[],
        )

    def get_threat_graph_summary(
        self,
        vertex_type: str = Field(
            description=f"Vertex type (path parameter). {VERTEX_TYPES_HINT}",
        ),
        ids: list[str] = Field(description="Vertex IDs to summarize."),
        scope: str | None = Field(default=None, description="Scope: 'device', 'customer', 'global', 'cspm', 'cwpp'."),
        nano: bool = Field(default=False, description="Use nano-precision timestamps."),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID to scope this call to a specific child tenant. Leave unset to use the parent account scope.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get a brief summary for vertices of a given type."""
        if not ids:
            return []
        if scope is not None and scope not in SCOPES:
            return [_format_error_response(
                f"`scope` must be one of {SCOPES}.",
                operation="combined_summary_get",
            )]
        params = prepare_api_parameters({"ids": ids, "scope": scope, "nano": nano})
        response = self.client.command_for(
            "combined_summary_get", member_cid=member_cid, parameters=params, vertex_type=vertex_type,
        )
        return handle_api_response(
            response, operation="combined_summary_get",
            error_message="Failed to fetch threat graph summary", default_result=[],
        )

    def get_threat_graph_ran_on(
        self,
        value: str = Field(description="Indicator value (e.g. SHA256, IP, domain)."),
        type: str = Field(
            description="Indicator type (e.g. 'sha256', 'ipv4', 'ipv6', 'domain', 'md5').",
        ),
        limit: int = Field(default=10, ge=1, le=100, description="Max edges to return."),
        offset: str | None = Field(default=None, description="Pagination token."),
        nano: bool = Field(default=False, description="Use nano-precision timestamps."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List devices an indicator (hash, IP, domain) ran on."""
        result = self._base_search_api_call(
            operation="combined_ran_on_get",
            search_params={
                "value": value, "type": type, "limit": limit,
                "offset": offset, "nano": nano,
            },
            error_message="Failed to fetch threat graph ran-on data",
        )
        if self._is_error(result):
            return [result]
        return result
