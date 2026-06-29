"""
Users module for Falcon MCP Server.

Provides tools for searching users and managing role assignments.
"""

from typing import Any

from mcp.server import FastMCP
from mcp.server.fastmcp.resources import TextResource
from mcp.types import ToolAnnotations
from pydantic import AnyUrl, Field

from falcon_mcp.common.errors import _format_error_response
from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule
from falcon_mcp.resources.users import SEARCH_USERS_FQL_DOCUMENTATION

logger = get_logger(__name__)

WRITE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True,
)


class UsersModule(BaseModule):
    """Module for CrowdStrike Falcon user and role management."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.search_users, name="search_users")
        self._add_tool(server=server, method=self.get_user_details, name="get_user_details")
        self._add_tool(server=server, method=self.list_user_roles, name="list_user_roles")
        self._add_tool(server=server, method=self.list_available_roles, name="list_available_roles")
        self._add_tool(
            server=server, method=self.grant_user_roles, name="grant_user_roles",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.revoke_user_roles, name="revoke_user_roles",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.create_user, name="create_user",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.update_user, name="update_user",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.delete_user, name="delete_user",
            annotations=ToolAnnotations(
                readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True,
            ),
        )
        self._add_tool(
            server=server, method=self.perform_user_action, name="perform_user_action",
            annotations=WRITE_ANNOTATIONS,
        )

    def register_resources(self, server: FastMCP) -> None:
        self._add_resource(server, TextResource(
            uri=AnyUrl("falcon://users/search/fql-guide"),
            name="falcon_search_users_fql_guide",
            description="FQL filter guide for the `falcon_search_users` tool.",
            text=SEARCH_USERS_FQL_DOCUMENTATION,
        ))

    def search_users(
        self,
        filter: str | None = Field(default=None, description="FQL filter; see `falcon://users/search/fql-guide`."),
        limit: int = Field(default=100, ge=1, le=500, description="Max records (max 500)."),
        offset: int | None = Field(default=None, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression (e.g. last_login_at.desc)."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search Falcon console users and return full user details."""
        uuids = self._base_search_api_call(
            operation="queryUserV1",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search users",
        )
        if self._is_error(uuids):
            if filter:
                return self._format_fql_error_response([uuids], filter, SEARCH_USERS_FQL_DOCUMENTATION)
            return [uuids]
        if not uuids:
            if filter:
                return self._format_fql_error_response([], filter, SEARCH_USERS_FQL_DOCUMENTATION)
            return []

        details = self._base_get_by_ids(operation="retrieveUsersGETV1", ids=uuids, id_key="ids")
        if self._is_error(details):
            return [details]
        return details

    def get_user_details(
        self,
        uuids: list[str] = Field(description="User UUIDs to retrieve details for."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Retrieve full user details for the given user UUIDs."""
        if not uuids:
            return []
        return self._base_get_by_ids(operation="retrieveUsersGETV1", ids=uuids, id_key="ids")

    def list_user_roles(
        self,
        user_uuid: str = Field(description="User UUID."),
        cid: str | None = Field(default=None, description="Optional customer ID."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List the role IDs granted to a user."""
        params: dict[str, Any] = {"user_uuid": user_uuid}
        if cid:
            params["cid"] = cid
        result = self._base_search_api_call(
            operation="combinedUserRolesV1",
            search_params=params,
            error_message="Failed to list user roles",
        )
        if self._is_error(result):
            return [result]
        return result

    def list_available_roles(
        self,
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List every role available in this CID, with descriptions."""
        ids = self._base_search_api_call(
            operation="queriesRolesV1",
            search_params={},
            error_message="Failed to list available role IDs",
        )
        if self._is_error(ids):
            return [ids]
        if not ids:
            return []
        details = self._base_get_by_ids(operation="entitiesRolesV1", ids=ids, use_params=True)
        if self._is_error(details):
            return [details]
        return details

    def grant_user_roles(
        self,
        user_uuid: str = Field(description="User UUID to grant roles to."),
        role_ids: list[str] = Field(description="Role IDs to grant."),
        cid: str = Field(
            description="Customer ID (CID) of the tenant the user lives in. Required by the API.",
        ),
    ) -> list[dict[str, Any]]:
        """Grant one or more roles to a user (uses userRolesActionV1)."""
        if not role_ids:
            return [_format_error_response("`role_ids` is required for grant.", operation="userRolesActionV1")]
        body = {
            "action": "grant",
            "cid": cid,
            "role_ids": role_ids,
            "uuid": user_uuid,
        }
        result = self._base_query_api_call(
            operation="userRolesActionV1",
            body_params=body,
            error_message="Failed to grant user roles",
        )
        if self._is_error(result):
            return [result]
        return result

    def revoke_user_roles(
        self,
        user_uuid: str = Field(description="User UUID to revoke roles from."),
        role_ids: list[str] = Field(description="Role IDs to revoke."),
        cid: str = Field(
            description="Customer ID (CID) of the tenant the user lives in. Required by the API.",
        ),
    ) -> list[dict[str, Any]]:
        """Revoke one or more roles from a user (uses userRolesActionV1)."""
        if not role_ids:
            return [_format_error_response("`role_ids` is required for revoke.", operation="userRolesActionV1")]
        body = {
            "action": "revoke",
            "cid": cid,
            "role_ids": role_ids,
            "uuid": user_uuid,
        }
        result = self._base_query_api_call(
            operation="userRolesActionV1",
            body_params=body,
            error_message="Failed to revoke user roles",
        )
        if self._is_error(result):
            return [result]
        return result

    def create_user(
        self,
        uid: str = Field(
            description="The user's email address. This becomes their username for console login.",
        ),
        first_name: str = Field(description="User's first name."),
        last_name: str = Field(description="User's last name."),
        cid: str | None = Field(
            default=None,
            description="Child CID to create the user in. Leave unset to create in the current (parent) CID.",
        ),
        password: str | None = Field(
            default=None,
            description="Initial password. Omit to send the user an activation email — recommended when SSO is enabled.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Create a new Falcon console user.

        After creation, use `falcon_grant_user_roles` to assign roles. If `password` is
        omitted, an activation email is sent to the user's address so they can set their
        own password.
        """
        body: dict[str, Any] = {
            "uid": uid,
            "first_name": first_name,
            "last_name": last_name,
        }
        if cid is not None:
            body["cid"] = cid
        if password is not None:
            body["password"] = password

        result = self._base_query_api_call(
            operation="createUserV1",
            body_params=body,
            error_message="Failed to create user",
        )
        if self._is_error(result):
            return [result]
        return result

    def update_user(
        self,
        user_uuid: str = Field(
            description="UUID of the user to update. Obtain from `falcon_search_users` or `falcon_get_user_details`.",
        ),
        first_name: str | None = Field(default=None, description="Updated first name."),
        last_name: str | None = Field(default=None, description="Updated last name."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Update a user's first or last name."""
        body: dict[str, Any] = {}
        if first_name is not None:
            body["first_name"] = first_name
        if last_name is not None:
            body["last_name"] = last_name

        result = self._base_query_api_call(
            operation="updateUserV1",
            query_params={"user_uuid": user_uuid},
            body_params=body,
            error_message="Failed to update user",
        )
        if self._is_error(result):
            return [result]
        return result

    def delete_user(
        self,
        user_uuid: str = Field(
            description="UUID of the user to permanently delete. Obtain from `falcon_search_users`.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Permanently delete a Falcon console user.

        IMPORTANT: This action is irreversible. The user will lose all console access immediately.
        """
        result = self._base_query_api_call(
            operation="deleteUserV1",
            query_params={"user_uuid": user_uuid},
            error_message="Failed to delete user",
        )
        if self._is_error(result):
            return [result]
        return result

    def perform_user_action(
        self,
        user_uuids: list[str] = Field(
            description="UUIDs of users to act on. Obtain from `falcon_search_users`.",
        ),
        action_name: str = Field(
            description="Action to perform: `reset_2fa` (remove two-factor auth) or `reset_password` (trigger password reset email).",
            examples=["reset_2fa", "reset_password"],
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Apply an administrative action to one or more users.

        Use `reset_2fa` to remove two-factor authentication requirements (e.g., when a user
        loses their authenticator device). Use `reset_password` to trigger a password reset email.
        """
        result = self._base_query_api_call(
            operation="userActionV1",
            body_params={
                "action": {"action_name": action_name},
                "ids": user_uuids,
            },
            error_message="Failed to perform user action",
        )
        if self._is_error(result):
            return [result]
        return result
