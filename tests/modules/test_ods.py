"""Tests for the ODS module."""

from falcon_mcp.modules.ods import OdsModule
from tests.modules.utils.test_modules import TestModules


def _ok(resources):
    return {"status_code": 200, "body": {"resources": resources}}


class TestOdsModule(TestModules):
    def setUp(self):
        self.setup_module(OdsModule)

    def test_register_tools(self):
        self.assert_tools_registered([
            "falcon_search_ods_scans",
            "falcon_get_ods_scan_details",
            "falcon_search_ods_host_scans",
            "falcon_get_ods_host_scan_details",
            "falcon_search_ods_scheduled_scans",
            "falcon_get_ods_scheduled_scan_details",
            "falcon_search_ods_malicious_files",
            "falcon_get_ods_malicious_file_details",
            "falcon_create_ods_scan",
            "falcon_cancel_ods_scans",
        ])

    def test_register_resources(self):
        self.assert_resources_registered(["falcon_ods_fql_guide"])

    def test_search_scans(self):
        self.mock_client.command.return_value = _ok(["s1"])
        self.module.search_ods_scans(filter=None, limit=10, offset=0, sort=None)
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "query_scans")

    def test_get_scan_details(self):
        self.mock_client.command.return_value = _ok([{"id": "s1"}])
        self.module.get_ods_scan_details(ids=["s1"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "get_scans_by_scan_ids_v2")

    def test_create_scan_validates_target(self):
        result = self.module.create_ods_scan(
            description="d", host_ids=None, host_group_ids=None,
            file_paths=None, scan_exclusions=None,
            cpu_priority=2, max_duration=2, max_file_size=60, pause_duration=2,
            quarantine=False, endpoint_notification=False,
            sensor_ml_level_detection=2, sensor_ml_level_prevention=2,
            cloud_ml_level_detection=2, cloud_ml_level_prevention=2,
        )
        self.assertIn("error", result[0])
        self.mock_client.command.assert_not_called()

    def test_create_scan_with_hosts(self):
        self.mock_client.command.return_value = _ok([{"id": "s1"}])
        self.module.create_ods_scan(
            description="Test scan", host_ids=["aid1"], host_group_ids=None,
            file_paths=["C:\\Users"], scan_exclusions=None,
            cpu_priority=1, max_duration=2, max_file_size=60, pause_duration=2,
            quarantine=False, endpoint_notification=False,
            sensor_ml_level_detection=2, sensor_ml_level_prevention=0,
            cloud_ml_level_detection=2, cloud_ml_level_prevention=0,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "create_scan")
        body = call[1]["body"]
        self.assertEqual(body["hosts"], ["aid1"])
        self.assertEqual(body["file_paths"], ["C:\\Users"])
        self.assertEqual(body["initiated_from"], "falcon-mcp")
        self.assertEqual(body["sensor_ml_level_prevention"], 0)

    def test_cancel_scans(self):
        self.mock_client.command.return_value = _ok([])
        self.module.cancel_ods_scans(ids=["s1", "s2"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "cancel_scans")
        self.assertEqual(call[1]["body"], {"ids": ["s1", "s2"]})
