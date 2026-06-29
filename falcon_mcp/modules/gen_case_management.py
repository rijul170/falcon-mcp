"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `case_management` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenCaseManagementModule(GeneratedModuleBase):
    """Generated tools for the Falcon `case_management` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.combined_file_details_get_v1, name="combined_file_details_get_v1")
        self._add_tool(server=server, method=self.entities_access_tags_get_v1, name="entities_access_tags_get_v1")
        self._add_tool(server=server, method=self.entities_fields_get_v1, name="entities_fields_get_v1")
        self._add_tool(server=server, method=self.entities_file_details_get_v1, name="entities_file_details_get_v1")
        self._add_tool(server=server, method=self.entities_files_download_get_v1, name="entities_files_download_get_v1")
        self._add_tool(server=server, method=self.entities_get_rtr_file_metadata_post_v1, name="entities_get_rtr_file_metadata_post_v1")
        self._add_tool(server=server, method=self.entities_notification_groups_get_v2, name="entities_notification_groups_get_v2")
        self._add_tool(server=server, method=self.entities_template_snapshots_get_v1, name="entities_template_snapshots_get_v1")
        self._add_tool(server=server, method=self.queries_access_tags_get_v1, name="queries_access_tags_get_v1")
        self._add_tool(server=server, method=self.queries_fields_get_v1, name="queries_fields_get_v1")
        self._add_tool(server=server, method=self.queries_file_details_get_v1, name="queries_file_details_get_v1")
        self._add_tool(server=server, method=self.queries_notification_groups_get_v2, name="queries_notification_groups_get_v2")
        self._add_tool(server=server, method=self.queries_template_snapshots_get_v1, name="queries_template_snapshots_get_v1")
        self._add_tool(server=server, method=self.entities_file_details_patch_v1, name="entities_file_details_patch_v1", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_files_bulk_download_post_v1, name="entities_files_bulk_download_post_v1", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_files_download_post_v1, name="entities_files_download_post_v1", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_notification_groups_patch_v2, name="entities_notification_groups_patch_v2", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_notification_groups_post_v2, name="entities_notification_groups_post_v2", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_retrieve_rtr_file_post_v1, name="entities_retrieve_rtr_file_post_v1", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_retrieve_rtr_recent_file_post_v1, name="entities_retrieve_rtr_recent_file_post_v1", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_files_delete_v1, name="entities_files_delete_v1", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_notification_groups_delete_v2, name="entities_notification_groups_delete_v2", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def combined_file_details_get_v1(
        self,
        filter: str | None = Field(default=None, description="FQL filter expression"),
        limit: int | None = Field(default=None, description="Page size"),
        offset: int | None = Field(default=None, description="Page offset"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Query file details"""
        return self._call(operation="combined_file_details_get_v1", query_params={"filter": filter, "limit": limit, "offset": offset}, error_message="combined_file_details_get_v1 failed", member_cid=member_cid)

    def entities_access_tags_get_v1(
        self,
        ids: list[str] = Field(description="Resource IDs"),
        with_has_access: bool | None = Field(default=None, description="Evaluate FGAC and return has_access property"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get access tags"""
        return self._call(operation="entities_access_tags_get_v1", query_params={"ids": ids, "with_has_access": with_has_access}, error_message="entities_access_tags_get_v1 failed", member_cid=member_cid)

    def entities_fields_get_v1(
        self,
        ids: list[str] = Field(description="Resource IDs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get fields by ID"""
        return self._call(operation="entities_fields_get_v1", query_params={"ids": ids}, error_message="entities_fields_get_v1 failed", member_cid=member_cid)

    def entities_file_details_get_v1(
        self,
        ids: list[str] = Field(description="Resource IDs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get file details by id"""
        return self._call(operation="entities_file_details_get_v1", query_params={"ids": ids}, error_message="entities_file_details_get_v1 failed", member_cid=member_cid)

    def entities_file_details_patch_v1(
        self,
        body: dict = Field(description="Request JSON body for `entities_file_details_patch_v1` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update file details"""
        return self._call(operation="entities_file_details_patch_v1", query_params=None, body_params=body, error_message="entities_file_details_patch_v1 failed", member_cid=member_cid)

    def entities_files_bulk_download_post_v1(
        self,
        body: dict = Field(description="Request JSON body for `entities_files_bulk_download_post_v1` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Download multiple existing file from case as a ZIP"""
        return self._call(operation="entities_files_bulk_download_post_v1", query_params=None, body_params=body, error_message="entities_files_bulk_download_post_v1 failed", member_cid=member_cid)

    def entities_files_delete_v1(
        self,
        ids: list[str] = Field(description="Resource IDs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete file details by id"""
        return self._call(operation="entities_files_delete_v1", query_params={"ids": ids}, error_message="entities_files_delete_v1 failed", member_cid=member_cid)

    def entities_files_download_get_v1(
        self,
        id: str = Field(description="Resource ID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Download existing file from case"""
        return self._call(operation="entities_files_download_get_v1", query_params={"id": id}, error_message="entities_files_download_get_v1 failed", member_cid=member_cid)

    def entities_files_download_post_v1(
        self,
        body: dict = Field(description="Request JSON body for `entities_files_download_post_v1` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Download existing files from case"""
        return self._call(operation="entities_files_download_post_v1", query_params=None, body_params=body, error_message="entities_files_download_post_v1 failed", member_cid=member_cid)

    def entities_get_rtr_file_metadata_post_v1(
        self,
        body: dict = Field(description="Request JSON body for `entities_get_rtr_file_metadata_post_v1` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """gets metadata for a file via RTR without retrieving it"""
        return self._call(operation="entities_get_rtr_file_metadata_post_v1", query_params=None, body_params=body, error_message="entities_get_rtr_file_metadata_post_v1 failed", member_cid=member_cid)

    def entities_notification_groups_delete_v2(
        self,
        ids: list[str] = Field(description="Resource IDs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete notification groups by ID"""
        return self._call(operation="entities_notification_groups_delete_v2", query_params={"ids": ids}, error_message="entities_notification_groups_delete_v2 failed", member_cid=member_cid)

    def entities_notification_groups_get_v2(
        self,
        ids: list[str] = Field(description="Resource IDs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get notification groups by ID"""
        return self._call(operation="entities_notification_groups_get_v2", query_params={"ids": ids}, error_message="entities_notification_groups_get_v2 failed", member_cid=member_cid)

    def entities_notification_groups_patch_v2(
        self,
        body: dict = Field(description="Request JSON body for `entities_notification_groups_patch_v2` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update notification group"""
        return self._call(operation="entities_notification_groups_patch_v2", query_params=None, body_params=body, error_message="entities_notification_groups_patch_v2 failed", member_cid=member_cid)

    def entities_notification_groups_post_v2(
        self,
        body: dict = Field(description="Request JSON body for `entities_notification_groups_post_v2` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create notification group"""
        return self._call(operation="entities_notification_groups_post_v2", query_params=None, body_params=body, error_message="entities_notification_groups_post_v2 failed", member_cid=member_cid)

    def entities_retrieve_rtr_file_post_v1(
        self,
        body: dict = Field(description="Request JSON body for `entities_retrieve_rtr_file_post_v1` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """retrieves a file from host using RTR and adds it to a case"""
        return self._call(operation="entities_retrieve_rtr_file_post_v1", query_params=None, body_params=body, error_message="entities_retrieve_rtr_file_post_v1 failed", member_cid=member_cid)

    def entities_retrieve_rtr_recent_file_post_v1(
        self,
        body: dict = Field(description="Request JSON body for `entities_retrieve_rtr_recent_file_post_v1` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """RetrieveRecentRTRFile retrieves a recently fetched RTR file and adds it to a case"""
        return self._call(operation="entities_retrieve_rtr_recent_file_post_v1", query_params=None, body_params=body, error_message="entities_retrieve_rtr_recent_file_post_v1 failed", member_cid=member_cid)

    def entities_template_snapshots_get_v1(
        self,
        ids: list[str] | None = Field(default=None, description="Snapshot IDs"),
        template_ids: list[str] | None = Field(default=None, description="Retrieves the latest snapshot for all Template IDs"),
        versions: list[str] | None = Field(default=None, description="Retrieve a specific version of the template from the parallel array template_ids. A value of zero will return the latest snapshot."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get template snapshots"""
        return self._call(operation="entities_template_snapshots_get_v1", query_params={"ids": ids, "template_ids": template_ids, "versions": versions}, error_message="entities_template_snapshots_get_v1 failed", member_cid=member_cid)

    def queries_access_tags_get_v1(
        self,
        filter: str | None = Field(default=None, description="FQL filter expression"),
        sort: str | None = Field(default=None, description="Sort expression"),
        limit: int | None = Field(default=None, description="Page size"),
        after: str | None = Field(default=None, description="Pagination token"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Query access tags"""
        return self._call(operation="queries_access_tags_get_v1", query_params={"filter": filter, "sort": sort, "limit": limit, "after": after}, error_message="queries_access_tags_get_v1 failed", member_cid=member_cid)

    def queries_fields_get_v1(
        self,
        filter: str | None = Field(default=None, description="FQL filter expression"),
        limit: int | None = Field(default=None, description="Page size"),
        offset: int | None = Field(default=None, description="Page offset"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Query fields"""
        return self._call(operation="queries_fields_get_v1", query_params={"filter": filter, "limit": limit, "offset": offset}, error_message="queries_fields_get_v1 failed", member_cid=member_cid)

    def queries_file_details_get_v1(
        self,
        filter: str | None = Field(default=None, description="FQL filter expression"),
        limit: int | None = Field(default=None, description="Page size"),
        offset: int | None = Field(default=None, description="Page offset"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Query for ids of file details"""
        return self._call(operation="queries_file_details_get_v1", query_params={"filter": filter, "limit": limit, "offset": offset}, error_message="queries_file_details_get_v1 failed", member_cid=member_cid)

    def queries_notification_groups_get_v2(
        self,
        filter: str | None = Field(default=None, description="FQL filter expression"),
        sort: str | None = Field(default=None, description="Sort expression"),
        limit: int | None = Field(default=None, description="Page size"),
        offset: int | None = Field(default=None, description="Page offset"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Query notification groups"""
        return self._call(operation="queries_notification_groups_get_v2", query_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset}, error_message="queries_notification_groups_get_v2 failed", member_cid=member_cid)

    def queries_template_snapshots_get_v1(
        self,
        filter: str | None = Field(default=None, description="FQL filter expression"),
        limit: int | None = Field(default=None, description="Page size"),
        offset: int | None = Field(default=None, description="Page offset"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Query template snapshots"""
        return self._call(operation="queries_template_snapshots_get_v1", query_params={"filter": filter, "limit": limit, "offset": offset}, error_message="queries_template_snapshots_get_v1 failed", member_cid=member_cid)
