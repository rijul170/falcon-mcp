"""Tests for the Message Center module."""

from falcon_mcp.modules.message_center import MessageCenterModule
from tests.modules.utils.test_modules import TestModules


def _ok(resources):
    return {"status_code": 200, "body": {"resources": resources}}


class TestMessageCenterModule(TestModules):
    def setUp(self):
        self.setup_module(MessageCenterModule)

    def test_register_tools(self):
        self.assert_tools_registered([
            "falcon_search_cases",
            "falcon_get_case_details",
            "falcon_search_case_activities",
            "falcon_get_case_activities",
            "falcon_create_case",
            "falcon_add_case_comment",
        ])

    def test_register_resources(self):
        self.assert_resources_registered(["falcon_message_center_fql_guide"])

    def test_search_cases(self):
        self.mock_client.command.side_effect = [
            _ok(["c1"]),
            _ok([{"id": "c1"}]),
        ]
        self.module.search_cases(filter="status:'New'", limit=10, offset=0, sort=None, q=None)
        c1, c2 = self.mock_client.command.call_args_list
        self.assertEqual(c1[0][0], "QueryCasesIdsByFilter")
        self.assertEqual(c2[0][0], "GetCaseEntitiesByIDs")
        self.assertEqual(c2[1]["body"], {"ids": ["c1"]})

    def test_search_case_activities(self):
        self.mock_client.command.return_value = _ok(["a1"])
        self.module.search_case_activities(
            case_id="c1", filter=None, limit=10, offset=0, sort=None, q=None,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "QueryActivityByCaseID")
        self.assertEqual(call[1]["parameters"]["case_id"], "c1")

    def test_get_case_activities(self):
        self.mock_client.command.return_value = _ok([{"id": "a1"}])
        self.module.get_case_activities(ids=["a1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "GetCaseActivityByIds")
        self.assertEqual(call[1]["body"], {"ids": ["a1"]})

    def test_create_case(self):
        self.mock_client.command.return_value = _ok([{"id": "c1"}])
        self.module.create_case(
            title="Need help", body="Got a strange detection",
            case_type="fc-detection-question", user_uuid="u1",
            detections=None, incidents=None,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "CreateCaseV2")
        self.assertEqual(call[1]["body"], {
            "title": "Need help", "body": "Got a strange detection",
            "type": "fc-detection-question", "user_uuid": "u1",
        })

    def test_add_comment(self):
        self.mock_client.command.return_value = _ok([{"id": "a1"}])
        self.module.add_case_comment(case_id="c1", comment="Looking into it", user_uuid="u1")
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "CaseAddActivity")
        self.assertEqual(call[1]["body"], {
            "case_id": "c1", "body": "Looking into it",
            "type": "comment", "user_uuid": "u1",
        })
