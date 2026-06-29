"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `certificate_based_exclusions` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenCertificateBasedExclusionsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `certificate_based_exclusions` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.cb_exclusions_get_v1, name="cb_exclusions_get_v1")
        self._add_tool(server=server, method=self.cb_exclusions_query_v1, name="cb_exclusions_query_v1")
        self._add_tool(server=server, method=self.certificates_get_v1, name="certificates_get_v1")
        self._add_tool(server=server, method=self.cb_exclusions_create_v1, name="cb_exclusions_create_v1", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.cb_exclusions_update_v1, name="cb_exclusions_update_v1", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.cb_exclusions_delete_v1, name="cb_exclusions_delete_v1", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def cb_exclusions_create_v1(
        self,
        body: dict = Field(description="Request JSON body for `cb_exclusions_create_v1` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create new Certificate Based Exclusions."""
        return self._call(operation="cb_exclusions_create_v1", query_params=None, body_params=body, error_message="cb_exclusions_create_v1 failed", member_cid=member_cid)

    def cb_exclusions_delete_v1(
        self,
        ids: list[str] = Field(description="The ids of the exclusions to delete"),
        comment: str | None = Field(default=None, description="The comment why these exclusions were deleted"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete the exclusions by id"""
        return self._call(operation="cb_exclusions_delete_v1", query_params={"ids": ids, "comment": comment}, error_message="cb_exclusions_delete_v1 failed", member_cid=member_cid)

    def cb_exclusions_get_v1(
        self,
        ids: list[str] = Field(description="The ids of the exclusions to retrieve"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Find all exclusion IDs matching the query with filter"""
        return self._call(operation="cb_exclusions_get_v1", query_params={"ids": ids}, error_message="cb_exclusions_get_v1 failed", member_cid=member_cid)

    def cb_exclusions_query_v1(
        self,
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results."),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        limit: int | None = Field(default=None, description="The maximum records to return. [1-100]"),
        sort: str | None = Field(default=None, description="The sort expression that should be used to sort the results."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for cert-based exclusions."""
        return self._call(operation="cb_exclusions_query_v1", query_params={"filter": filter, "offset": offset, "limit": limit, "sort": sort}, error_message="cb_exclusions_query_v1 failed", member_cid=member_cid)

    def cb_exclusions_update_v1(
        self,
        body: dict = Field(description="Request JSON body for `cb_exclusions_update_v1` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Updates existing Certificate Based Exclusions"""
        return self._call(operation="cb_exclusions_update_v1", query_params=None, body_params=body, error_message="cb_exclusions_update_v1 failed", member_cid=member_cid)

    def certificates_get_v1(
        self,
        ids: str = Field(description="The SHA256 Hash of the file to retrieve certificate signing info for"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves certificate signing information for a file"""
        return self._call(operation="certificates_get_v1", query_params={"ids": ids}, error_message="certificates_get_v1 failed", member_cid=member_cid)
