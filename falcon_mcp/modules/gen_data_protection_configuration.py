"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `data_protection_configuration` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenDataProtectionConfigurationModule(GeneratedModuleBase):
    """Generated tools for the Falcon `data_protection_configuration` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.entities_classification_get_v2, name="entities_classification_get_v2")
        self._add_tool(server=server, method=self.entities_cloud_application_get, name="entities_cloud_application_get")
        self._add_tool(server=server, method=self.entities_content_pattern_get, name="entities_content_pattern_get")
        self._add_tool(server=server, method=self.entities_enterprise_account_get, name="entities_enterprise_account_get")
        self._add_tool(server=server, method=self.entities_file_type_get, name="entities_file_type_get")
        self._add_tool(server=server, method=self.entities_local_application_get, name="entities_local_application_get")
        self._add_tool(server=server, method=self.entities_local_application_group_get, name="entities_local_application_group_get")
        self._add_tool(server=server, method=self.entities_policy_get_v2, name="entities_policy_get_v2")
        self._add_tool(server=server, method=self.entities_sensitivity_label_get_v2, name="entities_sensitivity_label_get_v2")
        self._add_tool(server=server, method=self.entities_web_location_get_v2, name="entities_web_location_get_v2")
        self._add_tool(server=server, method=self.queries_classification_get_v2, name="queries_classification_get_v2")
        self._add_tool(server=server, method=self.queries_cloud_application_get_v2, name="queries_cloud_application_get_v2")
        self._add_tool(server=server, method=self.queries_content_pattern_get_v2, name="queries_content_pattern_get_v2")
        self._add_tool(server=server, method=self.queries_enterprise_account_get_v2, name="queries_enterprise_account_get_v2")
        self._add_tool(server=server, method=self.queries_file_type_get_v2, name="queries_file_type_get_v2")
        self._add_tool(server=server, method=self.queries_local_application_get, name="queries_local_application_get")
        self._add_tool(server=server, method=self.queries_local_application_group_get, name="queries_local_application_group_get")
        self._add_tool(server=server, method=self.queries_policy_get_v2, name="queries_policy_get_v2")
        self._add_tool(server=server, method=self.queries_sensitivity_label_get_v2, name="queries_sensitivity_label_get_v2")
        self._add_tool(server=server, method=self.queries_web_location_get_v2, name="queries_web_location_get_v2")
        self._add_tool(server=server, method=self.entities_classification_patch_v2, name="entities_classification_patch_v2", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_classification_post_v2, name="entities_classification_post_v2", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_cloud_application_create, name="entities_cloud_application_create", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_cloud_application_patch, name="entities_cloud_application_patch", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_content_pattern_create, name="entities_content_pattern_create", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_content_pattern_patch, name="entities_content_pattern_patch", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_enterprise_account_create, name="entities_enterprise_account_create", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_enterprise_account_patch, name="entities_enterprise_account_patch", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_local_application_create, name="entities_local_application_create", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_local_application_group_create, name="entities_local_application_group_create", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_local_application_group_patch, name="entities_local_application_group_patch", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_local_application_patch, name="entities_local_application_patch", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_policy_patch_v2, name="entities_policy_patch_v2", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_policy_post_v2, name="entities_policy_post_v2", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_policy_precedence_post_v1, name="entities_policy_precedence_post_v1", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_sensitivity_label_create_v2, name="entities_sensitivity_label_create_v2", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_web_location_create_v2, name="entities_web_location_create_v2", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_web_location_patch_v2, name="entities_web_location_patch_v2", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_classification_delete_v2, name="entities_classification_delete_v2", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_cloud_application_delete, name="entities_cloud_application_delete", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_content_pattern_delete, name="entities_content_pattern_delete", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_enterprise_account_delete, name="entities_enterprise_account_delete", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_local_application_delete, name="entities_local_application_delete", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_local_application_group_delete, name="entities_local_application_group_delete", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_policy_delete_v2, name="entities_policy_delete_v2", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_sensitivity_label_delete_v2, name="entities_sensitivity_label_delete_v2", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_web_location_delete_v2, name="entities_web_location_delete_v2", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def entities_classification_delete_v2(
        self,
        ids: list[str] = Field(description="IDs of the classifications to delete"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deletes classifications that match the provided ids"""
        return self._call(operation="entities_classification_delete_v2", query_params={"ids": ids}, error_message="entities_classification_delete_v2 failed", member_cid=member_cid)

    def entities_classification_get_v2(
        self,
        ids: list[str] = Field(description="IDs of the classifications to get"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Gets the classifications that match the provided ids"""
        return self._call(operation="entities_classification_get_v2", query_params={"ids": ids}, error_message="entities_classification_get_v2 failed", member_cid=member_cid)

    def entities_classification_patch_v2(
        self,
        body: dict = Field(description="Request JSON body for `entities_classification_patch_v2` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update classifications"""
        return self._call(operation="entities_classification_patch_v2", query_params=None, body_params=body, error_message="entities_classification_patch_v2 failed", member_cid=member_cid)

    def entities_classification_post_v2(
        self,
        body: dict = Field(description="Request JSON body for `entities_classification_post_v2` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create classifications"""
        return self._call(operation="entities_classification_post_v2", query_params=None, body_params=body, error_message="entities_classification_post_v2 failed", member_cid=member_cid)

    def entities_cloud_application_create(
        self,
        body: dict = Field(description="Request JSON body for `entities_cloud_application_create` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Persist the given cloud application for the provided entity instance"""
        return self._call(operation="entities_cloud_application_create", query_params=None, body_params=body, error_message="entities_cloud_application_create failed", member_cid=member_cid)

    def entities_cloud_application_delete(
        self,
        ids: list[str] = Field(description="The id of the cloud application to delete."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete cloud application"""
        return self._call(operation="entities_cloud_application_delete", query_params={"ids": ids}, error_message="entities_cloud_application_delete failed", member_cid=member_cid)

    def entities_cloud_application_get(
        self,
        ids: list[str] = Field(description="The cloud application id(s) to get."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get a particular cloud-application"""
        return self._call(operation="entities_cloud_application_get", query_params={"ids": ids}, error_message="entities_cloud_application_get failed", member_cid=member_cid)

    def entities_cloud_application_patch(
        self,
        id: str = Field(description="The cloud app id to update."),
        body: dict = Field(description="Request JSON body for `entities_cloud_application_patch` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update a cloud application"""
        return self._call(operation="entities_cloud_application_patch", query_params={"id": id}, body_params=body, error_message="entities_cloud_application_patch failed", member_cid=member_cid)

    def entities_content_pattern_create(
        self,
        body: dict = Field(description="Request JSON body for `entities_content_pattern_create` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Persist the given content pattern for the provided entity instance"""
        return self._call(operation="entities_content_pattern_create", query_params=None, body_params=body, error_message="entities_content_pattern_create failed", member_cid=member_cid)

    def entities_content_pattern_delete(
        self,
        ids: list[str] = Field(description="The id(s) of the content pattern to delete."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete content pattern"""
        return self._call(operation="entities_content_pattern_delete", query_params={"ids": ids}, error_message="entities_content_pattern_delete failed", member_cid=member_cid)

    def entities_content_pattern_get(
        self,
        ids: list[str] = Field(description="The content-pattern id(s) to get."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get a particular content-pattern(s)"""
        return self._call(operation="entities_content_pattern_get", query_params={"ids": ids}, error_message="entities_content_pattern_get failed", member_cid=member_cid)

    def entities_content_pattern_patch(
        self,
        id: str = Field(description="The id of the content pattern to patch."),
        body: dict = Field(description="Request JSON body for `entities_content_pattern_patch` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update a content pattern"""
        return self._call(operation="entities_content_pattern_patch", query_params={"id": id}, body_params=body, error_message="entities_content_pattern_patch failed", member_cid=member_cid)

    def entities_enterprise_account_create(
        self,
        body: dict = Field(description="Request JSON body for `entities_enterprise_account_create` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Persist the given enterprise account for the provided entity instance"""
        return self._call(operation="entities_enterprise_account_create", query_params=None, body_params=body, error_message="entities_enterprise_account_create failed", member_cid=member_cid)

    def entities_enterprise_account_delete(
        self,
        ids: list[str] = Field(description="The id of the enterprise account to delete."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete enterprise account"""
        return self._call(operation="entities_enterprise_account_delete", query_params={"ids": ids}, error_message="entities_enterprise_account_delete failed", member_cid=member_cid)

    def entities_enterprise_account_get(
        self,
        ids: list[str] = Field(description="The enterprise-account id(s) to get."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get a particular enterprise-account(s)"""
        return self._call(operation="entities_enterprise_account_get", query_params={"ids": ids}, error_message="entities_enterprise_account_get failed", member_cid=member_cid)

    def entities_enterprise_account_patch(
        self,
        id: str = Field(description="The id of the enterprise account to update."),
        body: dict = Field(description="Request JSON body for `entities_enterprise_account_patch` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update a enterprise account"""
        return self._call(operation="entities_enterprise_account_patch", query_params={"id": id}, body_params=body, error_message="entities_enterprise_account_patch failed", member_cid=member_cid)

    def entities_file_type_get(
        self,
        ids: list[str] = Field(description="The file-type id(s) to get."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get a particular file-type"""
        return self._call(operation="entities_file_type_get", query_params={"ids": ids}, error_message="entities_file_type_get failed", member_cid=member_cid)

    def entities_local_application_create(
        self,
        body: dict = Field(description="Request JSON body for `entities_local_application_create` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Persist the given local application for the provided entity instance"""
        return self._call(operation="entities_local_application_create", query_params=None, body_params=body, error_message="entities_local_application_create failed", member_cid=member_cid)

    def entities_local_application_delete(
        self,
        ids: list[str] = Field(description="The id of the local application to delete."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Soft Delete local application. The application wont be visible anymore, but will still be in the database"""
        return self._call(operation="entities_local_application_delete", query_params={"ids": ids}, error_message="entities_local_application_delete failed", member_cid=member_cid)

    def entities_local_application_get(
        self,
        ids: list[str] = Field(description="The local application id(s) to get."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get a particular local application"""
        return self._call(operation="entities_local_application_get", query_params={"ids": ids}, error_message="entities_local_application_get failed", member_cid=member_cid)

    def entities_local_application_group_create(
        self,
        body: dict = Field(description="Request JSON body for `entities_local_application_group_create` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Persist the given local application group for the provided entity instance"""
        return self._call(operation="entities_local_application_group_create", query_params=None, body_params=body, error_message="entities_local_application_group_create failed", member_cid=member_cid)

    def entities_local_application_group_delete(
        self,
        ids: list[str] = Field(description="The id of the local application group to delete."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Soft Delete local application. The application won't be visible anymore, but will still be in the database"""
        return self._call(operation="entities_local_application_group_delete", query_params={"ids": ids}, error_message="entities_local_application_group_delete failed", member_cid=member_cid)

    def entities_local_application_group_get(
        self,
        ids: list[str] = Field(description="The local application group id(s) to get."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get particular local application groups"""
        return self._call(operation="entities_local_application_group_get", query_params={"ids": ids}, error_message="entities_local_application_group_get failed", member_cid=member_cid)

    def entities_local_application_group_patch(
        self,
        id: str = Field(description="The local app id to update."),
        body: dict = Field(description="Request JSON body for `entities_local_application_group_patch` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update a local application group"""
        return self._call(operation="entities_local_application_group_patch", query_params={"id": id}, body_params=body, error_message="entities_local_application_group_patch failed", member_cid=member_cid)

    def entities_local_application_patch(
        self,
        id: str = Field(description="The local app id to update."),
        body: dict = Field(description="Request JSON body for `entities_local_application_patch` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update a local application"""
        return self._call(operation="entities_local_application_patch", query_params={"id": id}, body_params=body, error_message="entities_local_application_patch failed", member_cid=member_cid)

    def entities_policy_delete_v2(
        self,
        ids: list[str] = Field(description="IDs of the policies to delete"),
        platform_name: str = Field(description="platform name of the policies to update, either 'win' or 'mac'"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deletes policies that match the provided ids"""
        return self._call(operation="entities_policy_delete_v2", query_params={"ids": ids, "platform_name": platform_name}, error_message="entities_policy_delete_v2 failed", member_cid=member_cid)

    def entities_policy_get_v2(
        self,
        ids: list[str] = Field(description="IDs of the policies to get"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Gets policies that match the provided ids"""
        return self._call(operation="entities_policy_get_v2", query_params={"ids": ids}, error_message="entities_policy_get_v2 failed", member_cid=member_cid)

    def entities_policy_patch_v2(
        self,
        platform_name: str = Field(description="platform name of the policies to update, either 'win' or 'mac'"),
        body: dict = Field(description="Request JSON body for `entities_policy_patch_v2` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update policies"""
        return self._call(operation="entities_policy_patch_v2", query_params={"platform_name": platform_name}, body_params=body, error_message="entities_policy_patch_v2 failed", member_cid=member_cid)

    def entities_policy_post_v2(
        self,
        platform_name: str = Field(description="platform name of the policies to update, either 'win' or 'mac'"),
        body: dict = Field(description="Request JSON body for `entities_policy_post_v2` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create policies"""
        return self._call(operation="entities_policy_post_v2", query_params={"platform_name": platform_name}, body_params=body, error_message="entities_policy_post_v2 failed", member_cid=member_cid)

    def entities_policy_precedence_post_v1(
        self,
        body: dict = Field(description="Request JSON body for `entities_policy_precedence_post_v1` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update Policy Precedence"""
        return self._call(operation="entities_policy_precedence_post_v1", query_params=None, body_params=body, error_message="entities_policy_precedence_post_v1 failed", member_cid=member_cid)

    def entities_sensitivity_label_create_v2(
        self,
        body: dict = Field(description="Request JSON body for `entities_sensitivity_label_create_v2` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create new sensitivity label (V2)"""
        return self._call(operation="entities_sensitivity_label_create_v2", query_params=None, body_params=body, error_message="entities_sensitivity_label_create_v2 failed", member_cid=member_cid)

    def entities_sensitivity_label_delete_v2(
        self,
        ids: list[str] = Field(description="The sensitivity label entity id(s) to delete."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete sensitivity labels matching the IDs (V2)"""
        return self._call(operation="entities_sensitivity_label_delete_v2", query_params={"ids": ids}, error_message="entities_sensitivity_label_delete_v2 failed", member_cid=member_cid)

    def entities_sensitivity_label_get_v2(
        self,
        ids: list[str] = Field(description="The sensitivity label entity id(s) to get."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get sensitivity label matching the IDs (V2)"""
        return self._call(operation="entities_sensitivity_label_get_v2", query_params={"ids": ids}, error_message="entities_sensitivity_label_get_v2 failed", member_cid=member_cid)

    def entities_web_location_create_v2(
        self,
        body: dict = Field(description="Request JSON body for `entities_web_location_create_v2` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Persist the given web-locations"""
        return self._call(operation="entities_web_location_create_v2", query_params=None, body_params=body, error_message="entities_web_location_create_v2 failed", member_cid=member_cid)

    def entities_web_location_delete_v2(
        self,
        ids: list[str] = Field(description="The ids of the web-location to delete."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete web-location"""
        return self._call(operation="entities_web_location_delete_v2", query_params={"ids": ids}, error_message="entities_web_location_delete_v2 failed", member_cid=member_cid)

    def entities_web_location_get_v2(
        self,
        ids: list[str] = Field(description="The web-location entity id(s) to get."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get web-location entities matching the provided ID(s)"""
        return self._call(operation="entities_web_location_get_v2", query_params={"ids": ids}, error_message="entities_web_location_get_v2 failed", member_cid=member_cid)

    def entities_web_location_patch_v2(
        self,
        id: str = Field(description="The web-location entity id to update."),
        body: dict = Field(description="Request JSON body for `entities_web_location_patch_v2` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update a web-location"""
        return self._call(operation="entities_web_location_patch_v2", query_params={"id": id}, body_params=body, error_message="entities_web_location_patch_v2 failed", member_cid=member_cid)

    def queries_classification_get_v2(
        self,
        filter: str | None = Field(default=None, description="Filter results by specific attributes , allowed attributes are [name created_at modified_at properties.content_patterns properties.content_patterns_operator properties.file_types properties.sensitivity_labels created_by modified_by properties.evidence_duplication_enabled properties.protection_mode properties.web_sources]"),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        limit: int | None = Field(default=None, description="The maximum records to return"),
        sort: str | None = Field(default=None, description="The property to sort by, allowed fields are :[name created_at modified_at]"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for classifications that match the provided criteria"""
        return self._call(operation="queries_classification_get_v2", query_params={"filter": filter, "offset": offset, "limit": limit, "sort": sort}, error_message="queries_classification_get_v2 failed", member_cid=member_cid)

    def queries_cloud_application_get_v2(
        self,
        filter: str | None = Field(default=None, description="Optional filter for searching cloud applications. Allowed filters are 'name' (string), 'type' (array of strings representing the tier, accepted values are: integrated, predefined, custom), 'deleted' (boolean), supports_network_inspection (boolean) and 'application_group_id' (string)"),
        sort: str | None = Field(default=None, description="The sort instructions to order by on. Allowed values are 'name' (string), 'type' (array of strings representing the tier, accepted values are: integrated, predefined, custom), 'deleted' (boolean) and 'application_group_id' (string)"),
        limit: int | None = Field(default=None, description="The number of items to return in this response (default: 100, max: 500). Use with the offset parameter to manage pagination of results."),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from. Use with the limit parameter to manage pagination of results."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get all cloud-application IDs matching the query with filter"""
        return self._call(operation="queries_cloud_application_get_v2", query_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset}, error_message="queries_cloud_application_get_v2 failed", member_cid=member_cid)

    def queries_content_pattern_get_v2(
        self,
        filter: str | None = Field(default=None, description="The filter to use when finding content patterns. Allowed filters are 'name', 'type', 'category', 'region', 'example', 'created_at', 'updated_at' and 'deleted'"),
        sort: str | None = Field(default=None, description="The sort instructions to order by on. Allowed values are 'name', 'type', 'category', 'region', 'created_at', 'updated_at', 'example' and 'deleted'"),
        limit: int | None = Field(default=None, description="The number of items to return in this response (default: 100, max: 500). Use with the offset parameter to manage pagination of results."),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from. Use with the limit parameter to manage pagination of results."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get all content-pattern IDs matching the query with filter"""
        return self._call(operation="queries_content_pattern_get_v2", query_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset}, error_message="queries_content_pattern_get_v2 failed", member_cid=member_cid)

    def queries_enterprise_account_get_v2(
        self,
        filter: str | None = Field(default=None, description="The filter to use when finding enterprise accounts. Allowed filters are 'name', 'application_group_id', 'deleted', 'created_at' and 'updated_at'"),
        sort: str | None = Field(default=None, description="The sort instructions to order by on. Allowed values are 'name', 'application_group_id', 'deleted', 'created_at' and 'updated_at'"),
        limit: int | None = Field(default=None, description="The number of items to return in this response (default: 100, max: 500). Use with the offset parameter to manage pagination of results."),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from. Use with the limit parameter to manage pagination of results."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get all enterprise-account IDs matching the query with filter"""
        return self._call(operation="queries_enterprise_account_get_v2", query_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset}, error_message="queries_enterprise_account_get_v2 failed", member_cid=member_cid)

    def queries_file_type_get_v2(
        self,
        filter: str | None = Field(default=None, description="The filter to use when finding file types. Allowed filter is 'name', 'created_at' and 'updated_at'"),
        sort: str | None = Field(default=None, description="The sort instructions to order by on. Allowed values are 'name', 'created_at' and 'updated_at'"),
        limit: int | None = Field(default=None, description="The number of items to return in this response (default: 100, max: 500). Use with the offset parameter to manage pagination of results."),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from. Use with the limit parameter to manage pagination of results."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get all file-type IDs matching the query with filter"""
        return self._call(operation="queries_file_type_get_v2", query_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset}, error_message="queries_file_type_get_v2 failed", member_cid=member_cid)

    def queries_local_application_get(
        self,
        filter: str | None = Field(default=None, description="Optional filter for searching local applications. Allowed filters are 'name' (string), is_deleted (boolean), 'created_at' and 'updated_at'"),
        limit: int | None = Field(default=None, description="The number of items to return in this response (default: 100, max: 500). Use with the offset parameter to manage pagination of results."),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from. Use with the limit parameter to manage pagination of results."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get all local-application IDs matching the query with filter"""
        return self._call(operation="queries_local_application_get", query_params={"filter": filter, "limit": limit, "offset": offset}, error_message="queries_local_application_get failed", member_cid=member_cid)

    def queries_local_application_group_get(
        self,
        filter: str | None = Field(default=None, description="Optional filter for searching local application group. Allowed filters are 'name' (string), is_deleted (boolean), platform (string), 'created_at' and 'updated_at'"),
        limit: int | None = Field(default=None, description="The number of items to return in this response (default: 100, max: 500). Use with the offset parameter to manage pagination of results."),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from. Use with the limit parameter to manage pagination of results."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get all local application group IDs matching the query with filter"""
        return self._call(operation="queries_local_application_group_get", query_params={"filter": filter, "limit": limit, "offset": offset}, error_message="queries_local_application_group_get failed", member_cid=member_cid)

    def queries_policy_get_v2(
        self,
        platform_name: str = Field(description="platform name of the policies to search, either 'win' or 'mac'"),
        filter: str | None = Field(default=None, description="Filter results by specific attributes , allowed attributes are [name properties.enable_content_inspection properties.be_exclude_domains properties.be_upload_timeout_response properties.be_paste_clipboard_max_size properties.evidence_storage_max_size precedence created_at modified_at properties.similarity_threshold properties.enable_clipboard_inspection properties.evidence_encrypted_enabled properties.enable_network_inspection properties.besplash_message_source properties.min_confidence_level properties.unsupported_browsers_action properties.similarity_detection properties.classifications properties.besplash_enabled properties.be_paste_timeout_response properties.be_paste_clipboard_min_size_unit properties.be_paste_clipboard_over_size_behaviour_block properties.browsers_without_active_extension description is_enabled created_by properties.max_file_size_to_inspect_unit properties.block_all_data_access properties.be_paste_timeout_duration_milliseconds properties.be_paste_clipboard_min_size is_default modified_by properties.enable_context_inspection properties.inspection_depth properties.evidence_download_enabled properties.besplash_custom_message properties.be_upload_timeout_duration_seconds properties.enable_end_user_notifications_unsupported_browser properties.custom_allow_notification properties.custom_block_notification properties.be_paste_clipboard_max_size_unit properties.evidence_storage_free_disk_perc properties.max_file_size_to_inspect properties.allow_notifications properties.block_notifications properties.evidence_duplication_enabled_default properties.network_inspection_files_exceeding_size_limit]"),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        limit: int | None = Field(default=None, description="The maximum records to return"),
        sort: str | None = Field(default=None, description="The property to sort by, allowed fields are :[modified_at name precedence created_at]"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for policies that match the provided criteria"""
        return self._call(operation="queries_policy_get_v2", query_params={"platform_name": platform_name, "filter": filter, "offset": offset, "limit": limit, "sort": sort}, error_message="queries_policy_get_v2 failed", member_cid=member_cid)

    def queries_sensitivity_label_get_v2(
        self,
        filter: str | None = Field(default=None, description="The filter to use when finding sensitivity labels. The only allowed filters are 'name', 'display_name', 'external_id' and 'deleted'"),
        sort: str | None = Field(default=None, description="The sort instructions to order by on. Allowed values are 'name', 'display_name', 'deleted', 'created_at' and 'updated_at'"),
        limit: int | None = Field(default=None, description="The number of items to return in this response (default: 100, max: 500). Use with the offset parameter to manage pagination of results."),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from. Use with the limit parameter to manage pagination of results."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get all sensitivity label IDs matching the query with filter"""
        return self._call(operation="queries_sensitivity_label_get_v2", query_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset}, error_message="queries_sensitivity_label_get_v2 failed", member_cid=member_cid)

    def queries_web_location_get_v2(
        self,
        filter: str | None = Field(default=None, description="The filter to use when finding web locations. Allowed filters are 'name', 'type', 'deleted', 'application_id', 'provider_location_id' and 'enterprise_account_id'"),
        type: str | None = Field(default=None, description="The type of entity to query. Allowed values are 'predefined' and 'custom'"),
        limit: int | None = Field(default=None, description="The number of items to return in this response (default: 100, max: 500). Use with the offset parameter to manage pagination of results."),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from. Use with the limit parameter to manage pagination of results."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get web-location IDs matching the query with filter"""
        return self._call(operation="queries_web_location_get_v2", query_params={"filter": filter, "type": type, "limit": limit, "offset": offset}, error_message="queries_web_location_get_v2 failed", member_cid=member_cid)
