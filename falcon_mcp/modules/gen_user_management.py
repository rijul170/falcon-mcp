"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `user_management` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenUserManagementModule(GeneratedModuleBase):
    """Generated tools for the Falcon `user_management` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.combined_user_roles_v2, name="combined_user_roles_v2")
        self._add_tool(server=server, method=self.get_available_role_ids, name="get_available_role_ids")
        self._add_tool(server=server, method=self.get_roles, name="get_roles")
        self._add_tool(server=server, method=self.get_user_role_ids, name="get_user_role_ids")
        self._add_tool(server=server, method=self.retrieve_emails_by_cid, name="retrieve_emails_by_cid")
        self._add_tool(server=server, method=self.retrieve_user, name="retrieve_user")
        self._add_tool(server=server, method=self.retrieve_user_uuid, name="retrieve_user_uuid")
        self._add_tool(server=server, method=self.retrieve_user_uui_ds_by_cid, name="retrieve_user_uui_ds_by_cid")
        self._add_tool(server=server, method=self.retrieve_user_user_management, name="retrieve_user_user_management")
        self._add_tool(server=server, method=self.create_user_user_management, name="create_user_user_management", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.grant_user_role_ids, name="grant_user_role_ids", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_user_user_management, name="update_user_user_management", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_user_user_management, name="delete_user_user_management", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.revoke_user_role_ids, name="revoke_user_role_ids", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_roles_getv2, name="entities_roles_getv2", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def combined_user_roles_v2(
        self,
        user_uuid: str = Field(description="User UUID to get available roles for."),
        cid: str | None = Field(default=None, description="Customer ID to get grants for. Empty CID would result in Role IDs for user against current CID in view."),
        direct_only: bool | None = Field(default=None, description="Specifies if to request direct Only role grants or all role grants between user and CID (specified in query params)"),
        filter: str | None = Field(default=None, description="Filter using a query in Falcon Query Language (FQL). Supported filters: expires_at, role_id, role_name"),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        limit: int | None = Field(default=None, description="The maximum records to return. [1-500]"),
        sort: str | None = Field(default=None, description="The property to sort by"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get User Grant(s). This endpoint lists both direct as well as flight control grants between a User and a Customer."""
        return self._call(operation="CombinedUserRolesV2", query_params={"user_uuid": user_uuid, "cid": cid, "direct_only": direct_only, "filter": filter, "offset": offset, "limit": limit, "sort": sort}, error_message="CombinedUserRolesV2 failed", member_cid=member_cid)

    def create_user_user_management(
        self,
        body: dict = Field(description="Request JSON body for `CreateUser` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deprecated : Please use createUserV1. Create a new user. After creating a user, assign one or more roles with GrantUserRoleIds"""
        return self._call(operation="CreateUser", query_params=None, body_params=body, error_message="CreateUser failed", member_cid=member_cid)

    def delete_user_user_management(
        self,
        user_uuid: str = Field(description="ID of a user. Find a user's ID from queryUserV1."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deprecated : Please use deleteUserV1. Delete a user permanently"""
        return self._call(operation="DeleteUser", query_params={"user_uuid": user_uuid}, error_message="DeleteUser failed", member_cid=member_cid)

    def get_available_role_ids(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deprecated : Please use queriesRolesV1. Show role IDs for all roles available in your customer account. For more information on each role, provide the role ID to entitiesRolesV1."""
        return self._call(operation="GetAvailableRoleIds", query_params=None, error_message="GetAvailableRoleIds failed", member_cid=member_cid)

    def get_roles(
        self,
        ids: list[str] = Field(description="ID of a role. Find a role ID from GetAvailableRoleIds or queriesRolesV1."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deprecated : Please use entitiesRolesV1. Get info about a role"""
        return self._call(operation="GetRoles", query_params={"ids": ids}, error_message="GetRoles failed", member_cid=member_cid)

    def get_user_role_ids(
        self,
        user_uuid: str = Field(description="ID of a user. Find a user's ID from queryUserV1."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deprecated : Please use combinedUserRolesV1. Show role IDs of roles assigned to a user. For more information on each role, provide the role ID to entitiesRolesV1."""
        return self._call(operation="GetUserRoleIds", query_params={"user_uuid": user_uuid}, error_message="GetUserRoleIds failed", member_cid=member_cid)

    def grant_user_role_ids(
        self,
        user_uuid: str = Field(description="ID of a user. Find a user's ID from queryUserV1."),
        body: dict = Field(description="Request JSON body for `GrantUserRoleIds` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deprecated : Please use userRolesActionV1. Assign one or more roles to a user"""
        return self._call(operation="GrantUserRoleIds", query_params={"user_uuid": user_uuid}, body_params=body, error_message="GrantUserRoleIds failed", member_cid=member_cid)

    def retrieve_emails_by_cid(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deprecated : Please use retrieveUsersGETV1. List the usernames (usually an email address) for all users in your customer account"""
        return self._call(operation="RetrieveEmailsByCID", query_params=None, error_message="RetrieveEmailsByCID failed", member_cid=member_cid)

    def retrieve_user(
        self,
        ids: list[str] = Field(description="ID of a user. Find a user's ID from queryUserV1."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deprecated : Please use retrieveUsersGETV1. Get info about a user"""
        return self._call(operation="RetrieveUser", query_params={"ids": ids}, error_message="RetrieveUser failed", member_cid=member_cid)

    def retrieve_user_uuid(
        self,
        uid: list[str] = Field(description="A username. This is usually the user's email address, but may vary based on your configuration."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deprecated : Please use queryUserV1. Get a user's ID by providing a username (usually an email address)"""
        return self._call(operation="RetrieveUserUUID", query_params={"uid": uid}, error_message="RetrieveUserUUID failed", member_cid=member_cid)

    def retrieve_user_uui_ds_by_cid(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deprecated : Please use queryUserV1. List user IDs for all users in your customer account. For more information on each user, provide the user ID to queryUserV1."""
        return self._call(operation="RetrieveUserUUIDsByCID", query_params=None, error_message="RetrieveUserUUIDsByCID failed", member_cid=member_cid)

    def revoke_user_role_ids(
        self,
        user_uuid: str = Field(description="ID of a user. Find a user's ID from queryUserV1."),
        ids: list[str] = Field(description="One or more role IDs to revoke. Find a role's ID from queriesRolesV1."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deprecated : Please use userRolesActionV1. Revoke one or more roles from a user"""
        return self._call(operation="RevokeUserRoleIds", query_params={"user_uuid": user_uuid, "ids": ids}, error_message="RevokeUserRoleIds failed", member_cid=member_cid)

    def update_user_user_management(
        self,
        user_uuid: str = Field(description="ID of a user. Find a user's ID from queryUserV1."),
        body: dict = Field(description="Request JSON body for `UpdateUser` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deprecated : Please use updateUserV1. Modify an existing user's first or last name"""
        return self._call(operation="UpdateUser", query_params={"user_uuid": user_uuid}, body_params=body, error_message="UpdateUser failed", member_cid=member_cid)

    def entities_roles_getv2(
        self,
        body: dict = Field(description="Request JSON body for `entitiesRolesGETV2` per the CrowdStrike API schema (required)."),
        cid: str | None = Field(default=None, description="Customer ID to get available roles for. Empty CID would result in Role IDs for current CID in view."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get info about a role"""
        return self._call(operation="entitiesRolesGETV2", query_params={"cid": cid}, body_params=body, error_message="entitiesRolesGETV2 failed", member_cid=member_cid)

    def retrieve_user_user_management(
        self,
        ids: list[str] = Field(description="ID of a user. Find a user's ID from queryUserV1."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Deprecated : Please use retrieveUsersGETV1. Get info about a user"""
        return self._call(operation="retrieveUser", query_params={"ids": ids}, error_message="retrieveUser failed", member_cid=member_cid)
