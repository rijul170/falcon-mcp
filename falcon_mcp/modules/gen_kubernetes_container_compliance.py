"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `kubernetes_container_compliance` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenKubernetesContainerComplianceModule(GeneratedModuleBase):
    """Generated tools for the Falcon `kubernetes_container_compliance` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.combined_images_findings, name="combined_images_findings")
        self._add_tool(server=server, method=self.combined_nodes_findings, name="combined_nodes_findings")
        self._add_tool(server=server, method=self.get_rules_metadata_by_id, name="get_rules_metadata_by_id")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def combined_images_findings(
        self,
        filter: str | None = Field(default=None, description="FQL filter expression used to limit the results. Filter fields include: cid, cloud_info.cloud_account_id, cloud_info.cloud_provider, cloud_info.cloud_region, cloud_info.cluster_id, cloud_info.cluster_name, cloud_info.cluster_type, cloud_info.namespace, compliance_finding.asset_uid, compliance_finding.framework_name, compliance_finding.framework_name_version, compliance_finding.framework_version, compliance_finding.id, compliance_finding.severity, compliance_finding.status, image_digest, image_id, image_registry, image_repository, image_tag"),
        after: str | None = Field(default=None, description="A pagination token used with the limit parameter to manage pagination of results. On your first request, don't provide an after token. On subsequent requests, provide the after token from the previous response to continue from that place in the results."),
        limit: int | None = Field(default=None, description="The maximum number of images for which assessments are to be returned: 1-100. Default is 100. Use with the after parameter to manage pagination of results."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns detailed compliance assessment results for container images, providing the information needed to identify compliance violations."""
        return self._call(operation="CombinedImagesFindings", query_params={"filter": filter, "after": after, "limit": limit}, error_message="CombinedImagesFindings failed", member_cid=member_cid)

    def combined_nodes_findings(
        self,
        filter: str | None = Field(default=None, description="FQL filter expression used to limit the results. Filter fields include: cid, cloud_info.cloud_account_id, cloud_info.cloud_provider, cloud_info.cloud_region, cloud_info.cluster_id, cloud_info.cluster_name, cloud_info.cluster_type, compliance_finding.asset_type, compliance_finding.asset_uid, compliance_finding.framework_name, compliance_finding.framework_name_version, compliance_finding.framework_version, compliance_finding.id, compliance_finding.severity, compliance_finding.status, aid, node_id, node_name, node_type"),
        after: str | None = Field(default=None, description="A pagination token used with the limit parameter to manage pagination of results. On your first request, don't provide an after token. On subsequent requests, provide the after token from the previous response to continue from that place in the results."),
        limit: int | None = Field(default=None, description="The maximum number of nodes for which assessments are to be returned: 1-100. Default is 100. Use with the after parameter to manage pagination of results."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns detailed compliance assessment results for kubernetes nodes, providing the information needed to identify compliance violations."""
        return self._call(operation="CombinedNodesFindings", query_params={"filter": filter, "after": after, "limit": limit}, error_message="CombinedNodesFindings failed", member_cid=member_cid)

    def get_rules_metadata_by_id(
        self,
        ids: list[str] = Field(description="comma separated list of rule ids"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve detailed compliance rule information including descriptions, remediation steps, and audit procedures by specifying rule identifiers."""
        return self._call(operation="getRulesMetadataByID", query_params={"ids": ids}, error_message="getRulesMetadataByID failed", member_cid=member_cid)
