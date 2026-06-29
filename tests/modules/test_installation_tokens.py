"""Tests for the Installation Tokens module."""

from falcon_mcp.modules.installation_tokens import InstallationTokensModule
from tests.modules.utils.test_modules import TestModules


def _ok(resources):
    return {"status_code": 200, "body": {"resources": resources}}


class TestInstallationTokensModule(TestModules):
    def setUp(self):
        self.setup_module(InstallationTokensModule)

    def test_register_tools(self):
        self.assert_tools_registered([
            "falcon_create_installation_token",
            "falcon_delete_installation_tokens",
            "falcon_get_installation_token_details",
            "falcon_get_installation_token_settings",
            "falcon_get_token_audit_event_details",
            "falcon_search_installation_tokens",
            "falcon_search_token_audit_events",
            "falcon_update_installation_token",
        ])

    def test_register_resources(self):
        self.assert_resources_registered(["falcon_search_installation_tokens_fql_guide"])

    def test_search(self):
        self.mock_client.command.side_effect = [
            _ok(["t1"]),
            _ok([{"id": "t1", "label": "lab"}]),
        ]
        self.module.search_installation_tokens(filter="revoked:false", limit=100, offset=None, sort=None)
        c1, c2 = self.mock_client.command.call_args_list
        self.assertEqual(c1[0][0], "tokens_query")
        self.assertEqual(c1[1]["parameters"]["filter"], "revoked:false")
        self.assertEqual(c2[0][0], "tokens_read")
        self.assertEqual(c2[1]["parameters"]["ids"], ["t1"])

    def test_get_details(self):
        self.mock_client.command.return_value = _ok([{"id": "t1"}])
        self.module.get_installation_token_details(ids=["t1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "tokens_read")
        self.assertEqual(call[1]["parameters"]["ids"], ["t1"])

    def test_settings(self):
        self.mock_client.command.return_value = _ok([{"max_active_tokens": 5}])
        self.module.get_installation_token_settings()
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "customer_settings_read")

    def test_create(self):
        self.mock_client.command.return_value = _ok([{"id": "t1"}])
        self.module.create_installation_token(label="proj", expires_timestamp="2026-12-31T23:59:59Z")
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "tokens_create")
        self.assertEqual(call[1]["body"], {
            "label": "proj", "expires_timestamp": "2026-12-31T23:59:59Z",
        })

    def test_create_no_expiry(self):
        self.mock_client.command.return_value = _ok([{"id": "t2"}])
        self.module.create_installation_token(label="proj", expires_timestamp=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[1]["body"], {"label": "proj"})

    def test_update_revoke(self):
        self.mock_client.command.return_value = _ok([])
        self.module.update_installation_token(
            ids=["t1"], label=None, revoked=True, expires_timestamp=None,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "tokens_update")
        self.assertEqual(call[1]["parameters"]["ids"], ["t1"])
        self.assertEqual(call[1]["body"], {"revoked": True})

    def test_update_label_and_expiry(self):
        self.mock_client.command.return_value = _ok([])
        self.module.update_installation_token(
            ids=["t1"], label="new", revoked=None, expires_timestamp="2027-01-01T00:00:00Z",
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[1]["body"], {
            "label": "new", "expires_timestamp": "2027-01-01T00:00:00Z",
        })

    def test_update_validates_no_fields(self):
        result = self.module.update_installation_token(
            ids=["t1"], label=None, revoked=None, expires_timestamp=None,
        )
        self.assertIn("error", result[0])
        self.mock_client.command.assert_not_called()

    def test_delete(self):
        self.mock_client.command.return_value = _ok([])
        self.module.delete_installation_tokens(ids=["t1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "tokens_delete")
        self.assertEqual(call[1]["parameters"]["ids"], ["t1"])
