"""Tests for the Falcon for IT module."""

from falcon_mcp.modules.falcon_for_it import FalconForItModule
from tests.modules.utils.test_modules import TestModules


def _ok(resources):
    return {"status_code": 200, "body": {"resources": resources}}


class TestFalconForItModule(TestModules):
    def setUp(self):
        self.setup_module(FalconForItModule)

    def test_register_tools(self):
        self.assert_tools_registered([
            "falcon_search_f4it_tasks",
            "falcon_get_f4it_task_details",
            "falcon_search_f4it_task_executions",
            "falcon_get_f4it_task_execution",
            "falcon_get_f4it_task_execution_host_status",
            "falcon_get_f4it_execution_results",
            "falcon_search_f4it_scheduled_tasks",
            "falcon_search_f4it_policies",
            "falcon_cancel_f4it_task_execution",
        ])

    def test_register_resources(self):
        self.assert_resources_registered(["falcon_f4it_fql_guide"])

    def test_search_tasks(self):
        self.mock_client.command.return_value = _ok([{"id": "t1"}])
        self.module.search_tasks(filter="status:'active'", limit=10, offset=0, sort=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "ITAutomationGetTasksByQuery")

    def test_get_task_details(self):
        self.mock_client.command.return_value = _ok([{"id": "t1"}])
        self.module.get_task_details(ids=["t1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "ITAutomationGetTasks")

    def test_get_task_execution(self):
        self.mock_client.command.return_value = _ok([{"id": "e1"}])
        self.module.get_task_execution(ids=["e1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "ITAutomationGetTaskExecution")

    def test_get_execution_results_uses_id_param(self):
        # Critical: API expects `id`, not `execution_id`.
        self.mock_client.command.return_value = _ok([])
        self.module.get_execution_results(execution_id="e1", offset=0, limit=100, sort=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "ITAutomationGetExecutionResults")
        self.assertEqual(call[1]["parameters"]["id"], "e1")
        self.assertNotIn("execution_id", call[1]["parameters"])

    def test_cancel_uses_body(self):
        self.mock_client.command.return_value = _ok([])
        self.module.cancel_task_execution(task_execution_id="e1")
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "ITAutomationCancelTaskExecution")
        # Critical: API expects body, not query parameters.
        self.assertEqual(call[1]["body"], {"task_execution_id": "e1"})
        self.assertNotIn("parameters", call[1])
