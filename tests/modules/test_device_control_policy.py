"""Tests for the Device Control Policy module."""

from falcon_mcp.modules.device_control_policy import DeviceControlPolicyModule
from tests.modules.utils.test_modules import TestModules


def _ok(resources):
    return {"status_code": 200, "body": {"resources": resources}}


class TestDeviceControlPolicyModule(TestModules):
    def setUp(self):
        self.setup_module(DeviceControlPolicyModule)

    def test_register_tools(self):
        self.assert_tools_registered([
            "falcon_assign_device_control_policy_host_groups",
            "falcon_configure_device_control_classes",
            "falcon_create_device_control_policy",
            "falcon_delete_device_control_policies",
            "falcon_get_device_control_policy_members",
            "falcon_search_device_control_policies",
            "falcon_set_device_control_policies_precedence",
            "falcon_set_device_control_policies_state",
            "falcon_unassign_device_control_policy_host_groups",
            "falcon_update_device_control_policy",
        ])

    def test_register_resources(self):
        self.assert_resources_registered(["falcon_device_control_policies_fql_guide"])

    def test_search(self):
        self.mock_client.command.return_value = _ok([{"id": "p1"}])
        self.module.search_device_control_policies(filter=None, limit=10, offset=None, sort=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "queryCombinedDeviceControlPolicies")

    def test_create(self):
        self.mock_client.command.return_value = _ok([{"id": "p1"}])
        self.module.create_device_control_policy(
            name="t", platform_name="Windows", description="d", clone_id=None, settings=None,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "createDeviceControlPolicies")
        self.assertEqual(call[1]["body"], {"resources": [
            {"name": "t", "platform_name": "Windows", "description": "d"}
        ]})

    def test_create_invalid_platform(self):
        result = self.module.create_device_control_policy(
            name="t", platform_name="Linux", description=None, clone_id=None, settings=None,
        )
        self.assertIn("error", result[0])
        self.mock_client.command.assert_not_called()

    def test_update(self):
        self.mock_client.command.return_value = _ok([])
        self.module.update_device_control_policy(
            id="p1", name="renamed", description=None, settings=None,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "updateDeviceControlPolicies")

    def test_delete(self):
        self.mock_client.command.return_value = _ok([])
        self.module.delete_device_control_policies(ids=["p1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "deleteDeviceControlPolicies")

    def test_assign_host_groups(self):
        self.mock_client.command.return_value = _ok([])
        self.module.assign_device_control_policy_host_groups(id="p1", host_group_ids=["g1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "performDeviceControlPoliciesAction")
        self.assertEqual(call[1]["parameters"]["action_name"], "add-host-group")

    def test_state(self):
        self.mock_client.command.return_value = _ok([])
        self.module.set_device_control_policies_state(ids=["p1"], enabled=True)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[1]["parameters"]["action_name"], "enable")

    def test_precedence(self):
        self.mock_client.command.return_value = _ok([])
        self.module.set_device_control_policies_precedence(ids=["p1"], platform_name="Windows")
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "setDeviceControlPoliciesPrecedence")
        self.assertEqual(call[1]["body"], {"ids": ["p1"], "platform_name": "Windows"})
