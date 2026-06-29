"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `container_detections` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenContainerDetectionsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `container_detections` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_runtime_detections_combined_v2, name="get_runtime_detections_combined_v2")
        self._add_tool(server=server, method=self.read_combined_detections, name="read_combined_detections")
        self._add_tool(server=server, method=self.read_detections, name="read_detections")
        self._add_tool(server=server, method=self.read_detections_count, name="read_detections_count")
        self._add_tool(server=server, method=self.read_detections_count_by_severity, name="read_detections_count_by_severity")
        self._add_tool(server=server, method=self.read_detections_count_by_type, name="read_detections_count_by_type")
        self._add_tool(server=server, method=self.search_detections_container_detections, name="search_detections_container_detections")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def get_runtime_detections_combined_v2(
        self,
        filter: str | None = Field(default=None, description="Filter Container Runtime Detections using a query in Falcon Query Language (FQL). Supported filter fields: agent_type aid cid cloud_name cloud cluster_name computer_name container_id detect_timestamp host_id host_type image_id name namespace pod_name severity"),
        sort: str | None = Field(default=None, description="The fields to sort the records on."),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve container runtime detections by the provided search criteria"""
        return self._call(operation="GetRuntimeDetectionsCombinedV2", query_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset}, error_message="GetRuntimeDetectionsCombinedV2 failed", member_cid=member_cid)

    def read_combined_detections(
        self,
        filter: str | None = Field(default=None, description="Filter images detections using a query in Falcon Query Language (FQL). Supported filter fields: cid detection_type image_digest image_registry image_repository image_tag severity"),
        sort: str | None = Field(default=None, description="The fields to sort the records on. Supported columns: containers_impacted detection_name detection_severity detection_type images_impacted last_detected"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve image assessment detections identified by the provided filter criteria"""
        return self._call(operation="ReadCombinedDetections", query_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset}, error_message="ReadCombinedDetections failed", member_cid=member_cid)

    def read_detections(
        self,
        filter: str | None = Field(default=None, description="Filter images detections using a query in Falcon Query Language (FQL). Supported filter fields: cid detection_type image_digest image_registry image_repository image_tag severity"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve image assessment detection entities identified by the provided filter criteria"""
        return self._call(operation="ReadDetections", query_params={"filter": filter, "limit": limit, "offset": offset}, error_message="ReadDetections failed", member_cid=member_cid)

    def read_detections_count(
        self,
        filter: str | None = Field(default=None, description="Filter images detections using a query in Falcon Query Language (FQL). Supported filter fields: cid detection_type image_digest image_registry image_repository image_tag severity"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Aggregate count of detections"""
        return self._call(operation="ReadDetectionsCount", query_params={"filter": filter}, error_message="ReadDetectionsCount failed", member_cid=member_cid)

    def read_detections_count_by_severity(
        self,
        filter: str | None = Field(default=None, description="Filter images detections using a query in Falcon Query Language (FQL). Supported filter fields: cid detection_type image_digest image_registry image_repository image_tag severity"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Aggregate counts of detections by severity"""
        return self._call(operation="ReadDetectionsCountBySeverity", query_params={"filter": filter}, error_message="ReadDetectionsCountBySeverity failed", member_cid=member_cid)

    def read_detections_count_by_type(
        self,
        filter: str | None = Field(default=None, description="Filter images detections using a query in Falcon Query Language (FQL). Supported filter fields: cid detection_type image_digest image_registry image_repository image_tag severity"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Aggregate counts of detections by detection type"""
        return self._call(operation="ReadDetectionsCountByType", query_params={"filter": filter}, error_message="ReadDetectionsCountByType failed", member_cid=member_cid)

    def search_detections_container_detections(
        self,
        filter: str | None = Field(default=None, description="Filter images detections using a query in Falcon Query Language (FQL). Supported filter fields: cid detection_type image_digest image_registry image_repository image_tag severity"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve image assessment detection entities identified by the provided filter criteria"""
        return self._call(operation="SearchDetections", query_params={"filter": filter, "limit": limit, "offset": offset}, error_message="SearchDetections failed", member_cid=member_cid)
