"""
Falcon for IT (IT Automation) module for Falcon MCP Server.

Provides read-only tools for inspecting CrowdStrike Falcon for IT (F4IT) tasks,
executions, host status, and policies.

Note: writeable operations (LiveQuery execution, scheduled task creation) are not
exposed via this module — they have complex per-platform body schemas and execute
real actions on production hosts. Use the Falcon console for those operations.
"""

from typing import Any

from mcp.server import FastMCP
from mcp.server.fastmcp.resources import TextResource
from mcp.types import ToolAnnotations
from pydantic import AnyUrl, Field

from falcon_mcp.common.errors import _format_error_response
from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule
from falcon_mcp.resources.falcon_for_it import F4IT_FQL_DOCUMENTATION

logger = get_logger(__name__)

WRITE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True,
)


class FalconForItModule(BaseModule):
    """Module for CrowdStrike Falcon for IT (F4IT)."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.search_tasks, name="search_f4it_tasks")
        self._add_tool(server=server, method=self.get_task_details, name="get_f4it_task_details")
        self._add_tool(server=server, method=self.search_task_executions, name="search_f4it_task_executions")
        self._add_tool(server=server, method=self.get_task_execution, name="get_f4it_task_execution")
        self._add_tool(server=server, method=self.get_task_execution_host_status, name="get_f4it_task_execution_host_status")
        self._add_tool(server=server, method=self.get_execution_results, name="get_f4it_execution_results")
        self._add_tool(server=server, method=self.search_scheduled_tasks, name="search_f4it_scheduled_tasks")
        self._add_tool(server=server, method=self.search_policies, name="search_f4it_policies")
        self._add_tool(
            server=server, method=self.cancel_task_execution, name="cancel_f4it_task_execution",
            annotations=WRITE_ANNOTATIONS,
        )

    def register_resources(self, server: FastMCP) -> None:
        self._add_resource(server, TextResource(
            uri=AnyUrl("falcon://f4it/fql-guide"),
            name="falcon_f4it_fql_guide",
            description="FQL filter guide for Falcon for IT search tools.",
            text=F4IT_FQL_DOCUMENTATION,
        ))

    def search_tasks(
        self,
        filter: str | None = Field(default=None, description="FQL filter; see `falcon://f4it/fql-guide`."),
        limit: int = Field(default=10, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search Falcon for IT tasks (combined: returns full task records)."""
        result = self._base_search_api_call(
            operation="ITAutomationGetTasksByQuery",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search F4IT tasks",
        )
        if self._is_error(result):
            if filter:
                return self._format_fql_error_response([result], filter, F4IT_FQL_DOCUMENTATION)
            return [result]
        return result

    def get_task_details(
        self,
        ids: list[str] = Field(description="Task IDs."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get full task definitions by ID."""
        if not ids:
            return []
        return self._base_get_by_ids(operation="ITAutomationGetTasks", ids=ids, use_params=True)

    def search_task_executions(
        self,
        filter: str | None = Field(default=None, description="FQL filter on executions."),
        limit: int = Field(default=10, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search task executions (combined: returns full execution records)."""
        result = self._base_search_api_call(
            operation="ITAutomationGetTaskExecutionsByQuery",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search F4IT task executions",
        )
        if self._is_error(result):
            return [result]
        return result

    def get_task_execution(
        self,
        ids: list[str] = Field(description="Task execution IDs."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get task execution status by ID."""
        if not ids:
            return []
        return self._base_get_by_ids(operation="ITAutomationGetTaskExecution", ids=ids, use_params=True)

    def get_task_execution_host_status(
        self,
        ids: list[str] = Field(description="Task execution host status IDs."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get per-host status for a task execution."""
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="ITAutomationGetTaskExecutionHostStatus", ids=ids, use_params=True,
        )

    def get_execution_results(
        self,
        execution_id: str = Field(description="Task execution ID."),
        offset: int = Field(default=0, ge=0, description="Offset within results."),
        limit: int = Field(default=100, ge=1, le=10000, description="Max rows."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Read raw results rows for a task execution."""
        result = self._base_search_api_call(
            operation="ITAutomationGetExecutionResults",
            search_params={"id": execution_id, "offset": offset, "limit": limit, "sort": sort},
            error_message="Failed to fetch F4IT execution results",
        )
        if self._is_error(result):
            return [result]
        return result

    def search_scheduled_tasks(
        self,
        filter: str | None = Field(default=None, description="FQL filter."),
        limit: int = Field(default=10, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search scheduled F4IT tasks."""
        result = self._base_search_api_call(
            operation="ITAutomationCombinedScheduledTasks",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search scheduled F4IT tasks",
        )
        if self._is_error(result):
            return [result]
        return result

    def search_policies(
        self,
        filter: str | None = Field(default=None, description="FQL filter."),
        limit: int = Field(default=10, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search F4IT policies (returns IDs)."""
        result = self._base_search_api_call(
            operation="ITAutomationQueryPolicies",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search F4IT policies",
        )
        if self._is_error(result):
            return [result]
        return result

    def cancel_task_execution(
        self,
        task_execution_id: str = Field(description="Task execution ID to cancel."),
    ) -> list[dict[str, Any]]:
        """Cancel a running F4IT task execution."""
        if not task_execution_id:
            return [_format_error_response(
                "`task_execution_id` is required.",
                operation="ITAutomationCancelTaskExecution",
            )]
        result = self._base_query_api_call(
            operation="ITAutomationCancelTaskExecution",
            body_params={"task_execution_id": task_execution_id},
            error_message="Failed to cancel F4IT execution",
        )
        if self._is_error(result):
            return [result]
        return result
