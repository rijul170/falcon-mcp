"""Tests for the Event Streams module."""

from falcon_mcp.modules.event_streams import EventStreamsModule
from tests.modules.utils.test_modules import TestModules


def _ok(resources):
    return {"status_code": 200, "body": {"resources": resources}}


class TestEventStreamsModule(TestModules):
    def setUp(self):
        self.setup_module(EventStreamsModule)
        # In this rebuild branch the shared mock does not wire command_for->command;
        # delegate here so assertions on mock_client.command work.
        self.mock_client.command_for.side_effect = (
            lambda op, member_cid=None, **kw: self.mock_client.command(op, **kw)
        )

    def test_register_tools(self):
        self.assert_tools_registered([
            "falcon_list_available_streams",
            "falcon_refresh_active_stream_session",
        ])

    def test_list_streams(self):
        self.mock_client.command.return_value = _ok([{"dataFeedURL": "https://..."}])
        self.module.list_available_streams(app_id="mcp-feed", format="json")
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "listAvailableStreamsOAuth2")
        self.assertEqual(call[1]["parameters"]["appId"], "mcp-feed")
        self.assertEqual(call[1]["parameters"]["format"], "json")

    def test_refresh(self):
        self.mock_client.command.return_value = _ok([])
        self.module.refresh_active_stream_session(app_id="mcp-feed", partition=0)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "refreshActiveStreamSession")
        params = call[1]["parameters"]
        self.assertEqual(params["action_name"], "refresh_active_stream_session")
        self.assertEqual(params["appId"], "mcp-feed")
        self.assertEqual(params["partition"], 0)
