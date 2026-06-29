"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `d4c_registration` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenD4cRegistrationModule(GeneratedModuleBase):
    """Generated tools for the Falcon `d4c_registration` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.discover_cloud_azure_download_certificate, name="discover_cloud_azure_download_certificate")
        self._add_tool(server=server, method=self.get_cspmgcp_user_scripts_attachment_d4c_registration, name="get_cspmgcp_user_scripts_attachment_d4c_registration")
        self._add_tool(server=server, method=self.get_d4_caws_account_scripts_attachment, name="get_d4_caws_account_scripts_attachment")
        self._add_tool(server=server, method=self.get_d4_c_aws_account, name="get_d4_c_aws_account")
        self._add_tool(server=server, method=self.get_d4_c_aws_console_setup_ur_ls, name="get_d4_c_aws_console_setup_ur_ls")
        self._add_tool(server=server, method=self.get_d4_ccgp_account, name="get_d4_ccgp_account")
        self._add_tool(server=server, method=self.get_d4_cgcp_service_accounts_ext, name="get_d4_cgcp_service_accounts_ext")
        self._add_tool(server=server, method=self.get_d4_cgcp_user_scripts, name="get_d4_cgcp_user_scripts")
        self._add_tool(server=server, method=self.get_d4_cgcp_user_scripts_attachment, name="get_d4_cgcp_user_scripts_attachment")
        self._add_tool(server=server, method=self.get_discover_cloud_azure_account, name="get_discover_cloud_azure_account")
        self._add_tool(server=server, method=self.get_discover_cloud_azure_tenant_i_ds, name="get_discover_cloud_azure_tenant_i_ds")
        self._add_tool(server=server, method=self.get_discover_cloud_azure_user_scripts, name="get_discover_cloud_azure_user_scripts")
        self._add_tool(server=server, method=self.get_discover_cloud_azure_user_scripts_attachment, name="get_discover_cloud_azure_user_scripts_attachment")
        self._add_tool(server=server, method=self.get_horizon_d4_c_scripts, name="get_horizon_d4_c_scripts")
        self._add_tool(server=server, method=self.connect_d4_cgcp_account, name="connect_d4_cgcp_account", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.create_d4_c_aws_account, name="create_d4_c_aws_account", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.create_d4_cgcp_account, name="create_d4_cgcp_account", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.create_discover_cloud_azure_account, name="create_discover_cloud_azure_account", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_d4_cgcp_service_accounts_ext, name="update_d4_cgcp_service_accounts_ext", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_discover_cloud_azure_account_client_id, name="update_discover_cloud_azure_account_client_id", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_d4_c_aws_account, name="delete_d4_c_aws_account", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_d4_cgcp_account, name="delete_d4_cgcp_account", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def connect_d4_cgcp_account(
        self,
        body: dict = Field(description="Request JSON body for `ConnectD4CGCPAccount` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Creates a new GCP account with newly-uploaded service account or connects with existing service account with only the following fields: parent_id, parent_type and service_account_id"""
        return self._call(operation="ConnectD4CGCPAccount", query_params=None, body_params=body, error_message="ConnectD4CGCPAccount failed", member_cid=member_cid)

    def create_d4_c_aws_account(
        self,
        body: dict = Field(description="Request JSON body for `CreateD4CAwsAccount` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Creates a new account in our system for a customer and generates a script for them to run in their AWS cloud environment to grant us access."""
        return self._call(operation="CreateD4CAwsAccount", query_params=None, body_params=body, error_message="CreateD4CAwsAccount failed", member_cid=member_cid)

    def create_d4_cgcp_account(
        self,
        body: dict = Field(description="Request JSON body for `CreateD4CGCPAccount` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Creates a new account in our system for a customer and generates a new service account for them to add access to in their GCP environment to grant us access."""
        return self._call(operation="CreateD4CGCPAccount", query_params=None, body_params=body, error_message="CreateD4CGCPAccount failed", member_cid=member_cid)

    def create_discover_cloud_azure_account(
        self,
        body: dict = Field(description="Request JSON body for `CreateDiscoverCloudAzureAccount` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Creates a new account in our system for a customer and generates a script for them to run in their cloud environment to grant us access."""
        return self._call(operation="CreateDiscoverCloudAzureAccount", query_params=None, body_params=body, error_message="CreateDiscoverCloudAzureAccount failed", member_cid=member_cid)

    def delete_d4_c_aws_account(
        self,
        ids: list[str] | None = Field(default=None, description="AWS account IDs to remove"),
        organization_ids: list[str] | None = Field(default=None, description="AWS organization IDs to remove"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deletes an existing AWS account or organization in our system."""
        return self._call(operation="DeleteD4CAwsAccount", query_params={"ids": ids, "organization-ids": organization_ids}, error_message="DeleteD4CAwsAccount failed", member_cid=member_cid)

    def delete_d4_cgcp_account(
        self,
        ids: list[str] | None = Field(default=None, description="Hierarchical Resource IDs of accounts"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deletes a GCP account from the system."""
        return self._call(operation="DeleteD4CGCPAccount", query_params={"ids": ids}, error_message="DeleteD4CGCPAccount failed", member_cid=member_cid)

    def discover_cloud_azure_download_certificate(
        self,
        tenant_id: list[str] = Field(description="Azure Tenant ID"),
        refresh: bool | None = Field(default=None, description="Setting to true will invalidate the current certificate and generate a new certificate"),
        years_valid: str | None = Field(default=None, description="Years the certificate should be valid (only used when refresh=true)"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns JSON object(s) that contain the base64 encoded certificate for a service principal."""
        return self._call(operation="DiscoverCloudAzureDownloadCertificate", query_params={"tenant_id": tenant_id, "refresh": refresh, "years_valid": years_valid}, error_message="DiscoverCloudAzureDownloadCertificate failed", member_cid=member_cid)

    def get_cspmgcp_user_scripts_attachment_d4c_registration(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Return a script for customer to run in their cloud environment to grant us access to their GCP environment as a downloadable attachment"""
        return self._call(operation="GetCSPMGCPUserScriptsAttachment", query_params=None, error_message="GetCSPMGCPUserScriptsAttachment failed", member_cid=member_cid)

    def get_d4_caws_account_scripts_attachment(
        self,
        ids: list[str] | None = Field(default=None, description="AWS account IDs"),
        template: str | None = Field(default=None, description="Template to be rendered"),
        accounts: list[str] | None = Field(default=None, description="The list of accounts to register"),
        behavior_assessment_enabled: str | None = Field(default=None, description="`behavior_assessment_enabled` query parameter."),
        sensor_management_enabled: str | None = Field(default=None, description="`sensor_management_enabled` query parameter."),
        dspm_enabled: str | None = Field(default=None, description="`dspm_enabled` query parameter."),
        dspm_regions: list[str] | None = Field(default=None, description="`dspm_regions` query parameter."),
        dspm_host_account_id: str | None = Field(default=None, description="`dspm_host_account_id` query parameter."),
        dspm_host_integration_role_name: str | None = Field(default=None, description="`dspm_host_integration_role_name` query parameter."),
        dspm_host_scanner_role_name: str | None = Field(default=None, description="`dspm_host_scanner_role_name` query parameter."),
        dspm_role: str | None = Field(default=None, description="`dspm_role` query parameter."),
        vulnerability_scanning_enabled: str | None = Field(default=None, description="`vulnerability_scanning_enabled` query parameter."),
        vulnerability_scanning_regions: list[str] | None = Field(default=None, description="`vulnerability_scanning_regions` query parameter."),
        vulnerability_scanning_host_account_id: str | None = Field(default=None, description="`vulnerability_scanning_host_account_id` query parameter."),
        vulnerability_scanning_host_integration_role_name: str | None = Field(default=None, description="`vulnerability_scanning_host_integration_role_name` query parameter."),
        vulnerability_scanning_host_scanner_role_name: str | None = Field(default=None, description="`vulnerability_scanning_host_scanner_role_name` query parameter."),
        vulnerability_scanning_role: str | None = Field(default=None, description="`vulnerability_scanning_role` query parameter."),
        use_existing_cloudtrail: str | None = Field(default=None, description="`use_existing_cloudtrail` query parameter."),
        organization_id: str | None = Field(default=None, description="The AWS organization ID to be registered"),
        organizational_unit_ids: list[str] | None = Field(default=None, description="The AWS Organizational Unit IDs to be registered"),
        aws_profile: str | None = Field(default=None, description="The AWS profile to be used during registration"),
        aws_region: str | None = Field(default=None, description="The AWS region to be used during registration"),
        iam_role_arn: str | None = Field(default=None, description="The custom IAM role to be used during registration"),
        falcon_client_id: str | None = Field(default=None, description="The Falcon client ID used during registration"),
        idp_enabled: str | None = Field(default=None, description="Set to true to enable Identity Protection feature"),
        tags: str | None = Field(default=None, description="Base64 encoded JSON string to be used as AWS tags"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Return a script for customer to run in their cloud environment to grant us access to their AWS environment as a downloadable attachment."""
        return self._call(operation="GetD4CAWSAccountScriptsAttachment", query_params={"ids": ids, "template": template, "accounts": accounts, "behavior_assessment_enabled": behavior_assessment_enabled, "sensor_management_enabled": sensor_management_enabled, "dspm_enabled": dspm_enabled, "dspm_regions": dspm_regions, "dspm_host_account_id": dspm_host_account_id, "dspm_host_integration_role_name": dspm_host_integration_role_name, "dspm_host_scanner_role_name": dspm_host_scanner_role_name, "dspm_role": dspm_role, "vulnerability_scanning_enabled": vulnerability_scanning_enabled, "vulnerability_scanning_regions": vulnerability_scanning_regions, "vulnerability_scanning_host_account_id": vulnerability_scanning_host_account_id, "vulnerability_scanning_host_integration_role_name": vulnerability_scanning_host_integration_role_name, "vulnerability_scanning_host_scanner_role_name": vulnerability_scanning_host_scanner_role_name, "vulnerability_scanning_role": vulnerability_scanning_role, "use_existing_cloudtrail": use_existing_cloudtrail, "organization_id": organization_id, "organizational_unit_ids": organizational_unit_ids, "aws_profile": aws_profile, "aws_region": aws_region, "iam_role_arn": iam_role_arn, "falcon_client_id": falcon_client_id, "idp_enabled": idp_enabled, "tags": tags}, error_message="GetD4CAWSAccountScriptsAttachment failed", member_cid=member_cid)

    def get_d4_c_aws_account(
        self,
        scan_type: str | None = Field(default=None, description="Type of scan, dry or full, to perform on selected accounts"),
        ids: list[str] | None = Field(default=None, description="AWS account IDs"),
        organization_ids: list[str] | None = Field(default=None, description="AWS organization IDs"),
        status: str | None = Field(default=None, description="Account status to filter results by."),
        limit: int | None = Field(default=None, description="The maximum records to return. Defaults to 100."),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        migrated: str | None = Field(default=None, description="Only return migrated d4c accounts"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns information about the current status of an AWS account."""
        return self._call(operation="GetD4CAwsAccount", query_params={"scan-type": scan_type, "ids": ids, "organization-ids": organization_ids, "status": status, "limit": limit, "offset": offset, "migrated": migrated}, error_message="GetD4CAwsAccount failed", member_cid=member_cid)

    def get_d4_c_aws_console_setup_ur_ls(
        self,
        region: str | None = Field(default=None, description="Region"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Return a URL for customer to visit in their cloud environment to grant us access to their AWS environment."""
        return self._call(operation="GetD4CAwsConsoleSetupURLs", query_params={"region": region}, error_message="GetD4CAwsConsoleSetupURLs failed", member_cid=member_cid)

    def get_d4_ccgp_account(
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
        return self._call(operation="GetD4CCGPAccount", query_params={"parent_type": parent_type, "ids": ids, "scan-type": scan_type, "status": status, "limit": limit, "offset": offset, "sort": sort}, error_message="GetD4CCGPAccount failed", member_cid=member_cid)

    def get_d4_cgcp_service_accounts_ext(
        self,
        id: str | None = Field(default=None, description="Service Account ID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns the service account id and client email for external clients."""
        return self._call(operation="GetD4CGCPServiceAccountsExt", query_params={"id": id}, error_message="GetD4CGCPServiceAccountsExt failed", member_cid=member_cid)

    def get_d4_cgcp_user_scripts(
        self,
        parent_type: str | None = Field(default=None, description="GCP Hierarchy Parent Type, organization/folder/project"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Return a script for customer to run in their cloud environment to grant us access to their GCP environment"""
        return self._call(operation="GetD4CGCPUserScripts", query_params={"parent_type": parent_type}, error_message="GetD4CGCPUserScripts failed", member_cid=member_cid)

    def get_d4_cgcp_user_scripts_attachment(
        self,
        parent_type: str | None = Field(default=None, description="GCP Hierarchy Parent Type, organization/folder/project"),
        ids: list[str] | None = Field(default=None, description="Hierarchical Resource IDs of accounts"),
        status: str | None = Field(default=None, description="Account status to filter results by."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Return a script for customer to run in their cloud environment to grant us access to their GCP environment as a downloadable attachment"""
        return self._call(operation="GetD4CGCPUserScriptsAttachment", query_params={"parent_type": parent_type, "ids": ids, "status": status}, error_message="GetD4CGCPUserScriptsAttachment failed", member_cid=member_cid)

    def get_discover_cloud_azure_account(
        self,
        ids: list[str] | None = Field(default=None, description="SubscriptionIDs of accounts to select for this status operation. If this is empty then all accounts are returned."),
        tenant_ids: list[str] | None = Field(default=None, description="Tenant ids to filter azure accounts"),
        scan_type: str | None = Field(default=None, description="Type of scan, dry or full, to perform on selected accounts"),
        status: str | None = Field(default=None, description="Account status to filter results by."),
        limit: int | None = Field(default=None, description="The maximum records to return. Defaults to 100."),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Return information about Azure account registration"""
        return self._call(operation="GetDiscoverCloudAzureAccount", query_params={"ids": ids, "tenant_ids": tenant_ids, "scan-type": scan_type, "status": status, "limit": limit, "offset": offset}, error_message="GetDiscoverCloudAzureAccount failed", member_cid=member_cid)

    def get_discover_cloud_azure_tenant_i_ds(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Return available tenant ids for discover for cloud"""
        return self._call(operation="GetDiscoverCloudAzureTenantIDs", query_params=None, error_message="GetDiscoverCloudAzureTenantIDs failed", member_cid=member_cid)

    def get_discover_cloud_azure_user_scripts(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Return a script for customer to run in their cloud environment to grant us access to their Azure environment"""
        return self._call(operation="GetDiscoverCloudAzureUserScripts", query_params=None, error_message="GetDiscoverCloudAzureUserScripts failed", member_cid=member_cid)

    def get_discover_cloud_azure_user_scripts_attachment(
        self,
        tenant_id: list[str] = Field(description="Azure Tenant ID"),
        subscription_ids: list[str] | None = Field(default=None, description="Azure Subscription ID"),
        template: str | None = Field(default=None, description="Template to be rendered"),
        azure_management_group: bool | None = Field(default=None, description="Use Azure Management Group"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Return a script for customer to run in their cloud environment to grant us access to their Azure environment as a downloadable attachment"""
        return self._call(operation="GetDiscoverCloudAzureUserScriptsAttachment", query_params={"tenant-id": tenant_id, "subscription_ids": subscription_ids, "template": template, "azure_management_group": azure_management_group}, error_message="GetDiscoverCloudAzureUserScriptsAttachment failed", member_cid=member_cid)

    def get_horizon_d4_c_scripts(
        self,
        single_account: str | None = Field(default=None, description="Get static script for single account"),
        organization_id: str | None = Field(default=None, description="AWS organization ID"),
        delete: str | None = Field(default=None, description="`delete` query parameter."),
        account_type: str | None = Field(default=None, description="Account type (e.g.: commercial,gov) Only applicable when registering AWS commercial account in a Gov environment"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns static install scripts for Horizon."""
        return self._call(operation="GetHorizonD4CScripts", query_params={"single_account": single_account, "organization-id": organization_id, "delete": delete, "account_type": account_type}, error_message="GetHorizonD4CScripts failed", member_cid=member_cid)

    def update_d4_cgcp_service_accounts_ext(
        self,
        body: dict = Field(description="Request JSON body for `UpdateD4CGCPServiceAccountsExt` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Patches the service account key for external clients."""
        return self._call(operation="UpdateD4CGCPServiceAccountsExt", query_params=None, body_params=body, error_message="UpdateD4CGCPServiceAccountsExt failed", member_cid=member_cid)

    def update_discover_cloud_azure_account_client_id(
        self,
        id: str = Field(description="ClientID to use for the Service Principal associated with the customer's Azure account"),
        object_id: str | None = Field(default=None, description="Object ID to use for the Service Principal associated with the customer's Azure account"),
        tenant_id: str | None = Field(default=None, description="Tenant ID to update client ID for. Required if multiple tenants are registered."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update an Azure service account in our system by with the user-created client_id created with the public key we've provided"""
        return self._call(operation="UpdateDiscoverCloudAzureAccountClientID", query_params={"id": id, "object_id": object_id, "tenant-id": tenant_id}, error_message="UpdateDiscoverCloudAzureAccountClientID failed", member_cid=member_cid)
