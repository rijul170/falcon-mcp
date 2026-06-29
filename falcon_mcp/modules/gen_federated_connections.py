"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `federated_connections` API service collection.

NOTE: This service collection is NOT yet present in FalconPy's endpoint registry.
All operations therefore use the APIHarnessV2 `override` kwarg
(format: 'METHOD,/path') to bypass the registry lookup.

API docs: https://developer.crowdstrike.com/api-reference/collections/federated-connections/
Required scope: Ngsiem Federated Connection: WRITE (all three operations)
"""

from typing import Any

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.errors import handle_api_response
from falcon_mcp.common.logging import get_logger
from falcon_mcp.common.utils import prepare_api_parameters
from falcon_mcp.common.generated_base import GeneratedModuleBase

logger = get_logger(__name__)

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)

_ENDPOINT = "/ngsiem/entities/federated-connections-config/v1"


class GenFederatedConnectionsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `federated_connections` collection.

    All three operations share the same endpoint path and differ only in HTTP method.
    Because FalconPy's endpoint registry does not yet include this service collection,
    calls go through the Uber class ``override`` mechanism.
    """

    # ------------------------------------------------------------------
    # Internal helper — uses the Uber class override to bypass the
    # FalconPy operation registry for endpoints not yet bundled in the
    # installed FalconPy release.
    # ------------------------------------------------------------------
    def _override_call(
        self,
        method: str,
        path: str,
        *,
        query_params: dict[str, Any] | None = None,
        body_params: dict[str, Any] | None = None,
        operation_label: str = "operation",
        member_cid: str | None = None,
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Issue an API call via the Uber class ``override`` kwarg.

        Args:
            method: HTTP method string (GET, POST, PATCH, DELETE, …).
            path: Absolute API path, e.g. ``/ngsiem/entities/…/v1``.
            query_params: Dict of query-string parameters (None values stripped).
            body_params: Dict of body parameters (None values stripped).
            operation_label: Human-readable label used in error messages.
            member_cid: Optional child CID for MSSP tenant scoping.

        Returns:
            Parsed API response resources list, or an error dict.
        """
        call_args: dict[str, Any] = {"override": f"{method.upper()},{path}"}

        if query_params:
            call_args["parameters"] = prepare_api_parameters(query_params)

        if body_params:
            call_args["body"] = prepare_api_parameters(body_params)

        logger.debug("override_call %s %s member_cid=%s args=%s", method, path, member_cid, call_args)

        response = self.client.command_for(operation_label, member_cid=member_cid, **call_args)

        return handle_api_response(
            response,
            operation=operation_label,
            error_message=f"{operation_label} failed",
            default_result=[],
        )

    # ------------------------------------------------------------------
    # Tool registration
    # ------------------------------------------------------------------
    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.post_federated_connections_config, name="post_federated_connections_config", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.patch_federated_connections_config, name="patch_federated_connections_config", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_federated_connections_config, name="delete_federated_connections_config", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    # ------------------------------------------------------------------
    # Operations
    # ------------------------------------------------------------------
    def post_federated_connections_config(
        self,
        cluster_url: str = Field(description="URL of the external cluster to federate."),
        connection_id: str = Field(description="ID of the federated connection to configure."),
        view_token: str = Field(description="Token for accessing the external cluster."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create configuration for a federated connection.

        Endpoint: POST /ngsiem/entities/federated-connections-config/v1
        Required scope: Ngsiem Federated Connection: WRITE
        """
        return self._override_call(
            "POST",
            _ENDPOINT,
            body_params={
                "cluster_url": cluster_url,
                "connection_id": connection_id,
                "view_token": view_token,
            },
            operation_label="PostFederatedConnectionsConfig",
            member_cid=member_cid,
        )

    def patch_federated_connections_config(
        self,
        connection_id: str = Field(description="Connection ID to update configuration for."),
        cluster_url: str | None = Field(default=None, description="Updated URL of the external cluster."),
        view_token: str | None = Field(default=None, description="Updated token for accessing the external cluster."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update configuration for a federated connection.

        Endpoint: PATCH /ngsiem/entities/federated-connections-config/v1
        Required scope: Ngsiem Federated Connection: WRITE
        At least one of ``cluster_url`` or ``view_token`` should be supplied.
        """
        return self._override_call(
            "PATCH",
            _ENDPOINT,
            query_params={"connection_id": connection_id},
            body_params={"cluster_url": cluster_url, "view_token": view_token},
            operation_label="PatchFederatedConnectionsConfig",
            member_cid=member_cid,
        )

    def delete_federated_connections_config(
        self,
        connection_id: str = Field(description="Connection ID to delete configuration for."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete configuration for a federated connection.

        Endpoint: DELETE /ngsiem/entities/federated-connections-config/v1
        Required scope: Ngsiem Federated Connection: WRITE
        """
        return self._override_call(
            "DELETE",
            _ENDPOINT,
            query_params={"connection_id": connection_id},
            operation_label="DeleteFederatedConnectionsConfig",
            member_cid=member_cid,
        )
