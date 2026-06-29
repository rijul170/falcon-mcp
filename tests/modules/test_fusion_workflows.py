"""Tests for the Fusion Workflows module."""

from falcon_mcp.modules.fusion_workflows import FusionWorkflowsModule
from tests.modules.utils.test_modules import TestModules


def _ok(resources):
    return {"status_code": 200, "body": {"resources": resources}}


class TestFusionWorkflowsModule(TestModules):
    def setUp(self):
        self.setup_module(FusionWorkflowsModule)

    def test_register_tools(self):
        self.assert_tools_registered([
            "falcon_cancel_workflow_executions",
            "falcon_execute_workflow",
            "falcon_export_workflow_definition",
            "falcon_get_workflow_execution_results",
            "falcon_import_workflow_definition",
            "falcon_list_workflow_human_inputs",
            "falcon_respond_to_workflow_human_input",
            "falcon_retry_workflow_execution",
            "falcon_run_mock_workflow",
            "falcon_search_workflow_activities",
            "falcon_search_workflow_definitions",
            "falcon_search_workflow_executions",
            "falcon_search_workflow_triggers",
            "falcon_update_workflow_definition",
        ])

    def test_register_resources(self):
        self.assert_resources_registered(["falcon_workflows_fql_guide"])

    def test_search_definitions(self):
        self.mock_client.command.return_value = _ok([{"id": "w1"}])
        self.module.search_workflow_definitions(filter=None, limit=10, offset=None, sort=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "WorkflowDefinitionsCombined")

    def test_search_executions(self):
        self.mock_client.command.return_value = _ok([{"id": "e1"}])
        self.module.search_workflow_executions(filter="status:'Failed'", limit=10, offset=None, sort=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "WorkflowExecutionsCombined")

    def test_get_execution_results(self):
        self.mock_client.command.return_value = _ok([{"id": "e1"}])
        self.module.get_workflow_execution_results(ids=["e1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "WorkflowExecutionResults")
        self.assertEqual(call[1]["parameters"]["ids"], ["e1"])

    def test_execute_workflow_by_id(self):
        self.mock_client.command.return_value = _ok([{"execution_id": "e1"}])
        self.module.execute_workflow(
            definition_id="w1", name=None, body={"input": "value"},
            key=None, execution_cid=None, source_event_url=None,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "WorkflowExecute")
        self.assertEqual(call[1]["parameters"]["definition_id"], "w1")
        self.assertEqual(call[1]["body"], {"input": "value"})

    def test_execute_workflow_validation(self):
        result = self.module.execute_workflow(
            definition_id=None, name=None, body={},
            key=None, execution_cid=None, source_event_url=None,
        )
        self.assertIn("error", result[0])
        self.mock_client.command.assert_not_called()

    def test_cancel(self):
        self.mock_client.command.return_value = _ok([])
        self.module.cancel_workflow_executions(ids=["e1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "WorkflowExecutionsAction")
        self.assertEqual(call[1]["parameters"]["action_name"], "cancel")
        self.assertEqual(call[1]["body"], {"ids": ["e1"]})
