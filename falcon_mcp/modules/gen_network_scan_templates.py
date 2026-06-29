"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `network_scan_templates` API service collection.

FalconPy note: FalconPy 1.6.1 does not include a dedicated NetworkScan service class.
These tools call the /netscan/ endpoints via the APIHarnessV2 uber-class using operation IDs
sourced directly from the CrowdStrike API reference:
  https://developer.crowdstrike.com/api-reference/collections/network-scan-templates/
Required OAuth2 scope: Network scanning: READ (reads) / WRITE (creates, updates, deletes).
"""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenNetworkScanTemplatesModule(GeneratedModuleBase):
    """Generated tools for the Falcon `network_scan_templates` collection.

    Covers the /netscan/entities/template-configs, /netscan/entities/templates, and
    /netscan/queries/templates endpoints.
    """

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_template_configs, name="get_template_configs")
        self._add_tool(server=server, method=self.get_templates, name="get_templates")
        self._add_tool(server=server, method=self.query_templates, name="query_templates")
        self._add_tool(server=server, method=self.create_templates, name="create_templates", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_templates, name="update_templates", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_templates, name="delete_templates", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def get_template_configs(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get details on the network scan template configurations. GETs /netscan/entities/template-configs/v1.
        Takes no filter parameters. Requires OAuth2 scope: Network scanning: READ."""
        return self._call(operation="get_template_configs", query_params=None, error_message="get_template_configs failed", member_cid=member_cid)

    def get_templates(
        self,
        ids: list[str] = Field(description="IDs of 'templates' to be retrieved (Min: 1, Max: 100)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get 'templates' by their IDs. GETs /netscan/entities/templates/v1.
        Requires OAuth2 scope: Network scanning: READ."""
        return self._call(operation="get_templates", query_params={"ids": ids}, error_message="get_templates failed", member_cid=member_cid)

    def create_templates(
        self,
        body: dict = Field(description="Request JSON body for `create_templates` per the CrowdStrike API schema. Supported fields: active_check_level (str), additional_tcp_ports (array of int), additional_udp_ports (array of int), auto_include_new_detections (bool), detections (array), ignore_tcp_resets (bool), name (str), ports_scan_level (str), scan_intensity (str), type (str)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create 'templates' using provided specifications. POSTs to /netscan/entities/templates/v1.
        Requires OAuth2 scope: Network scanning: WRITE."""
        return self._call(operation="create_templates", query_params=None, body_params=body, error_message="create_templates failed", member_cid=member_cid)

    def delete_templates(
        self,
        ids: list[str] = Field(description="IDs of 'templates' to be deleted (Min: 1, Max: 100)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete 'templates' by their IDs. DELETEs /netscan/entities/templates/v1.
        Requires OAuth2 scope: Network scanning: WRITE."""
        return self._call(operation="delete_templates", query_params={"ids": ids}, error_message="delete_templates failed", member_cid=member_cid)

    def update_templates(
        self,
        body: dict = Field(description="Request JSON body for `update_templates` per the CrowdStrike API schema. Supported fields: id (str, required — the template to update), active_check_level (str), additional_tcp_ports (array of int), additional_udp_ports (array of int), auto_include_new_detections (bool), detections (array), ignore_tcp_resets (bool), name (str), ports_scan_level (str), scan_intensity (str)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update 'templates' using provided specifications. PATCHes /netscan/entities/templates/v1.
        Requires OAuth2 scope: Network scanning: WRITE."""
        return self._call(operation="update_templates", query_params=None, body_params=body, error_message="update_templates failed", member_cid=member_cid)

    def query_templates(
        self,
        offset: int | None = Field(default=None, description="Starting index for pagination. Do not provide on the first request."),
        limit: int | None = Field(default=None, description="Number of template IDs to return (Min: 1, Max: 100, Default: 100)."),
        sort: str | None = Field(default=None, description="Sort 'templates' by their properties. A single sort field is allowed."),
        filter: str | None = Field(default=None, description="FQL filter to search for 'templates'. Example: `name:'my-template'`"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get 'template IDs' by filter. GETs /netscan/queries/templates/v1.
        Requires OAuth2 scope: Network scanning: READ."""
        return self._call(operation="query_templates", query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter}, error_message="query_templates failed", member_cid=member_cid)
