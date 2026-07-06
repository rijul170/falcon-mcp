"""
Falcon API Client for MCP Server

This module provides the Falcon API client and authentication utilities for the Falcon MCP server.
"""

import os
import platform
import sys
import time
from importlib.metadata import PackageNotFoundError, version
from typing import Any

# Import the APIHarnessV2 from FalconPy
from falconpy import APIHarnessV2  # type: ignore[import-untyped]

from falcon_mcp.common.logging import get_logger

logger = get_logger(__name__)


class FalconClient:
    """Client for interacting with the CrowdStrike Falcon API."""

    def __init__(
        self,
        base_url: str | None = None,
        debug: bool = False,
        user_agent_comment: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        member_cid: str | None = None,
    ):
        """Initialize the Falcon client.

        Args:
            base_url: Falcon API base URL (defaults to FALCON_BASE_URL env var)
            debug: Enable debug logging
            user_agent_comment: Additional information to include in the User-Agent comment section
            client_id: Falcon API Client ID (defaults to FALCON_CLIENT_ID env var)
            client_secret: Falcon API Client Secret (defaults to FALCON_CLIENT_SECRET env var)
            member_cid: Child CID for Flight Control (MSSP) support (defaults to FALCON_MEMBER_CID env var)
        """
        # Get credentials from parameters or environment variables (parameters take precedence)
        self.client_id = client_id or os.environ.get("FALCON_CLIENT_ID")
        self.client_secret = client_secret or os.environ.get("FALCON_CLIENT_SECRET")
        self.base_url = base_url or os.environ.get(
            "FALCON_BASE_URL", "https://api.crowdstrike.com"
        )
        self.debug = debug
        self.user_agent_comment = user_agent_comment or os.environ.get(
            "FALCON_MCP_USER_AGENT_COMMENT"
        )
        self.member_cid = member_cid or os.environ.get("FALCON_MEMBER_CID")

        if not self.client_id or not self.client_secret:
            raise ValueError(
                "Falcon API credentials not provided. Either pass client_id and client_secret "
                "parameters or set FALCON_CLIENT_ID and FALCON_CLIENT_SECRET environment variables."
            )

        # Build APIHarnessV2 initialization parameters
        api_params = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "base_url": self.base_url,
            "debug": debug,
            "user_agent": self.get_user_agent(),
        }

        # Only include member_cid if it's provided
        if self.member_cid:
            api_params["member_cid"] = self.member_cid

        # Initialize the Falcon API client using APIHarnessV2
        self.client = APIHarnessV2(**api_params)

        # Cache of per-member-CID child clients, lazily created on first use
        self._child_clients: dict[str, APIHarnessV2] = {}

        logger.debug("Initialized Falcon client with base URL: %s", self.base_url)
        if self.member_cid:
            logger.debug("Flight Control member_cid: %s", self.member_cid)

    def authenticate(self) -> bool:
        """Authenticate with the Falcon API.

        Returns:
            bool: True if authentication was successful
        """
        result: bool = self.client.login()
        return result

    def is_authenticated(self) -> bool:
        """Check if the client is authenticated.

        Returns:
            bool: True if the client is authenticated
        """
        result: bool = self.client.token_valid
        return result

    def command(self, operation: str, **kwargs: Any) -> dict[str, Any]:
        """Execute a Falcon API command against the default (parent or startup-scoped) client."""
        result: dict[str, Any] = self.client.command(operation, **kwargs)
        return result

    def command_for(
        self, operation: str, member_cid: str | None = None, **kwargs: Any
    ) -> dict[str, Any]:
        """Execute a Falcon API command, optionally scoped to a child tenant.

        When member_cid is None, delegates to the default client (parent or startup
        member_cid). When member_cid is provided, uses a cached child-scoped client,
        creating and authenticating it on first use.

        Automatically retries up to 3 times with exponential backoff (1s, 2s, 4s)
        on HTTP 429 rate-limit responses.
        """
        last_response: dict[str, Any] | None = None
        for attempt in range(3):
            if member_cid is None:
                response = self.command(operation, **kwargs)
            else:
                response = self._get_child_client(member_cid).command(operation, **kwargs)
            if isinstance(response, dict) and response.get("status_code") == 429:
                last_response = response
                if attempt < 2:
                    delay = 2 ** attempt  # 1s, 2s, 4s
                    logger.warning(
                        "Rate limit (429) on operation %s, retrying in %ds (attempt %d/3)",
                        operation,
                        delay,
                        attempt + 1,
                    )
                    time.sleep(delay)
                    continue
            else:
                self._audit_mutation(operation, member_cid, kwargs, response)
                return response
        # All retries exhausted — return the last 429 response
        assert last_response is not None
        self._audit_mutation(operation, member_cid, kwargs, last_response)
        return last_response

    def _audit_mutation(
        self,
        operation: str,
        member_cid: str | None,
        kwargs: dict[str, Any],
        response: Any,
    ) -> None:
        """Append a tamper-evident JSONL record for every mutating API call.

        Reads (HTTP GET) are skipped. The trail is the system of record for changes
        made via the MCP when no web console is used. Target identifiers (query
        parameters) are recorded; request bodies are recorded by key only to avoid
        persisting sensitive configuration payloads. Override the path with
        FALCON_MCP_AUDIT_LOG (default: ~/.falcon-mcp/audit.jsonl).
        """
        # Lazily build the operation -> HTTP method map from the harness endpoints.
        if not hasattr(self, "_op_method"):
            try:
                self._op_method = {
                    c[0]: c[1] for c in self.client.commands if isinstance(c, (list, tuple)) and len(c) >= 2
                }
            except Exception:  # noqa: BLE001
                self._op_method = {}
        method = self._op_method.get(operation, "")
        if method not in ("POST", "PATCH", "PUT", "DELETE"):
            return  # reads are not audited

        import datetime
        import json

        body = kwargs.get("body")
        record = {
            "ts": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "region": self.base_url,
            "member_cid": member_cid or self.member_cid,
            "operation": operation,
            "method": method,
            "parameters": kwargs.get("parameters") or {},
            "body_keys": sorted(body.keys()) if isinstance(body, dict) else None,
            "status_code": response.get("status_code") if isinstance(response, dict) else None,
        }
        logger.info(
            "AUDIT mutation: %s %s region=%s member_cid=%s status=%s",
            method, operation, self.base_url, record["member_cid"], record["status_code"],
        )
        path = os.environ.get("FALCON_MCP_AUDIT_LOG") or os.path.expanduser("~/.falcon-mcp/audit.jsonl")
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "a", encoding="utf-8") as fh:
                fh.write(json.dumps(record) + "\n")
        except OSError as exc:
            logger.warning("Failed to write audit log to %s: %s", path, exc)

    def _get_child_client(self, member_cid: str) -> APIHarnessV2:
        """Return a cached APIHarnessV2 scoped to a specific child CID."""
        if member_cid not in self._child_clients:
            child: APIHarnessV2 = APIHarnessV2(
                client_id=self.client_id,
                client_secret=self.client_secret,
                base_url=self.base_url,
                member_cid=member_cid,
                debug=self.debug,
                user_agent=self.get_user_agent(),
            )
            child.login()
            self._child_clients[member_cid] = child
            logger.debug("Created child client for member_cid: %s", member_cid)
        return self._child_clients[member_cid]

    def get_user_agent(self) -> str:
        """Get RFC-compliant user agent string for API requests.

        Returns:
            str: User agent string in RFC format "falcon-mcp/VERSION (comment; falconpy/VERSION; Python/VERSION; Platform/VERSION)"
        """
        # Get falcon-mcp version
        falcon_mcp_version = get_version()

        # Get Python version
        python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"

        # Get platform information
        platform_info = f"{platform.system()}/{platform.release()}"

        # Get FalconPy version
        try:
            falconpy_version = version("crowdstrike-falconpy")
        except PackageNotFoundError:
            falconpy_version = "unknown"
            logger.debug("crowdstrike-falconpy package version not found")

        # Build comment section components (RFC-compliant format)
        comment_parts = []
        if self.user_agent_comment:
            comment_parts.append(self.user_agent_comment.strip())
        comment_parts.extend(
            [f"falconpy/{falconpy_version}", f"Python/{python_version}", platform_info]
        )

        return f"falcon-mcp/{falcon_mcp_version} ({'; '.join(comment_parts)})"

    def get_headers(self) -> dict[str, str]:
        """Get authentication headers for API requests.

        This method returns the authentication headers from the underlying Falcon API client,
        which can be used for custom HTTP requests or advanced integration scenarios.

        Returns:
            dict[str, str]: Authentication headers including the bearer token
        """
        headers: dict[str, str] = self.client.auth_headers
        return headers


