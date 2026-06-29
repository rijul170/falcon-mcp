"""
Base module for Falcon MCP Server

This module provides the base class for all Falcon MCP server modules.
"""

import os
from abc import ABC, abstractmethod
from typing import Any, Callable

from mcp import Resource
from mcp.server import FastMCP
from mcp.types import ToolAnnotations

from falcon_mcp.client import FalconClient
from falcon_mcp.common.errors import handle_api_response
from falcon_mcp.common.logging import get_logger
from falcon_mcp.common.utils import prepare_api_parameters

logger = get_logger(__name__)

# Default: read-only tool that talks to an external API
READ_ONLY_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=True,
    destructiveHint=False,
    idempotentHint=True,
    openWorldHint=True,
)

# Truthy values for the safety environment flags.
_READONLY_TRUTHY = {"true", "1", "yes"}


def is_readonly_mode() -> bool:
    """Return True if read-only mode is enabled via the FALCON_MCP_READONLY env var.

    Truthy values (case-insensitive): "true", "1", "yes". Anything else
    (including unset) means read-only mode is OFF and all tools register normally.
    """
    return os.environ.get("FALCON_MCP_READONLY", "").strip().lower() in _READONLY_TRUTHY


_DESTRUCTIVE_FALSY = {"", "false", "0", "no", "off"}


def destructive_policy() -> str | frozenset[str]:
    """Parse FALCON_MCP_ALLOW_DESTRUCTIVE into a destructive-enablement policy.

    This is the second tier of the safety gate. Even when writes are enabled
    (FALCON_MCP_READONLY off), tools annotated destructiveHint=True — RTR command
    execution, host containment, cloud-account/user/CID deletes, etc. — stay
    suppressed unless permitted here. Returns:

    - ``"all"``  when the value is truthy ("true", "1", "yes") — arms EVERY
      destructive tool (blunt; ~119 tools incl. cloud-account/user deletion).
    - ``frozenset`` of allowed tool names when given a comma-separated list
      (with or without the ``falcon_`` prefix) — arms ONLY those tools. This is
      the recommended way to enable a curated subset (e.g. host containment +
      RTR) without arming destructive cloud/MSSP/user operations.
    - ``"none"`` when unset/false/empty — no destructive tools (default).
    """
    raw = os.environ.get("FALCON_MCP_ALLOW_DESTRUCTIVE", "").strip()
    if raw.lower() in _READONLY_TRUTHY:
        return "all"
    if raw.lower() in _DESTRUCTIVE_FALSY:
        return "none"
    names = set()
    for tok in raw.split(","):
        tok = tok.strip()
        if tok:
            names.add(tok if tok.startswith("falcon_") else f"falcon_{tok}")
    return frozenset(names) if names else "none"


def is_allow_destructive() -> bool:
    """Backward-compatible: True if ANY destructive tool is permitted."""
    return destructive_policy() != "none"


def _destructive_permitted(prefixed_name: str) -> bool:
    """Whether a specific destructive tool is permitted under the current policy."""
    policy = destructive_policy()
    if policy == "all":
        return True
    if policy == "none":
        return False
    return prefixed_name in policy


