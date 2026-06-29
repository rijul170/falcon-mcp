"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `cloud_snapshots` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenCloudSnapshotsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `cloud_snapshots` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.combined_detections, name="combined_detections")
        self._add_tool(server=server, method=self.get_credentials_iac, name="get_credentials_iac")
        self._add_tool(server=server, method=self.get_credentials_mixin0, name="get_credentials_mixin0")
        self._add_tool(server=server, method=self.get_scan_report, name="get_scan_report")
        self._add_tool(server=server, method=self.read_deployments_combined, name="read_deployments_combined")
        self._add_tool(server=server, method=self.read_deployments_entities, name="read_deployments_entities")
        self._add_tool(server=server, method=self.create_deployment_entity, name="create_deployment_entity", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.register_cspm_snapshot_account, name="register_cspm_snapshot_account", annotations=WRITE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def combined_detections(
        self,
        filter: str | None = Field(default=None, description="Search IaC detections using a query in Falcon Query Language (FQL). Supported filters: detection_uuid,file_name,last_detected,platform,project_name,project_owner,project_ref,provider,resource_name ,rule_category,rule_name,rule_type,rule_uuid,service,severity"),
        limit: int | None = Field(default=None, description="the upper-bound on the number of records to retrieve"),
        offset: int | None = Field(default=None, description="The offset from where to begin."),
        sort: str | None = Field(default=None, description="fields to sort the records on. Supported columns: [detection_uuid file_name last_detected platform project_name project_owner project_ref provider resource_name rule_category rule_name rule_type rule_uuid service severity]"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search IaC Detections using a query in Falcon Query Language"""
        return self._call(operation="CombinedDetections", query_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort}, error_message="CombinedDetections failed", member_cid=member_cid)

    def create_deployment_entity(
        self,
        body: dict = Field(description="Request JSON body for `CreateDeploymentEntity` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Launch a snapshot scan for a given cloud asset"""
        return self._call(operation="CreateDeploymentEntity", query_params=None, body_params=body, error_message="CreateDeploymentEntity failed", member_cid=member_cid)

    def get_credentials_iac(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Gets the registry credentials (external endpoint)"""
        return self._call(operation="GetCredentialsIAC", query_params=None, error_message="GetCredentialsIAC failed", member_cid=member_cid)

    def get_credentials_mixin0(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Gets the registry credentials"""
        return self._call(operation="GetCredentialsMixin0", query_params=None, error_message="GetCredentialsMixin0 failed", member_cid=member_cid)

    def get_scan_report(
        self,
        ids: list[str] = Field(description="the instance identifiers to fetch the report for"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """retrieve the scan report for an instance"""
        return self._call(operation="GetScanReport", query_params={"ids": ids}, error_message="GetScanReport failed", member_cid=member_cid)

    def read_deployments_combined(
        self,
        filter: str | None = Field(default=None, description="Search snapshot jobs using a query in Falcon Query Language (FQL). Supported filters: account_id,asset_identifier,cloud_provider,region,status"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve."),
        offset: int | None = Field(default=None, description="The offset from where to begin."),
        sort: str | None = Field(default=None, description="The fields to sort the records on. Supported columns: [account_id asset_identifier cloud_provider instance_type last_updated_timestamp region status]"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve snapshot jobs identified by the provided IDs"""
        return self._call(operation="ReadDeploymentsCombined", query_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort}, error_message="ReadDeploymentsCombined failed", member_cid=member_cid)

    def read_deployments_entities(
        self,
        ids: list[str] | None = Field(default=None, description="Search snapshot jobs by ids - The maximum amount is 100 IDs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve snapshot jobs identified by the provided IDs"""
        return self._call(operation="ReadDeploymentsEntities", query_params={"ids": ids}, error_message="ReadDeploymentsEntities failed", member_cid=member_cid)

    def register_cspm_snapshot_account(
        self,
        body: dict = Field(description="Request JSON body for `RegisterCspmSnapshotAccount` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Register customer cloud account for snapshot scanning"""
        return self._call(operation="RegisterCspmSnapshotAccount", query_params=None, body_params=body, error_message="RegisterCspmSnapshotAccount failed", member_cid=member_cid)
