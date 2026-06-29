"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `cloud_aws_registration` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenCloudAwsRegistrationModule(GeneratedModuleBase):
    """Generated tools for the Falcon `cloud_aws_registration` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.cloud_registration_aws_get_accounts, name="cloud_registration_aws_get_accounts")
        self._add_tool(server=server, method=self.cloud_registration_aws_query_accounts, name="cloud_registration_aws_query_accounts")
        self._add_tool(server=server, method=self.cloud_registration_aws_create_account, name="cloud_registration_aws_create_account", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.cloud_registration_aws_update_account, name="cloud_registration_aws_update_account", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.cloud_registration_aws_validate_accounts, name="cloud_registration_aws_validate_accounts", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.cloud_registration_aws_delete_account, name="cloud_registration_aws_delete_account", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.cloud_registration_aws_trigger_health_check, name="cloud_registration_aws_trigger_health_check", annotations=WRITE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def cloud_registration_aws_create_account(
        self,
        body: dict = Field(description="Request JSON body for `cloud_registration_aws_create_account` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Creates a new account in our system for a customer."""
        return self._call(operation="cloud_registration_aws_create_account", query_params=None, body_params=body, error_message="cloud_registration_aws_create_account failed", member_cid=member_cid)

    def cloud_registration_aws_delete_account(
        self,
        ids: list[str] | None = Field(default=None, description="AWS account IDs to remove"),
        organization_ids: list[str] | None = Field(default=None, description="AWS organization IDs to remove"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deletes an existing AWS account or organization in our system."""
        return self._call(operation="cloud_registration_aws_delete_account", query_params={"ids": ids, "organization-ids": organization_ids}, error_message="cloud_registration_aws_delete_account failed", member_cid=member_cid)

    def cloud_registration_aws_get_accounts(
        self,
        ids: list[str] | None = Field(default=None, description="AWS account IDs to filter"),
        organization_ids: list[str] | None = Field(default=None, description="AWS organization IDs to filter"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve existing AWS accounts by account IDs or organization IDs"""
        return self._call(operation="cloud_registration_aws_get_accounts", query_params={"ids": ids, "organization-ids": organization_ids}, error_message="cloud_registration_aws_get_accounts failed", member_cid=member_cid)

    def cloud_registration_aws_query_accounts(
        self,
        products: list[str] = Field(description="Products registered for an account"),
        features: list[str] = Field(description="Features registered for an account"),
        organization_ids: list[str] | None = Field(default=None, description="Organization IDs used to filter accounts"),
        account_status: str | None = Field(default=None, description="Account status to filter results by."),
        limit: int | None = Field(default=None, description="The maximum number of items to return. When not specified or 0, 100 is used. When larger than 500, 500 is used."),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from."),
        group_by: str | None = Field(default=None, description="Field to group by."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve existing AWS accounts by account IDs"""
        return self._call(operation="cloud_registration_aws_query_accounts", query_params={"organization-ids": organization_ids, "products": products, "features": features, "account-status": account_status, "limit": limit, "offset": offset, "group_by": group_by}, error_message="cloud_registration_aws_query_accounts failed", member_cid=member_cid)

    def cloud_registration_aws_trigger_health_check(
        self,
        account_ids: list[str] | None = Field(default=None, description="AWS Account IDs."),
        organization_ids: list[str] | None = Field(default=None, description="Organization IDs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Trigger health check scan for AWS accounts"""
        return self._call(operation="cloud_registration_aws_trigger_health_check", query_params={"account-ids": account_ids, "organization-ids": organization_ids}, error_message="cloud_registration_aws_trigger_health_check failed", member_cid=member_cid)

    def cloud_registration_aws_update_account(
        self,
        body: dict = Field(description="Request JSON body for `cloud_registration_aws_update_account` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Patches a existing account in our system for a customer."""
        return self._call(operation="cloud_registration_aws_update_account", query_params=None, body_params=body, error_message="cloud_registration_aws_update_account failed", member_cid=member_cid)

    def cloud_registration_aws_validate_accounts(
        self,
        account_id: str | None = Field(default=None, description="AWS Account ID. organization-id shouldn't be specified if this is specified"),
        iam_role_arn: str | None = Field(default=None, description="IAM Role ARN"),
        organization_id: str | None = Field(default=None, description="AWS organization ID to validate master account. account-id shouldn't be specified if this is specified"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Validates the AWS account registration status, and discover organization child accounts if organization is specified"""
        return self._call(operation="cloud_registration_aws_validate_accounts", query_params={"account-id": account_id, "iam-role-arn": iam_role_arn, "organization-id": organization_id}, error_message="cloud_registration_aws_validate_accounts failed", member_cid=member_cid)
