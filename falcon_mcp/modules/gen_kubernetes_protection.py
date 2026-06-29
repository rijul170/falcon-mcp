"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `kubernetes_protection` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenKubernetesProtectionModule(GeneratedModuleBase):
    """Generated tools for the Falcon `kubernetes_protection` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.find_containers_by_container_run_time_version, name="find_containers_by_container_run_time_version")
        self._add_tool(server=server, method=self.find_containers_count_affected_by_zero_day_vulnerabilities, name="find_containers_count_affected_by_zero_day_vulns")
        self._add_tool(server=server, method=self.get_aws_accounts_mixin0, name="get_aws_accounts_mixin0")
        self._add_tool(server=server, method=self.get_azure_install_script, name="get_azure_install_script")
        self._add_tool(server=server, method=self.get_azure_tenant_config, name="get_azure_tenant_config")
        self._add_tool(server=server, method=self.get_azure_tenant_i_ds, name="get_azure_tenant_i_ds")
        self._add_tool(server=server, method=self.get_clusters, name="get_clusters")
        self._add_tool(server=server, method=self.get_combined_cloud_clusters, name="get_combined_cloud_clusters")
        self._add_tool(server=server, method=self.get_helm_values_yaml, name="get_helm_values_yaml")
        self._add_tool(server=server, method=self.get_locations, name="get_locations")
        self._add_tool(server=server, method=self.get_static_scripts, name="get_static_scripts")
        self._add_tool(server=server, method=self.group_containers_by_managed, name="group_containers_by_managed")
        self._add_tool(server=server, method=self.list_azure_accounts, name="list_azure_accounts")
        self._add_tool(server=server, method=self.read_cluster_combined_v2, name="read_cluster_combined_v2")
        self._add_tool(server=server, method=self.read_cluster_count, name="read_cluster_count")
        self._add_tool(server=server, method=self.read_cluster_enrichment, name="read_cluster_enrichment")
        self._add_tool(server=server, method=self.read_clusters_by_date_range_count, name="read_clusters_by_date_range_count")
        self._add_tool(server=server, method=self.read_clusters_by_kubernetes_version_count, name="read_clusters_by_kubernetes_version_count")
        self._add_tool(server=server, method=self.read_clusters_by_status_count, name="read_clusters_by_status_count")
        self._add_tool(server=server, method=self.read_container_count_by_registry, name="read_container_count_by_registry")
        self._add_tool(server=server, method=self.read_container_enrichment, name="read_container_enrichment")
        self._add_tool(server=server, method=self.read_container_image_detections_count_by_date, name="read_container_image_detections_count_by_date")
        self._add_tool(server=server, method=self.read_container_images_by_most_used, name="read_container_images_by_most_used")
        self._add_tool(server=server, method=self.read_container_images_by_state, name="read_container_images_by_state")
        self._add_tool(server=server, method=self.read_container_vulnerabilities_by_severity_count, name="read_container_vulnerabilities_by_severity_count")
        self._add_tool(server=server, method=self.read_containers_by_date_range_count, name="read_containers_by_date_range_count")
        self._add_tool(server=server, method=self.read_containers_sensor_coverage, name="read_containers_sensor_coverage")
        self._add_tool(server=server, method=self.read_deployment_combined, name="read_deployment_combined")
        self._add_tool(server=server, method=self.read_deployment_count, name="read_deployment_count")
        self._add_tool(server=server, method=self.read_deployment_enrichment, name="read_deployment_enrichment")
        self._add_tool(server=server, method=self.read_deployments_by_date_range_count, name="read_deployments_by_date_range_count")
        self._add_tool(server=server, method=self.read_distinct_container_image_count, name="read_distinct_container_image_count")
        self._add_tool(server=server, method=self.read_kubernetes_iom_by_date_range, name="read_kubernetes_iom_by_date_range")
        self._add_tool(server=server, method=self.read_kubernetes_iom_count, name="read_kubernetes_iom_count")
        self._add_tool(server=server, method=self.read_kubernetes_iom_entities, name="read_kubernetes_iom_entities")
        self._add_tool(server=server, method=self.read_namespace_count, name="read_namespace_count")
        self._add_tool(server=server, method=self.read_namespaces_by_date_range_count, name="read_namespaces_by_date_range_count")
        self._add_tool(server=server, method=self.read_node_combined, name="read_node_combined")
        self._add_tool(server=server, method=self.read_node_count, name="read_node_count")
        self._add_tool(server=server, method=self.read_node_enrichment, name="read_node_enrichment")
        self._add_tool(server=server, method=self.read_nodes_by_cloud_count, name="read_nodes_by_cloud_count")
        self._add_tool(server=server, method=self.read_nodes_by_container_engine_version_count, name="read_nodes_by_container_engine_version_count")
        self._add_tool(server=server, method=self.read_nodes_by_date_range_count, name="read_nodes_by_date_range_count")
        self._add_tool(server=server, method=self.read_pod_combined, name="read_pod_combined")
        self._add_tool(server=server, method=self.read_pod_count, name="read_pod_count")
        self._add_tool(server=server, method=self.read_pod_enrichment, name="read_pod_enrichment")
        self._add_tool(server=server, method=self.read_pods_by_date_range_count, name="read_pods_by_date_range_count")
        self._add_tool(server=server, method=self.read_running_container_images, name="read_running_container_images")
        self._add_tool(server=server, method=self.read_vulnerable_container_image_count, name="read_vulnerable_container_image_count")
        self._add_tool(server=server, method=self.search_and_read_kubernetes_iom_entities, name="search_and_read_kubernetes_iom_entities")
        self._add_tool(server=server, method=self.search_kubernetes_ioms, name="search_kubernetes_ioms")
        self._add_tool(server=server, method=self.create_aws_account, name="create_aws_account", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.create_azure_subscription, name="create_azure_subscription", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.patch_azure_service_principal, name="patch_azure_service_principal", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.post_search_kubernetes_iom_entities, name="post_search_kubernetes_iom_entities", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_aws_account, name="update_aws_account", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_aws_accounts_mixin0, name="delete_aws_accounts_mixin0", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_azure_subscription, name="delete_azure_subscription", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.regenerate_api_key, name="regenerate_api_key", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.trigger_scan, name="trigger_scan", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def create_aws_account(
        self,
        body: dict = Field(description="Request JSON body for `CreateAWSAccount` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Creates a new AWS account in our system for a customer and generates the installation script"""
        return self._call(operation="CreateAWSAccount", query_params=None, body_params=body, error_message="CreateAWSAccount failed", member_cid=member_cid)

    def create_azure_subscription(
        self,
        body: dict = Field(description="Request JSON body for `CreateAzureSubscription` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Creates a new Azure Subscription in our system"""
        return self._call(operation="CreateAzureSubscription", query_params=None, body_params=body, error_message="CreateAzureSubscription failed", member_cid=member_cid)

    def delete_aws_accounts_mixin0(
        self,
        ids: list[str] = Field(description="AWS Account IDs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete AWS accounts."""
        return self._call(operation="DeleteAWSAccountsMixin0", query_params={"ids": ids}, error_message="DeleteAWSAccountsMixin0 failed", member_cid=member_cid)

    def delete_azure_subscription(
        self,
        ids: list[str] | None = Field(default=None, description="Azure Subscription IDs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deletes a new Azure Subscription in our system"""
        return self._call(operation="DeleteAzureSubscription", query_params={"ids": ids}, error_message="DeleteAzureSubscription failed", member_cid=member_cid)

    def find_containers_by_container_run_time_version(
        self,
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 200."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        sort: str | None = Field(default=None, description="The fields to sort the records on."),
        filter: str | None = Field(default=None, description="Retrieve count of Kubernetes containers that match a query in Falcon Query Language (FQL). Supported filter fields: agent_id agent_type ai_related allow_privilege_escalation app_name cid cloud_account_id cloud_instance_id cloud_name cloud_region cloud_service cluster_id cluster_name container_id container_image_id container_name cve_id detection_name first_seen image_detection_count image_digest image_has_been_assessed image_id image_registry image_repository image_tag image_vulnerability_count insecure_mount_source insecure_mount_type insecure_propagation_mode interactive_mode ipv4 ipv6 kac_agent_id labels last_seen namespace node_name node_uid package_name_version pod_id pod_name port privileged root_write_access run_as_root_group run_as_root_user running_status"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve containers by container_runtime_version"""
        return self._call(operation="FindContainersByContainerRunTimeVersion", query_params={"limit": limit, "offset": offset, "sort": sort, "filter": filter}, error_message="FindContainersByContainerRunTimeVersion failed", member_cid=member_cid)

    def find_containers_count_affected_by_zero_day_vulnerabilities(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve containers count affected by zero day vulnerabilities"""
        return self._call(operation="FindContainersCountAffectedByZeroDayVulnerabilities", query_params=None, error_message="FindContainersCountAffectedByZeroDayVulnerabilities failed", member_cid=member_cid)

    def get_aws_accounts_mixin0(
        self,
        ids: list[str] | None = Field(default=None, description="AWS Account IDs"),
        is_horizon_acct: str | None = Field(default=None, description="Filter by whether an account originates from Horizon or not"),
        status: str | None = Field(default=None, description="Filter by account status"),
        limit: int | None = Field(default=None, description="Limit returned accounts"),
        offset: int | None = Field(default=None, description="Offset returned accounts"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Provides a list of AWS accounts."""
        return self._call(operation="GetAWSAccountsMixin0", query_params={"ids": ids, "is_horizon_acct": is_horizon_acct, "status": status, "limit": limit, "offset": offset}, error_message="GetAWSAccountsMixin0 failed", member_cid=member_cid)

    def get_azure_install_script(
        self,
        id: str | None = Field(default=None, description="Azure Tenant ID"),
        subscription_id: list[str] | None = Field(default=None, description="Azure Subscription IDs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Provides the script to run for a given tenant id and subscription IDs"""
        return self._call(operation="GetAzureInstallScript", query_params={"id": id, "subscription_id": subscription_id}, error_message="GetAzureInstallScript failed", member_cid=member_cid)

    def get_azure_tenant_config(
        self,
        ids: list[str] | None = Field(default=None, description="Azure Tenant IDs"),
        limit: int | None = Field(default=None, description="Limit returned accounts"),
        offset: int | None = Field(default=None, description="Offset returned accounts"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Gets the Azure tenant Config"""
        return self._call(operation="GetAzureTenantConfig", query_params={"ids": ids, "limit": limit, "offset": offset}, error_message="GetAzureTenantConfig failed", member_cid=member_cid)

    def get_azure_tenant_i_ds(
        self,
        ids: list[str] | None = Field(default=None, description="Azure Tenant IDs"),
        status: str | None = Field(default=None, description="Cluster Status"),
        limit: int | None = Field(default=None, description="Limit returned accounts"),
        offset: int | None = Field(default=None, description="Offset returned accounts"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Provides all the azure subscriptions and tenants"""
        return self._call(operation="GetAzureTenantIDs", query_params={"ids": ids, "status": status, "limit": limit, "offset": offset}, error_message="GetAzureTenantIDs failed", member_cid=member_cid)

    def get_clusters(
        self,
        cluster_names: list[str] | None = Field(default=None, description="Cluster name. For EKS it will be cluster ARN."),
        status: list[str] | None = Field(default=None, description="Cluster Status"),
        account_ids: list[str] | None = Field(default=None, description="Cluster Account id. For EKS it will be AWS account ID."),
        locations: list[str] | None = Field(default=None, description="Cloud location"),
        cluster_service: str | None = Field(default=None, description="Cluster Service"),
        limit: int | None = Field(default=None, description="Limit returned accounts"),
        offset: int | None = Field(default=None, description="Offset returned accounts"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Provides the clusters acknowledged by the Kubernetes Protection service"""
        return self._call(operation="GetClusters", query_params={"cluster_names": cluster_names, "status": status, "account_ids": account_ids, "locations": locations, "cluster_service": cluster_service, "limit": limit, "offset": offset}, error_message="GetClusters failed", member_cid=member_cid)

    def get_combined_cloud_clusters(
        self,
        locations: list[str] | None = Field(default=None, description="Cloud location"),
        ids: list[str] | None = Field(default=None, description="Cloud Account IDs"),
        cluster_service: list[str] | None = Field(default=None, description="Cluster Service"),
        cluster_status: list[str] | None = Field(default=None, description="Cluster Status"),
        limit: int | None = Field(default=None, description="Limit returned accounts"),
        offset: int | None = Field(default=None, description="Offset returned accounts"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns a combined list of provisioned cloud accounts and known kubernetes clusters"""
        return self._call(operation="GetCombinedCloudClusters", query_params={"locations": locations, "ids": ids, "cluster_service": cluster_service, "cluster_status": cluster_status, "limit": limit, "offset": offset}, error_message="GetCombinedCloudClusters failed", member_cid=member_cid)

    def get_helm_values_yaml(
        self,
        cluster_name: str = Field(description="Cluster name. For EKS it will be cluster ARN."),
        is_self_managed_cluster: bool | None = Field(default=None, description="Set to true if the cluster is not managed by a cloud provider, false if it is."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Provides a sample Helm values.yaml file for a customer to install alongside the agent Helm chart"""
        return self._call(operation="GetHelmValuesYaml", query_params={"cluster_name": cluster_name, "is_self_managed_cluster": is_self_managed_cluster}, error_message="GetHelmValuesYaml failed", member_cid=member_cid)

    def get_locations(
        self,
        clouds: list[str] | None = Field(default=None, description="Cloud Provider"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Provides the cloud locations acknowledged by the Kubernetes Protection service"""
        return self._call(operation="GetLocations", query_params={"clouds": clouds}, error_message="GetLocations failed", member_cid=member_cid)

    def get_static_scripts(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Gets static bash scripts that are used during registration"""
        return self._call(operation="GetStaticScripts", query_params=None, error_message="GetStaticScripts failed", member_cid=member_cid)

    def group_containers_by_managed(
        self,
        filter: str | None = Field(default=None, description="Retrieve count of Kubernetes containers that match a query in Falcon Query Language (FQL). Supported filter fields: agent_id ai_related allow_privilege_escalation app_name cid cloud_account_id cloud_instance_id cloud_name cloud_region cloud_service cluster_id cluster_name container_id container_image_id container_name cve_id detection_name first_seen image_detection_count image_digest image_has_been_assessed image_id image_registry image_repository image_tag image_vulnerability_count insecure_mount_source insecure_mount_type insecure_propagation_mode interactive_mode ipv4 ipv6 kac_agent_id labels last_seen namespace node_name node_uid pod_id pod_name port privileged root_write_access run_as_root_group run_as_root_user running_status"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Group the containers by Managed"""
        return self._call(operation="GroupContainersByManaged", query_params={"filter": filter}, error_message="GroupContainersByManaged failed", member_cid=member_cid)

    def list_azure_accounts(
        self,
        ids: list[str] | None = Field(default=None, description="Azure Tenant IDs"),
        subscription_id: list[str] | None = Field(default=None, description="Azure Subscription IDs"),
        status: str | None = Field(default=None, description="Filter by account status"),
        is_horizon_acct: str | None = Field(default=None, description="Filter by whether an account originates from Horizon or not"),
        limit: int | None = Field(default=None, description="Limit returned accounts"),
        offset: int | None = Field(default=None, description="Offset returned accounts"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Provides the azure subscriptions registered to Kubernetes Protection"""
        return self._call(operation="ListAzureAccounts", query_params={"ids": ids, "subscription_id": subscription_id, "status": status, "is_horizon_acct": is_horizon_acct, "limit": limit, "offset": offset}, error_message="ListAzureAccounts failed", member_cid=member_cid)

    def patch_azure_service_principal(
        self,
        id: str = Field(description="Azure Tenant ID"),
        client_id: str = Field(description="Azure Client ID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Adds the client ID for the given tenant ID to our system"""
        return self._call(operation="PatchAzureServicePrincipal", query_params={"id": id, "client_id": client_id}, error_message="PatchAzureServicePrincipal failed", member_cid=member_cid)

    def post_search_kubernetes_iom_entities(
        self,
        body: dict = Field(description="Request JSON body for `PostSearchKubernetesIOMEntities` per the CrowdStrike API schema (required)."),
        filter: str | None = Field(default=None, description="Search Kubernetes IOMs using a query in Falcon Query Language (FQL). Supported filter fields: cid cis_id cluster_id cluster_name containers_impacted_ai_related containers_impacted_count containers_impacted_ids detection_type name namespace prevented resource_id resource_name resource_typeseverity"),
        sort: str | None = Field(default=None, description="The fields to sort the records on."),
        limit: int | None = Field(default=None, description="Maximum number of records to return (default: 100, max: 500)"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for Kubernetes IOMs with filtering options.Pagination is supported via Elasticsearch's search_after search param and point in time. Assets are sorted by unique ID in ascending direction."""
        return self._call(operation="PostSearchKubernetesIOMEntities", query_params={"filter": filter, "sort": sort, "limit": limit}, body_params=body, error_message="PostSearchKubernetesIOMEntities failed", member_cid=member_cid)

    def read_cluster_combined_v2(
        self,
        filter: str | None = Field(default=None, description="Search Kubernetes clusters using a query in Falcon Query Language (FQL). Supported filter fields: access agent_id agent_status agent_type cid cloud_account_id cloud_name cloud_region cloud_service cluster_id cluster_name cluster_status container_count iar_coverage kac_agent_id kubernetes_version last_seen management_status namespace node_count pod_count pod_name tags"),
        sort: str | None = Field(default=None, description="The fields to sort the records on."),
        include_counts: bool | None = Field(default=None, description="Flag to include node, pod and container counts in the response"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 200."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve Kubernetes cluster data"""
        return self._call(operation="ReadClusterCombinedV2", query_params={"filter": filter, "sort": sort, "include_counts": include_counts, "limit": limit, "offset": offset}, error_message="ReadClusterCombinedV2 failed", member_cid=member_cid)

    def read_cluster_count(
        self,
        filter: str | None = Field(default=None, description="Retrieve count of Kubernetes clusters that match a query in Falcon Query Language (FQL). Supported filter fields: access agent_id agent_status agent_type cid cloud_account_id cloud_name cloud_region cloud_service cluster_id cluster_name cluster_status container_count iar_coverage kac_agent_id kubernetes_version last_seen management_status namespace node_count pod_count pod_name tags"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve cluster counts"""
        return self._call(operation="ReadClusterCount", query_params={"filter": filter}, error_message="ReadClusterCount failed", member_cid=member_cid)

    def read_cluster_enrichment(
        self,
        cluster_id: list[str] = Field(description="One or more cluster ids for which to retrieve enrichment info"),
        filter: str | None = Field(default=None, description="Supported filter fields: cloud_account_id cloud_name cloud_region cluster_id cluster_name last_seen namespace"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve cluster enrichment data"""
        return self._call(operation="ReadClusterEnrichment", query_params={"cluster_id": cluster_id, "filter": filter}, error_message="ReadClusterEnrichment failed", member_cid=member_cid)

    def read_clusters_by_date_range_count(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve clusters by date range counts"""
        return self._call(operation="ReadClustersByDateRangeCount", query_params=None, error_message="ReadClustersByDateRangeCount failed", member_cid=member_cid)

    def read_clusters_by_kubernetes_version_count(
        self,
        filter: str | None = Field(default=None, description="Retrieve count of Kubernetes clusters that match a query in Falcon Query Language (FQL). Supported filter fields: access agent_id agent_status agent_type cid cloud_account_id cloud_name cloud_region cloud_service cluster_id cluster_name cluster_status container_count iar_coverage kac_agent_id kubernetes_version last_seen management_status namespace node_count pod_count pod_name tags"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Bucket clusters by kubernetes version"""
        return self._call(operation="ReadClustersByKubernetesVersionCount", query_params={"filter": filter}, error_message="ReadClustersByKubernetesVersionCount failed", member_cid=member_cid)

    def read_clusters_by_status_count(
        self,
        filter: str | None = Field(default=None, description="Retrieve count of Kubernetes clusters that match a query in Falcon Query Language (FQL). Supported filter fields: access agent_id agent_status agent_type cid cloud_account_id cloud_name cloud_region cloud_service cluster_id cluster_name cluster_status container_count iar_coverage kac_agent_id kubernetes_version last_seen management_status namespace node_count pod_count pod_name tags"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Bucket clusters by status"""
        return self._call(operation="ReadClustersByStatusCount", query_params={"filter": filter}, error_message="ReadClustersByStatusCount failed", member_cid=member_cid)

    def read_container_count_by_registry(
        self,
        under_assessment: bool | None = Field(default=None, description="(true/false) whether to return registries under assessment or not under assessment. Ifnot provided all registries are considered"),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve."),
        filter: str | None = Field(default=None, description="Retrieve count of Kubernetes container image registries that match a query in Falcon Query Language (FQL). Supported filter fields: agent_id agent_type ai_related allow_privilege_escalation app_name cid cloud_account_id cloud_instance_id cloud_name cloud_region cloud_service cluster_id cluster_name container_id container_image_id container_name cve_id detection_name first_seen image_detection_count image_digest image_has_been_assessed image_id image_registry image_repository image_tag image_vulnerability_count insecure_mount_source insecure_mount_type insecure_propagation_mode interactive_mode ipv4 ipv6 kac_agent_id labels last_seen namespace node_name node_uid package_name_version pod_id pod_name port privileged root_write_access run_as_root_group run_as_root_user running_status"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves a list with the top container image registries. Maximum page size: 200"""
        return self._call(operation="ReadContainerCountByRegistry", query_params={"under_assessment": under_assessment, "limit": limit, "filter": filter}, error_message="ReadContainerCountByRegistry failed", member_cid=member_cid)

    def read_container_enrichment(
        self,
        container_id: list[str] = Field(description="One or more container ids for which to retrieve enrichment info"),
        filter: str | None = Field(default=None, description="Supported filter fields: cloud_account_id cloud_name cloud_region cluster_id cluster_name last_seen namespace"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve container enrichment data"""
        return self._call(operation="ReadContainerEnrichment", query_params={"container_id": container_id, "filter": filter}, error_message="ReadContainerEnrichment failed", member_cid=member_cid)

    def read_container_image_detections_count_by_date(
        self,
        filter: str | None = Field(default=None, description="Retrieve count of Kubernetes containers that match a query in Falcon Query Language (FQL). Supported filter fields: agent_id agent_type ai_related allow_privilege_escalation app_name cid cloud_account_id cloud_instance_id cloud_name cloud_region cloud_service cluster_id cluster_name container_id container_image_id container_name cve_id detection_name first_seen image_detection_count image_digest image_has_been_assessed image_id image_registry image_repository image_tag image_vulnerability_count insecure_mount_source insecure_mount_type insecure_propagation_mode interactive_mode ipv4 ipv6 kac_agent_id labels last_seen namespace node_name node_uid package_name_version pod_id pod_name port privileged root_write_access run_as_root_group run_as_root_user running_status"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve count of image assessment detections on running containers over a period of time"""
        return self._call(operation="ReadContainerImageDetectionsCountByDate", query_params={"filter": filter}, error_message="ReadContainerImageDetectionsCountByDate failed", member_cid=member_cid)

    def read_container_images_by_most_used(
        self,
        filter: str | None = Field(default=None, description="Retrieve count of Kubernetes containers that match a query in Falcon Query Language (FQL). Supported filter fields: agent_id agent_type ai_related allow_privilege_escalation app_name cid cloud_account_id cloud_instance_id cloud_name cloud_region cloud_service cluster_id cluster_name container_id container_image_id container_name cve_id detection_name first_seen image_detection_count image_digest image_has_been_assessed image_id image_registry image_repository image_tag image_vulnerability_count insecure_mount_source insecure_mount_type insecure_propagation_mode interactive_mode ipv4 ipv6 kac_agent_id labels last_seen namespace node_name node_uid package_name_version pod_id pod_name port privileged root_write_access run_as_root_group run_as_root_user running_status"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Bucket container by image-digest"""
        return self._call(operation="ReadContainerImagesByMostUsed", query_params={"filter": filter}, error_message="ReadContainerImagesByMostUsed failed", member_cid=member_cid)

    def read_container_images_by_state(
        self,
        filter: str | None = Field(default=None, description="Filter using a query in Falcon Query Language (FQL). Supported filter fields: cid"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve count of image states running on containers"""
        return self._call(operation="ReadContainerImagesByState", query_params={"filter": filter}, error_message="ReadContainerImagesByState failed", member_cid=member_cid)

    def read_container_vulnerabilities_by_severity_count(
        self,
        filter: str | None = Field(default=None, description="Get vulnerabilities count by severity for container using a query in Falcon Query Language (FQL). Supported filter fields: agent_id agent_type ai_related allow_privilege_escalation app_name cid cloud_account_id cloud_instance_id cloud_name cloud_region cloud_service cluster_id cluster_name container_id container_image_id container_name cve_id detection_name first_seen image_detection_count image_digest image_has_been_assessed image_id image_registry image_repository image_tag image_vulnerability_count insecure_mount_source insecure_mount_type insecure_propagation_mode interactive_mode ipv4 ipv6 kac_agent_id labels last_seen namespace node_name node_uid package_name_version pod_id pod_name port privileged root_write_access run_as_root_group run_as_root_user running_status"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve container vulnerabilities by severity counts"""
        return self._call(operation="ReadContainerVulnerabilitiesBySeverityCount", query_params={"filter": filter}, error_message="ReadContainerVulnerabilitiesBySeverityCount failed", member_cid=member_cid)

    def read_containers_by_date_range_count(
        self,
        filter: str | None = Field(default=None, description="Get container counts using a query in Falcon Query Language (FQL). Supported filter fields: agent_id agent_type ai_related allow_privilege_escalation app_name cid cloud_account_id cloud_instance_id cloud_name cloud_region cloud_service cluster_id cluster_name container_id container_image_id container_name cve_id detection_name first_seen image_detection_count image_digest image_has_been_assessed image_id image_registry image_repository image_tag image_vulnerability_count insecure_mount_source insecure_mount_type insecure_propagation_mode interactive_mode ipv4 ipv6 kac_agent_id labels last_seen namespace node_name node_uid package_name_version pod_id pod_name portprivileged root_write_access run_as_root_group run_as_root_user running_status"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve containers by date range counts"""
        return self._call(operation="ReadContainersByDateRangeCount", query_params={"filter": filter}, error_message="ReadContainersByDateRangeCount failed", member_cid=member_cid)

    def read_containers_sensor_coverage(
        self,
        filter: str | None = Field(default=None, description="Retrieve count of Kubernetes containers that match a query in Falcon Query Language (FQL). Supported filter fields: agent_id agent_type ai_related allow_privilege_escalation app_name cid cloud_account_id cloud_instance_id cloud_name cloud_region cloud_service cluster_id cluster_name container_id container_image_id container_name cve_id detection_name first_seen image_detection_count image_digest image_has_been_assessed image_id image_registry image_repository image_tag image_vulnerability_count insecure_mount_source insecure_mount_type insecure_propagation_mode interactive_mode ipv4 ipv6 kac_agent_id labels last_seen namespace node_name node_uid package_name_version pod_id pod_name port privileged root_write_access run_as_root_group run_as_root_user running_status"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Bucket containers by agent type and calculate sensor coverage"""
        return self._call(operation="ReadContainersSensorCoverage", query_params={"filter": filter}, error_message="ReadContainersSensorCoverage failed", member_cid=member_cid)

    def read_deployment_combined(
        self,
        filter: str | None = Field(default=None, description="Search Kubernetes deployments using a query in Falcon Query Language (FQL). Supported filter fields: agent_id agent_type annotations_list cid cloud_account_id cloud_name cloud_region cloud_service cluster_id cluster_name deployment_id deployment_name deployment_status first_seen kac_agent_id last_seen namespace pod_count resource_status"),
        sort: str | None = Field(default=None, description="The fields to sort the records on."),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 200."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve kubernetes deployments identified by the provided filter criteria"""
        return self._call(operation="ReadDeploymentCombined", query_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset}, error_message="ReadDeploymentCombined failed", member_cid=member_cid)

    def read_deployment_count(
        self,
        filter: str | None = Field(default=None, description="Retrieve count of Kubernetes deployments that match a query in Falcon Query Language (FQL). Supported filter fields: agent_id agent_type annotations_list cid cloud_account_id cloud_name cloud_region cloud_service cluster_id cluster_name deployment_id deployment_name deployment_status first_seen kac_agent_id last_seen namespace pod_count resource_status"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve deployment counts"""
        return self._call(operation="ReadDeploymentCount", query_params={"filter": filter}, error_message="ReadDeploymentCount failed", member_cid=member_cid)

    def read_deployment_enrichment(
        self,
        deployment_id: list[str] = Field(description="One or more deployment ids for which to retrieve enrichment info"),
        filter: str | None = Field(default=None, description="Supported filter fields: cloud_account_id cloud_name cloud_region cluster_id cluster_name last_seen namespace"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve deployment enrichment data"""
        return self._call(operation="ReadDeploymentEnrichment", query_params={"deployment_id": deployment_id, "filter": filter}, error_message="ReadDeploymentEnrichment failed", member_cid=member_cid)

    def read_deployments_by_date_range_count(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve deployments by date range counts"""
        return self._call(operation="ReadDeploymentsByDateRangeCount", query_params=None, error_message="ReadDeploymentsByDateRangeCount failed", member_cid=member_cid)

    def read_distinct_container_image_count(
        self,
        filter: str | None = Field(default=None, description="Search Kubernetes containers using a query in Falcon Query Language (FQL). Supported filter fields: agent_id agent_type ai_related allow_privilege_escalation app_name cid cloud_account_id cloud_instance_id cloud_name cloud_region cloud_service cluster_id cluster_name container_id container_image_id container_name cve_id detection_name first_seen image_detection_count image_digest image_has_been_assessed image_id image_registry image_repository image_tag image_vulnerability_count insecure_mount_source insecure_mount_type insecure_propagation_mode interactive_mode ipv4 ipv6 kac_agent_id labels last_seen namespace node_name node_uid package_name_version pod_id pod_name portprivileged root_write_access run_as_root_group run_as_root_user running_status"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve count of distinct images running on containers"""
        return self._call(operation="ReadDistinctContainerImageCount", query_params={"filter": filter}, error_message="ReadDistinctContainerImageCount failed", member_cid=member_cid)

    def read_kubernetes_iom_by_date_range(
        self,
        filter: str | None = Field(default=None, description="Filter Kubernetes IOMs using a query in Falcon Query Language (FQL). Supported filter fields: cid created_timestamp detect_timestamp prevented severity"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns the count of Kubernetes IOMs by the date. by default it's for 7 days."""
        return self._call(operation="ReadKubernetesIomByDateRange", query_params={"filter": filter}, error_message="ReadKubernetesIomByDateRange failed", member_cid=member_cid)

    def read_kubernetes_iom_count(
        self,
        filter: str | None = Field(default=None, description="Filter Kubernetes IOMs using a query in Falcon Query Language (FQL). Supported filter fields: cid created_timestamp detect_timestamp prevented severity"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns the total count of Kubernetes IOMs over the past seven days"""
        return self._call(operation="ReadKubernetesIomCount", query_params={"filter": filter}, error_message="ReadKubernetesIomCount failed", member_cid=member_cid)

    def read_kubernetes_iom_entities(
        self,
        ids: list[str] | None = Field(default=None, description="Search Kubernetes IOMs by ids - The maximum amount is 100 IDs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve Kubernetes IOM entities identified by the provided IDs"""
        return self._call(operation="ReadKubernetesIomEntities", query_params={"ids": ids}, error_message="ReadKubernetesIomEntities failed", member_cid=member_cid)

    def read_namespace_count(
        self,
        filter: str | None = Field(default=None, description="Retrieve count of Kubernetes namespaces that match a query in Falcon Query Language (FQL). Supported filter fields: agent_id agent_type annotations_list cid cloud_account_id cloud_name cloud_region cloud_service cluster_id cluster_name first_seen kac_agent_id last_seen namespace_id namespace_name resource_status"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve namespace counts"""
        return self._call(operation="ReadNamespaceCount", query_params={"filter": filter}, error_message="ReadNamespaceCount failed", member_cid=member_cid)

    def read_namespaces_by_date_range_count(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve namespaces by date range counts"""
        return self._call(operation="ReadNamespacesByDateRangeCount", query_params=None, error_message="ReadNamespacesByDateRangeCount failed", member_cid=member_cid)

    def read_node_combined(
        self,
        filter: str | None = Field(default=None, description="Search Kubernetes nodes using a query in Falcon Query Language (FQL). Supported filter fields: agent_id agent_type annotations_list cid cloud_account_id cloud_name cloud_region cloud_service cluster_id cluster_name container_count container_runtime_version first_seen image_digestipv4 kac_agent_id last_seen linux_sensor_coverage node_name node_uid pod_count resource_status"),
        sort: str | None = Field(default=None, description="The fields to sort the records on."),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 200."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve kubernetes nodes identified by the provided filter criteria"""
        return self._call(operation="ReadNodeCombined", query_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset}, error_message="ReadNodeCombined failed", member_cid=member_cid)

    def read_node_count(
        self,
        filter: str | None = Field(default=None, description="Retrieve count of Kubernetes nodes that match a query in Falcon Query Language (FQL). Supported filter fields: agent_id agent_type annotations_list cid cloud_account_id cloud_name cloud_region cloud_service cluster_id cluster_name container_count container_runtime_version first_seen image_digest ipv4 kac_agent_id last_seen linux_sensor_coverage node_name node_uid pod_count resource_status"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve node counts"""
        return self._call(operation="ReadNodeCount", query_params={"filter": filter}, error_message="ReadNodeCount failed", member_cid=member_cid)

    def read_node_enrichment(
        self,
        node_name: list[str] = Field(description="One or more node names for which to retrieve enrichment info"),
        filter: str | None = Field(default=None, description="Supported filter fields: cloud_account_id cloud_name cloud_region cluster_id cluster_name last_seen namespace"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve node enrichment data"""
        return self._call(operation="ReadNodeEnrichment", query_params={"node_name": node_name, "filter": filter}, error_message="ReadNodeEnrichment failed", member_cid=member_cid)

    def read_nodes_by_cloud_count(
        self,
        filter: str | None = Field(default=None, description="Search Kubernetes nodes using a query in Falcon Query Language (FQL). Supported filter fields: agent_id agent_type annotations_list cid cloud_account_id cloud_name cloud_region cloud_service cluster_id cluster_name container_count container_runtime_version first_seen image_digestipv4 kac_agent_id last_seen linux_sensor_coverage node_name node_uid pod_count resource_status"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Bucket nodes by cloud providers"""
        return self._call(operation="ReadNodesByCloudCount", query_params={"filter": filter}, error_message="ReadNodesByCloudCount failed", member_cid=member_cid)

    def read_nodes_by_container_engine_version_count(
        self,
        filter: str | None = Field(default=None, description="Search Kubernetes nodes using a query in Falcon Query Language (FQL). Supported filter fields: agent_id agent_type annotations_list cid cloud_account_id cloud_name cloud_region cloud_service cluster_id cluster_name container_count container_runtime_version first_seen image_digestipv4 kac_agent_id last_seen linux_sensor_coverage node_name node_uid pod_count resource_status"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Bucket nodes by their container engine version"""
        return self._call(operation="ReadNodesByContainerEngineVersionCount", query_params={"filter": filter}, error_message="ReadNodesByContainerEngineVersionCount failed", member_cid=member_cid)

    def read_nodes_by_date_range_count(
        self,
        filter: str | None = Field(default=None, description="Search Kubernetes nodes using a query in Falcon Query Language (FQL). Supported filter fields: agent_id agent_type annotations_list cid cloud_account_id cloud_name cloud_region cloud_service cluster_id cluster_name container_count container_runtime_version first_seen image_digestipv4 kac_agent_id last_seen linux_sensor_coverage node_name node_uid pod_count resource_status"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve nodes by date range counts"""
        return self._call(operation="ReadNodesByDateRangeCount", query_params={"filter": filter}, error_message="ReadNodesByDateRangeCount failed", member_cid=member_cid)

    def read_pod_combined(
        self,
        filter: str | None = Field(default=None, description="Search Kubernetes pods using a query in Falcon Query Language (FQL). Supported filter fields: agent_id agent_type allow_privilege_escalation annotations_list app_name cid cloud_account_id cloud_name cloud_region cloud_service cluster_id cluster_name container_count first_seen ipv4 ipv6 kac_agent_id labels last_seen namespace node_name node_uid owner_id owner_type pod_external_id pod_idpod_name port privileged resource_status root_write_access run_as_root_group run_as_root_user"),
        sort: str | None = Field(default=None, description="The fields to sort the records on."),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 200."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve kubernetes pods identified by the provided filter criteria"""
        return self._call(operation="ReadPodCombined", query_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset}, error_message="ReadPodCombined failed", member_cid=member_cid)

    def read_pod_count(
        self,
        filter: str | None = Field(default=None, description="Retrieve count of Kubernetes pods that match a query in Falcon Query Language (FQL). Supported filter fields: agent_id agent_type allow_privilege_escalation annotations_list app_name cid cloud_account_id cloud_name cloud_region cloud_service cluster_id cluster_name container_count first_seen ipv4 ipv6 kac_agent_id labels last_seen namespace node_name node_uid owner_id owner_type pod_external_id pod_id pod_name port privileged resource_status root_write_access run_as_root_group run_as_root_user"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve pod counts"""
        return self._call(operation="ReadPodCount", query_params={"filter": filter}, error_message="ReadPodCount failed", member_cid=member_cid)

    def read_pod_enrichment(
        self,
        pod_id: list[str] = Field(description="One or more pod ids for which to retrieve enrichment info"),
        filter: str | None = Field(default=None, description="Supported filter fields: cloud_account_id cloud_name cloud_region cluster_id cluster_name last_seen namespace"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve pod enrichment data"""
        return self._call(operation="ReadPodEnrichment", query_params={"pod_id": pod_id, "filter": filter}, error_message="ReadPodEnrichment failed", member_cid=member_cid)

    def read_pods_by_date_range_count(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve pods by date range counts"""
        return self._call(operation="ReadPodsByDateRangeCount", query_params=None, error_message="ReadPodsByDateRangeCount failed", member_cid=member_cid)

    def read_running_container_images(
        self,
        filter: str | None = Field(default=None, description="Retrieve list of images on running containers using a query in Falcon Query Language (FQL). Supported filter fields: cid cloud_account_id cloud_name cloud_region cluster_id cluster_name hosts image_digest image_has_been_assessed image_id image_name image_registry image_repository image_tag last_seen namespace running_status"),
        sort: str | None = Field(default=None, description="The fields to sort the records on."),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 200."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve images on running containers"""
        return self._call(operation="ReadRunningContainerImages", query_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset}, error_message="ReadRunningContainerImages failed", member_cid=member_cid)

    def read_vulnerable_container_image_count(
        self,
        filter: str | None = Field(default=None, description="Retrieve count of Kubernetes containers that match a query in Falcon Query Language (FQL). Supported filter fields: agent_id agent_type ai_related allow_privilege_escalation app_name cid cloud_account_id cloud_instance_id cloud_name cloud_region cloud_service cluster_id cluster_name container_id container_image_id container_name cve_id detection_name first_seen image_detection_count image_digest image_has_been_assessed image_id image_registry image_repository image_tag image_vulnerability_count insecure_mount_source insecure_mount_type insecure_propagation_mode interactive_mode ipv4 ipv6 kac_agent_id labels last_seen namespace node_name node_uid package_name_version pod_id pod_name port privileged root_write_access run_as_root_group run_as_root_user running_status"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve count of vulnerable images running on containers"""
        return self._call(operation="ReadVulnerableContainerImageCount", query_params={"filter": filter}, error_message="ReadVulnerableContainerImageCount failed", member_cid=member_cid)

    def regenerate_api_key(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Regenerate API key for docker registry integrations"""
        return self._call(operation="RegenerateAPIKey", query_params=None, error_message="RegenerateAPIKey failed", member_cid=member_cid)

    def search_and_read_kubernetes_iom_entities(
        self,
        filter: str | None = Field(default=None, description="Search Kubernetes IOMs using a query in Falcon Query Language (FQL). Supported filter fields: cid cis_id cluster_id cluster_name containers_impacted_ai_related containers_impacted_count containers_impacted_ids detection_type name namespace prevented resource_id resource_name resource_typeseverity"),
        sort: str | None = Field(default=None, description="The fields to sort the records on."),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves a list of Kubernetes IOMs identified by the provided search criteria. Maximum page size: 100. Maximum available Kubernetes IOMs: 10,000"""
        return self._call(operation="SearchAndReadKubernetesIomEntities", query_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset}, error_message="SearchAndReadKubernetesIomEntities failed", member_cid=member_cid)

    def search_kubernetes_ioms(
        self,
        filter: str | None = Field(default=None, description="Search Kubernetes IOMs using a query in Falcon Query Language (FQL). Supported filter fields: cid cis_id cluster_id cluster_name containers_impacted_ai_related containers_impacted_count containers_impacted_ids detection_type name namespace prevented resource_id resource_name resource_typeseverity"),
        sort: str | None = Field(default=None, description="The fields to sort the records on."),
        limit: int | None = Field(default=None, description="The upper-bound on the number of records to retrieve. Maximum limit: 100."),
        offset: int | None = Field(default=None, description="The offset from where to begin. Maximum offset = 10000 - limit."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search Kubernetes IOMs by the provided search criteria. this endpoint returns a list of Kubernetes IOM UUIDs matching the query"""
        return self._call(operation="SearchKubernetesIoms", query_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset}, error_message="SearchKubernetesIoms failed", member_cid=member_cid)

    def trigger_scan(
        self,
        scan_type: str = Field(description="Scan Type to do"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Triggers a dry run or a full scan of a customer's kubernetes footprint"""
        return self._call(operation="TriggerScan", query_params={"scan_type": scan_type}, error_message="TriggerScan failed", member_cid=member_cid)

    def update_aws_account(
        self,
        ids: list[str] = Field(description="AWS Account ID"),
        region: str | None = Field(default=None, description="Default Region for Account Automation"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Updates the AWS account per the query parameters provided"""
        return self._call(operation="UpdateAWSAccount", query_params={"ids": ids, "region": region}, error_message="UpdateAWSAccount failed", member_cid=member_cid)
