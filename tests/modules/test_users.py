"""Tests for the Users module."""

from falcon_mcp.modules.users import UsersModule
from tests.modules.utils.test_modules import TestModules


def _ok(resources):
    return {"status_code": 200, "body": {"resources": resources}}


class TestUsersModule(TestModules):
    def setUp(self):
        self.setup_module(UsersModule)

    def test_register_tools(self):
        self.assert_tools_registered([
            "falcon_create_user",
            "falcon_delete_user",
            "falcon_get_user_details",
            "falcon_grant_user_roles",
            "falcon_list_available_roles",
            "falcon_list_user_roles",
            "falcon_perform_user_action",
            "falcon_revoke_user_roles",
            "falcon_search_users",
            "falcon_update_user",
        ])

    def test_register_resources(self):
        self.assert_resources_registered(["falcon_search_users_fql_guide"])

    def test_search_users(self):
        self.mock_client.command.side_effect = [
            _ok(["u1", "u2"]),
            _ok([{"uuid": "u1"}, {"uuid": "u2"}]),
        ]
        self.module.search_users(filter="status:'active'", limit=100, offset=None, sort=None)
        c1, c2 = self.mock_client.command.call_args_list
        self.assertEqual(c1[0][0], "queryUserV1")
        self.assertEqual(c1[1]["parameters"]["filter"], "status:'active'")
        self.assertEqual(c2[0][0], "retrieveUsersGETV1")
        self.assertEqual(c2[1]["body"], {"ids": ["u1", "u2"]})

    def test_get_user_details(self):
        self.mock_client.command.return_value = _ok([{"uuid": "u1"}])
        self.module.get_user_details(uuids=["u1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "retrieveUsersGETV1")
        self.assertEqual(call[1]["body"], {"ids": ["u1"]})

    def test_list_user_roles(self):
        self.mock_client.command.return_value = _ok([{"role_id": "r1"}])
        self.module.list_user_roles(user_uuid="u1", cid=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "combinedUserRolesV1")
        self.assertEqual(call[1]["parameters"]["user_uuid"], "u1")
        self.assertNotIn("cid", call[1]["parameters"])

    def test_list_user_roles_with_cid(self):
        self.mock_client.command.return_value = _ok([])
        self.module.list_user_roles(user_uuid="u1", cid="cidA")
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[1]["parameters"]["cid"], "cidA")

    def test_list_available_roles(self):
        self.mock_client.command.side_effect = [
            _ok(["r1", "r2"]),
            _ok([{"id": "r1"}, {"id": "r2"}]),
        ]
        self.module.list_available_roles()
        c1, c2 = self.mock_client.command.call_args_list
        self.assertEqual(c1[0][0], "queriesRolesV1")
        self.assertEqual(c2[0][0], "entitiesRolesV1")
        self.assertEqual(c2[1]["parameters"]["ids"], ["r1", "r2"])

    def test_grant_user_roles(self):
        self.mock_client.command.return_value = _ok([])
        self.module.grant_user_roles(user_uuid="u1", role_ids=["r1", "r2"], cid="cidA")
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "userRolesActionV1")
        self.assertEqual(call[1]["body"], {
            "action": "grant", "cid": "cidA", "role_ids": ["r1", "r2"], "uuid": "u1",
        })

    def test_revoke_user_roles(self):
        self.mock_client.command.return_value = _ok([])
        self.module.revoke_user_roles(user_uuid="u1", role_ids=["r1"], cid="cidA")
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "userRolesActionV1")
        self.assertEqual(call[1]["body"], {
            "action": "revoke", "cid": "cidA", "role_ids": ["r1"], "uuid": "u1",
        })

    def test_grant_empty_roles_validates(self):
        result = self.module.grant_user_roles(user_uuid="u1", role_ids=[], cid="cidA")
        self.assertIn("error", result[0])
        self.mock_client.command.assert_not_called()
