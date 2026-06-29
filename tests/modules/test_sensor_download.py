"""Tests for the Sensor Download module."""

from falcon_mcp.modules.sensor_download import SensorDownloadModule
from tests.modules.utils.test_modules import TestModules


def _ok(resources):
    return {"status_code": 200, "body": {"resources": resources}}


class TestSensorDownloadModule(TestModules):
    def setUp(self):
        self.setup_module(SensorDownloadModule)

    def test_register_tools(self):
        self.assert_tools_registered([
            "falcon_search_sensor_installers",
            "falcon_get_sensor_installer_details",
            "falcon_get_ccid",
        ])

    def test_register_resources(self):
        self.assert_resources_registered(["falcon_search_sensor_installers_fql_guide"])

    def test_search(self):
        self.mock_client.command.return_value = _ok([{"sha256": "abc"}])
        self.module.search_sensor_installers(
            filter="platform:'windows'", limit=5, offset=0, sort=None,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "GetCombinedSensorInstallersByQueryV3")
        self.assertEqual(call[1]["parameters"]["filter"], "platform:'windows'")

    def test_get_details(self):
        self.mock_client.command.return_value = _ok([{"sha256": "abc"}])
        self.module.get_sensor_installer_details(ids=["abc"])
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "GetSensorInstallersEntitiesV3")

    def test_get_ccid(self):
        self.mock_client.command.return_value = _ok(["ABCDEFG-AB"])
        self.module.get_ccid()
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "GetSensorInstallersCCIDByQuery")
