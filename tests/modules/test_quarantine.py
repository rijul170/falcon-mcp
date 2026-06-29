"""Tests for the Quarantine module."""

from falcon_mcp.modules.quarantine import QuarantineModule
from tests.modules.utils.test_modules import TestModules


def _ok(resources):
    return {"status_code": 200, "body": {"resources": resources}}


class TestQuarantineModule(TestModules):
    def setUp(self):
        self.setup_module(QuarantineModule)
        # In this rebuild branch the shared mock does not wire command_for->command;
        # delegate here so assertions on mock_client.command work.
        self.mock_client.command_for.side_effect = (
            lambda op, member_cid=None, **kw: self.mock_client.command(op, **kw)
        )

    def test_register_tools(self):
        self.assert_tools_registered([
            "falcon_search_quarantined_files",
            "falcon_get_quarantine_file_details",
            "falcon_update_quarantined_files",
        ])

    def test_search(self):
        self.mock_client.command.side_effect = [_ok(["q1"]), _ok([{"id": "q1"}])]
        self.module.search_quarantined_files(filter="state:'quarantined'", limit=10, offset=None, sort=None)
        calls = self.mock_client.command.call_args_list
        self.assertEqual(calls[0][0][0], "QueryQuarantineFiles")
        self.assertEqual(calls[1][0][0], "GetQuarantineFiles")
        self.assertEqual(calls[1][1]["body"]["ids"], ["q1"])

    def test_get_details(self):
        self.mock_client.command.return_value = _ok([{"id": "q1"}])
        self.module.get_quarantine_file_details(ids=["q1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "GetQuarantineFiles")
        self.assertEqual(call[1]["body"]["ids"], ["q1"])

    def test_update_release(self):
        self.mock_client.command.return_value = _ok([])
        self.module.update_quarantined_files(ids=["q1"], action="release", comment="cleared")
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "UpdateQuarantinedDetectsByIds")
        body = call[1]["body"]
        self.assertEqual(body["ids"], ["q1"])
        self.assertEqual(body["action"], "release")
        self.assertEqual(body["comment"], "cleared")

    def test_update_invalid_action(self):
        result = self.module.update_quarantined_files(ids=["q1"], action="nope")
        self.assertTrue(self.module._is_error(result[0]))
        self.mock_client.command.assert_not_called()
