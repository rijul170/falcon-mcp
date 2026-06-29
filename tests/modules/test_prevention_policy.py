"""Tests for the Prevention Policy module."""

from falcon_mcp.modules.prevention_policy import PreventionPolicyModule
from tests.modules.utils.test_modules import TestModules


def _ok(resources):
    return {"status_code": 200, "body": {"resources": resources}}


class TestPreventionPolicyModule(TestModules):
    def setUp(self):
        self.setup_module(PreventionPolicyModule)

    def test_register_tools(self):
        self.assert_tools_registered([
            "falcon_search_prevention_policies",
            "falcon_get_prevention_policy_members",
            "falcon_create_prevention_policy",
            "falcon_update_prevention_policy",
            "falcon_delete_prevention_policies",
            "falcon_assign_prevention_policy_host_groups",
            "falcon_unassign_prevention_policy_host_groups",
            "falcon_set_prevention_policies_state",
            "falcon_set_prevention_policies_precedence",
        ])

    def test_register_resources(self):
        self.assert_resources_registered(["falcon_prevention_policies_fql_guide"])

    def test_search(self):
        self.mock_client.command.return_value = _ok([{"id": "p1"}])
        self.module.search_prevention_policies(filter="enabled:true", limit=5, offset=None, sort=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "queryCombinedPreventionPolicies")
        self.assertEqual(call[1]["parameters"]["filter"], "enabled:true")

    def test_members(self):
        self.mock_client.command.return_value = _ok([])
        self.module.get_prevention_policy_members(id="p1", filter=None, limit=10, offset=None, sort=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "queryCombinedPreventionPolicyMembers")
        self.assertEqual(call[1]["parameters"]["id"], "p1")

    def test_create(self):
        self.mock_client.command.return_value = _ok([{"id": "p1"}])
        self.module.create_prevention_policy(
            name="t", platform_name="Windows", description="d",
            clone_id=None, settings=None,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "createPreventionPolicies")
        self.assertEqual(call[1]["body"], {"resources": [
            {"name": "t", "platform_name": "Windows", "description": "d"}
        ]})

    def test_create_invalid_platform(self):
        result = self.module.create_prevention_policy(
            name="t", platform_name="Solaris", description=None, clone_id=None, settings=None,
        )
        self.assertIn("error", result[0])
        self.mock_client.command.assert_not_called()

    def test_update(self):
        self.mock_client.command.return_value = _ok([{"id": "p1"}])
        self.module.update_prevention_policy(
            id="p1", name="renamed", description=None, settings=None,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "updatePreventionPolicies")
        self.assertEqual(call[1]["body"], {"resources": [{"id": "p1", "name": "renamed"}]})

    def test_delete(self):
        self.mock_client.command.return_value = _ok([])
        self.module.delete_prevention_policies(ids=["p1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "deletePreventionPolicies")
        self.assertEqual(call[1]["parameters"]["ids"], ["p1"])

    def test_assign_host_groups(self):
        self.mock_client.command.return_value = _ok([])
        self.module.assign_prevention_policy_host_groups(id="p1", host_group_ids=["g1", "g2"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "performPreventionPoliciesAction")
        self.assertEqual(call[1]["parameters"]["action_name"], "add-host-group")
        self.assertEqual(call[1]["body"]["ids"], ["p1"])
        self.assertEqual(call[1]["body"]["action_parameters"], [
            {"name": "group_id", "value": "g1"},
            {"name": "group_id", "value": "g2"},
        ])

    def test_unassign_host_groups(self):
        self.mock_client.command.return_value = _ok([])
        self.module.unassign_prevention_policy_host_groups(id="p1", host_group_ids=["g1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[1]["parameters"]["action_name"], "remove-host-group")

    def test_state_enable(self):
        self.mock_client.command.return_value = _ok([])
        self.module.set_prevention_policies_state(ids=["p1"], enabled=True)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "performPreventionPoliciesAction")
        self.assertEqual(call[1]["parameters"]["action_name"], "enable")
        self.assertEqual(call[1]["body"], {"ids": ["p1"]})

    def test_state_disable(self):
        self.mock_client.command.return_value = _ok([])
        self.module.set_prevention_policies_state(ids=["p1"], enabled=False)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[1]["parameters"]["action_name"], "disable")

    def test_precedence(self):
        self.mock_client.command.return_value = _ok([])
        self.module.set_prevention_policies_precedence(
            ids=["p1", "p2"], platform_name="Windows",
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "setPreventionPoliciesPrecedence")
        self.assertEqual(call[1]["body"], {"ids": ["p1", "p2"], "platform_name": "Windows"})
