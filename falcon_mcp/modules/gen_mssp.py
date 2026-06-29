"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `mssp` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenMsspModule(GeneratedModuleBase):
    """Generated tools for the Falcon `mssp` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_cid_group_by_id_v2, name="get_cid_group_by_id_v2")
        self._add_tool(server=server, method=self.get_cid_group_members_by_v2, name="get_cid_group_members_by_v2")
        self._add_tool(server=server, method=self.get_children_v2, name="get_children_v2")
        self._add_tool(server=server, method=self.get_user_group_members_by_idv2, name="get_user_group_members_by_idv2")
        self._add_tool(server=server, method=self.get_user_groups_by_idv2, name="get_user_groups_by_idv2")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def get_cid_group_by_id_v2(
        self,
        ids: list[str] = Field(description="CID group IDs to search for"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get CID Groups by ID."""
        return self._call(operation="getCIDGroupByIdV2", query_params={"ids": ids}, error_message="getCIDGroupByIdV2 failed", member_cid=member_cid)

    def get_cid_group_members_by_v2(
        self,
        ids: list[str] = Field(description="CID group IDs search for"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get CID group members by CID Group ID."""
        return self._call(operation="getCIDGroupMembersByV2", query_params={"ids": ids}, error_message="getCIDGroupMembersByV2 failed", member_cid=member_cid)

    def get_children_v2(
        self,
        body: dict = Field(description="Request JSON body for `getChildrenV2` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get link to child customer by child CID(s)"""
        return self._call(operation="getChildrenV2", query_params=None, body_params=body, error_message="getChildrenV2 failed", member_cid=member_cid)

    def get_user_group_members_by_idv2(
        self,
        ids: list[str] = Field(description="User group IDs to search for"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get user group members by user group ID."""
        return self._call(operation="getUserGroupMembersByIDV2", query_params={"ids": ids}, error_message="getUserGroupMembersByIDV2 failed", member_cid=member_cid)

    def get_user_groups_by_idv2(
        self,
        ids: list[str] = Field(description="User group IDs to search for"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get user groups by ID."""
        return self._call(operation="getUserGroupsByIDV2", query_params={"ids": ids}, error_message="getUserGroupsByIDV2 failed", member_cid=member_cid)
