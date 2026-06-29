"""Tests for the Tailored Intelligence module."""

from falcon_mcp.modules.tailored_intelligence import TailoredIntelligenceModule
from tests.modules.utils.test_modules import TestModules


def _ok(resources):
    return {"status_code": 200, "body": {"resources": resources}}


class TestTailoredIntelligenceModule(TestModules):
    def setUp(self):
        self.setup_module(TailoredIntelligenceModule)
        self.mock_client.command_for.side_effect = (
            lambda op, member_cid=None, **kw: self.mock_client.command(op, **kw)
        )

    def test_register_tools(self):
        self.assert_tools_registered([
            "falcon_search_tailored_intel_events",
            "falcon_get_tailored_intel_event_details",
            "falcon_search_tailored_intel_rules",
            "falcon_get_tailored_intel_rule_details",
        ])

    def test_search_events(self):
        self.mock_client.command.return_value = _ok(["e1"])
        self.module.search_tailored_intel_events(
            filter=None, limit=10, offset=None, sort=None, q=None, member_cid=None,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "QueryEvents")

    def test_get_event_details(self):
        self.mock_client.command.return_value = _ok([{"id": "e1"}])
        self.module.get_tailored_intel_event_details(ids=["e1"], member_cid=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "GetEventsEntities")
        self.assertEqual(call[1]["body"]["ids"], ["e1"])

    def test_search_rules(self):
        self.mock_client.command.return_value = _ok(["r1"])
        self.module.search_tailored_intel_rules(
            filter="type:'yara-master'", limit=10, offset=None, sort=None, q=None, member_cid=None,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "QueryRules")

    def test_get_rule_details(self):
        self.mock_client.command.return_value = _ok([{"id": "r1"}])
        self.module.get_tailored_intel_rule_details(ids=["r1"], member_cid=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "GetRulesEntities")
        self.assertEqual(call[1]["body"]["ids"], ["r1"])
