"""Tests for the IOA Exclusions module."""

from falcon_mcp.modules.ioa_exclusions import IOAExclusionsModule
from tests.modules.utils.test_modules import TestModules


def _ok(resources):
    return {"status_code": 200, "body": {"resources": resources}}


class TestIOAExclusionsModule(TestModules):
    def setUp(self):
        self.setup_module(IOAExclusionsModule)
        # In this rebuild branch the shared mock does not wire command_for->command;
        # delegate here so assertions on mock_client.command work.
        self.mock_client.command_for.side_effect = (
            lambda op, member_cid=None, **kw: self.mock_client.command(op, **kw)
        )

    def test_register_tools(self):
        self.assert_tools_registered([
            "falcon_search_ioa_exclusions",
            "falcon_get_ioa_exclusion_details",
            "falcon_create_ioa_exclusion",
            "falcon_update_ioa_exclusion",
            "falcon_delete_ioa_exclusions",
        ])

    def test_search(self):
        self.mock_client.command.side_effect = [_ok(["x1"]), _ok([{"id": "x1"}])]
        self.module.search_ioa_exclusions(filter=None, limit=10, offset=None, sort=None)
        calls = self.mock_client.command.call_args_list
        self.assertEqual(calls[0][0][0], "queryIOAExclusionsV1")
        self.assertEqual(calls[1][0][0], "getIOAExclusionsV1")

    def test_get_details(self):
        self.mock_client.command.return_value = _ok([{"id": "x1"}])
        self.module.get_ioa_exclusion_details(ids=["x1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "getIOAExclusionsV1")

    def test_create(self):
        self.mock_client.command.return_value = _ok([{"id": "x1"}])
        self.module.create_ioa_exclusion(
            name="excl", pattern_id="1234", pattern_name=None, cl_regex=".*evil.*",
            ifn_regex=None, groups=None, description=None, detection_json=None, comment=None,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "createIOAExclusionsV1")
        body = call[1]["body"]
        self.assertEqual(body["name"], "excl")
        self.assertEqual(body["pattern_id"], "1234")
        self.assertEqual(body["cl_regex"], ".*evil.*")
        self.assertEqual(body["groups"], ["all"])

    def test_update(self):
        self.mock_client.command.return_value = _ok([{"id": "x1"}])
        self.module.update_ioa_exclusion(
            id="x1", name="renamed", cl_regex=None, ifn_regex=None,
            groups=None, description=None, comment=None,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "updateIOAExclusionsV1")
        self.assertEqual(call[1]["body"], {"id": "x1", "name": "renamed"})

    def test_update_requires_field(self):
        result = self.module.update_ioa_exclusion(
            id="x1", name=None, cl_regex=None, ifn_regex=None,
            groups=None, description=None, comment=None,
        )
        self.assertTrue(self.module._is_error(result[0]))
        self.mock_client.command.assert_not_called()

    def test_delete(self):
        self.mock_client.command.return_value = _ok([])
        self.module.delete_ioa_exclusions(ids=["x1"], comment=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "deleteIOAExclusionsV1")
        self.assertEqual(call[1]["parameters"]["ids"], ["x1"])
