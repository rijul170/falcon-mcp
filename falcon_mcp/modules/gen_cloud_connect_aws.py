"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `cloud_connect_aws` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenCloudConnectAwsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `cloud_connect_aws` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_aws_accounts, name="get_aws_accounts")
        self._add_tool(server=server, method=self.get_aws_settings, name="get_aws_settings")
        self._add_tool(server=server, method=self.query_aws_accounts, name="query_aws_accounts")
        self._add_tool(server=server, method=self.query_aws_accounts_for_i_ds, name="query_aws_accounts_for_i_ds")
        self._add_tool(server=server, method=self.create_or_update_aws_settings, name="create_or_update_aws_settings", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.provision_aws_accounts, name="provision_aws_accounts", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_aws_accounts, name="update_aws_accounts", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.verify_aws_account_access, name="verify_aws_account_access", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_aws_accounts, name="delete_aws_accounts", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def create_or_update_aws_settings(
        self,
        body: dict = Field(description="Request JSON body for `CreateOrUpdateAWSSettings` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create or update Global Settings which are applicable to all provisioned AWS accounts"""
        return self._call(operation="CreateOrUpdateAWSSettings", query_params=None, body_params=body, error_message="CreateOrUpdateAWSSettings failed", member_cid=member_cid)

    def delete_aws_accounts(
        self,
        ids: list[str] = Field(description="IDs of accounts to remove"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete a set of AWS Accounts by specifying their IDs"""
        return self._call(operation="DeleteAWSAccounts", query_params={"ids": ids}, error_message="DeleteAWSAccounts failed", member_cid=member_cid)

    def get_aws_accounts(
        self,
        ids: list[str] = Field(description="IDs of accounts to retrieve details"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve a set of AWS Accounts by specifying their IDs"""
        return self._call(operation="GetAWSAccounts", query_params={"ids": ids}, error_message="GetAWSAccounts failed", member_cid=member_cid)

    def get_aws_settings(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve a set of Global Settings which are applicable to all provisioned AWS accounts"""
        return self._call(operation="GetAWSSettings", query_params=None, error_message="GetAWSSettings failed", member_cid=member_cid)

    def provision_aws_accounts(
        self,
        body: dict = Field(description="Request JSON body for `ProvisionAWSAccounts` per the CrowdStrike API schema (required)."),
        mode: str | None = Field(default=None, description="Mode for provisioning. Allowed values are manual or cloudformation. Defaults to manual if not defined."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Provision AWS Accounts by specifying details about the accounts to provision"""
        return self._call(operation="ProvisionAWSAccounts", query_params={"mode": mode}, body_params=body, error_message="ProvisionAWSAccounts failed", member_cid=member_cid)

    def query_aws_accounts(
        self,
        limit: int | None = Field(default=None, description="The maximum records to return. [1-1000]. Defaults to 100."),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        sort: str | None = Field(default=None, description="The property to sort by (e.g. alias.desc or state.asc)"),
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for provisioned AWS Accounts by providing an FQL filter and paging details. Returns a set of AWS accounts which match the filter criteria"""
        return self._call(operation="QueryAWSAccounts", query_params={"limit": limit, "offset": offset, "sort": sort, "filter": filter}, error_message="QueryAWSAccounts failed", member_cid=member_cid)

    def query_aws_accounts_for_i_ds(
        self,
        limit: int | None = Field(default=None, description="The maximum records to return. [1-1000]. Defaults to 100."),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        sort: str | None = Field(default=None, description="The property to sort by (e.g. alias.desc or state.asc)"),
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for provisioned AWS Accounts by providing an FQL filter and paging details. Returns a set of AWS account IDs which match the filter criteria"""
        return self._call(operation="QueryAWSAccountsForIDs", query_params={"limit": limit, "offset": offset, "sort": sort, "filter": filter}, error_message="QueryAWSAccountsForIDs failed", member_cid=member_cid)

    def update_aws_accounts(
        self,
        body: dict = Field(description="Request JSON body for `UpdateAWSAccounts` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update AWS Accounts by specifying the ID of the account and details to update"""
        return self._call(operation="UpdateAWSAccounts", query_params=None, body_params=body, error_message="UpdateAWSAccounts failed", member_cid=member_cid)

    def verify_aws_account_access(
        self,
        ids: list[str] = Field(description="IDs of accounts to verify access on"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Performs an Access Verification check on the specified AWS Account IDs"""
        return self._call(operation="VerifyAWSAccountAccess", query_params={"ids": ids}, error_message="VerifyAWSAccountAccess failed", member_cid=member_cid)
