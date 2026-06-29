"""Tests for the Host Groups module."""

from falcon_mcp.modules.host_groups import HostGroupsModule
from tests.modules.utils.test_modules import TestModules


def _ok(resources):
    return {"status_code": 200, "body": {"resources": resources}}


class TestHostGroupsModule(TestModules):
    def setUp(self):
        self.setup_module(HostGroupsModule)

    def test_register_tools(self):
        self.assert_tools_registered([
            "falcon_search_host_groups",
            "falcon_get_host_group_members",
            "falcon_create_host_group",
            "falcon_update_host_group",
            "falcon_delete_host_groups",
            "falcon_add_hosts_to_group",
            "falcon_remove_hosts_from_group",
        ])

    def test_register_resources(self):
        self.assert_resources_registered(["falcon_search_host_groups_fql_guide"])

    def test_search_host_groups(self):
        self.mock_client.command.side_effect = [
            _ok(["g1", "g2"]),
            _ok([{"id": "g1"}, {"id": "g2"}]),
        ]
        result = self.module.search_host_groups(filter="name:'Prod*'", limit=50)
        c1 = self.mock_client.command.call_args_list[0]
        self.assertEqual(c1[0][0], "queryHostGroups")
        self.assertEqual(c1[1]["parameters"]["filter"], "name:'Prod*'")
        self.assertEqual(c1[1]["parameters"]["limit"], 50)
        c2 = self.mock_client.command.call_args_list[1]
        self.assertEqual(c2[0][0], "getHostGroups")
        self.assertEqual(c2[1]["parameters"]["ids"], ["g1", "g2"])
        self.assertEqual(len(result), 2)

    def test_get_host_group_members(self):
        self.mock_client.command.return_value = _ok([{"device_id": "aid1"}])
        self.module.get_host_group_members(id="g1", limit=10)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "queryCombinedGroupMembers")
        self.assertEqual(call[1]["parameters"]["id"], "g1")
        self.assertEqual(call[1]["parameters"]["limit"], 10)

    def test_create_host_group_static(self):
        self.mock_client.command.return_value = _ok([{"id": "g1"}])
        self.module.create_host_group(
            name="t", group_type="static", description="d", assignment_rule=None,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "createHostGroups")
        self.assertEqual(call[1]["body"], {"resources": [
            {"name": "t", "group_type": "static", "description": "d"}
        ]})

    def test_create_host_group_dynamic_requires_assignment_rule(self):
        result = self.module.create_host_group(
            name="t", group_type="dynamic", description=None, assignment_rule=None,
        )
        self.assertIn("error", result[0])
        self.mock_client.command.assert_not_called()

    def test_create_host_group_dynamic(self):
        self.mock_client.command.return_value = _ok([{"id": "g2"}])
        self.module.create_host_group(
            name="t", group_type="dynamic", description=None,
            assignment_rule="platform_name:'Windows'",
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "createHostGroups")
        self.assertEqual(call[1]["body"]["resources"][0]["group_type"], "dynamic")
        self.assertEqual(
            call[1]["body"]["resources"][0]["assignment_rule"], "platform_name:'Windows'"
        )

    def test_update_host_group_requires_some_field(self):
        result = self.module.update_host_group(
            id="g1", name=None, description=None, assignment_rule=None,
        )
        self.assertIn("error", result[0])
        self.mock_client.command.assert_not_called()

    def test_update_host_group(self):
        self.mock_client.command.return_value = _ok([{"id": "g1"}])
        self.module.update_host_group(
            id="g1", name="renamed", description=None, assignment_rule=None,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "updateHostGroups")
        self.assertEqual(call[1]["body"], {"resources": [{"id": "g1", "name": "renamed"}]})

    def test_delete_host_groups(self):
        self.mock_client.command.return_value = _ok([])
        self.module.delete_host_groups(ids=["g1", "g2"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "deleteHostGroups")
        self.assertEqual(call[1]["parameters"]["ids"], ["g1", "g2"])

    def test_add_hosts_to_group(self):
        self.mock_client.command.return_value = _ok([])
        self.module.add_hosts_to_group(group_id="g1", host_ids=["aid1", "aid2"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "performGroupAction")
        self.assertEqual(call[1]["parameters"]["action_name"], "add-hosts")
        self.assertEqual(call[1]["body"]["ids"], ["g1"])
        self.assertEqual(
            call[1]["body"]["action_parameters"][0],
            {"name": "filter", "value": "device_id:['aid1','aid2']"},
        )

    def test_remove_hosts_from_group(self):
        self.mock_client.command.return_value = _ok([])
        self.module.remove_hosts_from_group(group_id="g1", host_ids=["aid1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[1]["parameters"]["action_name"], "remove-hosts")
