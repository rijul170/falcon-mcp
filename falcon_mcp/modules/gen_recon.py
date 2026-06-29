"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `recon` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenReconModule(GeneratedModuleBase):
    """Generated tools for the Falcon `recon` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_actions_v1, name="get_actions_v1")
        self._add_tool(server=server, method=self.get_export_jobs_v1, name="get_export_jobs_v1")
        self._add_tool(server=server, method=self.get_file_content_for_export_jobs_v1, name="get_file_content_for_export_jobs_v1")
        self._add_tool(server=server, method=self.get_notifications_detailed_translated_v1, name="get_notifications_detailed_translated_v1")
        self._add_tool(server=server, method=self.get_notifications_detailed_v1, name="get_notifications_detailed_v1")
        self._add_tool(server=server, method=self.get_notifications_exposed_data_records_v1, name="get_notifications_exposed_data_records_v1")
        self._add_tool(server=server, method=self.get_notifications_translated_v1, name="get_notifications_translated_v1")
        self._add_tool(server=server, method=self.preview_rule_v1, name="preview_rule_v1")
        self._add_tool(server=server, method=self.query_actions_v1, name="query_actions_v1")
        self._add_tool(server=server, method=self.query_notifications_exposed_data_records_v1, name="query_notifications_exposed_data_records_v1")
        self._add_tool(server=server, method=self.create_actions_v1, name="create_actions_v1", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.create_export_jobs_v1, name="create_export_jobs_v1", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_action_v1, name="update_action_v1", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_action_v1, name="delete_action_v1", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_export_jobs_v1, name="delete_export_jobs_v1", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def create_actions_v1(
        self,
        body: dict = Field(description="Request JSON body for `CreateActionsV1` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create actions for a monitoring rule. Accepts a list of actions that will be attached to the monitoring rule."""
        return self._call(operation="CreateActionsV1", query_params=None, body_params=body, error_message="CreateActionsV1 failed", member_cid=member_cid)

    def create_export_jobs_v1(
        self,
        body: dict = Field(description="Request JSON body for `CreateExportJobsV1` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Launch asynchronous export job. Use the job ID to poll the status of the job using GET /entities/exports/v1."""
        return self._call(operation="CreateExportJobsV1", query_params=None, body_params=body, error_message="CreateExportJobsV1 failed", member_cid=member_cid)

    def delete_action_v1(
        self,
        id: str = Field(description="ID of the action."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete an action from a monitoring rule based on the action ID."""
        return self._call(operation="DeleteActionV1", query_params={"id": id}, error_message="DeleteActionV1 failed", member_cid=member_cid)

    def delete_export_jobs_v1(
        self,
        ids: list[str] = Field(description="Export Job IDs."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete export jobs (and their associated file(s)) based on their IDs."""
        return self._call(operation="DeleteExportJobsV1", query_params={"ids": ids}, error_message="DeleteExportJobsV1 failed", member_cid=member_cid)

    def get_actions_v1(
        self,
        ids: list[str] = Field(description="Action IDs."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get actions based on their IDs. IDs can be retrieved using the GET /queries/actions/v1 endpoint."""
        return self._call(operation="GetActionsV1", query_params={"ids": ids}, error_message="GetActionsV1 failed", member_cid=member_cid)

    def get_export_jobs_v1(
        self,
        ids: list[str] = Field(description="Export Job IDs."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get the status of export jobs based on their IDs. Export jobs can be launched by calling POST /entities/exports/v1. When a job is complete, use the job ID to download the file(s) associated with it using GET entities/export-files/v1."""
        return self._call(operation="GetExportJobsV1", query_params={"ids": ids}, error_message="GetExportJobsV1 failed", member_cid=member_cid)

    def get_file_content_for_export_jobs_v1(
        self,
        id: str = Field(description="Export Job ID."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Download the file associated with a job ID."""
        return self._call(operation="GetFileContentForExportJobsV1", query_params={"id": id}, error_message="GetFileContentForExportJobsV1 failed", member_cid=member_cid)

    def get_notifications_detailed_translated_v1(
        self,
        ids: list[str] = Field(description="Notification IDs."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get detailed notifications based on their IDs. These include the translated raw intelligence content that generated the match or part of it."""
        return self._call(operation="GetNotificationsDetailedTranslatedV1", query_params={"ids": ids}, error_message="GetNotificationsDetailedTranslatedV1 failed", member_cid=member_cid)

    def get_notifications_detailed_v1(
        self,
        ids: list[str] = Field(description="Notification IDs."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get detailed notifications based on their IDs. These include the raw intelligence content that generated the match or part of it."""
        return self._call(operation="GetNotificationsDetailedV1", query_params={"ids": ids}, error_message="GetNotificationsDetailedV1 failed", member_cid=member_cid)

    def get_notifications_exposed_data_records_v1(
        self,
        ids: list[str] = Field(description="Notification exposed records IDs."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get notifications exposed data records based on their IDs. IDs can be retrieved using the GET /queries/notifications-exposed-data-records/v1 endpoint. The associate notification can be fetched using the /entities/notifications/v* endpoints"""
        return self._call(operation="GetNotificationsExposedDataRecordsV1", query_params={"ids": ids}, error_message="GetNotificationsExposedDataRecordsV1 failed", member_cid=member_cid)

    def get_notifications_translated_v1(
        self,
        ids: list[str] = Field(description="Notification IDs."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get notifications based on their IDs. IDs can be retrieved using the GET /queries/notifications/v1 endpoint. This endpoint will return translated notification content. The only target language available is English."""
        return self._call(operation="GetNotificationsTranslatedV1", query_params={"ids": ids}, error_message="GetNotificationsTranslatedV1 failed", member_cid=member_cid)

    def preview_rule_v1(
        self,
        body: dict = Field(description="Request JSON body for `PreviewRuleV1` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Preview rules notification count and distribution. This will return aggregations on: channel, count, site."""
        return self._call(operation="PreviewRuleV1", query_params=None, body_params=body, error_message="PreviewRuleV1 failed", member_cid=member_cid)

    def query_actions_v1(
        self,
        offset: int | None = Field(default=None, description="Starting index of overall result set from which to return IDs."),
        limit: int | None = Field(default=None, description="Number of IDs to return. Offset + limit should NOT be above 10K."),
        sort: str | None = Field(default=None, description="Possible order by fields: created_timestamp, updated_timestamp. Ex: 'updated_timestamp|desc'."),
        filter: str | None = Field(default=None, description="FQL query to filter actions by. Possible filter properties are: [id cid user_uuid rule_id type frequency content_format trigger_matchless recipients status created_timestamp updated_timestamp]"),
        q: str | None = Field(default=None, description="Free text search across all indexed fields"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Query actions based on provided criteria. Use the IDs from this response to get the action entities on GET /entities/actions/v1."""
        return self._call(operation="QueryActionsV1", query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter, "q": q}, error_message="QueryActionsV1 failed", member_cid=member_cid)

    def query_notifications_exposed_data_records_v1(
        self,
        offset: int | None = Field(default=None, description="Starting index of overall result set from which to return ids."),
        limit: int | None = Field(default=None, description="Number of IDs to return. Offset + limit should NOT be above 10K."),
        sort: str | None = Field(default=None, description="Possible order by fields: created_date, updated_date. Ex: 'updated_date|desc'."),
        filter: str | None = Field(default=None, description="FQL query to filter notifications by. Possible filter properties are: [id cid user_uuid created_date exposure_date rule.id rule.name rule.topic notification_id notification_group_id source_category site site_id author author_id user_id user_name credentials_url credentials_domain credentials_ip email domain hash_type display_name full_name user_ip phone_number company job_position file.name file.complete_data_set file.download_urls location.postal_code location.city location.state location.federal_district location.federal_admin_region location.country_code social.twitter_id social.facebook_id social.vk_id social.vk_token social.aim_id social.icq_id social.msn_id social.instagram_id social.skype_id financial.credit_card financial.bank_account financial.crypto_currency_addresses login_id credential_status _all bot.operating_system.hardware_id bot.bot_id]"),
        q: str | None = Field(default=None, description="Free text search across all indexed fields."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Query notifications exposed data records based on provided criteria. Use the IDs from this response to get the notification +entities on GET /entities/notifications-exposed-data-records/v1"""
        return self._call(operation="QueryNotificationsExposedDataRecordsV1", query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter, "q": q}, error_message="QueryNotificationsExposedDataRecordsV1 failed", member_cid=member_cid)

    def update_action_v1(
        self,
        body: dict = Field(description="Request JSON body for `UpdateActionV1` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update an action for a monitoring rule."""
        return self._call(operation="UpdateActionV1", query_params=None, body_params=body, error_message="UpdateActionV1 failed", member_cid=member_cid)
