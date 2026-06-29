"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `deployments` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenDeploymentsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `deployments` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.combined_release_notes_v1, name="combined_release_notes_v1")
        self._add_tool(server=server, method=self.combined_releases_v1_mixin0, name="combined_releases_v1_mixin0")
        self._add_tool(server=server, method=self.get_deployments_external_v1, name="get_deployments_external_v1")
        self._add_tool(server=server, method=self.get_entity_i_ds_by_query_postv2, name="get_entity_i_ds_by_query_postv2")
        self._add_tool(server=server, method=self.query_release_notes_v1, name="query_release_notes_v1")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def combined_release_notes_v1(
        self,
        filter: str | None = Field(default=None, description="FQL query specifying filter parameters."),
        limit: int | None = Field(default=None, description="Maximum number of records to return."),
        offset: str | None = Field(default=None, description="Starting pagination offset of records to return."),
        sort: str | None = Field(default=None, description="Sort items by providing a comma separated list of property and direction (eg name.desc,time.asc). If direction is omitted, defaults to descending."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Queries for release-notes resources and returns details"""
        return self._call(operation="CombinedReleaseNotesV1", query_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort}, error_message="CombinedReleaseNotesV1 failed", member_cid=member_cid)

    def combined_releases_v1_mixin0(
        self,
        filter: str | None = Field(default=None, description="FQL query specifying filter parameters."),
        limit: int | None = Field(default=None, description="Maximum number of records to return."),
        offset: str | None = Field(default=None, description="Starting pagination offset of records to return."),
        sort: str | None = Field(default=None, description="Sort items by providing a comma separated list of property and direction (eg name.desc,time.asc). If direction is omitted, defaults to descending."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Queries for releases resources and returns details"""
        return self._call(operation="CombinedReleasesV1Mixin0", query_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort}, error_message="CombinedReleasesV1Mixin0 failed", member_cid=member_cid)

    def get_deployments_external_v1(
        self,
        ids: list[str] = Field(description="release version ids to retrieve deployment details"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get deployment resources by ids"""
        return self._call(operation="GetDeploymentsExternalV1", query_params={"ids": ids}, error_message="GetDeploymentsExternalV1 failed", member_cid=member_cid)

    def get_entity_i_ds_by_query_postv2(
        self,
        body: dict = Field(description="Request JSON body for `GetEntityIDsByQueryPOSTV2` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """returns the release notes for the IDs in the request with EA and GA dates in ISO 8601 format"""
        return self._call(operation="GetEntityIDsByQueryPOSTV2", query_params=None, body_params=body, error_message="GetEntityIDsByQueryPOSTV2 failed", member_cid=member_cid)

    def query_release_notes_v1(
        self,
        filter: str | None = Field(default=None, description="FQL query specifying filter parameters."),
        limit: int | None = Field(default=None, description="Maximum number of records to return."),
        offset: str | None = Field(default=None, description="Starting pagination offset of records to return."),
        sort: str | None = Field(default=None, description="Sort items by providing a comma separated list of property and direction (eg name.desc,time.asc). If direction is omitted, defaults to descending."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Queries for release-notes resources and returns ids"""
        return self._call(operation="QueryReleaseNotesV1", query_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort}, error_message="QueryReleaseNotesV1 failed", member_cid=member_cid)
