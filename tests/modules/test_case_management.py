"""Tests for the Case Management module."""

from falcon_mcp.modules.case_management import CaseManagementModule
from tests.modules.utils.test_modules import TestModules


def _ok(resources):
    return {"status_code": 200, "body": {"resources": resources}}


class TestCaseManagementModule(TestModules):
    def setUp(self):
        self.setup_module(CaseManagementModule)

    def test_register_tools(self):
        self.assert_tools_registered([
            "falcon_add_ngsiem_case_tags",
            "falcon_attach_alert_evidence",
            "falcon_attach_event_evidence",
            "falcon_create_case_sla",
            "falcon_create_case_template",
            "falcon_create_ngsiem_case",
            "falcon_create_notification_group",
            "falcon_delete_case_slas",
            "falcon_delete_case_templates",
            "falcon_delete_notification_groups",
            "falcon_export_case_template",
            "falcon_get_case_sla",
            "falcon_get_case_template",
            "falcon_get_ngsiem_case_details",
            "falcon_get_notification_groups",
            "falcon_import_case_template",
            "falcon_remove_ngsiem_case_tags",
            "falcon_search_case_slas",
            "falcon_search_case_templates",
            "falcon_search_ngsiem_cases",
            "falcon_search_notification_groups",
            "falcon_update_case_sla",
            "falcon_update_case_template",
            "falcon_update_ngsiem_case",
            "falcon_update_notification_group",
        ])

    def test_register_resources(self):
        self.assert_resources_registered(["falcon_ngsiem_cases_fql_guide"])

    def test_search(self):
        self.mock_client.command.side_effect = [
            _ok(["c1"]),
            _ok([{"id": "c1"}]),
        ]
        self.module.search_ngsiem_cases(
            filter="status:'New'", limit=10, offset=0, sort=None, q=None,
        )
        c1, c2 = self.mock_client.command.call_args_list
        self.assertEqual(c1[0][0], "queries_cases_get_v1")
        self.assertEqual(c2[0][0], "entities_cases_post_v2")
        self.assertEqual(c2[1]["body"], {"ids": ["c1"]})

    def test_create(self):
        self.mock_client.command.return_value = _ok([{"id": "c1"}])
        self.module.create_ngsiem_case(
            name="New case", description="d", severity=4, status="New",
            assigned_to_user_uuid=None, tags=["tag1"],
            alert_ids=["a1"], event_ids=None, template_id=None,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "entities_cases_put_v2")
        self.assertEqual(call[1]["body"], {
            "name": "New case", "severity": 4, "description": "d",
            "status": "New", "tags": ["tag1"],
            "evidence": {"alerts": [{"id": "a1"}]},
        })

    def test_update_validates(self):
        result = self.module.update_ngsiem_case(
            id="c1", name=None, description=None, severity=None,
            status=None, assigned_to_user_uuid=None,
        )
        self.assertIn("error", result[0])
        self.mock_client.command.assert_not_called()

    def test_update(self):
        self.mock_client.command.return_value = _ok([])
        self.module.update_ngsiem_case(
            id="c1", name=None, description=None, severity=None,
            status="Resolved", assigned_to_user_uuid=None,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "entities_cases_patch_v2")
        self.assertEqual(call[1]["body"], {"id": "c1", "status": "Resolved"})

    def test_add_tags(self):
        self.mock_client.command.return_value = _ok([])
        self.module.add_ngsiem_case_tags(id="c1", tags=["t1", "t2"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "entities_case_tags_post_v1")
        self.assertEqual(call[1]["body"], {"id": "c1", "tags": ["t1", "t2"]})

    def test_remove_tags_uses_query(self):
        self.mock_client.command.return_value = _ok([])
        self.module.remove_ngsiem_case_tags(id="c1", tags=["t1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "entities_case_tags_delete_v1")
        # API requires query params, not body.
        self.assertEqual(call[1]["parameters"], {"id": "c1", "tag": ["t1"]})

    def test_attach_alert_evidence(self):
        self.mock_client.command.return_value = _ok([])
        self.module.attach_alert_evidence(case_id="c1", alert_ids=["a1", "a2"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "entities_alert_evidence_post_v1")
        self.assertEqual(call[1]["body"], {
            "id": "c1", "alerts": [{"id": "a1"}, {"id": "a2"}],
        })

    def test_attach_event_evidence(self):
        self.mock_client.command.return_value = _ok([])
        self.module.attach_event_evidence(case_id="c1", event_ids=["e1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "entities_event_evidence_post_v1")
        self.assertEqual(call[1]["body"], {
            "id": "c1", "events": [{"id": "e1"}],
        })