class BaseModule(ABC):
    """Base class for all Falcon MCP server modules."""

    def __init__(self, client: FalconClient):
        """Initialize the module.

        Args:
            client: Falcon API client
        """
        self.client = client
        self.tools: list[str] = []  # List to track registered tools
        self.resources: list[str] = []  # List to track registered resources

    @abstractmethod
    def register_tools(self, server: FastMCP) -> None:
        """Register tools with the MCP server.

        Args:
            server: MCP server instance
        """

    def register_resources(self, server: FastMCP) -> None:
        """Register resources with the MCP Server.

        Args:
            server: MCP server instance
        """

    def _add_tool(
        self,
        server: FastMCP,
        method: Callable[..., Any],
        name: str,
        annotations: ToolAnnotations | None = None,
    ) -> None:
        """Add a tool to the MCP server and track it.

        Args:
            server: MCP server instance
            method: Method to register
            name: Tool name
            annotations: MCP tool annotations. Defaults to READ_ONLY_ANNOTATIONS.
        """
        prefixed_name = f"falcon_{name}"
        effective_annotations = annotations or READ_ONLY_ANNOTATIONS

        # Read-only safety gate: when read-only mode is on, mutating tools
        # (anything whose effective annotation is not explicitly readOnlyHint=True)
        # are skipped entirely — not registered with the server and not tracked.
        if is_readonly_mode() and effective_annotations.readOnlyHint is not True:
            logger.info(
                "Read-only mode active: suppressing mutating tool %s (readOnlyHint=%s)",
                prefixed_name,
                effective_annotations.readOnlyHint,
            )
            return

        # Destructive safety gate (second tier): even when writes are enabled,
        # destructive tools stay suppressed unless permitted by FALCON_MCP_ALLOW_DESTRUCTIVE
        # (truthy = all destructive tools; comma-list = only those named tools).
        if effective_annotations.destructiveHint is True and not _destructive_permitted(prefixed_name):
            logger.info(
                "Destructive tool suppressed (enable via FALCON_MCP_ALLOW_DESTRUCTIVE "
                "= true, or a comma-list of tool names): %s",
                prefixed_name,
            )
            return

        server.add_tool(method, name=prefixed_name, annotations=effective_annotations)
        self.tools.append(prefixed_name)
        logger.debug("Added tool: %s", prefixed_name)

    def _add_resource(self, server: FastMCP, resource: Resource) -> None:
        """Add a resource to the MCP server and track it.

        Args:
            server: MCP server instance
            resource: Resource object
        """
        # FastMCP expects its own Resource type, cast accordingly
        server.add_resource(resource=resource)  # type: ignore[arg-type]

        resource_uri = resource.uri
        self.resources.append(str(resource_uri))
        logger.debug("Added resource: %s", resource_uri)

    def _base_get_by_ids(
        self,
        operation: str,
        ids: list[str],
        id_key: str = "ids",
        use_params: bool = False,
        member_cid: str | None = None,
        **additional_params: Any,
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Helper method for API operations that retrieve entities by IDs.

        Args:
            operation: The API operation name
            ids: List of entity IDs
            id_key: The key name for IDs in the request (default: "ids")
            use_params: If True, send IDs as query parameters (GET).
                       If False, send as request body (POST). Default: False
            member_cid: Optional child CID to scope the call to a specific tenant.
            **additional_params: Additional parameters to include in the request

        Returns:
            List of entity details or error dict
        """
        # Build the request params with dynamic ID key and additional parameters
        request_params = {id_key: ids}
        request_params.update(additional_params)

        prepared = prepare_api_parameters(request_params)

        # Make the API request using either parameters (GET) or body (POST)
        if use_params:
            response = self.client.command_for(operation, member_cid=member_cid, parameters=prepared)
        else:
            response = self.client.command_for(operation, member_cid=member_cid, body=prepared)

        # Handle the response
        return handle_api_response(
            response,
            operation=operation,
            error_message="Failed to perform operation",
            default_result=[],
        )

    def _base_search_api_call(
        self,
        operation: str,
        search_params: dict[str, Any],
        error_message: str = "Search operation failed",
        default_result: Any = None,
        member_cid: str | None = None,
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Standardized API call for search operations with parameters.

        Args:
            operation: The API operation name (e.g., "QueryDevicesByFilter")
            search_params: Dictionary of search parameters (filter, limit, offset, sort, etc.)
            error_message: Custom error message for failed operations
            default_result: Default value to return if no results found
            member_cid: Optional child CID to scope the call to a specific tenant.

        Returns:
            API response data or error dict
        """
        prepared_params = prepare_api_parameters(search_params)

        logger.debug("Executing %s with params: %s", operation, prepared_params)

        response = self.client.command_for(operation, member_cid=member_cid, parameters=prepared_params)

        return handle_api_response(
            response,
            operation=operation,
            error_message=error_message,
            default_result=default_result if default_result is not None else [],
        )

    def _base_query_api_call(
        self,
        operation: str,
        query_params: dict[str, Any] | None = None,
        body_params: dict[str, Any] | None = None,
        path_params: dict[str, Any] | None = None,
        error_message: str = "Query operation failed",
        default_result: Any = None,
        member_cid: str | None = None,
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Standardized API call for operations that can use both parameters and body.

        Args:
            operation: The API operation name
            query_params: Dictionary of query parameters (for parameters= argument)
            body_params: Dictionary of body parameters (for body= argument)
            path_params: Dictionary of path parameters. FalconPy's Uber class
                substitutes these into the URL route from top-level kwargs keyed
                by field name, so each entry is forwarded as its own kwarg.
            error_message: Custom error message for failed operations
            default_result: Default value to return if no results found
            member_cid: Optional child CID to scope the call to a specific tenant.

        Returns:
            API response data or error dict
        """
        call_args = {}

        if query_params:
            call_args["parameters"] = prepare_api_parameters(query_params)

        if body_params:
            call_args["body"] = prepare_api_parameters(body_params)

        if path_params:
            # Path substitution reads from top-level kwargs by field name, not
            # from parameters=, so inject each path value as its own kwarg.
            for key, value in prepare_api_parameters(path_params).items():
                call_args[key] = value

        logger.debug("Executing %s with args: %s", operation, call_args)

        response = self.client.command_for(operation, member_cid=member_cid, **call_args)

        # Handle GraphQL operations differently - they don't use "resources" structure
        if operation == "api_preempt_proxy_post_graphql":
            # For GraphQL, check status and return the full body on success
            if response.get("status_code") == 200:
                body: dict[str, Any] = response.get("body", {})
                return body
            else:
                # Use standard error handling for failed GraphQL requests
                return handle_api_response(
                    response,
                    operation=operation,
                    error_message=error_message,
                    default_result=default_result if default_result is not None else {},
                )

        # Handle the response using standard resource extraction
        return handle_api_response(
            response,
            operation=operation,
            error_message=error_message,
            default_result=default_result if default_result is not None else [],
        )

    def _base_get_api_call(
        self,
        operation: str,
        api_params: dict[str, Any],
        error_message: str = "GET operation failed",
        decode_binary: bool = True,
        member_cid: str | None = None,
    ) -> list[dict[str, Any]] | dict[str, Any] | str:
        """Standardized API call for GET operations with optional binary response handling.

        Args:
            operation: The API operation name (e.g., "GetMitreReport", "GetReportPdf")
            api_params: Dictionary of API parameters
            error_message: Custom error message for failed operations
            decode_binary: Whether to decode binary responses as UTF-8 (default: True)
            member_cid: Optional child CID to scope the call to a specific tenant.

        Returns:
            - For successful operations with binary responses: decoded string content
            - For successful operations with JSON responses: standard API response
            - For failed operations: error dict
        """
        prepared_params = prepare_api_parameters(api_params)

        logger.debug("Executing %s with params: %s", operation, prepared_params)

        command_response = self.client.command_for(operation, member_cid=member_cid, parameters=prepared_params)

        # FalconPy returns raw bytes for binary download endpoints (e.g., GetMitreReport)
        if isinstance(command_response, bytes):
            if decode_binary:
                return command_response.decode('utf-8')
            return command_response

        # Dict response - check status code and use standard error handling
        status_code = command_response.get("status_code")

        if status_code != 200:
            return handle_api_response(
                command_response,
                operation=operation,
                error_message=error_message,
                default_result=[],
            )

        # Standard response handling for dict responses
        return handle_api_response(
            command_response,
            operation=operation,
            error_message=error_message,
            default_result=[],
        )

    def _is_error(self, response: Any) -> bool:
        return isinstance(response, dict) and "error" in response

    def _format_fql_error_response(
        self,
        error_or_empty: list[dict[str, Any]],
        filter_used: str | None,
        fql_documentation: str,
    ) -> dict[str, Any]:
        """Format response with FQL guide for search errors or empty results ONLY.

        Use this helper when the FQL filter itself may be the issue:
        - Empty results: User may need to refine their filter
        - Search errors: Likely FQL syntax issues

        Do NOT use for downstream errors (e.g., fetching details after valid IDs)
        or success cases - those should return results directly.

        Args:
            error_or_empty: Empty list or list containing single error dict
            filter_used: The FQL filter string that was used (can be None)
            fql_documentation: Module-specific FQL documentation constant

        Returns:
            Dict with results, filter_used, fql_guide, and contextual hint
        """
        is_error = error_or_empty and self._is_error(error_or_empty[0])
        return {
            "results": error_or_empty,
            "filter_used": filter_used,
            "fql_guide": fql_documentation,
            "hint": "Filter error occurred. Review the FQL guide above to correct your query syntax."
            if is_error
            else "No results matched your filter. Review the FQL guide above to refine your query.",
        }
