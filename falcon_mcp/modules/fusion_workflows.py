"""
Fusion SOAR Workflows module for Falcon MCP Server.

Provides tools for searching workflow definitions/executions and executing on-demand
workflows. Defines + execute are write operations.
"""

from typing import Any

from mcp.server import FastMCP
from mcp.server.fastmcp.resources import TextResource
from mcp.types import ToolAnnotations
from pydantic import AnyUrl, Field

from falcon_mcp.common.errors import _format_error_response, handle_api_response
from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule
from falcon_mcp.resources.fusion_workflows import WORKFLOWS_FQL_DOCUMENTATION

logger = get_logger(__name__)

WRITE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True,
)
READ_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=True,
)


class FusionWorkflowsModule(BaseModule):
    """Module for CrowdStrike Fusion SOAR Workflows."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.search_workflow_definitions, name="search_workflow_definitions")
        self._add_tool(server=server, method=self.search_workflow_executions, name="search_workflow_executions")
        self._add_tool(server=server, method=self.search_workflow_triggers, name="search_workflow_triggers")
        self._add_tool(server=server, method=self.search_workflow_activities, name="search_workflow_activities")
        self._add_tool(server=server, method=self.get_workflow_execution_results, name="get_workflow_execution_results")
        self._add_tool(
            server=server, method=self.execute_workflow, name="execute_workflow",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.cancel_workflow_executions, name="cancel_workflow_executions",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.update_workflow_definition, name="update_workflow_definition",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(server=server, method=self.export_workflow_definition, name="export_workflow_definition")
        self._add_tool(
            server=server, method=self.import_workflow_definition, name="import_workflow_definition",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.run_mock_workflow, name="run_mock_workflow",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.retry_workflow_execution, name="retry_workflow_execution",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(server=server, method=self.list_workflow_human_inputs, name="list_workflow_human_inputs")
        self._add_tool(
            server=server, method=self.respond_to_workflow_human_input, name="respond_to_workflow_human_input",
            annotations=WRITE_ANNOTATIONS,
        )

    def register_resources(self, server: FastMCP) -> None:
        self._add_resource(server, TextResource(
            uri=AnyUrl("falcon://workflows/fql-guide"),
            name="falcon_workflows_fql_guide",
            description="FQL filter guide for Fusion Workflows search tools.",
            text=WORKFLOWS_FQL_DOCUMENTATION,
        ))

    def search_workflow_definitions(
        self,
        filter: str | None = Field(default=None, description="FQL filter; see `falcon://workflows/fql-guide`."),
        limit: int = Field(default=10, ge=1, le=500, description="Max records."),
        offset: str | None = Field(default=None, description="Pagination offset (string token)."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search Fusion workflow definitions and return full definitions."""
        result = self._base_search_api_call(
            operation="WorkflowDefinitionsCombined",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search workflow definitions",
        )
        if self._is_error(result):
            if filter:
                return self._format_fql_error_response([result], filter, WORKFLOWS_FQL_DOCUMENTATION)
            return [result]
        return result

    def search_workflow_executions(
        self,
        filter: str | None = Field(default=None, description="FQL filter."),
        limit: int = Field(default=10, ge=1, le=500, description="Max records."),
        offset: str | None = Field(default=None, description="Pagination offset (string token)."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search workflow executions and return full execution details."""
        result = self._base_search_api_call(
            operation="WorkflowExecutionsCombined",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search workflow executions",
        )
        if self._is_error(result):
            return [result]
        return result

    def search_workflow_triggers(
        self,
        filter: str | None = Field(default=None, description="FQL filter."),
        limit: int = Field(default=10, ge=1, le=500, description="Max records."),
        offset: str | None = Field(default=None, description="Pagination offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List the available workflow triggers."""
        result = self._base_search_api_call(
            operation="WorkflowTriggersCombined",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to list workflow triggers",
        )
        if self._is_error(result):
            return [result]
        return result

    def search_workflow_activities(
        self,
        filter: str | None = Field(default=None, description="FQL filter."),
        limit: int = Field(default=10, ge=1, le=500, description="Max records."),
        offset: str | None = Field(default=None, description="Pagination offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List the available workflow activities (the actions a workflow can perform)."""
        result = self._base_search_api_call(
            operation="WorkflowActivitiesCombined",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to list workflow activities",
        )
        if self._is_error(result):
            return [result]
        return result

    def get_workflow_execution_results(
        self,
        ids: list[str] = Field(description="Execution IDs."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get results for the given workflow execution IDs."""
        if not ids:
            return []
        return self._base_get_by_ids(operation="WorkflowExecutionResults", ids=ids, use_params=True)

    def execute_workflow(
        self,
        definition_id: str | None = Field(
            default=None,
            description="Workflow definition ID. Either `definition_id` or `name` is required.",
        ),
        name: str | None = Field(
            default=None,
            description="Workflow definition name. Either `definition_id` or `name` is required.",
        ),
        body: dict[str, Any] = Field(
            default_factory=dict,
            description="Workflow input payload (passed verbatim as the request body).",
        ),
        key: str | None = Field(
            default=None,
            description="Optional dedup key. If unset the API generates a UUID.",
        ),
        execution_cid: str | None = Field(
            default=None,
            description="(Flight Control) Member CID to execute the workflow against.",
        ),
        source_event_url: str | None = Field(
            default=None,
            description="Optional URL recorded as the source that triggered this workflow.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Execute an on-demand Fusion workflow.

        WARNING: this triggers a real workflow run, which may have side-effects on
        production resources depending on the workflow definition.
        """
        if not definition_id and not name:
            return [_format_error_response(
                "Provide `definition_id` or `name`.", operation="WorkflowExecute",
            )]
        query: dict[str, Any] = {}
        if definition_id:
            query["definition_id"] = definition_id
        if name:
            query["name"] = name
        if key:
            query["key"] = key
        if execution_cid:
            query["execution_cid"] = execution_cid
        if source_event_url:
            query["source_event_url"] = source_event_url
        result = self._base_query_api_call(
            operation="WorkflowExecute",
            query_params=query,
            body_params=body or {},
            error_message="Failed to execute workflow",
        )
        if self._is_error(result):
            return [result]
        return result

    def cancel_workflow_executions(
        self,
        ids: list[str] = Field(description="Execution IDs to cancel."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Cancel running workflow executions."""
        if not ids:
            return [_format_error_response(
                "`ids` is required.", operation="WorkflowExecutionsAction",
            )]
        result = self._base_query_api_call(
            operation="WorkflowExecutionsAction",
            query_params={"action_name": "cancel"},
            body_params={"ids": ids},
            error_message="Failed to cancel workflow executions",
        )
        if self._is_error(result):
            return [result]
        return result

    def update_workflow_definition(
        self,
        definition_body: dict[str, Any] = Field(
            description=(
                "Full workflow definition object to replace the existing definition. "
                "Must include `id` of the definition to update. Obtain the current definition "
                "via `falcon_export_workflow_definition`, modify it, then pass it here."
            ),
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Update (replace) a Fusion workflow definition.

        Provide the complete definition object including the `id` field. Fetch the current
        definition with `falcon_export_workflow_definition` first to avoid overwriting
        unintended fields.
        """
        if not definition_body.get("id"):
            return [_format_error_response(
                "`definition_body` must contain an `id` field.", operation="WorkflowDefinitionsUpdate",
            )]
        result = self._base_query_api_call(
            operation="WorkflowDefinitionsUpdate",
            body_params=definition_body,
            error_message="Failed to update workflow definition",
        )
        if self._is_error(result):
            return [result]
        return result

    def export_workflow_definition(
        self,
        id: str = Field(description="Workflow definition ID to export. Obtain from `falcon_search_workflow_definitions`."),
    ) -> dict[str, Any]:
        """Export a workflow definition as a YAML string.

        Returns the raw YAML content of the workflow definition, suitable for backup,
        editing, or re-importing via `falcon_import_workflow_definition`.
        """
        response = self.client.command_for("WorkflowDefinitionsExport", parameters={"id": id})
        if not isinstance(response, dict):
            return {"error": "Unexpected response format"}
        status = response.get("status_code")
        if status not in (200, None):
            return handle_api_response(
                response, operation="WorkflowDefinitionsExport",
                error_message="Failed to export workflow definition", default_result={},
            )
        body = response.get("body", "")
        if isinstance(body, bytes):
            return {"definition_yaml": body.decode("utf-8", errors="replace"), "id": id}
        return {"definition_yaml": str(body), "id": id}

    def import_workflow_definition(
        self,
        definition_yaml: str = Field(
            description="Workflow definition as a YAML string. Obtain from `falcon_export_workflow_definition`, modify as needed, then pass here.",
        ),
        name: str | None = Field(
            default=None,
            description="Override the workflow name on import. If omitted, uses the name from the YAML definition.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Import a workflow definition from YAML.

        Creates a new workflow definition from the provided YAML content.
        Typically used to restore a backup or deploy a workflow to another tenant.
        """
        data: dict[str, Any] = {"data_file": definition_yaml}
        params: dict[str, Any] = {}
        if name:
            params["name"] = name
        response = self.client.command_for(
            "WorkflowDefinitionsImport",
            data=data,
            parameters=params if params else None,
        )
        return handle_api_response(
            response, operation="WorkflowDefinitionsImport",
            error_message="Failed to import workflow definition", default_result=[],
        )

    def run_mock_workflow(
        self,
        definition: dict[str, Any] = Field(
            description="Workflow definition object to mock-execute (same structure as a real definition).",
        ),
        mocks: dict[str, Any] | None = Field(
            default=None,
            description="Optional mock activity outputs keyed by activity ID. Use to simulate specific API responses during the test run.",
        ),
        execution_cid: str | None = Field(
            default=None,
            description="(Flight Control) Member CID to run the mock against. Leave unset for parent tenant.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Run a mock workflow execution for testing without side-effects.

        Executes the workflow definition in a sandbox — actions are simulated using
        the provided `mocks` rather than calling real APIs. Use this to validate
        workflow logic before activating it in production.
        """
        body: dict[str, Any] = {"definition": definition}
        if mocks:
            body["mocks"] = mocks
        query: dict[str, Any] = {}
        if execution_cid:
            query["execution_cid"] = execution_cid
        result = self._base_query_api_call(
            operation="WorkflowMockExecute",
            query_params=query if query else None,
            body_params=body,
            error_message="Failed to run mock workflow",
        )
        if self._is_error(result):
            return [result]
        return result

    def retry_workflow_execution(
        self,
        ids: list[str] = Field(description="Execution IDs to retry. Obtain from `falcon_search_workflow_executions`."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Retry failed workflow executions.

        Re-queues the specified executions from the point of failure.
        Only executions in a terminal failed state can be retried.
        """
        if not ids:
            return [_format_error_response("`ids` is required.", operation="WorkflowExecutionsAction")]
        result = self._base_query_api_call(
            operation="WorkflowExecutionsAction",
            query_params={"action_name": "retry"},
            body_params={"ids": ids},
            error_message="Failed to retry workflow executions",
        )
        if self._is_error(result):
            return [result]
        return result

    def list_workflow_human_inputs(
        self,
        ids: list[str] = Field(description="Human input request IDs. Obtain from workflow execution results."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Retrieve workflow human input requests by ID.

        Returns pending human decision requests embedded in paused workflow executions.
        Use `falcon_respond_to_workflow_human_input` to approve, deny, or provide data.
        """
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="WorkflowGetHumanInputV1", ids=ids, use_params=True,
        )

    def respond_to_workflow_human_input(
        self,
        id: str = Field(description="Human input request ID. Obtain from `falcon_list_workflow_human_inputs`."),
        input: str = Field(
            description="Response value. For approval prompts: 'true' or 'false'. For data-entry prompts: the value to inject into the workflow.",
        ),
        note: str | None = Field(
            default=None,
            description="Optional analyst note recorded with the response (e.g., justification for approval).",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Respond to a pending workflow human input request.

        Unblocks a paused workflow execution that is waiting for human review.
        After responding, the workflow resumes from the human-input step.
        """
        body: dict[str, Any] = {"id": id, "input": input}
        if note:
            body["note"] = note
        result = self._base_query_api_call(
            operation="WorkflowUpdateHumanInputV1",
            body_params=body,
            error_message="Failed to respond to workflow human input",
        )
        if self._is_error(result):
            return [result]
        return result
