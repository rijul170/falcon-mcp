import unittest
from unittest import mock
from unittest.mock import MagicMock

from mcp.server import FastMCP
from mcp.types import ToolAnnotations

from falcon_mcp.client import FalconClient


class TestModules(unittest.TestCase):
    def setup_module(self, module_class):
        """
        Set up test fixtures with the specified module class.

        Args:
            module_class: The module class to instantiate
        """
        # Module catalog tests assert the FULL tool set, so open the destructive
        # safety gate for the duration of each test (read-only mode is already off
        # by default since FALCON_MCP_READONLY is unset). Cleaned up automatically.
        destructive_patch = mock.patch.dict(
            "os.environ", {"FALCON_MCP_ALLOW_DESTRUCTIVE": "true"}
        )
        destructive_patch.start()
        self.addCleanup(destructive_patch.stop)

        # Create a mock client
        self.mock_client = MagicMock(spec=FalconClient)

        # The base module helpers call ``client.command_for(operation, member_cid=..., **kwargs)``
        # (MSSP-aware). Tests use one of two conventions:
        #   (a) legacy: configure ``command.return_value`` and assert on ``command``
        #   (b) newer:  configure ``command_for.return_value`` and assert on ``command_for``
        # Support both: command_for records its own calls (so member_cid assertions work) and
        # returns its own return_value when a test set one, otherwise delegates to ``command``
        # (dropping member_cid) so legacy ``command``-based tests keep working unchanged.
        _CF_DEFAULT = object()
        self.mock_client.command_for.return_value = _CF_DEFAULT

        def _command_for(operation, *args, member_cid=None, **kwargs):
            rv = self.mock_client.command_for.return_value
            if rv is not _CF_DEFAULT:
                return rv
            return self.mock_client.command(operation, *args, **kwargs)

        self.mock_client.command_for.side_effect = _command_for

        # Create a mock server
        self.mock_server = MagicMock(spec=FastMCP)

        # Create the module
        self.module = module_class(self.mock_client)

    def assert_tools_registered(self, expected_tools):
        """
        Helper method to verify that a module correctly registers its tools.

        Args:
            expected_tools: List of tool names that should be registered
        """
        # Call register_tools
        self.module.register_tools(self.mock_server)

        # Verify that add_tool was called for each tool
        self.assertEqual(self.mock_server.add_tool.call_count, len(expected_tools))

        # Get the tool names that were registered
        registered_tools = [
            call.kwargs["name"] for call in self.mock_server.add_tool.call_args_list
        ]

        # Verify that all expected tools were registered
        for tool in expected_tools:
            self.assertIn(tool, registered_tools)

    def assert_resources_registered(self, expected_resources):
        """
        Helper method to verify that a module correctly registers its resources.

        Args:
            expected_tools: List of resources names that should be registered
        """
        # Call register_tools
        self.module.register_resources(self.mock_server)

        # Verify that add_resource was called for each resource
        self.assertEqual(
            self.mock_server.add_resource.call_count, len(expected_resources)
        )

        # Get the tool names that were registered
        registered_resources = [
            call.kwargs["resource"].name
            for call in self.mock_server.add_resource.call_args_list
        ]

        # Verify that all expected tools were registered
        for tool in expected_resources:
            self.assertIn(tool, registered_resources)

    def assert_tool_annotations(self, tool_name: str, expected_annotations: ToolAnnotations):
        """Verify that a tool was registered with the expected annotations.

        Args:
            tool_name: The full tool name (e.g., "falcon_search_detections")
            expected_annotations: The expected ToolAnnotations instance
        """
        for call in self.mock_server.add_tool.call_args_list:
            if call.kwargs.get("name") == tool_name:
                self.assertEqual(call.kwargs.get("annotations"), expected_annotations)
                return
        self.fail(f"Tool {tool_name} not found in registered tools")