def get_version() -> str:
    """Get falcon-mcp version with multiple fallback methods.

    This function tries multiple methods to determine the version:
    1. importlib.metadata (works when package is properly installed)
    2. pyproject.toml (works in development/Docker environments)
    3. Hardcoded fallback

    Returns:
        str: The version string
    """
    # Try importlib.metadata first (works when properly installed)
    try:
        return version("falcon-mcp-extended")
    except PackageNotFoundError:
        logger.debug(
            "falcon-mcp-extended package not found via importlib.metadata, trying pyproject.toml"
        )

    # Try reading from pyproject.toml (works in development/Docker)
    try:
        import pathlib
        import tomllib  # Python 3.11+

        # Look for pyproject.toml in current directory and parent directories
        current_path = pathlib.Path(__file__).parent
        for _ in range(3):  # Check up to 3 levels up
            pyproject_path = current_path / "pyproject.toml"
            if pyproject_path.exists():
                with open(pyproject_path, "rb") as f:
                    data = tomllib.load(f)
                    version_str: str = data["project"]["version"]
                    logger.debug(
                        "Found version %s in pyproject.toml at %s",
                        version_str,
                        pyproject_path,
                    )
                    return version_str
            current_path = current_path.parent

        logger.debug("pyproject.toml not found in current or parent directories")
    except (KeyError, ImportError, OSError, TypeError) as e:
        logger.debug("Failed to read version from pyproject.toml: %s", e)

    # Final fallback
    fallback_version = "0.1.0"
    logger.debug("Using fallback version: %s", fallback_version)
    return fallback_version
