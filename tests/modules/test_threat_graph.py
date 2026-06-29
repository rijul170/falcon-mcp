"""Tests for the Threat Graph module."""

from falcon_mcp.modules.threat_graph import ThreatGraphModule
from tests.modules.utils.test_modules import TestModules


def _ok(resources):
    return {"status_code": 200, "body": {"resources": resources}}


class TestThreatGraphModule(TestModules):
    def setUp(self):
        self.setup_module(ThreatGraphModule)

    def test_register_tools(self):
        self.assert_tools_registered([
            "falcon_list_threat_graph_edge_types",
            "falcon_get_threat_graph_edges",
            "falcon_get_threat_graph_vertices",
            "falcon_get_threat_graph_summary",
            "falcon_get_threat_graph_ran_on",
        ])

    def test_register_resources(self):
        self.assert_resources_registered(["falcon_threat_graph_guide"])

    def test_list_edge_types(self):
        self.mock_client.command.return_value = _ok(["e1"])
        self.module.list_threat_graph_edge_types()
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "queries_edgetypes_get")

    def test_get_edges(self):
        self.mock_client.command.return_value = _ok([])
        self.module.get_threat_graph_edges(
            ids="v1", edge_type="child_processes", direction="out",
            scope="customer", limit=10, offset=None, nano=False,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "combined_edges_get")
        self.assertEqual(call[1]["parameters"]["ids"], "v1")
        self.assertEqual(call[1]["parameters"]["edge_type"], "child_processes")

    def test_get_edges_invalid_direction(self):
        result = self.module.get_threat_graph_edges(
            ids="v1", edge_type="x", direction="lateral",
            scope=None, limit=10, offset=None, nano=False,
        )
        self.assertIn("error", result[0])
        self.mock_client.command.assert_not_called()

    def test_get_vertices_passes_path_kwarg(self):
        self.mock_client.command_for.return_value = _ok([{"id": "v1"}])
        self.module.get_threat_graph_vertices(
            vertex_type="device", ids=["v1"], scope=None, nano=False,
        )
        call = self.mock_client.command_for.call_args_list[0]
        self.assertEqual(call[0][0], "entities_vertices_getv2")
        # vertex_type must be a top-level kwarg, NOT inside parameters,
        # so falconpy's scrub_target can substitute the URL placeholder.
        self.assertEqual(call[1]["vertex_type"], "device")
        self.assertEqual(call[1]["parameters"]["ids"], ["v1"])

    def test_get_summary_passes_path_kwarg(self):
        self.mock_client.command_for.return_value = _ok([{"id": "v1"}])
        self.module.get_threat_graph_summary(
            vertex_type="process", ids=["v1"], scope="device", nano=False,
        )
        call = self.mock_client.command_for.call_args_list[0]
        self.assertEqual(call[0][0], "combined_summary_get")
        self.assertEqual(call[1]["vertex_type"], "process")
        self.assertEqual(call[1]["parameters"]["scope"], "device")

    def test_ran_on(self):
        self.mock_client.command.return_value = _ok([])
        self.module.get_threat_graph_ran_on(
            value="abc...", type="sha256", limit=10, offset=None, nano=False,
        )
        call = self.mock_client.command.call_args_list[0]
        self.assertEqual(call[0][0], "combined_ran_on_get")
        self.assertEqual(call[1]["parameters"]["value"], "abc...")
        self.assertEqual(call[1]["parameters"]["type"], "sha256")
