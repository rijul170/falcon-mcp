"""
Flight Control (MSSP) module for Falcon MCP Server

Provides tools for managing the MSSP tenant hierarchy: listing child accounts,
managing CID groups, user groups, and role assignments across tenants.

All operations target the parent MSSP account. No member_cid is applied — this
module is designed to run as the parent and manage the child estate.
"""

from typing import Any

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.errors import _format_error_response
from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule

logger = get_logger(__name__)

WRITE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False,
    destructiveHint=False,
    idempotentHint=False,
    openWorldHint=True,
)

DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False,
    destructiveHint=True,
    idempotentHint=True,
    openWorldHint=True,
)


class FlightControlModule(BaseModule):
    """Module for CrowdStrike Flight Control (MSSP) tenant hierarchy management."""

    def register_tools(self, server: FastMCP) -> None:
        # --- Child account read tools ---
        self._add_tool(server=server, method=self.list_child_accounts, name="list_child_accounts")
        self._add_tool(server=server, method=self.get_child_account_details, name="get_child_account_details")

        # --- CID group read tools ---
        self._add_tool(server=server, method=self.list_cid_groups, name="list_cid_groups")
        self._add_tool(server=server, method=self.get_cid_group_details, name="get_cid_group_details")
        self._add_tool(server=server, method=self.list_cid_group_members, name="list_cid_group_members")
        self._add_tool(server=server, method=self.find_cid_group_for_tenant, name="find_cid_group_for_tenant")

        # --- User group read tools ---
        self._add_tool(server=server, method=self.list_user_groups, name="list_user_groups")
        self._add_tool(server=server, method=self.get_user_group_details, name="get_user_group_details")
        self._add_tool(server=server, method=self.list_user_group_members, name="list_user_group_members")
        self._add_tool(server=server, method=self.find_user_group_for_user, name="find_user_group_for_user")

        # --- MSSP role read tools ---
        self._add_tool(server=server, method=self.list_mssp_roles, name="list_mssp_roles")

        # --- CID group write tools ---
        self._add_tool(
            server=server, method=self.create_cid_group, name="create_cid_group",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.update_cid_group, name="update_cid_group",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.delete_cid_groups, name="delete_cid_groups",
            annotations=DESTRUCTIVE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.add_cid_group_members, name="add_cid_group_members",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.remove_cid_group_members, name="remove_cid_group_members",
            annotations=WRITE_ANNOTATIONS,
        )

        # --- User group write tools ---
        self._add_tool(
            server=server, method=self.create_user_group, name="create_user_group",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.update_user_group, name="update_user_group",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.delete_user_groups, name="delete_user_groups",
            annotations=DESTRUCTIVE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.add_user_group_members, name="add_user_group_members",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.remove_user_group_members, name="remove_user_group_members",
            annotations=WRITE_ANNOTATIONS,
        )

        # --- MSSP role write tools ---
        self._add_tool(
            server=server, method=self.assign_mssp_role, name="assign_mssp_role",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.remove_mssp_roles, name="remove_mssp_roles",
            annotations=WRITE_ANNOTATIONS,
        )

    # -------------------------------------------------------------------------
    # Child account tools
    # -------------------------------------------------------------------------

    def list_child_accounts(
        self,
        filter: str | None = Field(
            default=None,
            description="FQL filter. Supported field: cid. Example: \"cid:'abc123'\"",
        ),
        limit: int = Field(default=20, ge=1, le=1000, description="Maximum records to return (max 1000)."),
        offset: int = Field(default=0, ge=0, description="Pagination offset."),
        sort: str = Field(
            default="last_modified_timestamp|desc",
            description="Sort order. Options: last_modified_timestamp|asc, last_modified_timestamp|desc",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List all child customer accounts (CIDs) linked under this MSSP parent.

        Returns child CID links. Use get_child_account_details to get full details
        for specific CIDs. This is the primary tool for enumerating your tenant estate.
        """
        child_ids = self._base_search_api_call(
            operation="queryChildren",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to list child accounts",
        )
        if self._is_error(child_ids):
            return [child_ids]
        if not child_ids:
            return []

        details = self._base_get_by_ids(
            operation="getChildren",
            ids=child_ids,
            id_key="ids",
            use_params=True,
        )
        if self._is_error(details):
            return [details]
        return details

    def get_child_account_details(
        self,
        child_cids: list[str] = Field(
            description="Child CID(s) to retrieve details for. Get these from list_child_accounts."
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Retrieve details for one or more specific child accounts by CID."""
        if not child_cids:
            return []
        details = self._base_get_by_ids(
            operation="getChildren",
            ids=child_cids,
            id_key="ids",
            use_params=True,
        )
        if self._is_error(details):
            return [details]
        return details

    # -------------------------------------------------------------------------
    # CID group tools
    # -------------------------------------------------------------------------

    def list_cid_groups(
        self,
        name: str | None = Field(default=None, description="Filter by group name (exact match lookup)."),
        limit: int = Field(default=20, ge=1, le=500, description="Maximum records to return."),
        offset: int = Field(default=0, ge=0, description="Pagination offset."),
        sort: str = Field(
            default="name|asc",
            description="Sort order. Options: name|asc, name|desc, last_modified_timestamp|asc, last_modified_timestamp|desc",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List CID groups (logical groupings of child tenants).

        CID groups let you apply policies, user access, and role assignments to
        multiple child tenants at once.
        """
        group_ids = self._base_search_api_call(
            operation="queryCIDGroups",
            search_params={"name": name, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to list CID groups",
        )
        if self._is_error(group_ids):
            return [group_ids]
        if not group_ids:
            return []

        details = self._base_get_by_ids(
            operation="getCIDGroupById",
            ids=group_ids,
            id_key="ids",
            use_params=True,
        )
        if self._is_error(details):
            return [details]
        return details

    def get_cid_group_details(
        self,
        cid_group_ids: list[str] = Field(description="CID group IDs to retrieve. Get from list_cid_groups."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Retrieve full details for one or more CID groups by ID."""
        if not cid_group_ids:
            return []
        details = self._base_get_by_ids(
            operation="getCIDGroupById",
            ids=cid_group_ids,
            id_key="ids",
            use_params=True,
        )
        if self._is_error(details):
            return [details]
        return details

    def list_cid_group_members(
        self,
        cid_group_ids: list[str] = Field(
            description="CID group IDs to get membership for. Get from list_cid_groups."
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List the child CIDs that belong to one or more CID groups."""
        if not cid_group_ids:
            return []
        result = self._base_get_by_ids(
            operation="getCIDGroupMembersBy",
            ids=cid_group_ids,
            id_key="ids",
            use_params=True,
        )
        if self._is_error(result):
            return [result]
        return result

    def find_cid_group_for_tenant(
        self,
        cid: str = Field(description="Child CID to look up. Returns the CID group(s) it belongs to."),
        limit: int = Field(default=20, ge=1, le=500, description="Maximum records to return."),
        offset: int = Field(default=0, ge=0, description="Pagination offset."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Find which CID group(s) a specific child tenant belongs to.

        Useful for auditing group membership or checking tenant assignment.
        """
        group_ids = self._base_search_api_call(
            operation="queryCIDGroupMembers",
            search_params={"cid": cid, "limit": limit, "offset": offset},
            error_message="Failed to find CID group for tenant",
        )
        if self._is_error(group_ids):
            return [group_ids]
        if not group_ids:
            return []

        details = self._base_get_by_ids(
            operation="getCIDGroupById",
            ids=group_ids,
            id_key="ids",
            use_params=True,
        )
        if self._is_error(details):
            return [details]
        return details

    # -------------------------------------------------------------------------
    # User group tools
    # -------------------------------------------------------------------------

    def list_user_groups(
        self,
        name: str | None = Field(default=None, description="Filter by user group name (exact match lookup)."),
        limit: int = Field(default=20, ge=1, le=500, description="Maximum records to return."),
        offset: int = Field(default=0, ge=0, description="Pagination offset."),
        sort: str = Field(
            default="name|asc",
            description="Sort order. Options: name|asc, name|desc, last_modified_timestamp|asc, last_modified_timestamp|desc",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List MSSP user groups.

        User groups define which operators/analysts have access to which CID groups
        and with what roles. Up to 500 user groups per MSSP parent.
        """
        group_ids = self._base_search_api_call(
            operation="queryUserGroups",
            search_params={"name": name, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to list user groups",
        )
        if self._is_error(group_ids):
            return [group_ids]
        if not group_ids:
            return []

        details = self._base_get_by_ids(
            operation="getUserGroupsByID",
            ids=group_ids,
            id_key="ids",
            use_params=True,
        )
        if self._is_error(details):
            return [details]
        return details

    def get_user_group_details(
        self,
        user_group_ids: list[str] = Field(description="User group IDs to retrieve. Get from list_user_groups."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Retrieve full details for one or more user groups by ID."""
        if not user_group_ids:
            return []
        details = self._base_get_by_ids(
            operation="getUserGroupsByID",
            ids=user_group_ids,
            id_key="ids",
            use_params=True,
        )
        if self._is_error(details):
            return [details]
        return details

    def list_user_group_members(
        self,
        user_group_ids: list[str] = Field(
            description="User group IDs to get membership for. Get from list_user_groups."
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List the user UUIDs that belong to one or more user groups."""
        if not user_group_ids:
            return []
        result = self._base_get_by_ids(
            operation="getUserGroupMembersByID",
            ids=user_group_ids,
            id_key="ids",
            use_params=True,
        )
        if self._is_error(result):
            return [result]
        return result

    def find_user_group_for_user(
        self,
        user_uuid: str = Field(description="User UUID to look up. Returns the user group(s) they belong to."),
        limit: int = Field(default=20, ge=1, le=500, description="Maximum records to return."),
        offset: int = Field(default=0, ge=0, description="Pagination offset."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Find which MSSP user group(s) a specific user belongs to.

        Useful for auditing user access or troubleshooting tenant visibility issues.
        """
        group_ids = self._base_search_api_call(
            operation="queryUserGroupMembers",
            search_params={"user_uuid": user_uuid, "limit": limit, "offset": offset},
            error_message="Failed to find user group for user",
        )
        if self._is_error(group_ids):
            return [group_ids]
        if not group_ids:
            return []

        details = self._base_get_by_ids(
            operation="getUserGroupsByID",
            ids=group_ids,
            id_key="ids",
            use_params=True,
        )
        if self._is_error(details):
            return [details]
        return details

    # -------------------------------------------------------------------------
    # MSSP role tools
    # -------------------------------------------------------------------------

    def list_mssp_roles(
        self,
        user_group_id: str | None = Field(
            default=None,
            description="Filter by user group ID. At least one of user_group_id or cid_group_id is recommended.",
        ),
        cid_group_id: str | None = Field(
            default=None,
            description="Filter by CID group ID.",
        ),
        role_id: str | None = Field(
            default=None,
            description="Filter by a specific role ID.",
        ),
        limit: int = Field(default=20, ge=1, le=500, description="Maximum records to return."),
        offset: int = Field(default=0, ge=0, description="Pagination offset."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List MSSP role assignments linking user groups to CID groups.

        Role assignment IDs are in the format <user_group_id>:<cid_group_id>.
        Provide at least user_group_id or cid_group_id for useful results.
        """
        if not user_group_id and not cid_group_id:
            return [_format_error_response(
                "Provide at least one of `user_group_id` or `cid_group_id` to filter results.",
                operation="queryRoles",
            )]

        assignment_ids = self._base_search_api_call(
            operation="queryRoles",
            search_params={
                "user_group_id": user_group_id,
                "cid_group_id": cid_group_id,
                "role_id": role_id,
                "limit": limit,
                "offset": offset,
            },
            error_message="Failed to list MSSP role assignments",
        )
        if self._is_error(assignment_ids):
            return [assignment_ids]
        if not assignment_ids:
            return []

        details = self._base_get_by_ids(
            operation="getRolesByID",
            ids=assignment_ids,
            id_key="ids",
            use_params=True,
        )
        if self._is_error(details):
            return [details]
        return details

    # -------------------------------------------------------------------------
    # CID group write operations
    # -------------------------------------------------------------------------

    def create_cid_group(
        self,
        name: str = Field(description="CID group name. Must be unique. Maximum 500 groups per MSSP parent."),
        description: str | None = Field(default=None, description="Optional description."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Create a new CID group for grouping child tenants.

        After creating, use add_cid_group_members to add child CIDs,
        then assign_mssp_role to grant user groups access.
        """
        resource: dict[str, Any] = {"name": name}
        if description:
            resource["description"] = description

        result = self._base_query_api_call(
            operation="createCIDGroups",
            body_params={"resources": [resource]},
            error_message="Failed to create CID group",
        )
        if self._is_error(result):
            return [result]
        return result

    def update_cid_group(
        self,
        cid_group_id: str = Field(description="CID group ID to update."),
        name: str = Field(description="New name for the group. Required by the API even if unchanged."),
        description: str | None = Field(
            default=None,
            description="New description. Empty string clears the existing description.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Update a CID group's name or description. Members are unaffected."""
        resource: dict[str, Any] = {"cid_group_id": cid_group_id, "name": name}
        if description is not None:
            resource["description"] = description

        result = self._base_query_api_call(
            operation="updateCIDGroups",
            body_params={"resources": [resource]},
            error_message="Failed to update CID group",
        )
        if self._is_error(result):
            return [result]
        return result

    def delete_cid_groups(
        self,
        cid_group_ids: list[str] = Field(description="CID group IDs to delete. Members are NOT deleted."),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID to scope this call to a specific child tenant. Leave unset to use the parent MSSP account scope.",
        ),
    ) -> dict[str, Any]:
        """Delete one or more CID groups by ID.

        Child CIDs that were members are not deleted — only the group container is removed.
        Any role assignments referencing these groups are also removed.
        """
        if not cid_group_ids:
            return _format_error_response("`cid_group_ids` is required.", operation="deleteCIDGroups")

        response = self.client.command_for(
            "deleteCIDGroups",
            member_cid=member_cid,
            parameters={"cid_group_ids": cid_group_ids},
        )
        from falcon_mcp.common.errors import handle_api_response
        result = handle_api_response(response, operation="deleteCIDGroups", error_message="Failed to delete CID groups")
        if self._is_error(result):
            return result
        return {"deleted": cid_group_ids, "status": "success"}

    def add_cid_group_members(
        self,
        cid_group_id: str = Field(description="CID group ID to add members to."),
        cids: list[str] = Field(description="Child CIDs to add to the group."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Add child CIDs (tenants) to an existing CID group."""
        if not cids:
            return [_format_error_response("`cids` is required.", operation="addCIDGroupMembers")]

        result = self._base_query_api_call(
            operation="addCIDGroupMembers",
            body_params={"resources": [{"cid_group_id": cid_group_id, "cids": cids}]},
            error_message="Failed to add CID group members",
        )
        if self._is_error(result):
            return [result]
        return result

    def remove_cid_group_members(
        self,
        cid_group_id: str = Field(description="CID group ID to remove members from."),
        cids: list[str] = Field(description="Child CIDs to remove from the group."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Remove child CIDs from a CID group.

        Cannot remove a CID if the group is its only group membership (API enforces minimum one group).
        """
        if not cids:
            return [_format_error_response("`cids` is required.", operation="deleteCIDGroupMembersV2")]

        result = self._base_query_api_call(
            operation="deleteCIDGroupMembersV2",
            body_params={"resources": [{"cid_group_id": cid_group_id, "cids": cids}]},
            error_message="Failed to remove CID group members",
        )
        if self._is_error(result):
            return [result]
        return result

    # -------------------------------------------------------------------------
    # User group write operations
    # -------------------------------------------------------------------------

    def create_user_group(
        self,
        name: str = Field(description="User group name. Must be unique. Maximum 500 groups per MSSP parent."),
        description: str | None = Field(default=None, description="Optional description."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Create a new MSSP user group.

        After creating, use add_user_group_members to add users,
        then assign_mssp_role to grant access to CID groups.
        """
        resource: dict[str, Any] = {"name": name}
        if description:
            resource["description"] = description

        result = self._base_query_api_call(
            operation="createUserGroups",
            body_params={"resources": [resource]},
            error_message="Failed to create user group",
        )
        if self._is_error(result):
            return [result]
        return result

    def update_user_group(
        self,
        user_group_id: str = Field(description="User group ID to update."),
        name: str = Field(description="New name. Required by the API even if unchanged."),
        description: str | None = Field(
            default=None,
            description="New description. Empty string clears the existing description.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Update a user group's name or description. Members and role assignments are unaffected."""
        resource: dict[str, Any] = {"user_group_id": user_group_id, "name": name}
        if description is not None:
            resource["description"] = description

        result = self._base_query_api_call(
            operation="updateUserGroups",
            body_params={"resources": [resource]},
            error_message="Failed to update user group",
        )
        if self._is_error(result):
            return [result]
        return result

    def delete_user_groups(
        self,
        user_group_ids: list[str] = Field(description="User group IDs to delete."),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID to scope this call to a specific child tenant. Leave unset to use the parent MSSP account scope.",
        ),
    ) -> dict[str, Any]:
        """Delete one or more user groups by ID.

        Users in the group are not deleted. Role assignments referencing these groups are removed.
        """
        if not user_group_ids:
            return _format_error_response("`user_group_ids` is required.", operation="deleteUserGroups")

        response = self.client.command_for(
            "deleteUserGroups",
            member_cid=member_cid,
            parameters={"user_group_ids": user_group_ids},
        )
        from falcon_mcp.common.errors import handle_api_response
        result = handle_api_response(response, operation="deleteUserGroups", error_message="Failed to delete user groups")
        if self._is_error(result):
            return result
        return {"deleted": user_group_ids, "status": "success"}

    def add_user_group_members(
        self,
        user_group_id: str = Field(description="User group ID to add members to."),
        user_uuids: list[str] = Field(description="User UUIDs to add. Maximum 500 members per group."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Add users to an existing MSSP user group."""
        if not user_uuids:
            return [_format_error_response("`user_uuids` is required.", operation="addUserGroupMembers")]

        result = self._base_query_api_call(
            operation="addUserGroupMembers",
            body_params={"resources": [{"user_group_id": user_group_id, "user_uuids": user_uuids}]},
            error_message="Failed to add user group members",
        )
        if self._is_error(result):
            return [result]
        return result

    def remove_user_group_members(
        self,
        user_group_id: str = Field(description="User group ID to remove members from."),
        user_uuids: list[str] = Field(description="User UUIDs to remove from the group."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Remove users from an MSSP user group."""
        if not user_uuids:
            return [_format_error_response("`user_uuids` is required.", operation="deleteUserGroupMembers")]

        result = self._base_query_api_call(
            operation="deleteUserGroupMembers",
            body_params={"resources": [{"user_group_id": user_group_id, "user_uuids": user_uuids}]},
            error_message="Failed to remove user group members",
        )
        if self._is_error(result):
            return [result]
        return result

    # -------------------------------------------------------------------------
    # MSSP role assignment tools
    # -------------------------------------------------------------------------

    def assign_mssp_role(
        self,
        user_group_id: str = Field(description="User group ID to grant access."),
        cid_group_id: str = Field(description="CID group ID to grant access to."),
        role_ids: list[str] = Field(
            description=(
                "Role IDs to assign. Common roles: falcon-access (read-only), "
                "falcon-analyst (analyst access), falcon-responder (response capabilities), "
                "falcon-admin (full admin). Get available roles from list_available_roles in the users module."
            ),
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Grant a user group access to a CID group with specified roles.

        Creates a role assignment link: users in `user_group_id` get `role_ids`
        access to all tenants in `cid_group_id`. Does not replace existing assignments.
        """
        if not role_ids:
            return [_format_error_response("`role_ids` is required.", operation="addRole")]

        result = self._base_query_api_call(
            operation="addRole",
            body_params={
                "resources": [{
                    "user_group_id": user_group_id,
                    "cid_group_id": cid_group_id,
                    "role_ids": role_ids,
                }]
            },
            error_message="Failed to assign MSSP role",
        )
        if self._is_error(result):
            return [result]
        return result

    def remove_mssp_roles(
        self,
        user_group_id: str = Field(description="User group ID."),
        cid_group_id: str = Field(description="CID group ID."),
        role_ids: list[str] | None = Field(
            default=None,
            description=(
                "Specific role IDs to remove. If omitted, the entire user_group ↔ cid_group "
                "association is dissolved (all roles removed)."
            ),
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Remove role assignments between a user group and CID group.

        Provide role_ids to remove specific roles only. Omit role_ids to completely
        dissolve the association between the user group and CID group.
        """
        resource: dict[str, Any] = {
            "user_group_id": user_group_id,
            "cid_group_id": cid_group_id,
        }
        if role_ids:
            resource["role_ids"] = role_ids

        result = self._base_query_api_call(
            operation="deletedRoles",
            body_params={"resources": [resource]},
            error_message="Failed to remove MSSP roles",
        )
        if self._is_error(result):
            return [result]
        return result
