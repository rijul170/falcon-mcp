"""Tests for the Recon module."""

from falcon_mcp.modules.recon_notifications import ReconModule
from tests.modules.utils.test_modules import TestModules


def _ok(resources):
    return {"status_code": 200, "body": {"resources": resources}}


class TestReconModule(TestModules):
    def setUp(self):
        self.setup_module(ReconModule)

    def test_register_tools(self):
        self.assert_tools_registered([
            "falcon_search_recon_notifications",
            "falcon_get_recon_notification_details",
            "falcon_search_recon_rules",
            "falcon_get_recon_rule_details",
            "falcon_update_recon_notifications",
            "falcon_delete_recon_notifications",
            "falcon_create_recon_rule",
            "falcon_update_recon_rule",
            "falcon_delete_recon_rules",
        ])

    def test_register_resources(self):
        self.assert_resources_registered(["falcon_recon_fql_guide"])

    def test_search_notifications(self):
        self.mock_client.command.side_effect = [
            _ok(["n1"]),
            _ok([{"id": "n1"}]),
        ]
        self.module.search_recon_notifications(
            filter="priority:'high'", limit=10, offset=0, sort=None, q=None,
        )
        c1, c2 = self.mock_client.command.call_args_list
        self.assertEqual(c1[0][0], "QueryNotificationsV1")
        self.assertEqual(c2[0][0], "GetNotificationsV1")

    def test_update_notifications_uses_list_body(self):
        self.mock_client.command_for.return_value = _ok(["n1"])
        updates = [
            {"id": "n1", "status": "in-progress"},
            {"id": "n2", "assigned_to_uuid": "u1"},
        ]
        self.module.update_recon_notifications(updates=updates)
        call = self.mock_client.command_for.call_args_list[0]
        self.assertEqual(call[0][0], "UpdateNotificationsV1")
        # Critical: top-level list body, NOT {"resources": [...]}
        self.assertEqual(call[1]["body"], updates)
        # MSSP-aware: the call now goes through command_for with member_cid threaded.
        self.assertIn("member_cid", call[1])

    def test_delete_notifications(self):
        self.mock_client.command.return_value = _ok([])
        self.module.delete_recon_notifications(ids=["n1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "DeleteNotificationsV1")
        self.assertEqual(call[1]["parameters"]["ids"], ["n1"])

    def test_create_rule_uses_list_body(self):
        self.mock_client.command_for.return_value = _ok([{"id": "r1"}])
        self.module.create_recon_rule(
            name="t", topic="SA_VIP", filter="actor:'apt28'",
            priority="high", permissions="private",
            breach_monitoring_enabled=False, substring_matching_enabled=False,
        )
        call = self.mock_client.command_for.call_args_list[0]
        self.assertEqual(call[0][0], "CreateRulesV1")
        self.assertEqual(call[1]["body"], [{
            "name": "t", "topic": "SA_VIP", "filter": "actor:'apt28'",
            "priority": "high", "permissions": "private",
            "breach_monitoring_enabled": False, "substring_matching_enabled": False,
        }])

    def test_create_rule_invalid_priority(self):
        result = self.module.create_recon_rule(
            name="t", topic="SA_VIP", filter="actor:'apt'",
            priority="urgent", permissions="private",
            breach_monitoring_enabled=False, substring_matching_enabled=False,
        )
        self.assertIn("error", result[0])
        self.mock_client.command.assert_not_called()

    def test_update_rule(self):
        self.mock_client.command_for.return_value = _ok([])
        self.module.update_recon_rule(
            id="r1", name="renamed", filter=None, priority=None,
            permissions=None, breach_monitoring_enabled=None, substring_matching_enabled=None,
        )
        call = self.mock_client.command_for.call_args_list[0]
        self.assertEqual(call[0][0], "UpdateRulesV1")
        self.assertEqual(call[1]["body"], [{"id": "r1", "name": "renamed"}])

    def test_delete_rules_with_notifications(self):
        self.mock_client.command.return_value = _ok([])
        self.module.delete_recon_rules(ids=["r1"], delete_notifications=True)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "DeleteRulesV1")
        self.assertEqual(call[1]["parameters"]["notificationsDeletionRequested"], True)
