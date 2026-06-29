"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `workflows` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenWorkflowsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `workflows` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.workflow_activities_content_combined, name="workflow_activities_content_combined")
        self._add_tool(server=server, method=self.v1_child_executions_query, name="v1_child_executions_query")
        self._add_tool(server=server, method=self.workflow_definitions_action, name="workflow_definitions_action", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.workflow_system_definitions_promote, name="workflow_system_definitions_promote", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.workflow_system_definitions_provision, name="workflow_system_definitions_provision", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.workflow_execute_internal, name="workflow_execute_internal", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.workflow_execute_single_node_v1, name="workflow_execute_single_node_v1", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.workflow_system_definitions_de_provision, name="workflow_system_definitions_de_provision", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def workflow_activities_content_combined(
        self,
        filter: str | None = Field(default=None, description="FQL query specifying filter parameters."),
        offset: str | None = Field(default=None, description="Starting pagination offset of records to return."),
        limit: int | None = Field(default=None, description="Maximum number of records to return."),
        sort: str | None = Field(default=None, description="Sort items by providing a comma separated list of property and direction (eg name.desc,time.asc). If direction is omitted, defaults to descending."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for activities by name. Returns all supported activities if no filter specified"""
        return self._call(operation="WorkflowActivitiesContentCombined", query_params={"filter": filter, "offset": offset, "limit": limit, "sort": sort}, error_message="WorkflowActivitiesContentCombined failed", member_cid=member_cid)

    def workflow_definitions_action(
        self,
        action_name: str = Field(description="Specify one of these actions: enable: enable the workflow(s) specified in ids. disable: disable the workflow(s) specified in ids. cancel: cancel all in-flight executions for the workflow specified in ids"),
        body: dict = Field(description="Request JSON body for `WorkflowDefinitionsAction` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Enable or disable a workflow definition, or stop all executions for a definition. When a definition is disabled it will not execute against any new trigger events."""
        return self._call(operation="WorkflowDefinitionsAction", query_params={"action_name": action_name}, body_params=body, error_message="WorkflowDefinitionsAction failed", member_cid=member_cid)

    def workflow_execute_internal(
        self,
        body: dict = Field(description="Request JSON body for `WorkflowExecuteInternal` per the CrowdStrike API schema (required)."),
        execution_cid: list[str] | None = Field(default=None, description="CID(s) to execute on. This can be a child if this is a flight control enabled definition. If unset the definition CID is used."),
        definition_id: list[str] | None = Field(default=None, description="Definition ID to execute, either a name or an ID can be specified."),
        name: str | None = Field(default=None, description="Workflow name to execute, either a name or an ID can be specified."),
        key: str | None = Field(default=None, description="Key used to help deduplicate executions, if unset a new UUID is used"),
        depth: int | None = Field(default=None, description="Used to record the execution depth to help limit execution loops when a workflow triggers another. The maximum depth is 4."),
        batch_size: int | None = Field(default=None, description="Used to set the batchSize, if unset the default batchSize is used"),
        source_event_url: str | None = Field(default=None, description="Used to record a URL to the source that led to triggering this workflow"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Executes an on-demand Workflow - internal workflows permitted, the body is JSON used to trigger the execution, the response the execution ID(s)"""
        return self._call(operation="WorkflowExecuteInternal", query_params={"execution_cid": execution_cid, "definition_id": definition_id, "name": name, "key": key, "depth": depth, "batch_size": batch_size, "source_event_url": source_event_url}, body_params=body, error_message="WorkflowExecuteInternal failed", member_cid=member_cid)

    def workflow_execute_single_node_v1(
        self,
        body: dict = Field(description="Request JSON body for `WorkflowExecuteSingleNodeV1` per the CrowdStrike API schema (required)."),
        execution_cid: list[str] | None = Field(default=None, description="CID(s) to execute on. This can be a child if this is a flight control enabled definition. If unset the definition CID is used."),
        definition_id: str | None = Field(default=None, description="Definition ID to execute, either a name or an ID, or the definition itself in the request body, can be specified."),
        name: str | None = Field(default=None, description="Workflow name to execute, either a name or an ID, or the definition itself in the request body, can be specified."),
        key: str | None = Field(default=None, description="Key used to help deduplicate executions, if unset a new UUID is used"),
        depth: int | None = Field(default=None, description="Used to record the execution depth to help limit execution loops when a workflow triggers another. The maximum depth is 4."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Executes a single activity node, resulting in an execution where test_mode=true and single_node_execution=true, associated with a definition ID if provided"""
        return self._call(operation="WorkflowExecuteSingleNodeV1", query_params={"execution_cid": execution_cid, "definition_id": definition_id, "name": name, "key": key, "depth": depth}, body_params=body, error_message="WorkflowExecuteSingleNodeV1 failed", member_cid=member_cid)

    def workflow_system_definitions_de_provision(
        self,
        body: dict = Field(description="Request JSON body for `WorkflowSystemDefinitionsDeProvision` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deprovisions a system definition that was previously provisioned on the target CID"""
        return self._call(operation="WorkflowSystemDefinitionsDeProvision", query_params=None, body_params=body, error_message="WorkflowSystemDefinitionsDeProvision failed", member_cid=member_cid)

    def workflow_system_definitions_promote(
        self,
        body: dict = Field(description="Request JSON body for `WorkflowSystemDefinitionsPromote` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Promotes a version of a system definition for a customer. The customer must already have been provisioned. This allows the caller to apply an updated template version to a specific cid and expects all parameters to be supplied. If the template supports multi-instance the customer scope definition ID must be supplied to determine which customer workflow should be updated."""
        return self._call(operation="WorkflowSystemDefinitionsPromote", query_params=None, body_params=body, error_message="WorkflowSystemDefinitionsPromote failed", member_cid=member_cid)

    def workflow_system_definitions_provision(
        self,
        body: dict = Field(description="Request JSON body for `WorkflowSystemDefinitionsProvision` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Provisions a system definition onto the target CID by using the template and provided parameters"""
        return self._call(operation="WorkflowSystemDefinitionsProvision", query_params=None, body_params=body, error_message="WorkflowSystemDefinitionsProvision failed", member_cid=member_cid)

    def v1_child_executions_query(
        self,
        filter: str | None = Field(default=None, description="FQL query specifying filter parameters."),
        offset: str | None = Field(default=None, description="Starting pagination offset of records to return."),
        limit: int | None = Field(default=None, description="Maximum number of records to return."),
        sort: str | None = Field(default=None, description="Sort items by providing a comma separated list of property and direction (eg name.desc,time.asc). If direction is omitted, defaults to descending."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for child executions by providing a FQL filter and paging details. Returns the set of child workflow execution IDs which match the filter criteria"""
        return self._call(operation="v1_child_executions_query", query_params={"filter": filter, "offset": offset, "limit": limit, "sort": sort}, error_message="v1_child_executions_query failed", member_cid=member_cid)
