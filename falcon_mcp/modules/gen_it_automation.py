"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `it_automation` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenItAutomationModule(GeneratedModuleBase):
    """Generated tools for the Falcon `it_automation` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.it_automation_get_associated_tasks, name="it_automation_get_associated_tasks")
        self._add_tool(server=server, method=self.it_automation_get_execution_results_search_status, name="it_automation_get_execution_results_search_status")
        self._add_tool(server=server, method=self.it_automation_get_policies, name="it_automation_get_policies")
        self._add_tool(server=server, method=self.it_automation_get_scheduled_tasks, name="it_automation_get_scheduled_tasks")
        self._add_tool(server=server, method=self.it_automation_get_task_groups, name="it_automation_get_task_groups")
        self._add_tool(server=server, method=self.it_automation_get_task_groups_by_query, name="it_automation_get_task_groups_by_query")
        self._add_tool(server=server, method=self.it_automation_get_user_group, name="it_automation_get_user_group")
        self._add_tool(server=server, method=self.it_automation_search_scheduled_tasks, name="it_automation_search_scheduled_tasks")
        self._add_tool(server=server, method=self.it_automation_search_task_executions, name="it_automation_search_task_executions")
        self._add_tool(server=server, method=self.it_automation_search_task_groups, name="it_automation_search_task_groups")
        self._add_tool(server=server, method=self.it_automation_search_tasks, name="it_automation_search_tasks")
        self._add_tool(server=server, method=self.it_automation_search_user_group, name="it_automation_search_user_group")
        self._add_tool(server=server, method=self.it_automation_create_policy, name="it_automation_create_policy", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.it_automation_create_scheduled_task, name="it_automation_create_scheduled_task", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.it_automation_create_task, name="it_automation_create_task", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.it_automation_create_task_group, name="it_automation_create_task_group", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.it_automation_create_user_group, name="it_automation_create_user_group", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.it_automation_start_execution_results_search, name="it_automation_start_execution_results_search", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.it_automation_start_task_execution, name="it_automation_start_task_execution", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.it_automation_update_policies, name="it_automation_update_policies", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.it_automation_update_policies_precedence, name="it_automation_update_policies_precedence", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.it_automation_update_policy_host_groups, name="it_automation_update_policy_host_groups", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.it_automation_update_scheduled_task, name="it_automation_update_scheduled_task", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.it_automation_update_task, name="it_automation_update_task", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.it_automation_update_task_group, name="it_automation_update_task_group", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.it_automation_update_user_group, name="it_automation_update_user_group", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.it_automation_delete_policy, name="it_automation_delete_policy", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.it_automation_delete_scheduled_tasks, name="it_automation_delete_scheduled_tasks", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.it_automation_delete_task, name="it_automation_delete_task", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.it_automation_delete_task_groups, name="it_automation_delete_task_groups", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.it_automation_delete_user_group, name="it_automation_delete_user_group", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.it_automation_rerun_task_execution, name="it_automation_rerun_task_execution", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.it_automation_run_live_query, name="it_automation_run_live_query", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def it_automation_create_policy(
        self,
        body: dict = Field(description="Request JSON body for `ITAutomationCreatePolicy` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Creates a new policy of the specified type. New policies are always added at the end of the precedence list for the provided policy type."""
        return self._call(operation="ITAutomationCreatePolicy", query_params=None, body_params=body, error_message="ITAutomationCreatePolicy failed", member_cid=member_cid)

    def it_automation_create_scheduled_task(
        self,
        body: dict = Field(description="Request JSON body for `ITAutomationCreateScheduledTask` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Creates a scheduled task from the given request"""
        return self._call(operation="ITAutomationCreateScheduledTask", query_params=None, body_params=body, error_message="ITAutomationCreateScheduledTask failed", member_cid=member_cid)

    def it_automation_create_task(
        self,
        body: dict = Field(description="Request JSON body for `ITAutomationCreateTask` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Creates a task with details from the given request."""
        return self._call(operation="ITAutomationCreateTask", query_params=None, body_params=body, error_message="ITAutomationCreateTask failed", member_cid=member_cid)

    def it_automation_create_task_group(
        self,
        body: dict = Field(description="Request JSON body for `ITAutomationCreateTaskGroup` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Creates a task group from the given request"""
        return self._call(operation="ITAutomationCreateTaskGroup", query_params=None, body_params=body, error_message="ITAutomationCreateTaskGroup failed", member_cid=member_cid)

    def it_automation_create_user_group(
        self,
        body: dict = Field(description="Request JSON body for `ITAutomationCreateUserGroup` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Creates a user group from the given request"""
        return self._call(operation="ITAutomationCreateUserGroup", query_params=None, body_params=body, error_message="ITAutomationCreateUserGroup failed", member_cid=member_cid)

    def it_automation_delete_policy(
        self,
        ids: list[str] = Field(description="list of task ids to delete"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deletes 1 or more policies."""
        return self._call(operation="ITAutomationDeletePolicy", query_params={"ids": ids}, error_message="ITAutomationDeletePolicy failed", member_cid=member_cid)

    def it_automation_delete_scheduled_tasks(
        self,
        ids: list[str] = Field(description="Comma separated values of scheduled task IDs to delete"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete one or more scheduled tasks by providing the scheduled tasks IDs"""
        return self._call(operation="ITAutomationDeleteScheduledTasks", query_params={"ids": ids}, error_message="ITAutomationDeleteScheduledTasks failed", member_cid=member_cid)

    def it_automation_delete_task(
        self,
        ids: list[str] = Field(description="IDs of tasks to delete. Use ITAutomationSearchTasks to fetch IDs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deletes tasks for each provided ID"""
        return self._call(operation="ITAutomationDeleteTask", query_params={"ids": ids}, error_message="ITAutomationDeleteTask failed", member_cid=member_cid)

    def it_automation_delete_task_groups(
        self,
        ids: list[str] = Field(description="Comma separated values of task group IDs to delete"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete one or more task groups by providing the task group IDs"""
        return self._call(operation="ITAutomationDeleteTaskGroups", query_params={"ids": ids}, error_message="ITAutomationDeleteTaskGroups failed", member_cid=member_cid)

    def it_automation_delete_user_group(
        self,
        ids: list[str] = Field(description="Comma separated values of user group ids to delete"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deletes user groups for each provided ids"""
        return self._call(operation="ITAutomationDeleteUserGroup", query_params={"ids": ids}, error_message="ITAutomationDeleteUserGroup failed", member_cid=member_cid)

    def it_automation_get_associated_tasks(
        self,
        id: str = Field(description="The ID of the file to fetch associated tasks for"),
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results. Allowed filter fields: [access_type, created_by, created_time, last_run_time, modified_by, modified_time, name, runs, task_type] Example: example_string_field:'example@example.com'+example_date_field:>='2024-08-27T03:21:32Z'"),
        sort: str | None = Field(default=None, description="The sort expression that should be used to sort the results. Allowed sort fields: [name]. Sort either asc (ascending) or desc (descending). Example: example_field|asc"),
        offset: int | None = Field(default=None, description="Starting index for record retrieval. Example: 100"),
        limit: int | None = Field(default=None, description="The maximum records to return. Example: 50"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve tasks associated with the provided file id"""
        return self._call(operation="ITAutomationGetAssociatedTasks", query_params={"id": id, "filter": filter, "sort": sort, "offset": offset, "limit": limit}, error_message="ITAutomationGetAssociatedTasks failed", member_cid=member_cid)

    def it_automation_get_execution_results_search_status(
        self,
        id: str = Field(description="Search Job ID to fetch. UseITAutomationStartExecutionResultsSearch to get the job id"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get the status of an async task execution results. Look for `is_pending: False` to know search is complete."""
        return self._call(operation="ITAutomationGetExecutionResultsSearchStatus", query_params={"id": id}, error_message="ITAutomationGetExecutionResultsSearchStatus failed", member_cid=member_cid)

    def it_automation_get_policies(
        self,
        ids: list[str] = Field(description="One or more (up to 500) policy ids in the form of ids=ID1&ids=ID2"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves the configuration for 1 or more policies."""
        return self._call(operation="ITAutomationGetPolicies", query_params={"ids": ids}, error_message="ITAutomationGetPolicies failed", member_cid=member_cid)

    def it_automation_get_scheduled_tasks(
        self,
        ids: list[str] = Field(description="Scheduled task IDs to fetch. Use ITAutomationSearchScheduledTasks to fetch scheduled task IDs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns scheduled tasks for each provided id"""
        return self._call(operation="ITAutomationGetScheduledTasks", query_params={"ids": ids}, error_message="ITAutomationGetScheduledTasks failed", member_cid=member_cid)

    def it_automation_get_task_groups(
        self,
        ids: list[str] = Field(description="Comma separated values of task group ids to fetch"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns task groups for each provided id"""
        return self._call(operation="ITAutomationGetTaskGroups", query_params={"ids": ids}, error_message="ITAutomationGetTaskGroups failed", member_cid=member_cid)

    def it_automation_get_task_groups_by_query(
        self,
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results. Allowed filter fields: [access_type, created_by, created_time, modified_by, modified_time, name] Example: example_string_field:'example@example.com'+example_date_field:>='2024-08-27T03:21:32Z'"),
        sort: str | None = Field(default=None, description="The sort expression that should be used to sort the results. Allowed sort fields: [access_type, created_by, created_time, modified_by, modified_time, name]. Sort either asc (ascending) or desc (descending). Example: example_field|asc"),
        offset: int | None = Field(default=None, description="Starting index for record retrieval. Example: 100"),
        limit: int | None = Field(default=None, description="The maximum records to return. Example: 50"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns full details of task groups matching the filter query parameter."""
        return self._call(operation="ITAutomationGetTaskGroupsByQuery", query_params={"filter": filter, "sort": sort, "offset": offset, "limit": limit}, error_message="ITAutomationGetTaskGroupsByQuery failed", member_cid=member_cid)

    def it_automation_get_user_group(
        self,
        ids: list[str] = Field(description="Comma separated values of user group ids to fetch"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns user groups for each provided id"""
        return self._call(operation="ITAutomationGetUserGroup", query_params={"ids": ids}, error_message="ITAutomationGetUserGroup failed", member_cid=member_cid)

    def it_automation_rerun_task_execution(
        self,
        body: dict = Field(description="Request JSON body for `ITAutomationRerunTaskExecution` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Rerun the task execution specified in the request"""
        return self._call(operation="ITAutomationRerunTaskExecution", query_params=None, body_params=body, error_message="ITAutomationRerunTaskExecution failed", member_cid=member_cid)

    def it_automation_run_live_query(
        self,
        body: dict = Field(description="Request JSON body for `ITAutomationRunLiveQuery` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Starts a new task execution from the provided query data in the request and returns the initiated task executions"""
        return self._call(operation="ITAutomationRunLiveQuery", query_params=None, body_params=body, error_message="ITAutomationRunLiveQuery failed", member_cid=member_cid)

    def it_automation_search_scheduled_tasks(
        self,
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results. Allowed filter fields: [created_by, created_time, end_time, group_ids, group_names, is_active, last_run, modified_by, modified_time, start_time, task_id, task_name, task_type] Example: example_string_field:'example@example.com'+example_date_field:>='2024-08-27T03:21:32Z'"),
        sort: str | None = Field(default=None, description="The sort expression that should be used to sort the results. Allowed sort fields: [created_by, created_time, end_time, group_ids, group_names, last_run, modified_by, modified_time, start_time, task_id, task_name, task_type]. Sort either asc (ascending) or desc (descending). Example: example_field|asc"),
        offset: int | None = Field(default=None, description="Starting index for record retrieval. Example: 100"),
        limit: int | None = Field(default=None, description="The maximum records to return. Example: 50"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns the list of scheduled task IDs matching the filter query parameter"""
        return self._call(operation="ITAutomationSearchScheduledTasks", query_params={"filter": filter, "sort": sort, "offset": offset, "limit": limit}, error_message="ITAutomationSearchScheduledTasks failed", member_cid=member_cid)

    def it_automation_search_task_executions(
        self,
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results. Allowed filter fields: [end_time, run_by, run_type, start_time, status, task_id, task_name, task_type] Example: example_string_field:'example@example.com'+example_date_field:>='2024-08-27T03:21:32Z'"),
        sort: str | None = Field(default=None, description="The sort expression that should be used to sort the results. Allowed sort fields: [end_time, run_by, run_type, start_time, status, task_id, task_name, task_type]. Sort either asc (ascending) or desc (descending). Example: example_field|asc"),
        offset: int | None = Field(default=None, description="Starting index for record retrieval. Example: 100"),
        limit: int | None = Field(default=None, description="The maximum records to return. Example: 50"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns the list of task execution IDs matching the filter query parameter. Can be used together with the entities endpoint to retrieve full information on executions"""
        return self._call(operation="ITAutomationSearchTaskExecutions", query_params={"filter": filter, "sort": sort, "offset": offset, "limit": limit}, error_message="ITAutomationSearchTaskExecutions failed", member_cid=member_cid)

    def it_automation_search_task_groups(
        self,
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results. Allowed filter fields: [access_type, created_by, created_time, modified_by, modified_time, name] Example: example_string_field:'example@example.com'+example_date_field:>='2024-08-27T03:21:32Z'"),
        sort: str | None = Field(default=None, description="The sort expression that should be used to sort the results. Allowed sort fields: [access_type, created_by, created_time, modified_by, modified_time, name]. Sort either asc (ascending) or desc (descending). Example: example_field|asc"),
        offset: int | None = Field(default=None, description="Starting index for record retrieval. Example: 100"),
        limit: int | None = Field(default=None, description="The maximum records to return. Example: 50"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns the list of task group ids matching the filter query parameter"""
        return self._call(operation="ITAutomationSearchTaskGroups", query_params={"filter": filter, "sort": sort, "offset": offset, "limit": limit}, error_message="ITAutomationSearchTaskGroups failed", member_cid=member_cid)

    def it_automation_search_tasks(
        self,
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results. Allowed filter fields: [access_type, created_by, created_time, last_run_time, modified_by, modified_time, name, runs, task_type] Example: example_string_field:'example@example.com'+example_date_field:>='2024-08-27T03:21:32Z'"),
        sort: str | None = Field(default=None, description="The sort expression that should be used to sort the results. Allowed sort fields: [access_type, created_by, created_time, last_run_time, modified_by, modified_time, name, runs, task_type]. Sort either asc (ascending) or desc (descending). Example: example_field|asc"),
        offset: int | None = Field(default=None, description="Starting index for record retrieval. Example: 100"),
        limit: int | None = Field(default=None, description="The maximum records to return. Example: 50"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns the list of task IDs matching the filter query parameter."""
        return self._call(operation="ITAutomationSearchTasks", query_params={"filter": filter, "sort": sort, "offset": offset, "limit": limit}, error_message="ITAutomationSearchTasks failed", member_cid=member_cid)

    def it_automation_search_user_group(
        self,
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results. Allowed filter fields: [created_by, created_time, description, modified_by, modified_time, name] Example: example_string_field:'example@example.com'+example_date_field:>='2024-08-27T03:21:32Z'"),
        sort: str | None = Field(default=None, description="The sort expression that should be used to sort the results. Allowed sort fields: [created_by, created_time, modified_by, modified_time, name]. Sort either asc (ascending) or desc (descending). Example: example_field|asc"),
        offset: int | None = Field(default=None, description="Starting index for record retrieval. Example: 100"),
        limit: int | None = Field(default=None, description="The maximum records to return. Example: 50"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Returns the list of user group ids matching the filter query parameter. It can be used together with the entities endpoint to retrieve full information on user groups"""
        return self._call(operation="ITAutomationSearchUserGroup", query_params={"filter": filter, "sort": sort, "offset": offset, "limit": limit}, error_message="ITAutomationSearchUserGroup failed", member_cid=member_cid)

    def it_automation_start_execution_results_search(
        self,
        body: dict = Field(description="Request JSON body for `ITAutomationStartExecutionResultsSearch` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Starts an async task execution results search. Poll ITAutomationGetExecutionResultsSearchStatus to check if the search is complete. You must retrieve the results using ITAutomationGetExecutionResults within 30 seconds of completion, or the job will be deleted."""
        return self._call(operation="ITAutomationStartExecutionResultsSearch", query_params=None, body_params=body, error_message="ITAutomationStartExecutionResultsSearch failed", member_cid=member_cid)

    def it_automation_start_task_execution(
        self,
        body: dict = Field(description="Request JSON body for `ITAutomationStartTaskExecution` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Starts a new task execution from an existing task provided in the request and returns the initiated task executions"""
        return self._call(operation="ITAutomationStartTaskExecution", query_params=None, body_params=body, error_message="ITAutomationStartTaskExecution failed", member_cid=member_cid)

    def it_automation_update_policies(
        self,
        body: dict = Field(description="Request JSON body for `ITAutomationUpdatePolicies` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Updates a new policy of the specified type."""
        return self._call(operation="ITAutomationUpdatePolicies", query_params=None, body_params=body, error_message="ITAutomationUpdatePolicies failed", member_cid=member_cid)

    def it_automation_update_policies_precedence(
        self,
        platform: str = Field(description="The policy platform for which to set the precedence order, must be one of Windows, Linux or Mac."),
        body: dict = Field(description="Request JSON body for `ITAutomationUpdatePoliciesPrecedence` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Updates the policy precedence for all policies of a specific platform."""
        return self._call(operation="ITAutomationUpdatePoliciesPrecedence", query_params={"platform": platform}, body_params=body, error_message="ITAutomationUpdatePoliciesPrecedence failed", member_cid=member_cid)

    def it_automation_update_policy_host_groups(
        self,
        body: dict = Field(description="Request JSON body for `ITAutomationUpdatePolicyHostGroups` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Manage host groups assigned to a policy."""
        return self._call(operation="ITAutomationUpdatePolicyHostGroups", query_params=None, body_params=body, error_message="ITAutomationUpdatePolicyHostGroups failed", member_cid=member_cid)

    def it_automation_update_scheduled_task(
        self,
        id: str = Field(description="The id of the scheduled task to update"),
        body: dict = Field(description="Request JSON body for `ITAutomationUpdateScheduledTask` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update an existing scheduled task with the supplied info"""
        return self._call(operation="ITAutomationUpdateScheduledTask", query_params={"id": id}, body_params=body, error_message="ITAutomationUpdateScheduledTask failed", member_cid=member_cid)

    def it_automation_update_task(
        self,
        id: str = Field(description="ID of the task to update. Use ITAutomationSearchTasks to fetch IDs"),
        body: dict = Field(description="Request JSON body for `ITAutomationUpdateTask` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update a task with details from the given request."""
        return self._call(operation="ITAutomationUpdateTask", query_params={"id": id}, body_params=body, error_message="ITAutomationUpdateTask failed", member_cid=member_cid)

    def it_automation_update_task_group(
        self,
        id: str = Field(description="The id of the task group to update"),
        body: dict = Field(description="Request JSON body for `ITAutomationUpdateTaskGroup` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update a task group for a given id"""
        return self._call(operation="ITAutomationUpdateTaskGroup", query_params={"id": id}, body_params=body, error_message="ITAutomationUpdateTaskGroup failed", member_cid=member_cid)

    def it_automation_update_user_group(
        self,
        id: str = Field(description="The id of the user groups to update"),
        body: dict = Field(description="Request JSON body for `ITAutomationUpdateUserGroup` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update a user group for a given id"""
        return self._call(operation="ITAutomationUpdateUserGroup", query_params={"id": id}, body_params=body, error_message="ITAutomationUpdateUserGroup failed", member_cid=member_cid)
