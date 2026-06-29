"""Tests for the FileVantage (File Integrity Monitoring) module."""

from falcon_mcp.modules.filevantage import FileVantageModule
from tests.modules.utils.test_modules import TestModules


def _ok(resources):
    return {"status_code": 200, "body": {"resources": resources}}


class TestFileVantageModule(TestModules):
    def setUp(self):
        self.setup_module(FileVantageModule)
        # Delegate command_for -> command so assertions on mock_client.command work.
        self.mock_client.command_for.side_effect = (
            lambda op, member_cid=None, **kw: self.mock_client.command(op, **kw)
        )

    def test_register_tools(self):
        self.assert_tools_registered([
            # reads
            "falcon_search_filevantage_changes",
            "falcon_get_filevantage_change_details",
            "falcon_get_filevantage_change_content",
            "falcon_search_filevantage_policies",
            "falcon_get_filevantage_policy_details",
            "falcon_search_filevantage_rule_groups",
            "falcon_get_filevantage_rule_group_details",
            "falcon_get_filevantage_rule_details",
            "falcon_search_filevantage_scheduled_exclusions",
            "falcon_get_filevantage_scheduled_exclusion_details",
            "falcon_search_filevantage_actions",
            "falcon_get_filevantage_action_details",
            # writes
            "falcon_create_filevantage_policy",
            "falcon_update_filevantage_policy",
            "falcon_update_filevantage_policy_host_groups",
            "falcon_update_filevantage_policy_precedence",
            "falcon_update_filevantage_policy_rule_groups",
            "falcon_create_filevantage_rule_group",
            "falcon_update_filevantage_rule_group",
            "falcon_update_filevantage_rule_group_precedence",
            "falcon_create_filevantage_rule",
            "falcon_update_filevantage_rule",
            "falcon_create_filevantage_scheduled_exclusion",
            "falcon_update_filevantage_scheduled_exclusion",
            "falcon_signal_filevantage_changes",
            # destructive
            "falcon_start_filevantage_action",
            "falcon_delete_filevantage_policies",
            "falcon_delete_filevantage_rule_groups",
            "falcon_delete_filevantage_rules",
            "falcon_delete_filevantage_scheduled_exclusions",
        ])

    def test_search_changes_chains_query_then_get(self):
        self.mock_client.command.side_effect = [_ok(["c1"]), _ok([{"id": "c1"}])]
        self.module.search_filevantage_changes(filter="severity:'High'", limit=10, offset=None, sort=None)
        calls = self.mock_client.command.call_args_list
        self.assertEqual(calls[0][0][0], "highVolumeQueryChanges")
        self.assertEqual(calls[1][0][0], "getChanges")

    def test_search_policies_requires_type_param(self):
        self.mock_client.command.side_effect = [_ok(["p1"]), _ok([{"id": "p1"}])]
        self.module.search_filevantage_policies(type="Windows", filter=None, limit=10, offset=None, sort=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "queryPolicies")
        self.assertEqual(call[1]["parameters"]["type"], "Windows")

    def test_create_policy_body(self):
        self.mock_client.command.return_value = _ok([{"id": "p1"}])
        self.module.create_filevantage_policy(name="FIM", platform="Windows", description="d")
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "createPolicies")
        self.assertEqual(call[1]["body"], {"name": "FIM", "platform": "Windows", "description": "d"})

    def test_update_policy_host_groups_uses_query_params(self):
        self.mock_client.command.return_value = _ok([])
        self.module.update_filevantage_policy_host_groups(policy_id="p1", action="assign", ids=["hg1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "updatePolicyHostGroups")
        params = call[1]["parameters"]
        self.assertEqual(params["policy_id"], "p1")
        self.assertEqual(params["action"], "assign")
        self.assertEqual(params["ids"], ["hg1"])

    def test_start_action_validates_operation(self):
        result = self.module.start_filevantage_action(change_ids=["c1"], operation="explode", comment=None)
        self.assertTrue(self.module._is_error(result[0]))
        # A valid operation should reach the API
        self.mock_client.command.return_value = _ok([])
        self.module.start_filevantage_action(change_ids=["c1"], operation="purge", comment="cleanup")
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "startActions")
        self.assertEqual(call[1]["body"]["operation"], "purge")

    def test_get_change_content_requires_id(self):
        result = self.module.get_filevantage_change_content(id="")
        self.assertTrue(self.module._is_error(result[0]))
