"""Shared base for auto-generated Falcon API modules.

The class name intentionally ends in ``Base`` (not ``Module``) and lives outside
the modules package so the registry's ``*Module`` auto-discovery never registers
it directly.
"""

from typing import Any

from falcon_mcp.modules.base import BaseModule


class GeneratedModuleBase(BaseModule):
    """Base for generated modules: thin wrapper over the standard query helper."""

    def _call(
        self,
        operation: str,
        *,
        query_params: dict[str, Any] | None = None,
        body_params: dict[str, Any] | None = None,
        path_params: dict[str, Any] | None = None,
        error_message: str = "Operation failed",
        member_cid: str | None = None,
    ) -> list[dict[str, Any]] | dict[str, Any]:
        # Returns the raw helper result. On error this is the error dict itself
        # (not a single-element list), matching the contract used by the hand-
        # written modules and the ``_base_*`` helpers in BaseModule.
        return self._base_query_api_call(
            operation=operation,
            query_params=query_params,
            body_params=body_params,
            path_params=path_params,
            error_message=error_message,
            member_cid=member_cid,
        )
