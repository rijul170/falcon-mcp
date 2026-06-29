"""Tests for the Alerts module."""

from falcon_mcp.modules.alerts import AlertsModule
from tests.modules.utils.test_modules import TestModules


def _ok(resources):
    return {"status_code": 200, "body": {"resources": resources}}


class TestAlertsModule(TestModules):
    def setUp(self):
        self.setup_module(AlertsModule)
        # In this rebuild branch the shared mock does not wire command_for->command;
        # delegate here so assertions on mock_client.command work.
        self.mock_client.command_for.side_effect = (
            lambda op, member_cid=None, **kw: self.mock_client.command(op, **kw)
        )

    def test_register_tools(self):
        self.assert_tools_registered([
            "falcon_search_alerts",
            "falcon_get_alert_details",
            "falcon_aggregate_alerts",
            "falcon_update_alerts",
        ])

    def test_register_resources(self):
        self.assert_resources_registered(["falcon_search_alerts_fql_guide"])

    def test_search(self):
        self.mock_client.command.side_effect = [_ok(["c1", "c2"]), _ok([{"composite_id": "c1"}])]
        self.module.search_alerts(filter="status:'new'", limit=10, offset=None, sort=None)
        calls = self.mock_client.command.call_args_list
        self.assertEqual(calls[0][0][0], "GetQueriesAlertsV2")
        self.assertEqual(calls[1][0][0], "PostEntitiesAlertsV2")
        self.assertEqual(calls[1][1]["body"]["composite_ids"], ["c1", "c2"])

    def test_get_details(self):
        self.mock_client.command.return_value = _ok([{"composite_id": "c1"}])
        self.module.get_alert_details(composite_ids=["c1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "PostEntitiesAlertsV2")
        self.assertEqual(call[1]["body"]["composite_ids"], ["c1"])

    def test_aggregate(self):
        self.mock_client.command.return_value = _ok([{"buckets": []}])
        self.module.aggregate_alerts(
            date_ranges=None, field="severity", filter=None, type="terms",
            interval=None, size=None, name="by_sev",
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "PostAggregatesAlertsV2")
        body = call[1]["body"]
        self.assertIsInstance(body, list)
        self.assertEqual(body[0]["field"], "severity")
        self.assertEqual(body[0]["type"], "terms")
        self.assertEqual(body[0]["name"], "by_sev")

    def test_update_status_and_tag(self):
        self.mock_client.command.return_value = _ok([])
        self.module.update_alerts(
            composite_ids=["c1"], update_status="closed", assign_to_uuid=None,
            assign_to_name=None, unassign=False, add_tag="triage", remove_tag=None,
            append_comment=None, show_in_ui=None,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "PatchEntitiesAlertsV3")
        body = call[1]["body"]
        self.assertEqual(body["composite_ids"], ["c1"])
        actions = body["action_parameters"]
        names = {a["name"]: a["value"] for a in actions}
        self.assertEqual(names["update_status"], "closed")
        self.assertEqual(names["add_tag"], "triage")
        self.assertEqual(set(names), {"update_status", "add_tag"})

    def test_update_requires_action(self):
        result = self.module.update_alerts(
            composite_ids=["c1"], update_status=None, assign_to_uuid=None,
            assign_to_name=None, unassign=False, add_tag=None, remove_tag=None,
            append_comment=None, show_in_ui=None,
        )
        self.assertTrue(self.module._is_error(result[0]))
        self.mock_client.command.assert_not_called()
