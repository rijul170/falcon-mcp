"""
Sensor Download module for Falcon MCP Server.

Provides tools for listing CrowdStrike Falcon sensor installers and the customer's CCID.
The actual binary download endpoint is intentionally not exposed - installers are
multi-megabyte binaries unsuitable for MCP tool responses.
"""

from typing import Any

from mcp.server import FastMCP
from mcp.server.fastmcp.resources import TextResource
from pydantic import AnyUrl, Field

from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule
from falcon_mcp.resources.sensor_download import SEARCH_SENSOR_INSTALLERS_FQL_DOCUMENTATION

logger = get_logger(__name__)


class SensorDownloadModule(BaseModule):
    """Module for CrowdStrike Falcon sensor installer metadata."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.search_sensor_installers, name="search_sensor_installers")
        self._add_tool(server=server, method=self.get_sensor_installer_details, name="get_sensor_installer_details")
        self._add_tool(server=server, method=self.get_ccid, name="get_ccid")

    def register_resources(self, server: FastMCP) -> None:
        self._add_resource(server, TextResource(
            uri=AnyUrl("falcon://sensor-download/fql-guide"),
            name="falcon_search_sensor_installers_fql_guide",
            description="FQL filter guide for `falcon_search_sensor_installers`.",
            text=SEARCH_SENSOR_INSTALLERS_FQL_DOCUMENTATION,
        ))

    def search_sensor_installers(
        self,
        filter: str | None = Field(
            default=None,
            description="FQL filter; see `falcon://sensor-download/fql-guide`.",
            examples=["platform:'windows'+os:'Windows 10'"],
        ),
        limit: int = Field(default=10, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression (e.g. release_date.desc)."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search available sensor installers (latest V3 endpoint, returns full metadata)."""
        result = self._base_search_api_call(
            operation="GetCombinedSensorInstallersByQueryV3",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search sensor installers",
        )
        if self._is_error(result):
            if filter:
                return self._format_fql_error_response(
                    [result], filter, SEARCH_SENSOR_INSTALLERS_FQL_DOCUMENTATION,
                )
            return [result]
        return result

    def get_sensor_installer_details(
        self,
        ids: list[str] = Field(description="Sensor installer SHA256 IDs."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get sensor installer details by SHA256 ID (latest V3 endpoint)."""
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="GetSensorInstallersEntitiesV3", ids=ids, use_params=True,
        )

    def get_ccid(self) -> list[dict[str, Any]] | dict[str, Any]:
        """Get the Customer Checksum ID (CCID) needed for sensor installation."""
        result = self._base_search_api_call(
            operation="GetSensorInstallersCCIDByQuery",
            search_params={},
            error_message="Failed to fetch CCID",
        )
        if self._is_error(result):
            return [result]
        return result
