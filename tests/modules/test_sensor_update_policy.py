"""Tests for the Sensor Update Policy module."""

from falcon_mcp.modules.sensor_update_policy import SensorUpdatePolicyModule
from tests.modules.utils.test_modules import TestModules


def _ok(resources):
    return {"status_code": 200, "body": {"resources": resources}}


class TestSensorUpdatePolicyModule(TestModules):
    def setUp(self):
        self.setup_module(SensorUpdatePolicyModule)

    def test_register_tools(self):
        self.assert_tools_registered([
            "falcon_assign_sensor_update_policy_host_groups",
            "falcon_create_sensor_update_policy",
            "falcon_delete_sensor_update_policies",
            "falcon_get_sensor_update_kernel_field_values",
            "falcon_get_sensor_update_policy_members",
            "falcon_list_sensor_builds",
            "falcon_list_sensor_update_kernels",
            "falcon_reveal_uninstall_token",
            "falcon_search_sensor_update_policies",
            "falcon_set_sensor_update_policies_precedence",
            "falcon_set_sensor_update_policies_state",
            "falcon_unassign_sensor_update_policy_host_groups",
            "falcon_update_sensor_update_policy",
        ])

    def test_register_resources(self):
        self.assert_resources_registered(["falcon_sensor_update_policies_fql_guide"])

    def test_search(self):
        self.mock_client.command.return_value = _ok([{"id": "p1"}])
        self.module.search_sensor_update_policies(filter=None, limit=10, offset=None, sort=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "queryCombinedSensorUpdatePoliciesV2")

    def test_list_builds(self):
        self.mock_client.command.return_value = _ok([{"build": "n-1"}])
        self.module.list_sensor_builds(platform="platform:'windows'")
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "queryCombinedSensorUpdateBuilds")
        self.assertEqual(call[1]["parameters"]["platform"], "platform:'windows'")

    def test_create(self):
        self.mock_client.command.return_value = _ok([{"id": "p1"}])
        self.module.create_sensor_update_policy(
            name="t", platform_name="Windows", build="n-1",
            description="d", uninstall_protection="ENABLED", settings=None,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "createSensorUpdatePoliciesV2")
        body = call[1]["body"]
        res = body["resources"][0]
        self.assertEqual(res["name"], "t")
        self.assertEqual(res["platform_name"], "Windows")
        self.assertEqual(res["description"], "d")
        self.assertEqual(res["settings"], {"build": "n-1", "uninstall_protection": "ENABLED"})

    def test_update(self):
        self.mock_client.command.return_value = _ok([{"id": "p1"}])
        self.module.update_sensor_update_policy(
            id="p1", name=None, description="updated", settings=None,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "updateSensorUpdatePoliciesV2")
        self.assertEqual(call[1]["body"], {"resources": [{"id": "p1", "description": "updated"}]})

    def test_delete(self):
        self.mock_client.command.return_value = _ok([])
        self.module.delete_sensor_update_policies(ids=["p1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "deleteSensorUpdatePolicies")
        self.assertEqual(call[1]["parameters"]["ids"], ["p1"])

    def test_assign_host_groups(self):
        self.mock_client.command.return_value = _ok([])
        self.module.assign_sensor_update_policy_host_groups(id="p1", host_group_ids=["g1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "performSensorUpdatePoliciesAction")
        self.assertEqual(call[1]["parameters"]["action_name"], "add-host-group")

    def test_state(self):
        self.mock_client.command.return_value = _ok([])
        self.module.set_sensor_update_policies_state(ids=["p1"], enabled=False)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[1]["parameters"]["action_name"], "disable")

    def test_precedence(self):
        self.mock_client.command.return_value = _ok([])
        self.module.set_sensor_update_policies_precedence(ids=["p1"], platform_name="Linux")
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "setSensorUpdatePoliciesPrecedence")
        self.assertEqual(call[1]["body"], {"ids": ["p1"], "platform_name": "Linux"})

    def test_reveal_uninstall_token(self):
        self.mock_client.command.return_value = _ok([{"uninstall_token": "ABC123"}])
        self.module.reveal_uninstall_token(device_id="aid1", audit_message="MCP test")
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "revealUninstallToken")
        self.assertEqual(call[1]["body"], {"device_id": "aid1", "audit_message": "MCP test"})

    def test_reveal_maintenance_token(self):
        self.mock_client.command.return_value = _ok([{"uninstall_token": "MAINT"}])
        self.module.reveal_uninstall_token(device_id="MAINTENANCE", audit_message=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[1]["body"], {"device_id": "MAINTENANCE"})
