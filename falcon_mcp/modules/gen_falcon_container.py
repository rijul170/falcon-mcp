"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `falcon_container` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenFalconContainerModule(GeneratedModuleBase):
    """Generated tools for the Falcon `falcon_container` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.download_export_file, name="download_export_file")
        self._add_tool(server=server, method=self.get_combined_images_falcon_container, name="get_combined_images_falcon_container")
        self._add_tool(server=server, method=self.get_credentials, name="get_credentials")
        self._add_tool(server=server, method=self.get_image_assessment_report, name="get_image_assessment_report")
        self._add_tool(server=server, method=self.get_report_by_reference, name="get_report_by_reference")
        self._add_tool(server=server, method=self.get_report_by_scan_id, name="get_report_by_scan_id")
        self._add_tool(server=server, method=self.image_matches_policy, name="image_matches_policy")
        self._add_tool(server=server, method=self.policy_checks, name="policy_checks")
        self._add_tool(server=server, method=self.query_export_jobs, name="query_export_jobs")
        self._add_tool(server=server, method=self.read_export_jobs, name="read_export_jobs")
        self._add_tool(server=server, method=self.read_image_vulnerabilities, name="read_image_vulnerabilities")
        self._add_tool(server=server, method=self.read_registry_entities, name="read_registry_entities")
        self._add_tool(server=server, method=self.read_registry_entities_by_uuid, name="read_registry_entities_by_uuid")
        self._add_tool(server=server, method=self.create_registry_entities, name="create_registry_entities", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.launch_export_job, name="launch_export_job", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_registry_entities, name="update_registry_entities", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_image_details, name="delete_image_details", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_registry_entities, name="delete_registry_entities", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.head_image_scan_inventory, name="head_image_scan_inventory", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.post_image_scan_inventory, name="post_image_scan_inventory", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def create_registry_entities(
        self,
        body: dict = Field(description="Request JSON body for `CreateRegistryEntities` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create a registry entity using the provided details"""
        return self._call(operation="CreateRegistryEntities", query_params=None, body_params=body, error_message="CreateRegistryEntities failed", member_cid=member_cid)

    def delete_image_details(
        self,
        image_id: str = Field(description="`image_id` path parameter (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete Images by ids."""
        return self._call(operation="DeleteImageDetails", query_params=None, path_params={"image_id": image_id}, error_message="DeleteImageDetails failed", member_cid=member_cid)

    def delete_registry_entities(
        self,
        ids: str = Field(description="Registry entity UUID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete the registry entity identified by the entity UUID"""
        return self._call(operation="DeleteRegistryEntities", query_params={"ids": ids}, error_message="DeleteRegistryEntities failed", member_cid=member_cid)

    def download_export_file(
        self,
        id: str = Field(description="Export job ID."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Download an export file"""
        return self._call(operation="DownloadExportFile", query_params={"id": id}, error_message="DownloadExportFile failed", member_cid=member_cid)

    def get_combined_images_falcon_container(
        self,
        filter: str | None = Field(default=None, description="Filter images using a query in Falcon Query Language (FQL). Supported filters: container_running_status, cve_id, first_seen, registry, repository, tag, vulnerability_severity"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve [1-100]"),
        offset: int | None = Field(default=None, description="The offset from where to begin."),
        sort: str | None = Field(default=None, description="The fields to sort the records on. Supported columns: [first_seen registry repository tag vulnerability_severity]"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get image assessment results by providing an FQL filter and paging details"""
        return self._call(operation="GetCombinedImages", query_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort}, error_message="GetCombinedImages failed", member_cid=member_cid)

    def get_credentials(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Gets the registry credentials"""
        return self._call(operation="GetCredentials", query_params=None, error_message="GetCredentials failed", member_cid=member_cid)

    def get_image_assessment_report(
        self,
        digest: str | None = Field(default=None, description="The hash digest for the image."),
        image_id: str | None = Field(default=None, description="The image ID."),
        repository: str | None = Field(default=None, description="The repository the image resides within."),
        tag: str | None = Field(default=None, description="The image tag."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves the Assessment report for the Image ID provided."""
        return self._call(operation="GetImageAssessmentReport", query_params={"digest": digest, "image_id": image_id, "repository": repository, "tag": tag}, error_message="GetImageAssessmentReport failed", member_cid=member_cid)

    def get_report_by_reference(
        self,
        registry: str | None = Field(default=None, description="Registry"),
        repository: str | None = Field(default=None, description="Repository"),
        tag: str | None = Field(default=None, description="Tag"),
        image_id: str | None = Field(default=None, description="Image ID"),
        digest: str | None = Field(default=None, description="Digest"),
        report_format: str | None = Field(default=None, description="Specify image-assessment scan report format. Supported formats: cyclonedx-json json sarif"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get image assessment scan report by image reference (v2)"""
        return self._call(operation="GetReportByReference", query_params={"registry": registry, "repository": repository, "tag": tag, "image_id": image_id, "digest": digest, "report_format": report_format}, error_message="GetReportByReference failed", member_cid=member_cid)

    def get_report_by_scan_id(
        self,
        uuid: str = Field(description="`uuid` path parameter (required)."),
        report_format: str | None = Field(default=None, description="Specify image-assessment scan report format. Supported formats: cyclonedx-json json sarif"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get image assessment scan report by scan UUID (v2)"""
        return self._call(operation="GetReportByScanID", query_params={"report_format": report_format}, path_params={"uuid": uuid}, error_message="GetReportByScanID failed", member_cid=member_cid)

    def head_image_scan_inventory(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get headers for POST request for image scan inventory"""
        return self._call(operation="HeadImageScanInventory", query_params=None, error_message="HeadImageScanInventory failed", member_cid=member_cid)

    def image_matches_policy(
        self,
        repository: str = Field(description="The repository the image resides within."),
        tag: str = Field(description="The image tag."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """After an image scan, use this operation to see if any images match a policy. If deny is true, the policy suggestion is that you do not deploy the image in your environment."""
        return self._call(operation="ImageMatchesPolicy", query_params={"repository": repository, "tag": tag}, error_message="ImageMatchesPolicy failed", member_cid=member_cid)

    def launch_export_job(
        self,
        body: dict = Field(description="Request JSON body for `LaunchExportJob` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Launch an export job of a Container Security resource. Maximum of 1 job in progress per resource"""
        return self._call(operation="LaunchExportJob", query_params=None, body_params=body, error_message="LaunchExportJob failed", member_cid=member_cid)

    def policy_checks(
        self,
        repository: str = Field(description="Repository"),
        tag: str = Field(description="Tag"),
        registry: str | None = Field(default=None, description="Registry"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Check image prevention policies"""
        return self._call(operation="PolicyChecks", query_params={"registry": registry, "repository": repository, "tag": tag}, error_message="PolicyChecks failed", member_cid=member_cid)

    def post_image_scan_inventory(
        self,
        body: dict = Field(description="Request JSON body for `PostImageScanInventory` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Post image scan inventory"""
        return self._call(operation="PostImageScanInventory", query_params=None, body_params=body, error_message="PostImageScanInventory failed", member_cid=member_cid)

    def query_export_jobs(
        self,
        filter: str | None = Field(default=None, description="Filter exports using a query in Falcon Query Language (FQL). Only the last 100 jobs are returned. Supported filter fields: resource status"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Query export jobs entities"""
        return self._call(operation="QueryExportJobs", query_params={"filter": filter}, error_message="QueryExportJobs failed", member_cid=member_cid)

    def read_export_jobs(
        self,
        ids: list[str] = Field(description="Export Job IDs to read. Allowed up to 100 IDs per request."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Read export jobs entities"""
        return self._call(operation="ReadExportJobs", query_params={"ids": ids}, error_message="ReadExportJobs failed", member_cid=member_cid)

    def read_image_vulnerabilities(
        self,
        body: dict = Field(description="Request JSON body for `ReadImageVulnerabilities` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve known vulnerabilities for the provided image"""
        return self._call(operation="ReadImageVulnerabilities", query_params=None, body_params=body, error_message="ReadImageVulnerabilities failed", member_cid=member_cid)

    def read_registry_entities(
        self,
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve."),
        offset: int | None = Field(default=None, description="The offset from where to begin."),
        sort: str | None = Field(default=None, description="The fields to sort the records on."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves a list of registry entities identified by the customer id. Maximum page size: 5,000"""
        return self._call(operation="ReadRegistryEntities", query_params={"limit": limit, "offset": offset, "sort": sort}, error_message="ReadRegistryEntities failed", member_cid=member_cid)

    def read_registry_entities_by_uuid(
        self,
        ids: str = Field(description="Registry entity UUID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves a list of registry entities by the provided UUIDs. Maximum page size: 100"""
        return self._call(operation="ReadRegistryEntitiesByUUID", query_params={"ids": ids}, error_message="ReadRegistryEntitiesByUUID failed", member_cid=member_cid)

    def update_registry_entities(
        self,
        id: str = Field(description="Registry entity UUID"),
        body: dict = Field(description="Request JSON body for `UpdateRegistryEntities` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update the registry entity, as identified by the entity UUID, using the provided details"""
        return self._call(operation="UpdateRegistryEntities", query_params={"id": id}, body_params=body, error_message="UpdateRegistryEntities failed", member_cid=member_cid)
