"""
On-Demand Scanning (ODS) module for Falcon MCP Server.

Provides tools for searching/launching/cancelling Windows on-demand scans against
hosts and host groups, and reading malicious files surfaced by past scans.
"""

from typing import Any

from mcp.server import FastMCP
from mcp.server.fastmcp.resources import TextResource
from mcp.types import ToolAnnotations
from pydantic import AnyUrl, Field

from falcon_mcp.common.errors import _format_error_response
from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule
from falcon_mcp.resources.ods import ODS_FQL_DOCUMENTATION

logger = get_logger(__name__)

WRITE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True,
)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True,
)


class OdsModule(BaseModule):
    """Module for Windows On-Demand Scanning."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.search_ods_scans, name="search_ods_scans")
        self._add_tool(server=server, method=self.get_ods_scan_details, name="get_ods_scan_details")
        self._add_tool(server=server, method=self.search_ods_host_scans, name="search_ods_host_scans")
        self._add_tool(server=server, method=self.get_ods_host_scan_details, name="get_ods_host_scan_details")
        self._add_tool(server=server, method=self.search_ods_scheduled_scans, name="search_ods_scheduled_scans")
        self._add_tool(server=server, method=self.get_ods_scheduled_scan_details, name="get_ods_scheduled_scan_details")
        self._add_tool(server=server, method=self.search_ods_malicious_files, name="search_ods_malicious_files")
        self._add_tool(server=server, method=self.get_ods_malicious_file_details, name="get_ods_malicious_file_details")
        self._add_tool(
            server=server, method=self.create_ods_scan, name="create_ods_scan",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.cancel_ods_scans, name="cancel_ods_scans",
            annotations=DESTRUCTIVE_ANNOTATIONS,
        )

    def register_resources(self, server: FastMCP) -> None:
        self._add_resource(server, TextResource(
            uri=AnyUrl("falcon://ods/fql-guide"),
            name="falcon_ods_fql_guide",
            description="FQL filter guide for ODS search tools.",
            text=ODS_FQL_DOCUMENTATION,
        ))

    def search_ods_scans(
        self,
        filter: str | None = Field(default=None, description="FQL filter; see `falcon://ods/fql-guide`."),
        limit: int = Field(default=10, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search ODS scans (returns IDs, hydrate with `falcon_get_ods_scan_details`)."""
        result = self._base_search_api_call(
            operation="query_scans",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search ODS scans",
        )
        if self._is_error(result):
            if filter:
                return self._format_fql_error_response([result], filter, ODS_FQL_DOCUMENTATION)
            return [result]
        return result

    def get_ods_scan_details(
        self,
        ids: list[str] = Field(description="Scan IDs."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get full ODS scan details (V2 endpoint)."""
        if not ids:
            return []
        return self._base_get_by_ids(operation="get_scans_by_scan_ids_v2", ids=ids, use_params=True)

    def search_ods_host_scans(
        self,
        filter: str | None = Field(default=None, description="FQL filter."),
        limit: int = Field(default=10, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search per-host scan progress records (returns IDs)."""
        result = self._base_search_api_call(
            operation="query_scan_host_metadata",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search ODS host scans",
        )
        if self._is_error(result):
            return [result]
        return result

    def get_ods_host_scan_details(
        self,
        ids: list[str] = Field(description="Host scan metadata IDs."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get per-host scan progress records by ID."""
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="get_scan_host_metadata_by_ids", ids=ids, use_params=True,
        )

    def search_ods_scheduled_scans(
        self,
        filter: str | None = Field(default=None, description="FQL filter."),
        limit: int = Field(default=10, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search scheduled ODS scans (returns IDs)."""
        result = self._base_search_api_call(
            operation="query_scheduled_scans",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search ODS scheduled scans",
        )
        if self._is_error(result):
            return [result]
        return result

    def get_ods_scheduled_scan_details(
        self,
        ids: list[str] = Field(description="Scheduled scan IDs."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get scheduled scan details by ID."""
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="get_scheduled_scans_by_scan_ids", ids=ids, use_params=True,
        )

    def search_ods_malicious_files(
        self,
        filter: str | None = Field(default=None, description="FQL filter."),
        limit: int = Field(default=10, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search malicious files surfaced by ODS scans (returns IDs)."""
        result = self._base_search_api_call(
            operation="query_malicious_files",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search ODS malicious files",
        )
        if self._is_error(result):
            return [result]
        return result

    def get_ods_malicious_file_details(
        self,
        ids: list[str] = Field(description="Malicious file IDs."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get malicious-file details by ID."""
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="get_malicious_files_by_ids", ids=ids, use_params=True,
        )

    def create_ods_scan(
        self,
        description: str = Field(description="Human-readable description of the scan."),
        host_ids: list[str] | None = Field(
            default=None,
            description="Target host AIDs. Either `host_ids` or `host_group_ids` is required.",
        ),
        host_group_ids: list[str] | None = Field(
            default=None,
            description="Target host group IDs. Either `host_ids` or `host_group_ids` is required.",
        ),
        file_paths: list[str] | None = Field(
            default=None,
            description="File path patterns to scan (e.g. ['C:\\\\Users\\\\*']). Optional - omit to scan defaults.",
        ),
        scan_exclusions: list[str] | None = Field(
            default=None,
            description="Path patterns to exclude.",
        ),
        cpu_priority: int = Field(
            default=2, ge=0, le=5,
            description="CPU priority 0-5 (0=idle, 5=highest).",
        ),
        max_duration: int = Field(
            default=2, ge=1, le=24,
            description="Max scan duration in hours.",
        ),
        max_file_size: int = Field(
            default=60, ge=1, le=2048,
            description="Max file size to scan, in MB.",
        ),
        pause_duration: int = Field(
            default=2, ge=0, le=24,
            description="Pause duration in hours when host is busy.",
        ),
        quarantine: bool = Field(default=False, description="Quarantine matches automatically."),
        endpoint_notification: bool = Field(default=False, description="Show notification on the host."),
        sensor_ml_level_detection: int = Field(default=2, ge=0, le=5, description="Sensor ML detection level 0-5."),
        sensor_ml_level_prevention: int = Field(default=2, ge=0, le=5, description="Sensor ML prevention level 0-5."),
        cloud_ml_level_detection: int = Field(default=2, ge=0, le=5, description="Cloud ML detection level 0-5."),
        cloud_ml_level_prevention: int = Field(default=2, ge=0, le=5, description="Cloud ML prevention level 0-5."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Launch an ad-hoc on-demand scan.

        WARNING: this initiates a real scan against production hosts. Quarantine and
        prevention levels can take action on detected files when set above 0.
        """
        if not host_ids and not host_group_ids:
            return [_format_error_response(
                "Provide `host_ids` or `host_group_ids`.", operation="create_scan",
            )]
        body: dict[str, Any] = {
            "description": description,
            "cpu_priority": cpu_priority,
            "max_duration": max_duration,
            "max_file_size": max_file_size,
            "pause_duration": pause_duration,
            "quarantine": quarantine,
            "endpoint_notification": endpoint_notification,
            "sensor_ml_level_detection": sensor_ml_level_detection,
            "sensor_ml_level_prevention": sensor_ml_level_prevention,
            "cloud_ml_level_detection": cloud_ml_level_detection,
            "cloud_ml_level_prevention": cloud_ml_level_prevention,
            "initiated_from": "falcon-mcp",
        }
        if host_ids:
            body["hosts"] = host_ids
        if host_group_ids:
            body["host_groups"] = host_group_ids
        if file_paths:
            body["file_paths"] = file_paths
        if scan_exclusions:
            body["scan_exclusions"] = scan_exclusions
        result = self._base_query_api_call(
            operation="create_scan",
            body_params=body,
            error_message="Failed to launch ODS scan",
        )
        if self._is_error(result):
            return [result]
        return result

    def cancel_ods_scans(
        self,
        ids: list[str] = Field(description="Scan IDs to cancel."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Cancel running ODS scans."""
        if not ids:
            return [_format_error_response(
                "`ids` is required.", operation="cancel_scans",
            )]
        result = self._base_query_api_call(
            operation="cancel_scans",
            body_params={"ids": ids},
            error_message="Failed to cancel ODS scans",
        )
        if self._is_error(result):
            return [result]
        return result
