"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `unidentified_containers` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenUnidentifiedContainersModule(GeneratedModuleBase):
    """Generated tools for the Falcon `unidentified_containers` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.read_unidentified_containers_by_date_range_count, name="read_unidentified_containers_by_date_range_count")
        self._add_tool(server=server, method=self.read_unidentified_containers_count, name="read_unidentified_containers_count")
        self._add_tool(server=server, method=self.search_and_read_unidentified_containers, name="search_and_read_unidentified_containers")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def read_unidentified_containers_by_date_range_count(
        self,
        filter: str | None = Field(default=None, description="Search Unidentified Containers using a query in Falcon Query Language (FQL). Supported filter fields: assessed_images_count cid cloud_account_id cloud_name cloud_region cluster_id cluster_name containers_impacted_count detections_count image_assessment_detections_count last_seen namespace node_name severity unassessed_images_count visible_to_k8s"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns the count of Unidentified Containers over the last 7 days"""
        return self._call(operation="ReadUnidentifiedContainersByDateRangeCount", query_params={"filter": filter}, error_message="ReadUnidentifiedContainersByDateRangeCount failed", member_cid=member_cid)

    def read_unidentified_containers_count(
        self,
        filter: str | None = Field(default=None, description="Search Unidentified Containers using a query in Falcon Query Language (FQL). Supported filter fields: assessed_images_count cid cloud_account_id cloud_name cloud_region cluster_id cluster_name containers_impacted_count detections_count image_assessment_detections_count last_seen namespace node_name severity unassessed_images_count visible_to_k8s"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns the total count of Unidentified Containers over a time period"""
        return self._call(operation="ReadUnidentifiedContainersCount", query_params={"filter": filter}, error_message="ReadUnidentifiedContainersCount failed", member_cid=member_cid)

    def search_and_read_unidentified_containers(
        self,
        filter: str | None = Field(default=None, description="Search Unidentified Containers using a query in Falcon Query Language (FQL). Supported filter fields: assessed_images_count cid cloud_account_id cloud_name cloud_region cluster_id cluster_name containers_impacted_count detections_count image_assessment_detections_count last_seen namespace node_name severity unassessed_images_count visible_to_k8s"),
        sort: str | None = Field(default=None, description="The fields to sort the records on."),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search Unidentified Containers by the provided search criteria"""
        return self._call(operation="SearchAndReadUnidentifiedContainers", query_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset}, error_message="SearchAndReadUnidentifiedContainers failed", member_cid=member_cid)
