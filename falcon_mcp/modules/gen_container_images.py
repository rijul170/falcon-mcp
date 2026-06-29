"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `container_images` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenContainerImagesModule(GeneratedModuleBase):
    """Generated tools for the Falcon `container_images` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.combined_base_images, name="combined_base_images")
        self._add_tool(server=server, method=self.combined_image_by_vulnerability_count, name="combined_image_by_vulnerability_count")
        self._add_tool(server=server, method=self.combined_image_detail, name="combined_image_detail")
        self._add_tool(server=server, method=self.combined_image_issues_summary, name="combined_image_issues_summary")
        self._add_tool(server=server, method=self.combined_image_vulnerability_summary, name="combined_image_vulnerability_summary")
        self._add_tool(server=server, method=self.get_combined_images, name="get_combined_images")
        self._add_tool(server=server, method=self.read_combined_images_export, name="read_combined_images_export")
        self._add_tool(server=server, method=self.create_base_images_entities, name="create_base_images_entities", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_base_images, name="delete_base_images", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def combined_base_images(
        self,
        filter: str | None = Field(default=None, description="Search base images using a query in Falcon Query Language (FQL). Supported filter fields: image_digest image_id registry repository tag"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves a list of base images for the provided filter. Maximum page size: 100"""
        return self._call(operation="CombinedBaseImages", query_params={"filter": filter}, error_message="CombinedBaseImages failed", member_cid=member_cid)

    def combined_image_by_vulnerability_count(
        self,
        filter: str | None = Field(default=None, description="Filter images using a query in Falcon Query Language (FQL). Supported filter fields: arch base_os cid first_seen image_digest image_id index_digest registry repository source tag"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve."),
        offset: int | None = Field(default=None, description="The fields to sort the records on. **Not supported.**"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve top x images with the most vulnerabilities"""
        return self._call(operation="CombinedImageByVulnerabilityCount", query_params={"filter": filter, "limit": limit, "offset": offset}, error_message="CombinedImageByVulnerabilityCount failed", member_cid=member_cid)

    def combined_image_detail(
        self,
        filter: str | None = Field(default=None, description="Filter images using a query in Falcon Query Language (FQL). Supported filter fields: arch base_os cid first_seen image_digest image_id index_digest registry repository source tag"),
        with_config: bool | None = Field(default=None, description="(true/false) include image config, default is false"),
        sort: str | None = Field(default=None, description="The fields to sort the records on."),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve image entities identified by the provided filter criteria"""
        return self._call(operation="CombinedImageDetail", query_params={"filter": filter, "with_config": with_config, "sort": sort, "limit": limit, "offset": offset}, error_message="CombinedImageDetail failed", member_cid=member_cid)

    def combined_image_issues_summary(
        self,
        cid: str = Field(description="CS Customer ID"),
        registry: str = Field(description="Registry"),
        repository: str = Field(description="Repository name"),
        tag: str = Field(description="Tag name"),
        image_digest: str | None = Field(default=None, description="Digest ID"),
        include_base_image_vuln: bool | None = Field(default=None, description="Include base image vulnerabilities."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve image issues summary such as Image detections, Runtime detections, Policies, vulnerabilities"""
        return self._call(operation="CombinedImageIssuesSummary", query_params={"cid": cid, "registry": registry, "repository": repository, "tag": tag, "image_digest": image_digest, "include_base_image_vuln": include_base_image_vuln}, error_message="CombinedImageIssuesSummary failed", member_cid=member_cid)

    def combined_image_vulnerability_summary(
        self,
        cid: str = Field(description="CS Customer ID"),
        registry: str = Field(description="Registry"),
        repository: str = Field(description="Repository name"),
        tag: str = Field(description="Tag name"),
        image_digest: str | None = Field(default=None, description="Digest ID"),
        include_base_image_vuln: bool | None = Field(default=None, description="Include base image vulnerabilities."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """aggregates information about vulnerabilities for an image"""
        return self._call(operation="CombinedImageVulnerabilitySummary", query_params={"cid": cid, "registry": registry, "repository": repository, "tag": tag, "image_digest": image_digest, "include_base_image_vuln": include_base_image_vuln}, error_message="CombinedImageVulnerabilitySummary failed", member_cid=member_cid)

    def create_base_images_entities(
        self,
        body: dict = Field(description="Request JSON body for `CreateBaseImagesEntities` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Creates base images using the provided details"""
        return self._call(operation="CreateBaseImagesEntities", query_params=None, body_params=body, error_message="CreateBaseImagesEntities failed", member_cid=member_cid)

    def delete_base_images(
        self,
        ids: list[str] = Field(description="BaseImageIDs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete base images by base image uuid"""
        return self._call(operation="DeleteBaseImages", query_params={"ids": ids}, error_message="DeleteBaseImages failed", member_cid=member_cid)

    def get_combined_images(
        self,
        filter: str | None = Field(default=None, description="Filter images using a query in Falcon Query Language (FQL). Supported filter fields: ai_related container_id container_running_status cve_id detection_name detection_severity first_seen image_digest image_id index_digest registry repository tag vulnerability_severity"),
        sort: str | None = Field(default=None, description="The fields to sort the records on. Supported columns: first_seen highest_detection_severity highest_vulnerability_severity image_digest image_id registry repository source tag"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get image assessment results by providing an FQL filter and paging details"""
        return self._call(operation="GetCombinedImages", query_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset}, error_message="GetCombinedImages failed", member_cid=member_cid)

    def read_combined_images_export(
        self,
        filter: str | None = Field(default=None, description="Filter images using a query in Falcon Query Language (FQL). Supported filter fields: ai_related ai_vulnerability_count arch base_os cid container_id container_running_status cps_rating crowdstrike_user cve_id detection_count detection_name detection_severity first_seen image_digest image_id include_base_image_vuln index_digest layer_digest package_name_version registry repository source tag vulnerability_count vulnerability_severity"),
        expand_vulnerabilities: bool | None = Field(default=None, description="Expand vulnerabilities details"),
        expand_detections: bool | None = Field(default=None, description="Expand detections details"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        sort: str | None = Field(default=None, description="The fields to sort the records on. Supported columns: ai_vulnerabilities base_os cid detections firstScanned first_seen highest_cps_current_rating highest_detection_severity highest_vulnerability_severity image_digest image_id last_seen layers_with_vulnerabilities packages registry repository source tag vulnerabilities"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves a paginated list of images, with an option to expand aggregated vulnerabilities/detections. Maximum page size: 100. Maximum available images: 10,000"""
        return self._call(operation="ReadCombinedImagesExport", query_params={"filter": filter, "expand_vulnerabilities": expand_vulnerabilities, "expand_detections": expand_detections, "limit": limit, "offset": offset, "sort": sort}, error_message="ReadCombinedImagesExport failed", member_cid=member_cid)
