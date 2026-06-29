"""Tests for the Falcon Sandbox (FalconX) module."""

from falcon_mcp.modules.falconx_sandbox import FalconXSandboxModule
from tests.modules.utils.test_modules import TestModules


def _ok(resources):
    return {"status_code": 200, "body": {"resources": resources}}


class TestFalconXSandboxModule(TestModules):
    def setUp(self):
        self.setup_module(FalconXSandboxModule)
        self.mock_client.command_for.side_effect = (
            lambda op, member_cid=None, **kw: self.mock_client.command(op, **kw)
        )

    def test_register_tools(self):
        self.assert_tools_registered([
            "falcon_query_sandbox_reports",
            "falcon_get_sandbox_report",
            "falcon_get_sandbox_report_summary",
            "falcon_submit_sandbox_analysis",
        ])

    def test_query(self):
        self.mock_client.command.return_value = _ok(["rep1"])
        self.module.query_sandbox_reports(filter="state:'success'", limit=10, offset=None, sort=None, member_cid=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "QueryReports")

    def test_get_report(self):
        self.mock_client.command.return_value = _ok([{"id": "rep1"}])
        self.module.get_sandbox_report(ids=["rep1"], member_cid=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "GetReports")

    def test_get_summary(self):
        self.mock_client.command.return_value = _ok([{"id": "rep1"}])
        self.module.get_sandbox_report_summary(ids=["rep1"], member_cid=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "GetSummaryReports")

    def test_submit_sha256(self):
        self.mock_client.command.return_value = _ok([{"id": "sub1"}])
        self.module.submit_sandbox_analysis(
            sha256="abc123", url=None, environment_id=160, action_script=None,
            command_line=None, document_password=None, submit_name=None, member_cid=None,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "Submit")
        item = call[1]["body"]["sandbox"][0]
        self.assertEqual(item["sha256"], "abc123")
        self.assertEqual(item["environment_id"], 160)

    def test_submit_requires_target(self):
        result = self.module.submit_sandbox_analysis(
            sha256=None, url=None, environment_id=160, action_script=None,
            command_line=None, document_password=None, submit_name=None, member_cid=None,
        )
        self.assertTrue(self.module._is_error(result[0]))
        self.mock_client.command.assert_not_called()

    def test_submit_rejects_both(self):
        result = self.module.submit_sandbox_analysis(
            sha256="abc", url="http://x", environment_id=160, action_script=None,
            command_line=None, document_password=None, submit_name=None, member_cid=None,
        )
        self.assertTrue(self.module._is_error(result[0]))
        self.mock_client.command.assert_not_called()
