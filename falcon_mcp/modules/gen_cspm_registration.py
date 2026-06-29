"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `cspm_registration` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenCspmRegistrationModule(GeneratedModuleBase):
    """Generated tools for the Falcon `cspm_registration` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.azure_download_certificate, name="azure_download_certificate")
        self._add_tool(server=server, method=self.get_behavior_detections, name="get_behavior_detections")
        self._add_tool(server=server, method=self.get_cspm_aws_account, name="get_cspm_aws_account")
        self._add_tool(server=server, method=self.get_cspm_aws_account_scripts_attachment, name="get_cspm_aws_account_scripts_attachment")
        self._add_tool(server=server, method=self.get_cspm_aws_console_setup_ur_ls, name="get_cspm_aws_console_setup_ur_ls")
        self._add_tool(server=server, method=self.get_cspm_azure_account, name="get_cspm_azure_account")
        self._add_tool(server=server, method=self.get_cspm_azure_management_group, name="get_cspm_azure_management_group")
        self._add_tool(server=server, method=self.get_cspm_azure_user_scripts_attachment, name="get_cspm_azure_user_scripts_attachment")
        self._add_tool(server=server, method=self.get_cspmcgp_account, name="get_cspmcgp_account")
        self._add_tool(server=server, method=self.get_cspmgcp_account, name="get_cspmgcp_account")
        self._add_tool(server=server, method=self.get_cspmgcp_service_accounts_ext, name="get_cspmgcp_service_accounts_ext")
        self._add_tool(server=server, method=self.get_cspmgcp_user_scripts_attachment, name="get_cspmgcp_user_scripts_attachment")
        self._add_tool(server=server, method=self.get_cspmgcp_validate_accounts_ext, name="get_cspmgcp_validate_accounts_ext")
        self._add_tool(server=server, method=self.get_cspm_policies_details, name="get_cspm_policies_details")
        self._add_tool(server=server, method=self.get_cspm_policy, name="get_cspm_policy")
        self._add_tool(server=server, method=self.get_cspm_policy_settings, name="get_cspm_policy_settings")
        self._add_tool(server=server, method=self.get_cspm_scan_schedule, name="get_cspm_scan_schedule")
        self._add_tool(server=server, method=self.get_configuration_detection_entities, name="get_configuration_detection_entities")
        self._add_tool(server=server, method=self.get_configuration_detection_i_ds_v2, name="get_configuration_detection_i_ds_v2")
        self._add_tool(server=server, method=self.get_configuration_detections, name="get_configuration_detections")
        self._add_tool(server=server, method=self.get_ioa_events, name="get_ioa_events")
        self._add_tool(server=server, method=self.get_ioa_users, name="get_ioa_users")
        self._add_tool(server=server, method=self.get_cloud_event_i_ds, name="get_cloud_event_i_ds")
        self._add_tool(server=server, method=self.azure_refresh_certificate, name="azure_refresh_certificate", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.connect_cspmgcp_account, name="connect_cspmgcp_account", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.create_cspm_aws_account, name="create_cspm_aws_account", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.create_cspm_azure_account, name="create_cspm_azure_account", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.create_cspm_azure_management_group, name="create_cspm_azure_management_group", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.create_cspmgcp_account, name="create_cspmgcp_account", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.patch_cspm_aws_account, name="patch_cspm_aws_account", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_cspm_azure_account, name="update_cspm_azure_account", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_cspm_azure_account_client_id, name="update_cspm_azure_account_client_id", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_cspm_azure_tenant_default_subscription_id, name="update_cspm_azure_tenant_default_subscription_id", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_cspmgcp_account, name="update_cspmgcp_account", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_cspmgcp_service_accounts_ext, name="update_cspmgcp_service_accounts_ext", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_cspm_policy_settings, name="update_cspm_policy_settings", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.validate_cspmgcp_service_account_ext, name="validate_cspmgcp_service_account_ext", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_cspm_aws_account, name="delete_cspm_aws_account", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_cspm_azure_account, name="delete_cspm_azure_account", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_cspm_azure_management_group, name="delete_cspm_azure_management_group", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_cspmgcp_account, name="delete_cspmgcp_account", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_cspm_scan_schedule, name="update_cspm_scan_schedule", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def azure_download_certificate(
        self,
        tenant_id: list[str] = Field(description="Azure Tenant ID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns JSON object(s) that contain the base64 encoded certificate for a service principal."""
        return self._call(operation="AzureDownloadCertificate", query_params={"tenant_id": tenant_id}, error_message="AzureDownloadCertificate failed", member_cid=member_cid)

    def azure_refresh_certificate(
        self,
        tenant_id: list[str] = Field(description="Azure Tenant ID"),
        years_valid: str | None = Field(default=None, description="Years the certificate should be valid. Max 2"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Refresh certificate and returns JSON object(s) that contain the base64 encoded certificate for a service principal."""
        return self._call(operation="AzureRefreshCertificate", query_params={"tenant_id": tenant_id, "years_valid": years_valid}, error_message="AzureRefreshCertificate failed", member_cid=member_cid)

    def connect_cspmgcp_account(
        self,
        body: dict = Field(description="Request JSON body for `ConnectCSPMGCPAccount` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Creates a new GCP account with newly-uploaded service account or connects with existing service account with only the following fields: parent_id, parent_type and service_account_id"""
        return self._call(operation="ConnectCSPMGCPAccount", query_params=None, body_params=body, error_message="ConnectCSPMGCPAccount failed", member_cid=member_cid)

    def create_cspm_aws_account(
        self,
        body: dict = Field(description="Request JSON body for `CreateCSPMAwsAccount` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Creates a new account in our system for a customer and generates a script for them to run in their AWS cloud environment to grant us access."""
        return self._call(operation="CreateCSPMAwsAccount", query_params=None, body_params=body, error_message="CreateCSPMAwsAccount failed", member_cid=member_cid)

    def create_cspm_azure_account(
        self,
        body: dict = Field(description="Request JSON body for `CreateCSPMAzureAccount` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Creates a new account in our system for a customer and generates a script for them to run in their cloud environment to grant us access."""
        return self._call(operation="CreateCSPMAzureAccount", query_params=None, body_params=body, error_message="CreateCSPMAzureAccount failed", member_cid=member_cid)

    def create_cspm_azure_management_group(
        self,
        body: dict = Field(description="Request JSON body for `CreateCSPMAzureManagementGroup` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Creates a new management group in our system for a customer."""
        return self._call(operation="CreateCSPMAzureManagementGroup", query_params=None, body_params=body, error_message="CreateCSPMAzureManagementGroup failed", member_cid=member_cid)

    def create_cspmgcp_account(
        self,
        body: dict = Field(description="Request JSON body for `CreateCSPMGCPAccount` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Creates a new account in our system for a customer and generates a new service account for them to add access to in their GCP environment to grant us access."""
        return self._call(operation="CreateCSPMGCPAccount", query_params=None, body_params=body, error_message="CreateCSPMGCPAccount failed", member_cid=member_cid)

    def delete_cspm_aws_account(
        self,
        ids: list[str] | None = Field(default=None, description="AWS account IDs to remove"),
        organization_ids: list[str] | None = Field(default=None, description="AWS organization IDs to remove"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deletes an existing AWS account or organization in our system."""
        return self._call(operation="DeleteCSPMAwsAccount", query_params={"ids": ids, "organization-ids": organization_ids}, error_message="DeleteCSPMAwsAccount failed", member_cid=member_cid)

    def delete_cspm_azure_account(
        self,
        ids: list[str] | None = Field(default=None, description="Azure subscription IDs to remove"),
        tenant_ids: list[str] | None = Field(default=None, description="Tenant ids to remove"),
        retain_tenant: str | None = Field(default=None, description="`retain_tenant` query parameter."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deletes an Azure subscription from the system."""
        return self._call(operation="DeleteCSPMAzureAccount", query_params={"ids": ids, "tenant_ids": tenant_ids, "retain_tenant": retain_tenant}, error_message="DeleteCSPMAzureAccount failed", member_cid=member_cid)

    def delete_cspm_azure_management_group(
        self,
        tenant_ids: list[str] | None = Field(default=None, description="Tenant ids to remove"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deletes Azure management groups from the system."""
        return self._call(operation="DeleteCSPMAzureManagementGroup", query_params={"tenant_ids": tenant_ids}, error_message="DeleteCSPMAzureManagementGroup failed", member_cid=member_cid)

    def delete_cspmgcp_account(
        self,
        ids: list[str] | None = Field(default=None, description="Hierarchical Resource IDs of accounts"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deletes a GCP account from the system."""
        return self._call(operation="DeleteCSPMGCPAccount", query_params={"ids": ids}, error_message="DeleteCSPMGCPAccount failed", member_cid=member_cid)

    def get_behavior_detections(
        self,
        cloud_provider: str | None = Field(default=None, description="Cloud Provider (e.g.: aws|azure)"),
        service: str | None = Field(default=None, description="Cloud Service (e.g. EC2 | EBS | S3)"),
        account_id: str | None = Field(default=None, description="Cloud Account ID (e.g.: AWS accountID, Azure subscriptionID)"),
        aws_account_id: str | None = Field(default=None, description="AWS Account ID"),
        azure_subscription_id: str | None = Field(default=None, description="Azure Subscription ID"),
        azure_tenant_id: str | None = Field(default=None, description="Azure Tenant ID"),
        state: str | None = Field(default=None, description="State (e.g.: open | closed)"),
        date_time_since: str | None = Field(default=None, description="Filter to get all events after this date, in format RFC3339 : e.g. 2006-01-02T15:04:05Z07:00"),
        since: str | None = Field(default=None, description="Filter events using a duration string (e.g. 24h)"),
        severity: str | None = Field(default=None, description="Policy Severity"),
        next_token: str | None = Field(default=None, description="String to get next page of results, is associated with a previous execution of GetBehaviorDetections. Must include all filters from previous execution."),
        limit: int | None = Field(default=None, description="The maximum records to return. [1-500]"),
        resource_id: list[str] | None = Field(default=None, description="Resource ID"),
        resource_uuid: list[str] | None = Field(default=None, description="Resource UUID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get list of detected behaviors"""
        return self._call(operation="GetBehaviorDetections", query_params={"cloud_provider": cloud_provider, "service": service, "account_id": account_id, "aws_account_id": aws_account_id, "azure_subscription_id": azure_subscription_id, "azure_tenant_id": azure_tenant_id, "state": state, "date_time_since": date_time_since, "since": since, "severity": severity, "next_token": next_token, "limit": limit, "resource_id": resource_id, "resource_uuid": resource_uuid}, error_message="GetBehaviorDetections failed", member_cid=member_cid)

    def get_cspm_aws_account(
        self,
        scan_type: str | None = Field(default=None, description="Type of scan, dry or full, to perform on selected accounts"),
        ids: list[str] | None = Field(default=None, description="AWS account IDs"),
        iam_role_arns: list[str] | None = Field(default=None, description="AWS IAM role ARNs"),
        organization_ids: list[str] | None = Field(default=None, description="AWS organization IDs"),
        status: str | None = Field(default=None, description="Account status to filter results by."),
        limit: int | None = Field(default=None, description="The maximum records to return. Defaults to 100."),
        cspm_lite: str | None = Field(default=None, description="Only return CSPM Lite accounts"),
        migrated: str | None = Field(default=None, description="Only return migrated d4c accounts"),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        group_by: str | None = Field(default=None, description="Field to group by."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns information about the current status of an AWS account."""
        return self._call(operation="GetCSPMAwsAccount", query_params={"scan-type": scan_type, "ids": ids, "iam_role_arns": iam_role_arns, "organization-ids": organization_ids, "status": status, "limit": limit, "cspm_lite": cspm_lite, "migrated": migrated, "offset": offset, "group_by": group_by}, error_message="GetCSPMAwsAccount failed", member_cid=member_cid)

    def get_cspm_aws_account_scripts_attachment(
        self,
        ids: list[str] | None = Field(default=None, description="AWS account IDs"),
        template: str | None = Field(default=None, description="Template to be rendered"),
        account_type: str | None = Field(default=None, description="Type of account, it can be commercial or gov"),
        accounts: list[str] | None = Field(default=None, description="The list of accounts to register, values should be in the form: account,profile"),
        behavior_assessment_enabled: str | None = Field(default=None, description="`behavior_assessment_enabled` query parameter."),
        sensor_management_enabled: str | None = Field(default=None, description="`sensor_management_enabled` query parameter."),
        dspm_enabled: str | None = Field(default=None, description="`dspm_enabled` query parameter."),
        dspm_regions: list[str] | None = Field(default=None, description="`dspm_regions` query parameter."),
        dspm_role: str | None = Field(default=None, description="`dspm_role` query parameter."),
        use_existing_cloudtrail: str | None = Field(default=None, description="`use_existing_cloudtrail` query parameter."),
        organization_id: str | None = Field(default=None, description="The AWS organization ID to be registered"),
        aws_profile: str | None = Field(default=None, description="The AWS profile to be used during registration"),
        custom_role_name: str | None = Field(default=None, description="The custom IAM role to be used during registration"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Return a script for customer to run in their cloud environment to grant us access to their AWS environment as a downloadable attachment."""
        return self._call(operation="GetCSPMAwsAccountScriptsAttachment", query_params={"ids": ids, "template": template, "account_type": account_type, "accounts": accounts, "behavior_assessment_enabled": behavior_assessment_enabled, "sensor_management_enabled": sensor_management_enabled, "dspm_enabled": dspm_enabled, "dspm_regions": dspm_regions, "dspm_role": dspm_role, "use_existing_cloudtrail": use_existing_cloudtrail, "organization_id": organization_id, "aws_profile": aws_profile, "custom_role_name": custom_role_name}, error_message="GetCSPMAwsAccountScriptsAttachment failed", member_cid=member_cid)

    def get_cspm_aws_console_setup_ur_ls(
        self,
        ids: list[str] | None = Field(default=None, description="AWS account IDs"),
        use_existing_cloudtrail: str | None = Field(default=None, description="`use_existing_cloudtrail` query parameter."),
        region: str | None = Field(default=None, description="Region"),
        tags: str | None = Field(default=None, description="Base64 encoded JSON string to be used as AWS tags"),
        template: str | None = Field(default=None, description="Template to be rendered"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Return a URL for customer to visit in their cloud environment to grant us access to their AWS environment."""
        return self._call(operation="GetCSPMAwsConsoleSetupURLs", query_params={"ids": ids, "use_existing_cloudtrail": use_existing_cloudtrail, "region": region, "tags": tags, "template": template}, error_message="GetCSPMAwsConsoleSetupURLs failed", member_cid=member_cid)

    def get_cspm_azure_account(
        self,
        ids: list[str] | None = Field(default=None, description="SubscriptionIDs of accounts to select for this status operation. If this is empty then all accounts are returned."),
        tenant_ids: list[str] | None = Field(default=None, description="Tenant ids to filter azure accounts"),
        scan_type: str | None = Field(default=None, description="Type of scan, dry or full, to perform on selected accounts"),
        status: str | None = Field(default=None, description="Account status to filter results by."),
        cspm_lite: str | None = Field(default=None, description="Only return CSPM Lite accounts"),
        limit: int | None = Field(default=None, description="The maximum records to return. Defaults to 100."),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Return information about Azure account registration"""
        return self._call(operation="GetCSPMAzureAccount", query_params={"ids": ids, "tenant_ids": tenant_ids, "scan-type": scan_type, "status": status, "cspm_lite": cspm_lite, "limit": limit, "offset": offset}, error_message="GetCSPMAzureAccount failed", member_cid=member_cid)

    def get_cspm_azure_management_group(
        self,
        tenant_ids: list[str] | None = Field(default=None, description="Tenant ids to filter azure accounts"),
        limit: int | None = Field(default=None, description="The maximum records to return. Defaults to 100."),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Return information about Azure management group registration"""
        return self._call(operation="GetCSPMAzureManagementGroup", query_params={"tenant_ids": tenant_ids, "limit": limit, "offset": offset}, error_message="GetCSPMAzureManagementGroup failed", member_cid=member_cid)

    def get_cspm_azure_user_scripts_attachment(
        self,
        tenant_id: str | None = Field(default=None, description="Tenant ID to generate script for. Defaults to most recently registered tenant."),
        subscription_ids: list[str] | None = Field(default=None, description="Subscription IDs to generate script for. Defaults to all."),
        account_type: str | None = Field(default=None, description="`account_type` query parameter."),
        template: str | None = Field(default=None, description="Template to be rendered"),
        azure_management_group: bool | None = Field(default=None, description="Use Azure Management Group"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Return a script for customer to run in their cloud environment to grant us access to their Azure environment as a downloadable attachment"""
        return self._call(operation="GetCSPMAzureUserScriptsAttachment", query_params={"tenant-id": tenant_id, "subscription_ids": subscription_ids, "account_type": account_type, "template": template, "azure_management_group": azure_management_group}, error_message="GetCSPMAzureUserScriptsAttachment failed", member_cid=member_cid)

    def get_cspmcgp_account(
        self,
        parent_type: str | None = Field(default=None, description="GCP Hierarchy Parent Type, organization/folder/project"),
        ids: list[str] | None = Field(default=None, description="Hierarchical Resource IDs of accounts"),
        scan_type: str | None = Field(default=None, description="Type of scan, dry or full, to perform on selected accounts"),
        status: str | None = Field(default=None, description="Account status to filter results by."),
        limit: int | None = Field(default=None, description="The maximum records to return. Defaults to 100."),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        sort: str | None = Field(default=None, description="Order fields in ascending or descending order. Ex: parent_type|asc."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns information about the current status of an GCP account."""
        return self._call(operation="GetCSPMCGPAccount", query_params={"parent_type": parent_type, "ids": ids, "scan-type": scan_type, "status": status, "limit": limit, "offset": offset, "sort": sort}, error_message="GetCSPMCGPAccount failed", member_cid=member_cid)

    def get_cspmgcp_account(
        self,
        parent_type: str | None = Field(default=None, description="GCP Hierarchy Parent Type, organization/folder/project"),
        ids: list[str] | None = Field(default=None, description="Hierarchical Resource IDs of accounts"),
        scan_type: str | None = Field(default=None, description="Type of scan, dry or full, to perform on selected accounts"),
        status: str | None = Field(default=None, description="Account status to filter results by."),
        limit: int | None = Field(default=None, description="The maximum records to return. Defaults to 100."),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        sort: str | None = Field(default=None, description="Order fields in ascending or descending order. Ex: parent_type|asc."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns information about the current status of an GCP account."""
        return self._call(operation="GetCSPMGCPAccount", query_params={"parent_type": parent_type, "ids": ids, "scan-type": scan_type, "status": status, "limit": limit, "offset": offset, "sort": sort}, error_message="GetCSPMGCPAccount failed", member_cid=member_cid)

    def get_cspmgcp_service_accounts_ext(
        self,
        id: str | None = Field(default=None, description="Service Account ID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns the service account id and client email for external clients."""
        return self._call(operation="GetCSPMGCPServiceAccountsExt", query_params={"id": id}, error_message="GetCSPMGCPServiceAccountsExt failed", member_cid=member_cid)

    def get_cspmgcp_user_scripts_attachment(
        self,
        parent_type: str | None = Field(default=None, description="GCP Hierarchy Parent Type, organization/folder/project"),
        ids: list[str] | None = Field(default=None, description="Hierarchical Resource IDs of accounts"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Return a script for customer to run in their cloud environment to grant us access to their GCP environment as a downloadable attachment"""
        return self._call(operation="GetCSPMGCPUserScriptsAttachment", query_params={"parent_type": parent_type, "ids": ids}, error_message="GetCSPMGCPUserScriptsAttachment failed", member_cid=member_cid)

    def get_cspmgcp_validate_accounts_ext(
        self,
        body: dict = Field(description="Request JSON body for `GetCSPMGCPValidateAccountsExt` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Run a synchronous health check."""
        return self._call(operation="GetCSPMGCPValidateAccountsExt", query_params=None, body_params=body, error_message="GetCSPMGCPValidateAccountsExt failed", member_cid=member_cid)

    def get_cspm_policies_details(
        self,
        ids: list[str] = Field(description="Policy IDs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Given an array of policy IDs, returns detailed policies information."""
        return self._call(operation="GetCSPMPoliciesDetails", query_params={"ids": ids}, error_message="GetCSPMPoliciesDetails failed", member_cid=member_cid)

    def get_cspm_policy(
        self,
        ids: int = Field(description="Policy ID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Given a policy ID, returns detailed policy information."""
        return self._call(operation="GetCSPMPolicy", query_params={"ids": ids}, error_message="GetCSPMPolicy failed", member_cid=member_cid)

    def get_cspm_policy_settings(
        self,
        service: str | None = Field(default=None, description="Service type to filter policy settings by."),
        policy_id: str | None = Field(default=None, description="Policy ID"),
        cloud_platform: str | None = Field(default=None, description="Cloud Platform (e.g.: aws|azure|gcp)"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns information about current policy settings."""
        return self._call(operation="GetCSPMPolicySettings", query_params={"service": service, "policy-id": policy_id, "cloud-platform": cloud_platform}, error_message="GetCSPMPolicySettings failed", member_cid=member_cid)

    def get_cspm_scan_schedule(
        self,
        cloud_platform: list[str] | None = Field(default=None, description="Cloud Platform"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns scan schedule configuration for one or more cloud platforms."""
        return self._call(operation="GetCSPMScanSchedule", query_params={"cloud-platform": cloud_platform}, error_message="GetCSPMScanSchedule failed", member_cid=member_cid)

    def get_configuration_detection_entities(
        self,
        ids: list[str] = Field(description="detection ids"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get misconfigurations based on the ID - including custom policy detections in addition to default policy detections."""
        return self._call(operation="GetConfigurationDetectionEntities", query_params={"ids": ids}, error_message="GetConfigurationDetectionEntities failed", member_cid=member_cid)

    def get_configuration_detection_i_ds_v2(
        self,
        filter: str | None = Field(default=None, description="use_current_scan_ids - *use this to get records for latest scans (ignored when next_token is set)* account_name account_id agent_id attack_types azure_subscription_id cloud_provider cloud_service_keyword custom_policy_id is_managed policy_id policy_type resource_id region status scan _time severity severity_string"),
        sort: str | None = Field(default=None, description="account_name account_id attack_types azure_subscription_id cloud_provider cloud_s ervice_keyword status is_managed policy_id policy_type resource_id region scan_time severity severity _string timestamp"),
        limit: int | None = Field(default=None, description="The max number of detections to return"),
        offset: int | None = Field(default=None, description="Offset returned detections. Cannot be combined with next_token filter"),
        next_token: str | None = Field(default=None, description="String to get next page of results. Cannot be combined with any filter except limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get list of active misconfiguration ids - including custom policy detections in addition to default policy detections."""
        return self._call(operation="GetConfigurationDetectionIDsV2", query_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset, "next_token": next_token}, error_message="GetConfigurationDetectionIDsV2 failed", member_cid=member_cid)

    def get_configuration_detections(
        self,
        cloud_provider: str | None = Field(default=None, description="Cloud Provider (e.g.: aws|azure|gcp)"),
        account_id: str | None = Field(default=None, description="AWS account ID or GCP Project Number or Azure subscription ID"),
        azure_subscription_id: str | None = Field(default=None, description="Azure Subscription ID"),
        azure_tenant_id: str | None = Field(default=None, description="Azure Tenant ID"),
        status: str | None = Field(default=None, description="Status (e.g.: new|reoccurring|all)"),
        region: str | None = Field(default=None, description="Cloud Provider Region"),
        severity: str | None = Field(default=None, description="Policy Severity"),
        service: str | None = Field(default=None, description="Cloud Service (e.g.: EBS|EC2|S3 etc.)"),
        next_token: str | None = Field(default=None, description="String to get next page of results, is associated with a previous execution of GetConfigurationDetections. Cannot be combined with any filter except limit."),
        limit: int | None = Field(default=None, description="The maximum records to return. [1-500]"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get list of active misconfigurations. This endpoint is deprecated, please use GetConfigurationDetectionIDsV2 and GetConfigurationDetectionEntities instead"""
        return self._call(operation="GetConfigurationDetections", query_params={"cloud_provider": cloud_provider, "account_id": account_id, "azure_subscription_id": azure_subscription_id, "azure_tenant_id": azure_tenant_id, "status": status, "region": region, "severity": severity, "service": service, "next_token": next_token, "limit": limit}, error_message="GetConfigurationDetections failed", member_cid=member_cid)

    def get_ioa_events(
        self,
        policy_id: str = Field(description="Policy ID"),
        cloud_provider: str = Field(description="Cloud Provider (e.g.: aws|azure|gcp)"),
        account_id: str | None = Field(default=None, description="Cloud account ID (e.g.: AWS accountID, Azure subscriptionID)"),
        aws_account_id: str | None = Field(default=None, description="AWS accountID"),
        azure_subscription_id: str | None = Field(default=None, description="Azure subscription ID"),
        azure_tenant_id: str | None = Field(default=None, description="Azure tenant ID"),
        user_ids: list[str] | None = Field(default=None, description="user IDs"),
        state: str | None = Field(default=None, description="state"),
        offset: int | None = Field(default=None, description="Starting index of overall result set from which to return events."),
        limit: int | None = Field(default=None, description="The maximum records to return. [1-500]"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """For CSPM IOA events, gets list of IOA events."""
        return self._call(operation="GetIOAEvents", query_params={"policy_id": policy_id, "cloud_provider": cloud_provider, "account_id": account_id, "aws_account_id": aws_account_id, "azure_subscription_id": azure_subscription_id, "azure_tenant_id": azure_tenant_id, "user_ids": user_ids, "state": state, "offset": offset, "limit": limit}, error_message="GetIOAEvents failed", member_cid=member_cid)

    def get_ioa_users(
        self,
        policy_id: str = Field(description="Policy ID"),
        cloud_provider: str = Field(description="Cloud Provider (e.g.: aws|azure|gcp)"),
        state: str | None = Field(default=None, description="state"),
        account_id: str | None = Field(default=None, description="Cloud account ID (e.g.: AWS accountID, Azure subscriptionID)"),
        aws_account_id: str | None = Field(default=None, description="AWS accountID"),
        azure_subscription_id: str | None = Field(default=None, description="Azure subscription ID"),
        azure_tenant_id: str | None = Field(default=None, description="Azure tenant ID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """For CSPM IOA users, gets list of IOA users."""
        return self._call(operation="GetIOAUsers", query_params={"policy_id": policy_id, "state": state, "cloud_provider": cloud_provider, "account_id": account_id, "aws_account_id": aws_account_id, "azure_subscription_id": azure_subscription_id, "azure_tenant_id": azure_tenant_id}, error_message="GetIOAUsers failed", member_cid=member_cid)

    def patch_cspm_aws_account(
        self,
        body: dict = Field(description="Request JSON body for `PatchCSPMAwsAccount` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Patches a existing account in our system for a customer."""
        return self._call(operation="PatchCSPMAwsAccount", query_params=None, body_params=body, error_message="PatchCSPMAwsAccount failed", member_cid=member_cid)

    def update_cspm_azure_account(
        self,
        body: dict = Field(description="Request JSON body for `UpdateCSPMAzureAccount` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Patches a existing account in our system for a customer."""
        return self._call(operation="UpdateCSPMAzureAccount", query_params=None, body_params=body, error_message="UpdateCSPMAzureAccount failed", member_cid=member_cid)

    def update_cspm_azure_account_client_id(
        self,
        id: str = Field(description="ClientID to use for the Service Principal associated with the customer's Azure account"),
        tenant_id: str | None = Field(default=None, description="Tenant ID to update client ID for. Required if multiple tenants are registered."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update an Azure service account in our system by with the user-created client_id created with the public key we've provided"""
        return self._call(operation="UpdateCSPMAzureAccountClientID", query_params={"id": id, "tenant-id": tenant_id}, error_message="UpdateCSPMAzureAccountClientID failed", member_cid=member_cid)

    def update_cspm_azure_tenant_default_subscription_id(
        self,
        subscription_id: str = Field(description="Default Subscription ID to patch for all subscriptions belonged to a tenant."),
        tenant_id: str | None = Field(default=None, description="Tenant ID to update client ID for. Required if multiple tenants are registered."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update an Azure default subscription_id in our system for given tenant_id"""
        return self._call(operation="UpdateCSPMAzureTenantDefaultSubscriptionID", query_params={"tenant-id": tenant_id, "subscription_id": subscription_id}, error_message="UpdateCSPMAzureTenantDefaultSubscriptionID failed", member_cid=member_cid)

    def update_cspmgcp_account(
        self,
        body: dict = Field(description="Request JSON body for `UpdateCSPMGCPAccount` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Patches a existing account in our system for a customer."""
        return self._call(operation="UpdateCSPMGCPAccount", query_params=None, body_params=body, error_message="UpdateCSPMGCPAccount failed", member_cid=member_cid)

    def update_cspmgcp_service_accounts_ext(
        self,
        body: dict = Field(description="Request JSON body for `UpdateCSPMGCPServiceAccountsExt` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Patches the service account key for external clients."""
        return self._call(operation="UpdateCSPMGCPServiceAccountsExt", query_params=None, body_params=body, error_message="UpdateCSPMGCPServiceAccountsExt failed", member_cid=member_cid)

    def update_cspm_policy_settings(
        self,
        body: dict = Field(description="Request JSON body for `UpdateCSPMPolicySettings` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Updates a policy setting - can be used to override policy severity or to disable a policy entirely."""
        return self._call(operation="UpdateCSPMPolicySettings", query_params=None, body_params=body, error_message="UpdateCSPMPolicySettings failed", member_cid=member_cid)

    def update_cspm_scan_schedule(
        self,
        body: dict = Field(description="Request JSON body for `UpdateCSPMScanSchedule` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Updates scan schedule configuration for one or more cloud platforms."""
        return self._call(operation="UpdateCSPMScanSchedule", query_params=None, body_params=body, error_message="UpdateCSPMScanSchedule failed", member_cid=member_cid)

    def validate_cspmgcp_service_account_ext(
        self,
        body: dict = Field(description="Request JSON body for `ValidateCSPMGCPServiceAccountExt` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Validates credentials for a service account"""
        return self._call(operation="ValidateCSPMGCPServiceAccountExt", query_params=None, body_params=body, error_message="ValidateCSPMGCPServiceAccountExt failed", member_cid=member_cid)

    def get_cloud_event_i_ds(
        self,
        id: str = Field(description="IOA Aggregate Event ID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get list of related cloud event LogScale IDs for a given IOA"""
        return self._call(operation="getCloudEventIDs", query_params={"id": id}, error_message="getCloudEventIDs failed", member_cid=member_cid)
