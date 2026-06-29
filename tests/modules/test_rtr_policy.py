"""Tests for the RTR Response Policy module."""

from falcon_mcp.modules.rtr_policy import RtrPolicyModule
from tests.modules.utils.test_modules import TestModules


def _ok(resources):
    return {"status_code": 200, "body": {"resources": resources}}


class TestRtrPolicyModule(TestModules):
    def setUp(self):
        self.setup_module(RtrPolicyModule)

    def test_register_tools(self):
        self.assert_tools_registered([
            "falcon_search_rtr_policies",
            "falcon_get_rtr_policy_members",
            "falcon_create_rtr_policy",
            "falcon_update_rtr_policy",
            "falcon_delete_rtr_policies",
            "falcon_assign_rtr_policy_host_groups",
            "falcon_unassign_rtr_policy_host_groups",
            "falcon_set_rtr_policies_state",
            "falcon_set_rtr_policies_precedence",
        ])

    def test_register_resources(self):
        self.assert_resources_registered(["falcon_rtr_policies_fql_guide"])

    def test_search(self):
        self.mock_client.command.return_value = _ok([{"id": "p1"}])
        self.module.search_rtr_policies(filter=None, limit=10, offset=None, sort=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "queryCombinedRTResponsePolicies")

    def test_members(self):
        self.mock_client.command.return_value = _ok([])
        self.module.get_rtr_policy_members(id="p1", filter=None, limit=10, offset=None, sort=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "queryCombinedRTResponsePolicyMembers")

    def test_create(self):
        self.mock_client.command.return_value = _ok([{"id": "p1"}])
        self.module.create_rtr_policy(
            name="t", platform_name="Windows", description=None, clone_id=None, settings=None,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "createRTResponsePolicies")
        self.assertEqual(call[1]["body"], {"resources": [
            {"name": "t", "platform_name": "Windows"}
        ]})

    def test_create_invalid_platform(self):
        result = self.module.create_rtr_policy(
            name="t", platform_name="Solaris", description=None, clone_id=None, settings=None,
        )
        self.assertIn("error", result[0])
        self.mock_client.command.assert_not_called()

    def test_update(self):
        self.mock_client.command.return_value = _ok([{"id": "p1"}])
        self.module.update_rtr_policy(id="p1", name="renamed", description=None, settings=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "updateRTResponsePolicies")
        self.assertEqual(call[1]["body"], {"resources": [{"id": "p1", "name": "renamed"}]})

    def test_delete(self):
        self.mock_client.command.return_value = _ok([])
        self.module.delete_rtr_policies(ids=["p1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "deleteRTResponsePolicies")
        self.assertEqual(call[1]["parameters"]["ids"], ["p1"])

    def test_assign_host_groups(self):
        self.mock_client.command.return_value = _ok([])
        self.module.assign_rtr_policy_host_groups(id="p1", host_group_ids=["g1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "performRTResponsePoliciesAction")
        self.assertEqual(call[1]["parameters"]["action_name"], "add-host-group")
        self.assertEqual(
            call[1]["body"]["action_parameters"], [{"name": "group_id", "value": "g1"}]
        )

    def test_state(self):
        self.mock_client.command.return_value = _ok([])
        self.module.set_rtr_policies_state(ids=["p1"], enabled=True)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[1]["parameters"]["action_name"], "enable")

    def test_precedence(self):
        self.mock_client.command.return_value = _ok([])
        self.module.set_rtr_policies_precedence(ids=["p1"], platform_name="Mac")
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "setRTResponsePoliciesPrecedence")
        self.assertEqual(call[1]["body"], {"ids": ["p1"], "platform_name": "Mac"})
