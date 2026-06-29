"""Tests for the Zero Trust module."""

from falcon_mcp.modules.zero_trust import ZeroTrustModule
from tests.modules.utils.test_modules import TestModules


def _ok(resources):
    return {"status_code": 200, "body": {"resources": resources}}


class TestZeroTrustModule(TestModules):
    def setUp(self):
        self.setup_module(ZeroTrustModule)

    def test_register_tools(self):
        self.assert_tools_registered([
            "falcon_get_zta_assessments",
            "falcon_search_zta_assessments",
            "falcon_get_zta_assessments_by_score",
            "falcon_get_zta_audit",
        ])

    def test_register_resources(self):
        self.assert_resources_registered(["falcon_zta_fql_guide"])

    def test_get_assessments(self):
        self.mock_client.command.return_value = _ok([{"aid": "a1", "score": 80}])
        self.module.get_zta_assessments(ids=["aid1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "getAssessmentV1")
        self.assertEqual(call[1]["parameters"]["ids"], ["aid1"])

    def test_get_assessments_empty(self):
        result = self.module.get_zta_assessments(ids=[])
        self.assertEqual(result, [])
        self.mock_client.command.assert_not_called()

    def test_search_assessments(self):
        self.mock_client.command.return_value = _ok([{"aid": "a1"}])
        self.module.search_zta_assessments(filter="score:<50", limit=100, offset=None, sort=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "getCombinedAssessmentsQuery")
        self.assertEqual(call[1]["parameters"]["filter"], "score:<50")

    def test_assessments_by_score(self):
        self.mock_client.command.return_value = _ok([])
        self.module.get_zta_assessments_by_score(filter=None, limit=10, offset=None, sort="score.asc")
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "getAssessmentsByScoreV1")
        self.assertEqual(call[1]["parameters"]["sort"], "score.asc")

    def test_get_audit(self):
        self.mock_client.command.return_value = _ok([{"summary": {}}])
        self.module.get_zta_audit()
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "getAuditV1")
