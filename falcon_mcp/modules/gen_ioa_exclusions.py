"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `ioa_exclusions` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenIoaExclusionsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `ioa_exclusions` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.ss_ioa_exclusions_get_reports_v2, name="ss_ioa_exclusions_get_reports_v2")
        self._add_tool(server=server, method=self.ss_ioa_exclusions_get_v2, name="ss_ioa_exclusions_get_v2")
        self._add_tool(server=server, method=self.ss_ioa_exclusions_search_v2, name="ss_ioa_exclusions_search_v2")
        self._add_tool(server=server, method=self.ss_ioa_exclusions_create_v2, name="ss_ioa_exclusions_create_v2", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.ss_ioa_exclusions_new_rules_v2, name="ss_ioa_exclusions_new_rules_v2", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.ss_ioa_exclusions_update_v2, name="ss_ioa_exclusions_update_v2", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.ss_ioa_exclusions_delete_v2, name="ss_ioa_exclusions_delete_v2", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.ss_ioa_exclusions_matched_rule_v2, name="ss_ioa_exclusions_matched_rule_v2", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def ss_ioa_exclusions_create_v2(
        self,
        body: dict = Field(description="Request JSON body for `ss_ioa_exclusions_create_v2` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create new Self Service IOA Exclusions."""
        return self._call(operation="ss_ioa_exclusions_create_v2", query_params=None, body_params=body, error_message="ss_ioa_exclusions_create_v2 failed", member_cid=member_cid)

    def ss_ioa_exclusions_delete_v2(
        self,
        ids: list[str] = Field(description="The ids of the exclusions to delete"),
        comment: str | None = Field(default=None, description="The comment why these ss ioa exclusions were deleted"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete the Self Service IOA Exclusions rule by id."""
        return self._call(operation="ss_ioa_exclusions_delete_v2", query_params={"ids": ids, "comment": comment}, error_message="ss_ioa_exclusions_delete_v2 failed", member_cid=member_cid)

    def ss_ioa_exclusions_get_reports_v2(
        self,
        body: dict = Field(description="Request JSON body for `ss_ioa_exclusions_get_reports_v2` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create a report of Self Service IOA Exclusions scoped by the given filters"""
        return self._call(operation="ss_ioa_exclusions_get_reports_v2", query_params=None, body_params=body, error_message="ss_ioa_exclusions_get_reports_v2 failed", member_cid=member_cid)

    def ss_ioa_exclusions_get_v2(
        self,
        ids: list[str] = Field(description="The ids of the exclusions to retrieve"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get the Self Service IOA Exclusions rules by id."""
        return self._call(operation="ss_ioa_exclusions_get_v2", query_params={"ids": ids}, error_message="ss_ioa_exclusions_get_v2 failed", member_cid=member_cid)

    def ss_ioa_exclusions_matched_rule_v2(
        self,
        body: dict = Field(description="Request JSON body for `ss_ioa_exclusions_matched_rule_v2` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get Self Service IOA Exclusions rules for matched IFN/CLI for child, parent and grandparent"""
        return self._call(operation="ss_ioa_exclusions_matched_rule_v2", query_params=None, body_params=body, error_message="ss_ioa_exclusions_matched_rule_v2 failed", member_cid=member_cid)

    def ss_ioa_exclusions_new_rules_v2(
        self,
        body: dict = Field(description="Request JSON body for `ss_ioa_exclusions_new_rules_v2` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get defaults for Self Service IOA Exclusions based on provided IFN/CLI for child, parent and grandparent."""
        return self._call(operation="ss_ioa_exclusions_new_rules_v2", query_params=None, body_params=body, error_message="ss_ioa_exclusions_new_rules_v2 failed", member_cid=member_cid)

    def ss_ioa_exclusions_search_v2(
        self,
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results. Filtered queries involving regex fields should specify their expressions in the ifn_regex and cl_regex parameters."),
        ifn_regex: str | None = Field(default=None, description="The ifn_regex expression to filter exclusions by, used alongside expressions specified in the filter query parameter."),
        cl_regex: str | None = Field(default=None, description="The cl_regex expression to filter exclusions by, used alongside expressions specified in the filter query parameter."),
        parent_ifn_regex: str | None = Field(default=None, description="The parent_ifn_regex expression to filter exclusions by, used alongside expressions specified in the filter query parameter."),
        parent_cl_regex: str | None = Field(default=None, description="The parent_cl_regex expression to filter exclusions by, used alongside expressions specified in the filter query parameter."),
        grandparent_ifn_regex: str | None = Field(default=None, description="The grandparent_ifn_regex expression to filter exclusions by, used alongside expressions specified in the filter query parameter."),
        grandparent_cl_regex: str | None = Field(default=None, description="The grandparent_cl_regex expression to filter exclusions by, used alongside expressions specified in the filter query parameter."),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        limit: int | None = Field(default=None, description="The maximum records to return. [1-500]"),
        sort: str | None = Field(default=None, description="The sort expression that should be used to sort the results."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for Self Service IOA Exclusions."""
        return self._call(operation="ss_ioa_exclusions_search_v2", query_params={"filter": filter, "ifn_regex": ifn_regex, "cl_regex": cl_regex, "parent_ifn_regex": parent_ifn_regex, "parent_cl_regex": parent_cl_regex, "grandparent_ifn_regex": grandparent_ifn_regex, "grandparent_cl_regex": grandparent_cl_regex, "offset": offset, "limit": limit, "sort": sort}, error_message="ss_ioa_exclusions_search_v2 failed", member_cid=member_cid)

    def ss_ioa_exclusions_update_v2(
        self,
        body: dict = Field(description="Request JSON body for `ss_ioa_exclusions_update_v2` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update the Self Service IOA Exclusions rule by id."""
        return self._call(operation="ss_ioa_exclusions_update_v2", query_params=None, body_params=body, error_message="ss_ioa_exclusions_update_v2 failed", member_cid=member_cid)
