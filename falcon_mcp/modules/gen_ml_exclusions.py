"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `ml_exclusions` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenMlExclusionsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `ml_exclusions` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.exclusions_get_all_v2, name="exclusions_get_all_v2")
        self._add_tool(server=server, method=self.exclusions_get_reports_v2, name="exclusions_get_reports_v2")
        self._add_tool(server=server, method=self.exclusions_get_v2, name="exclusions_get_v2")
        self._add_tool(server=server, method=self.exclusions_search_v2, name="exclusions_search_v2")
        self._add_tool(server=server, method=self.exclusions_create_v2, name="exclusions_create_v2", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.exclusions_update_v2, name="exclusions_update_v2", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.exclusions_delete_v2, name="exclusions_delete_v2", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.exclusions_perform_action_v2, name="exclusions_perform_action_v2", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def exclusions_create_v2(
        self,
        body: dict = Field(description="Request JSON body for `exclusions_create_v2` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create the exclusions, with ancestor fields."""
        return self._call(operation="exclusions_create_v2", query_params=None, body_params=body, error_message="exclusions_create_v2 failed", member_cid=member_cid)

    def exclusions_delete_v2(
        self,
        ids: list[str] = Field(description="The ids of the exclusions to delete"),
        comment: str | None = Field(default=None, description="The comment why these exclusions were deleted"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete the exclusions by id, with ancestor fields."""
        return self._call(operation="exclusions_delete_v2", query_params={"ids": ids, "comment": comment}, error_message="exclusions_delete_v2 failed", member_cid=member_cid)

    def exclusions_get_all_v2(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get all exclusions."""
        return self._call(operation="exclusions_get_all_v2", query_params=None, error_message="exclusions_get_all_v2 failed", member_cid=member_cid)

    def exclusions_get_reports_v2(
        self,
        body: dict = Field(description="Request JSON body for `exclusions_get_reports_v2` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create a report of ML exclusions scoped by the given filters"""
        return self._call(operation="exclusions_get_reports_v2", query_params=None, body_params=body, error_message="exclusions_get_reports_v2 failed", member_cid=member_cid)

    def exclusions_get_v2(
        self,
        ids: list[str] = Field(description="The ids of the exclusions to retrieve"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get the exclusions by id, with ancestor fields."""
        return self._call(operation="exclusions_get_v2", query_params={"ids": ids}, error_message="exclusions_get_v2 failed", member_cid=member_cid)

    def exclusions_perform_action_v2(
        self,
        action_name: str = Field(description="The action to perform."),
        body: dict = Field(description="Request JSON body for `exclusions_perform_action_v2` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Actions used to manipulate the content of exclusions, with ancestor fields."""
        return self._call(operation="exclusions_perform_action_v2", query_params={"action_name": action_name}, body_params=body, error_message="exclusions_perform_action_v2 failed", member_cid=member_cid)

    def exclusions_search_v2(
        self,
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results."),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        limit: int | None = Field(default=None, description="The maximum records to return. [1-500]"),
        sort: str | None = Field(default=None, description="The sort expression that should be used to sort the results."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for exclusions, with ancestor fields."""
        return self._call(operation="exclusions_search_v2", query_params={"filter": filter, "offset": offset, "limit": limit, "sort": sort}, error_message="exclusions_search_v2 failed", member_cid=member_cid)

    def exclusions_update_v2(
        self,
        body: dict = Field(description="Request JSON body for `exclusions_update_v2` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update the exclusions by id, with ancestor fields."""
        return self._call(operation="exclusions_update_v2", query_params=None, body_params=body, error_message="exclusions_update_v2 failed", member_cid=member_cid)
