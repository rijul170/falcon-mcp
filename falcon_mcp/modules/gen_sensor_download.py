"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `sensor_download` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenSensorDownloadModule(GeneratedModuleBase):
    """Generated tools for the Falcon `sensor_download` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.download_sensor_installer_by_id_v3, name="download_sensor_installer_by_id_v3")
        self._add_tool(server=server, method=self.get_sensor_installers_by_query_v3, name="get_sensor_installers_by_query_v3")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def download_sensor_installer_by_id_v3(
        self,
        id: str = Field(description="SHA256 of the installer to download"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Download sensor installer by SHA256 ID"""
        return self._call(operation="DownloadSensorInstallerByIdV3", query_params={"id": id}, error_message="DownloadSensorInstallerByIdV3 failed", member_cid=member_cid)

    def get_sensor_installers_by_query_v3(
        self,
        offset: int | None = Field(default=None, description="The first item to return, where 0 is the latest item. Use with the limit parameter to manage pagination of results."),
        limit: int | None = Field(default=None, description="The number of items to return in this response (default: 100, max: 500). Use with the offset parameter to manage pagination of results."),
        sort: str | None = Field(default=None, description="Sort items using their properties. Common sort options include:nn<ul><li>version|asc</li><li>release_date|desc</li></ul>"),
        filter: str | None = Field(default=None, description="Filter items using a query in Falcon Query Language (FQL). An asterisk wildcard * includes all results.nnCommon filter options include:n<ul><li>platform:'windows'</li><li>version:>'5.2'</li></ul>"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get sensor installer IDs by provided query"""
        return self._call(operation="GetSensorInstallersByQueryV3", query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter}, error_message="GetSensorInstallersByQueryV3 failed", member_cid=member_cid)
