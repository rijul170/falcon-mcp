"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `aspm` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenAspmModule(GeneratedModuleBase):
    """Generated tools for the Falcon `aspm` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.execute_function_data, name="execute_function_data")
        self._add_tool(server=server, method=self.execute_function_data_query, name="execute_function_data_query")
        self._add_tool(server=server, method=self.execute_function_data_query_count, name="execute_function_data_query_count")
        self._add_tool(server=server, method=self.execute_functions, name="execute_functions")
        self._add_tool(server=server, method=self.execute_functions_overtime, name="execute_functions_overtime")
        self._add_tool(server=server, method=self.execute_functions_query, name="execute_functions_query")
        self._add_tool(server=server, method=self.execute_functions_query_count, name="execute_functions_query_count")
        self._add_tool(server=server, method=self.execute_functions_query_overtime, name="execute_functions_query_overtime")
        self._add_tool(server=server, method=self.get_cloud_security_integration_state, name="get_cloud_security_integration_state")
        self._add_tool(server=server, method=self.get_executor_nodes, name="get_executor_nodes")
        self._add_tool(server=server, method=self.get_executor_nodes_metadata, name="get_executor_nodes_metadata")
        self._add_tool(server=server, method=self.get_group_hierarchy, name="get_group_hierarchy")
        self._add_tool(server=server, method=self.get_groups_v2, name="get_groups_v2")
        self._add_tool(server=server, method=self.get_integration_tasks_admin, name="get_integration_tasks_admin")
        self._add_tool(server=server, method=self.get_integration_tasks_metadata, name="get_integration_tasks_metadata")
        self._add_tool(server=server, method=self.get_integration_tasks_v2, name="get_integration_tasks_v2")
        self._add_tool(server=server, method=self.get_integration_types, name="get_integration_types")
        self._add_tool(server=server, method=self.get_integrations_v2, name="get_integrations_v2")
        self._add_tool(server=server, method=self.get_service_violation_types, name="get_service_violation_types")
        self._add_tool(server=server, method=self.get_services_count, name="get_services_count")
        self._add_tool(server=server, method=self.get_tags, name="get_tags")
        self._add_tool(server=server, method=self.get_users_v2, name="get_users_v2")
        self._add_tool(server=server, method=self.service_now_get_deployments, name="service_now_get_deployments")
        self._add_tool(server=server, method=self.service_now_get_services, name="service_now_get_services")
        self._add_tool(server=server, method=self.get_service_artifacts, name="get_service_artifacts")
        self._add_tool(server=server, method=self.create_executor_node, name="create_executor_node", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.create_integration, name="create_integration", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.create_integration_task, name="create_integration_task", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.post_group_v2, name="post_group_v2", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.set_cloud_security_integration_state, name="set_cloud_security_integration_state", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_executor_node, name="update_executor_node", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_integration, name="update_integration", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_integration_task, name="update_integration_task", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.upsert_business_applications, name="upsert_business_applications", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.upsert_tags, name="upsert_tags", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_executor_node, name="delete_executor_node", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_integration, name="delete_integration", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_integration_task, name="delete_integration_task", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_tags, name="delete_tags", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.execute_function_data_count, name="execute_function_data_count", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.execute_functions_count, name="execute_functions_count", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.execute_query, name="execute_query", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def create_executor_node(
        self,
        body: dict = Field(description="Request JSON body for `CreateExecutorNode` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create a new relay node"""
        return self._call(operation="CreateExecutorNode", query_params=None, body_params=body, error_message="CreateExecutorNode failed", member_cid=member_cid)

    def create_integration(
        self,
        body: dict = Field(description="Request JSON body for `CreateIntegration` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create a new integration"""
        return self._call(operation="CreateIntegration", query_params=None, body_params=body, error_message="CreateIntegration failed", member_cid=member_cid)

    def create_integration_task(
        self,
        body: dict = Field(description="Request JSON body for `CreateIntegrationTask` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create new integration task."""
        return self._call(operation="CreateIntegrationTask", query_params=None, body_params=body, error_message="CreateIntegrationTask failed", member_cid=member_cid)

    def delete_executor_node(
        self,
        id: str = Field(description="`id` path parameter (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete a relay node"""
        return self._call(operation="DeleteExecutorNode", query_params=None, path_params={"id": id}, error_message="DeleteExecutorNode failed", member_cid=member_cid)

    def delete_integration(
        self,
        id: str = Field(description="`id` path parameter (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete an existing integration by its ID"""
        return self._call(operation="DeleteIntegration", query_params=None, path_params={"id": id}, error_message="DeleteIntegration failed", member_cid=member_cid)

    def delete_integration_task(
        self,
        id: str = Field(description="`id` path parameter (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete an existing integration task by its ID"""
        return self._call(operation="DeleteIntegrationTask", query_params=None, path_params={"id": id}, error_message="DeleteIntegrationTask failed", member_cid=member_cid)

    def delete_tags(
        self,
        body: dict = Field(description="Request JSON body for `DeleteTags` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Remove existing tags"""
        return self._call(operation="DeleteTags", query_params=None, body_params=body, error_message="DeleteTags failed", member_cid=member_cid)

    def execute_function_data(
        self,
        field: str = Field(description="`field` query parameter."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """A selected list of queryLanguage queries. request & response are in MSA format"""
        return self._call(operation="ExecuteFunctionData", query_params={"field": field}, error_message="ExecuteFunctionData failed", member_cid=member_cid)

    def execute_function_data_count(
        self,
        query_name: str = Field(description="`query_name` query parameter."),
        cloud_provider: str = Field(description="`cloud_provider` query parameter."),
        aws_lambda_arn: str | None = Field(default=None, description="required for 'aws' cloud provider"),
        gcp_cloud_function_url: str | None = Field(default=None, description="required for 'gcp' cloud provider"),
        azure_site_subscription_id: str | None = Field(default=None, description="required for 'azure' cloud provider"),
        azure_site_resource_group: str | None = Field(default=None, description="required for 'azure' cloud provider"),
        azure_function_app_name: str | None = Field(default=None, description="required for 'azure' cloud provider"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """A selected list of queryLanguage count queries. request & response are in MSA format"""
        return self._call(operation="ExecuteFunctionDataCount", query_params={"query_name": query_name, "cloud_provider": cloud_provider, "aws_lambda_arn": aws_lambda_arn, "gcp_cloud_function_url": gcp_cloud_function_url, "azure_site_subscription_id": azure_site_subscription_id, "azure_site_resource_group": azure_site_resource_group, "azure_function_app_name": azure_function_app_name}, error_message="ExecuteFunctionDataCount failed", member_cid=member_cid)

    def execute_function_data_query(
        self,
        field: str = Field(description="`field` query parameter."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """A selected list of queryLanguage queries. request & response are in MSA format"""
        return self._call(operation="ExecuteFunctionDataQuery", query_params={"field": field}, error_message="ExecuteFunctionDataQuery failed", member_cid=member_cid)

    def execute_function_data_query_count(
        self,
        field: str = Field(description="`field` query parameter."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """A selected list of queryLanguage count queries. request & response are in MSA format"""
        return self._call(operation="ExecuteFunctionDataQueryCount", query_params={"field": field}, error_message="ExecuteFunctionDataQueryCount failed", member_cid=member_cid)

    def execute_functions(
        self,
        field: str = Field(description="`field` query parameter."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """A selected list of queryLanguage services queries. request & response are in MSA format"""
        return self._call(operation="ExecuteFunctions", query_params={"field": field}, error_message="ExecuteFunctions failed", member_cid=member_cid)

    def execute_functions_count(
        self,
        query_name: str = Field(description="`query_name` query parameter."),
        cloud_provider: list[str] | None = Field(default=None, description="`cloud_provider` query parameter."),
        cloud_account_id: list[str] | None = Field(default=None, description="required for 'aws' cloud provider"),
        region: list[str] | None = Field(default=None, description="required for 'gcp' cloud provider"),
        cid: list[str] | None = Field(default=None, description="required for 'azure' cloud provider"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """A selected list of queryLanguage count queries. request & response are in MSA format"""
        return self._call(operation="ExecuteFunctionsCount", query_params={"query_name": query_name, "cloud_provider": cloud_provider, "cloud_account_id": cloud_account_id, "region": region, "cid": cid}, error_message="ExecuteFunctionsCount failed", member_cid=member_cid)

    def execute_functions_overtime(
        self,
        field: str = Field(description="`field` query parameter."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """A selected list of queryLanguage overtime queries. request & response are in MSA format"""
        return self._call(operation="ExecuteFunctionsOvertime", query_params={"field": field}, error_message="ExecuteFunctionsOvertime failed", member_cid=member_cid)

    def execute_functions_query(
        self,
        field: str = Field(description="`field` query parameter."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """A selected list of queryLanguage services queries. request & response are in MSA format"""
        return self._call(operation="ExecuteFunctionsQuery", query_params={"field": field}, error_message="ExecuteFunctionsQuery failed", member_cid=member_cid)

    def execute_functions_query_count(
        self,
        field: str = Field(description="`field` query parameter."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """A selected list of queryLanguage count queries. request & response are in MSA format"""
        return self._call(operation="ExecuteFunctionsQueryCount", query_params={"field": field}, error_message="ExecuteFunctionsQueryCount failed", member_cid=member_cid)

    def execute_functions_query_overtime(
        self,
        field: str = Field(description="`field` query parameter."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """A selected list of queryLanguage overtime queries. request & response are in MSA format"""
        return self._call(operation="ExecuteFunctionsQueryOvertime", query_params={"field": field}, error_message="ExecuteFunctionsQueryOvertime failed", member_cid=member_cid)

    def execute_query(
        self,
        body: dict = Field(description="Request JSON body for `ExecuteQuery` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Execute a query. The syntax used is identical to that of the query page."""
        return self._call(operation="ExecuteQuery", query_params=None, body_params=body, error_message="ExecuteQuery failed", member_cid=member_cid)

    def get_cloud_security_integration_state(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get Cloud Security integration state"""
        return self._call(operation="GetCloudSecurityIntegrationState", query_params=None, error_message="GetCloudSecurityIntegrationState failed", member_cid=member_cid)

    def get_executor_nodes(
        self,
        node_type: str = Field(description="`node_type` query parameter."),
        integration_type: int | None = Field(default=None, description="`integration_type` query parameter."),
        offset: int | None = Field(default=None, description="`offset` query parameter."),
        limit: int | None = Field(default=None, description="`limit` query parameter."),
        order_by: str | None = Field(default=None, description="`order_by` query parameter."),
        direction: str | None = Field(default=None, description="`direction` query parameter."),
        executor_node_ids: list[str] | None = Field(default=None, description="executor node ids"),
        executor_node_names: list[str] | None = Field(default=None, description="executor node names"),
        executor_node_states: list[str] | None = Field(default=None, description="executor node states"),
        executor_node_types: list[str] | None = Field(default=None, description="executor node types"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get all the relay nodes"""
        return self._call(operation="GetExecutorNodes", query_params={"node_type": node_type, "integration_type": integration_type, "offset": offset, "limit": limit, "order_by": order_by, "direction": direction, "executor_node_ids": executor_node_ids, "executor_node_names": executor_node_names, "executor_node_states": executor_node_states, "executor_node_types": executor_node_types}, error_message="GetExecutorNodes failed", member_cid=member_cid)

    def get_executor_nodes_metadata(
        self,
        executor_node_ids: list[str] | None = Field(default=None, description="executor node ids"),
        executor_node_names: list[str] | None = Field(default=None, description="executor node names"),
        executor_node_states: list[str] | None = Field(default=None, description="executor node states"),
        executor_node_types: list[str] | None = Field(default=None, description="executor node types"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get metadata about all executor nodes"""
        return self._call(operation="GetExecutorNodesMetadata", query_params={"executor_node_ids": executor_node_ids, "executor_node_names": executor_node_names, "executor_node_states": executor_node_states, "executor_node_types": executor_node_types}, error_message="GetExecutorNodesMetadata failed", member_cid=member_cid)

    def get_group_hierarchy(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get group hierarchy"""
        return self._call(operation="GetGroupHierarchy", query_params=None, error_message="GetGroupHierarchy failed", member_cid=member_cid)

    def get_groups_v2(
        self,
        type: str | None = Field(default=None, description="Group types to query - can either be empty (all), parents, children"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """"""
        return self._call(operation="GetGroupsV2", query_params={"type": type}, error_message="GetGroupsV2 failed", member_cid=member_cid)

    def get_integration_tasks_admin(
        self,
        integration_task_type: int | None = Field(default=None, description="`integration_task_type` query parameter."),
        category: str | None = Field(default=None, description="`category` query parameter."),
        offset: int | None = Field(default=None, description="`offset` query parameter."),
        limit: int | None = Field(default=None, description="`limit` query parameter."),
        orderBy: str | None = Field(default=None, description="`orderBy` query parameter."),
        direction: str | None = Field(default=None, description="`direction` query parameter."),
        integration_task_types: int | None = Field(default=None, description="`integration_task_types` query parameter."),
        ids: int | None = Field(default=None, description="`ids` query parameter."),
        names: str | None = Field(default=None, description="`names` query parameter."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get all the integration tasks, requires admin scope"""
        return self._call(operation="GetIntegrationTasksAdmin", query_params={"integration_task_type": integration_task_type, "category": category, "offset": offset, "limit": limit, "orderBy": orderBy, "direction": direction, "integration_task_types": integration_task_types, "ids": ids, "names": names}, error_message="GetIntegrationTasksAdmin failed", member_cid=member_cid)

    def get_integration_tasks_metadata(
        self,
        category: str | None = Field(default=None, description="`category` query parameter."),
        integration_task_types: int | None = Field(default=None, description="`integration_task_types` query parameter."),
        ids: int | None = Field(default=None, description="`ids` query parameter."),
        names: str | None = Field(default=None, description="`names` query parameter."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get metadata about all integration tasks"""
        return self._call(operation="GetIntegrationTasksMetadata", query_params={"category": category, "integration_task_types": integration_task_types, "ids": ids, "names": names}, error_message="GetIntegrationTasksMetadata failed", member_cid=member_cid)

    def get_integration_tasks_v2(
        self,
        integration_task_type: int | None = Field(default=None, description="`integration_task_type` query parameter."),
        category: str | None = Field(default=None, description="`category` query parameter."),
        offset: int | None = Field(default=None, description="`offset` query parameter."),
        limit: int | None = Field(default=None, description="`limit` query parameter."),
        orderBy: str | None = Field(default=None, description="`orderBy` query parameter."),
        direction: str | None = Field(default=None, description="`direction` query parameter."),
        integration_task_types: int | None = Field(default=None, description="`integration_task_types` query parameter."),
        ids: int | None = Field(default=None, description="`ids` query parameter."),
        names: str | None = Field(default=None, description="`names` query parameter."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get all the integration tasks"""
        return self._call(operation="GetIntegrationTasksV2", query_params={"integration_task_type": integration_task_type, "category": category, "offset": offset, "limit": limit, "orderBy": orderBy, "direction": direction, "integration_task_types": integration_task_types, "ids": ids, "names": names}, error_message="GetIntegrationTasksV2 failed", member_cid=member_cid)

    def get_integration_types(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get all the integration types"""
        return self._call(operation="GetIntegrationTypes", query_params=None, error_message="GetIntegrationTypes failed", member_cid=member_cid)

    def get_integrations_v2(
        self,
        integration_type: int | None = Field(default=None, description="`integration_type` query parameter."),
        category: str | None = Field(default=None, description="`category` query parameter."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get a list of all the integrations"""
        return self._call(operation="GetIntegrationsV2", query_params={"integration_type": integration_type, "category": category}, error_message="GetIntegrationsV2 failed", member_cid=member_cid)

    def get_service_violation_types(
        self,
        body: dict = Field(description="Request JSON body for `GetServiceViolationTypes` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get the different types of violation"""
        return self._call(operation="GetServiceViolationTypes", query_params=None, body_params=body, error_message="GetServiceViolationTypes failed", member_cid=member_cid)

    def get_services_count(
        self,
        body: dict = Field(description="Request JSON body for `GetServicesCount` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get the total amount of existing services"""
        return self._call(operation="GetServicesCount", query_params=None, body_params=body, error_message="GetServicesCount failed", member_cid=member_cid)

    def get_tags(
        self,
        isUnique: bool | None = Field(default=None, description="`isUnique` query parameter."),
        tagName: str | None = Field(default=None, description="`tagName` query parameter."),
        limit: int | None = Field(default=None, description="`limit` query parameter."),
        offset: int | None = Field(default=None, description="`offset` query parameter."),
        name: list[str] | None = Field(default=None, description="`name` query parameter."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get all the tags"""
        return self._call(operation="GetTags", query_params={"isUnique": isUnique, "tagName": tagName, "limit": limit, "offset": offset, "name": name}, error_message="GetTags failed", member_cid=member_cid)

    def get_users_v2(
        self,
        pagination: str | None = Field(default=None, description="URL encoded pagination JSON - limit, offset, direction, orderBy"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """List users"""
        return self._call(operation="GetUsersV2", query_params={"pagination": pagination}, error_message="GetUsersV2 failed", member_cid=member_cid)

    def post_group_v2(
        self,
        body: dict = Field(description="Request JSON body for `PostGroupV2` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create group"""
        return self._call(operation="PostGroupV2", query_params=None, body_params=body, error_message="PostGroupV2 failed", member_cid=member_cid)

    def service_now_get_deployments(
        self,
        ql_filters: str | None = Field(default=None, description="`ql_filters` query parameter."),
        limit: int | None = Field(default=None, description="`limit` query parameter."),
        offset: int | None = Field(default=None, description="`offset` query parameter."),
        orderBy: str | None = Field(default=None, description="`orderBy` query parameter."),
        direction: str | None = Field(default=None, description="`direction` query parameter."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """"""
        return self._call(operation="ServiceNowGetDeployments", query_params={"ql_filters": ql_filters, "limit": limit, "offset": offset, "orderBy": orderBy, "direction": direction}, error_message="ServiceNowGetDeployments failed", member_cid=member_cid)

    def service_now_get_services(
        self,
        ql_filters: str | None = Field(default=None, description="`ql_filters` query parameter."),
        exclude_artifacts: bool | None = Field(default=None, description="`exclude_artifacts` query parameter."),
        limit: int | None = Field(default=None, description="`limit` query parameter."),
        offset: int | None = Field(default=None, description="`offset` query parameter."),
        orderBy: str | None = Field(default=None, description="`orderBy` query parameter."),
        direction: str | None = Field(default=None, description="`direction` query parameter."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """"""
        return self._call(operation="ServiceNowGetServices", query_params={"ql_filters": ql_filters, "exclude_artifacts": exclude_artifacts, "limit": limit, "offset": offset, "orderBy": orderBy, "direction": direction}, error_message="ServiceNowGetServices failed", member_cid=member_cid)

    def set_cloud_security_integration_state(
        self,
        body: dict = Field(description="Request JSON body for `SetCloudSecurityIntegrationState` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Set Cloud Security integration state"""
        return self._call(operation="SetCloudSecurityIntegrationState", query_params=None, body_params=body, error_message="SetCloudSecurityIntegrationState failed", member_cid=member_cid)

    def update_executor_node(
        self,
        body: dict = Field(description="Request JSON body for `UpdateExecutorNode` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update an existing relay node"""
        return self._call(operation="UpdateExecutorNode", query_params=None, body_params=body, error_message="UpdateExecutorNode failed", member_cid=member_cid)

    def update_integration(
        self,
        id: str = Field(description="`id` path parameter (required)."),
        body: dict = Field(description="Request JSON body for `UpdateIntegration` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update an existing integration by its ID"""
        return self._call(operation="UpdateIntegration", query_params=None, path_params={"id": id}, body_params=body, error_message="UpdateIntegration failed", member_cid=member_cid)

    def update_integration_task(
        self,
        id: str = Field(description="`id` path parameter (required)."),
        body: dict = Field(description="Request JSON body for `UpdateIntegrationTask` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update an existing integration task by its ID"""
        return self._call(operation="UpdateIntegrationTask", query_params=None, path_params={"id": id}, body_params=body, error_message="UpdateIntegrationTask failed", member_cid=member_cid)

    def upsert_business_applications(
        self,
        body: dict = Field(description="Request JSON body for `UpsertBusinessApplications` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create or Update Business Applications"""
        return self._call(operation="UpsertBusinessApplications", query_params=None, body_params=body, error_message="UpsertBusinessApplications failed", member_cid=member_cid)

    def upsert_tags(
        self,
        body: dict = Field(description="Request JSON body for `UpsertTags` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create new or update existing tag. You can update unique tags table or regular tags table"""
        return self._call(operation="UpsertTags", query_params=None, body_params=body, error_message="UpsertTags failed", member_cid=member_cid)

    def get_service_artifacts(
        self,
        persistentSignature: str = Field(description="`persistentSignature` query parameter."),
        optionalTime: int | None = Field(default=None, description="`optionalTime` query parameter."),
        revisionId: int | None = Field(default=None, description="`revisionId` query parameter."),
        limit: int | None = Field(default=None, description="`limit` query parameter."),
        offset: int | None = Field(default=None, description="`offset` query parameter."),
        orderBy: list[str] | None = Field(default=None, description="`orderBy` query parameter."),
        direction: str | None = Field(default=None, description="`direction` query parameter."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """"""
        return self._call(operation="getServiceArtifacts", query_params={"persistentSignature": persistentSignature, "optionalTime": optionalTime, "revisionId": revisionId, "limit": limit, "offset": offset, "orderBy": orderBy, "direction": direction}, error_message="getServiceArtifacts failed", member_cid=member_cid)
