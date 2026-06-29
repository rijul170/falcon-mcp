"""Tests for the ML Exclusions module."""

from falcon_mcp.modules.ml_exclusions import MLExclusionsModule
from tests.modules.utils.test_modules import TestModules


def _ok(resources):
    return {"status_code": 200, "body": {"resources": resources}}


class TestMLExclusionsModule(TestModules):
    def setUp(self):
        self.setup_module(MLExclusionsModule)
        # In this rebuild branch the shared mock does not wire command_for->command;
        # delegate here so assertions on mock_client.command work.
        self.mock_client.command_for.side_effect = (
            lambda op, member_cid=None, **kw: self.mock_client.command(op, **kw)
        )

    def test_register_tools(self):
        self.assert_tools_registered([
            "falcon_search_ml_exclusions",
            "falcon_get_ml_exclusion_details",
            "falcon_create_ml_exclusion",
            "falcon_update_ml_exclusion",
            "falcon_delete_ml_exclusions",
        ])

    def test_search(self):
        self.mock_client.command.side_effect = [_ok(["e1"]), _ok([{"id": "e1"}])]
        self.module.search_ml_exclusions(filter=None, limit=10, offset=None, sort=None)
        calls = self.mock_client.command.call_args_list
        self.assertEqual(calls[0][0][0], "queryMLExclusionsV1")
        self.assertEqual(calls[1][0][0], "getMLExclusionsV1")

    def test_get_details(self):
        self.mock_client.command.return_value = _ok([{"id": "e1"}])
        self.module.get_ml_exclusion_details(ids=["e1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "getMLExclusionsV1")

    def test_create(self):
        self.mock_client.command.return_value = _ok([{"id": "e1"}])
        self.module.create_ml_exclusion(
            value="C:\\app\\*", excluded_from=None, groups=None, comment=None,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "createMLExclusionsV1")
        body = call[1]["body"]
        self.assertEqual(body["value"], "C:\\app\\*")
        self.assertEqual(body["groups"], ["all"])

    def test_update(self):
        self.mock_client.command.return_value = _ok([{"id": "e1"}])
        self.module.update_ml_exclusion(id="e1", value="C:\\new\\*", groups=None, comment=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "updateMLExclusionsV1")
        self.assertEqual(call[1]["body"], {"id": "e1", "value": "C:\\new\\*"})

    def test_update_requires_field(self):
        result = self.module.update_ml_exclusion(id="e1", value=None, groups=None, comment=None)
        self.assertTrue(self.module._is_error(result[0]))
        self.mock_client.command.assert_not_called()

    def test_delete(self):
        self.mock_client.command.return_value = _ok([])
        self.module.delete_ml_exclusions(ids=["e1"], comment="cleanup")
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "deleteMLExclusionsV1")
        self.assertEqual(call[1]["parameters"]["ids"], ["e1"])
