"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `api_integrations` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenApiIntegrationsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `api_integrations` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_combined_plugin_configs, name="get_combined_plugin_configs")
        self._add_tool(server=server, method=self.execute_command, name="execute_command", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.execute_command_proxy, name="execute_command_proxy", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def execute_command(
        self,
        body: dict = Field(description="Request JSON body for `ExecuteCommand` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Execute a command."""
        return self._call(operation="ExecuteCommand", query_params=None, body_params=body, error_message="ExecuteCommand failed", member_cid=member_cid)

    def execute_command_proxy(
        self,
        body: dict = Field(description="Request JSON body for `ExecuteCommandProxy` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Execute a command and proxy the response directly."""
        return self._call(operation="ExecuteCommandProxy", query_params=None, body_params=body, error_message="ExecuteCommandProxy failed", member_cid=member_cid)

    def get_combined_plugin_configs(
        self,
        filter: str | None = Field(default=None, description="Filter items using a query in Falcon Query Language (FQL)."),
        limit: int | None = Field(default=None, description="The number of items to return in this response (default: 100, max: 500). Use with the offset parameter to manage pagination of results."),
        offset: int | None = Field(default=None, description="The first item to return, where 0 is the latest item. Use with the limit parameter to manage pagination of results."),
        sort: str | None = Field(default=None, description="Sort items using their properties."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Queries for config resources and returns details"""
        return self._call(operation="GetCombinedPluginConfigs", query_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort}, error_message="GetCombinedPluginConfigs failed", member_cid=member_cid)
