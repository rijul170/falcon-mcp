"""Tests for the MalQuery module."""

from falcon_mcp.modules.malquery import MalQueryModule
from tests.modules.utils.test_modules import TestModules


def _ok(resources):
    return {"status_code": 200, "body": {"resources": resources}}


class TestMalQueryModule(TestModules):
    def setUp(self):
        self.setup_module(MalQueryModule)
        self.mock_client.command_for.side_effect = (
            lambda op, member_cid=None, **kw: self.mock_client.command(op, **kw)
        )

    def test_register_tools(self):
        self.assert_tools_registered([
            "falcon_get_malquery_quotas",
            "falcon_get_malquery_sample_metadata",
            "falcon_get_malquery_request_results",
            "falcon_malquery_exact_search",
            "falcon_malquery_hunt",
        ])

    def test_quotas(self):
        self.mock_client.command.return_value = _ok([{"quota": {}}])
        self.module.get_malquery_quotas(member_cid=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "GetMalQueryQuotasV1")

    def test_metadata(self):
        self.mock_client.command.return_value = _ok([{"sha256": "abc"}])
        self.module.get_malquery_sample_metadata(ids=["abc"], member_cid=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "GetMalQueryMetadataV1")

    def test_request_results(self):
        self.mock_client.command.return_value = _ok([{"id": "r1"}])
        self.module.get_malquery_request_results(ids=["r1"], member_cid=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "GetMalQueryRequestV1")

    def test_exact_search(self):
        self.mock_client.command.return_value = _ok([{"id": "req1"}])
        self.module.malquery_exact_search(
            patterns=[{"type": "ascii", "value": "evil"}],
            filter_filetypes=["pe32"], filter_meta=None, limit=50,
            min_size=None, max_size=None, min_date=None, max_date=None, member_cid=None,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "PostMalQueryExactSearchV1")
        body = call[1]["body"]
        self.assertEqual(body["patterns"], [{"type": "ascii", "value": "evil"}])
        self.assertEqual(body["options"]["filter_filetypes"], ["pe32"])
        self.assertEqual(body["options"]["limit"], 50)

    def test_exact_search_requires_patterns(self):
        result = self.module.malquery_exact_search(
            patterns=[], filter_filetypes=None, filter_meta=None, limit=None,
            min_size=None, max_size=None, min_date=None, max_date=None, member_cid=None,
        )
        self.assertTrue(self.module._is_error(result[0]))
        self.mock_client.command.assert_not_called()

    def test_hunt(self):
        self.mock_client.command.return_value = _ok([{"id": "req2"}])
        self.module.malquery_hunt(
            yara_rule="rule x {condition: true}", filter_filetypes=None, filter_meta=None,
            limit=None, min_size=None, max_size=None, min_date=None, max_date=None, member_cid=None,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "PostMalQueryHuntV1")
        self.assertEqual(call[1]["body"]["yara_rule"], "rule x {condition: true}")
