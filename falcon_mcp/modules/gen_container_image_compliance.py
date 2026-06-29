"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `container_image_compliance` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenContainerImageComplianceModule(GeneratedModuleBase):
    """Generated tools for the Falcon `container_image_compliance` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.ext_aggregate_cluster_assessments, name="ext_aggregate_cluster_assessments")
        self._add_tool(server=server, method=self.ext_aggregate_failed_containers_by_rules_path, name="ext_aggregate_failed_containers_by_rules_path")
        self._add_tool(server=server, method=self.ext_aggregate_failed_containers_count_by_severity, name="ext_aggregate_failed_containers_count_by_severity")
        self._add_tool(server=server, method=self.ext_aggregate_failed_images_by_rules_path, name="ext_aggregate_failed_images_by_rules_path")
        self._add_tool(server=server, method=self.ext_aggregate_failed_images_count_by_severity, name="ext_aggregate_failed_images_count_by_severity")
        self._add_tool(server=server, method=self.ext_aggregate_failed_rules_by_clusters, name="ext_aggregate_failed_rules_by_clusters")
        self._add_tool(server=server, method=self.ext_aggregate_failed_rules_by_images, name="ext_aggregate_failed_rules_by_images")
        self._add_tool(server=server, method=self.ext_aggregate_failed_rules_count_by_severity, name="ext_aggregate_failed_rules_count_by_severity")
        self._add_tool(server=server, method=self.ext_aggregate_image_assessments, name="ext_aggregate_image_assessments")
        self._add_tool(server=server, method=self.ext_aggregate_rules_assessments, name="ext_aggregate_rules_assessments")
        self._add_tool(server=server, method=self.ext_aggregate_rules_by_status, name="ext_aggregate_rules_by_status")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def ext_aggregate_cluster_assessments(
        self,
        filter: str | None = Field(default=None, description="Filter results using a query in Falcon Query Language (FQL). Supported Filters: cloud_info.cloud_account_id: Cloud account ID cloud_info.cloud_provider: Cloud provider cloud_info.cluster_name: Kubernetes cluster name compliance_finding.framework: Compliance finding framework (available values: CIS) cid: Customer ID cloud_info.cloud_region: Cloud region cloud_info.namespace: Kubernetes namespace"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """get the assessments for each cluster"""
        return self._call(operation="extAggregateClusterAssessments", query_params={"filter": filter}, error_message="extAggregateClusterAssessments failed", member_cid=member_cid)

    def ext_aggregate_failed_containers_by_rules_path(
        self,
        filter: str | None = Field(default=None, description="Filter results using a query in Falcon Query Language (FQL). Supported Filters: image_id: Image ID image_registry: Image registry compliance_finding.name: Compliance finding Name cid: Customer ID cloud_info.cloud_provider: Cloud provider compliance_finding.framework: Compliance finding framework (available values: CIS) cloud_info.namespace: Kubernetes namespace compliance_finding.id: Compliance finding ID image_repository: Image repository cloud_info.cloud_account_id: Cloud account ID image_tag: Image tag cloud_info.cloud_region: Cloud region compliance_finding.severity: Compliance finding severity; available values: 4, 3, 2, 1 (4: critical, 3: high, 2: medium, 1:low) image_digest: Image digest (sha256 digest) cloud_info.cluster_name: Kubernetes cluster name"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """get the containers grouped into rules on which they failed"""
        return self._call(operation="extAggregateFailedContainersByRulesPath", query_params={"filter": filter}, error_message="extAggregateFailedContainersByRulesPath failed", member_cid=member_cid)

    def ext_aggregate_failed_containers_count_by_severity(
        self,
        filter: str | None = Field(default=None, description="Filter results using a query in Falcon Query Language (FQL). Supported Filters: image_registry: Image registry cloud_info.cloud_provider: Cloud provider cid: Customer ID compliance_finding.id: Compliance finding ID compliance_finding.severity: Compliance finding severity; available values: 4, 3, 2, 1 (4: critical, 3: high, 2: medium, 1:low) compliance_finding.name: Compliance finding Name image_id: Image ID cloud_info.cloud_account_id: Cloud account ID image_digest: Image digest (sha256 digest) cloud_info.cluster_name: Kubernetes cluster name compliance_finding.framework: Compliance finding framework (available values: CIS) image_tag: Image tag cloud_info.cloud_region: Cloud region cloud_info.namespace: Kubernetes namespace image_repository: Image repository"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """get the failed containers count grouped into severity levels"""
        return self._call(operation="extAggregateFailedContainersCountBySeverity", query_params={"filter": filter}, error_message="extAggregateFailedContainersCountBySeverity failed", member_cid=member_cid)

    def ext_aggregate_failed_images_by_rules_path(
        self,
        filter: str | None = Field(default=None, description="Filter results using a query in Falcon Query Language (FQL). Supported Filters: image_tag: Image tag cloud_info.cloud_region: Cloud region compliance_finding.severity: Compliance finding severity; available values: 4, 3, 2, 1 (4: critical, 3: high, 2: medium, 1:low) image_digest: Image digest (sha256 digest) image_id: Image ID cloud_info.cloud_provider: Cloud provider compliance_finding.framework: Compliance finding framework (available values: CIS) cid: Customer ID cloud_info.namespace: Kubernetes namespace image_repository: Image repository cloud_info.cloud_account_id: Cloud account ID compliance_finding.name: Compliance finding Name compliance_finding.id: Compliance finding ID image_registry: Image registry cloud_info.cluster_name: Kubernetes cluster name"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """get the images grouped into rules on which they failed"""
        return self._call(operation="extAggregateFailedImagesByRulesPath", query_params={"filter": filter}, error_message="extAggregateFailedImagesByRulesPath failed", member_cid=member_cid)

    def ext_aggregate_failed_images_count_by_severity(
        self,
        filter: str | None = Field(default=None, description="Filter results using a query in Falcon Query Language (FQL). Supported Filters: compliance_finding.name: Compliance finding Name image_tag: Image tag cloud_info.namespace: Kubernetes namespace compliance_finding.id: Compliance finding ID image_repository: Image repository compliance_finding.framework: Compliance finding framework (available values: CIS) compliance_finding.severity: Compliance finding severity; available values: 4, 3, 2, 1 (4: critical, 3: high, 2: medium, 1:low) image_id: Image ID cloud_info.cloud_provider: Cloud provider cloud_info.cluster_name: Kubernetes cluster name cid: Customer ID cloud_info.cloud_account_id: Cloud account ID cloud_info.cloud_region: Cloud region image_digest: Image digest (sha256 digest) image_registry: Image registry"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """get the failed images count grouped into severity levels"""
        return self._call(operation="extAggregateFailedImagesCountBySeverity", query_params={"filter": filter}, error_message="extAggregateFailedImagesCountBySeverity failed", member_cid=member_cid)

    def ext_aggregate_failed_rules_by_clusters(
        self,
        filter: str | None = Field(default=None, description="Filter results using a query in Falcon Query Language (FQL). Supported Filters: cloud_info.cloud_account_id: Cloud account ID compliance_finding.id: Compliance finding ID cloud_info.cluster_name: Kubernetes cluster name compliance_finding.framework: Compliance finding framework (available values: CIS) asset_type: asset type (container, image) cloud_info.cloud_region: Cloud region image_repository: Image repository image_registry: Image registry compliance_finding.name: Compliance finding Name cid: Customer ID image_tag: Image tag compliance_finding.severity: Compliance finding severity; available values: 4, 3, 2, 1 (4: critical, 3: high, 2: medium, 1:low) image_id: Image ID cloud_info.cloud_provider: Cloud provider image_digest: Image digest (sha256 digest)"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """get the failed rules for each cluster grouped into severity levels"""
        return self._call(operation="extAggregateFailedRulesByClusters", query_params={"filter": filter}, error_message="extAggregateFailedRulesByClusters failed", member_cid=member_cid)

    def ext_aggregate_failed_rules_by_images(
        self,
        filter: str | None = Field(default=None, description="Filter results using a query in Falcon Query Language (FQL). Supported Filters: image_repository: Image repository image_registry: Image registry cloud_info.cluster_name: Kubernetes cluster name cid: Customer ID image_tag: Image tag image_digest: Image digest (sha256 digest) cloud_info.cloud_provider: Cloud provider cloud_info.cloud_account_id: Cloud account ID compliance_finding.id: Compliance finding ID image_id: Image ID compliance_finding.framework: Compliance finding framework (available values: CIS) compliance_finding.name: Compliance finding Name asset_type: asset type (container, image) cloud_info.cloud_region: Cloud region cloud_info.namespace: Kubernetes namespace compliance_finding.severity: Compliance finding severity; available values: 4, 3, 2, 1 (4: critical, 3: high, 2: medium, 1:low)"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """get images with failed rules, rule count grouped by severity for each image"""
        return self._call(operation="extAggregateFailedRulesByImages", query_params={"filter": filter}, error_message="extAggregateFailedRulesByImages failed", member_cid=member_cid)

    def ext_aggregate_failed_rules_count_by_severity(
        self,
        filter: str | None = Field(default=None, description="Filter results using a query in Falcon Query Language (FQL). Supported Filters: image_tag: Image tag cloud_info.cloud_region: Cloud region compliance_finding.id: Compliance finding ID image_registry: Image registry compliance_finding.framework: Compliance finding framework (available values: CIS) image_repository: Image repository image_id: Image ID asset_type: asset type (container, image) cid: Customer ID image_digest: Image digest (sha256 digest) cloud_info.cluster_name: Kubernetes cluster name cloud_info.cloud_account_id: Cloud account ID compliance_finding.severity: Compliance finding severity; available values: 4, 3, 2, 1 (4: critical, 3: high, 2: medium, 1:low) cloud_info.cloud_provider: Cloud provider compliance_finding.name: Compliance finding Name"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """get the failed rules count grouped into severity levels"""
        return self._call(operation="extAggregateFailedRulesCountBySeverity", query_params={"filter": filter}, error_message="extAggregateFailedRulesCountBySeverity failed", member_cid=member_cid)

    def ext_aggregate_image_assessments(
        self,
        filter: str | None = Field(default=None, description="Filter results using a query in Falcon Query Language (FQL). Supported Filters: cloud_info.cloud_region: Cloud region image_digest: Image digest (sha256 digest) cloud_info.cloud_provider: Cloud provider compliance_finding.id: Compliance finding ID compliance_finding.severity: Compliance finding severity; available values: 4, 3, 2, 1 (4: critical, 3: high, 2: medium, 1:low) image_repository: Image repository image_id: Image ID image_registry: Image registry cloud_info.cluster_name: Kubernetes cluster name asset_type: asset type (container, image) cloud_info.cloud_account_id: Cloud account ID cid: Customer ID image_tag: Image tag cloud_info.namespace: Kubernetes namespace compliance_finding.framework: Compliance finding framework (available values: CIS) compliance_finding.name: Compliance finding Name"),
        after: str | None = Field(default=None, description="'after' value from the last response. Keep it empty for the first request."),
        limit: str | None = Field(default=None, description="number of images to return in the response after 'after' key. Keep it empty for the default number of 10000"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """get the assessments for each image"""
        return self._call(operation="extAggregateImageAssessments", query_params={"filter": filter, "after": after, "limit": limit}, error_message="extAggregateImageAssessments failed", member_cid=member_cid)

    def ext_aggregate_rules_assessments(
        self,
        filter: str | None = Field(default=None, description="Filter results using a query in Falcon Query Language (FQL). Supported Filters: compliance_finding.framework: Compliance finding framework (available values: CIS) cid: Customer ID cloud_info.cloud_region: Cloud region compliance_finding.id: Compliance finding ID compliance_finding.severity: Compliance finding severity; available values: 4, 3, 2, 1 (4: critical, 3: high, 2: medium, 1:low) image_repository: Image repository image_id: Image ID image_registry: Image registry compliance_finding.name: Compliance finding Name image_tag: Image tag image_digest: Image digest (sha256 digest) cloud_info.cluster_name: Kubernetes cluster name cloud_info.cloud_account_id: Cloud account ID cloud_info.cloud_provider: Cloud provider"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """get the assessments for each rule"""
        return self._call(operation="extAggregateRulesAssessments", query_params={"filter": filter}, error_message="extAggregateRulesAssessments failed", member_cid=member_cid)

    def ext_aggregate_rules_by_status(
        self,
        filter: str | None = Field(default=None, description="Filter results using a query in Falcon Query Language (FQL). Supported Filters: container_id: Container ID cid: Customer ID image_digest: Image digest (sha256 digest) container_name: Container name image_id: Image ID image_repository: Image repository asset_type: asset type (container, image) image_tag: Image tag cloud_info.cloud_region: Cloud region compliance_finding.id: Compliance finding ID image_registry: Image registry cloud_info.cloud_provider: Cloud provider cloud_info.cloud_account_id: Cloud account ID compliance_finding.name: Compliance finding Name compliance_finding.severity: Compliance finding severity; available values: 4, 3, 2, 1 (4: critical, 3: high, 2: medium, 1:low) cloud_info.cluster_name: Kubernetes cluster name compliance_finding.framework: Compliance finding framework (available values: CIS)"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """get the rules grouped by their statuses"""
        return self._call(operation="extAggregateRulesByStatus", query_params={"filter": filter}, error_message="extAggregateRulesByStatus failed", member_cid=member_cid)
