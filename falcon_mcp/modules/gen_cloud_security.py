"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `cloud_security` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenCloudSecurityModule(GeneratedModuleBase):
    """Generated tools for the Falcon `cloud_security` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.list_cloud_group_i_ds_external, name="list_cloud_group_i_ds_external")
        self._add_tool(server=server, method=self.list_cloud_groups_by_id_external, name="list_cloud_groups_by_id_external")
        self._add_tool(server=server, method=self.list_cloud_groups_external, name="list_cloud_groups_external")
        self._add_tool(server=server, method=self.combined_cloud_risks, name="combined_cloud_risks")
        self._add_tool(server=server, method=self.create_cloud_group_external, name="create_cloud_group_external", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_cloud_group_external, name="update_cloud_group_external", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_cloud_groups_external, name="delete_cloud_groups_external", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def create_cloud_group_external(
        self,
        body: dict = Field(description="Request JSON body for `CreateCloudGroupExternal` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create a Cloud Group. The created_by field will be set to the API client ID."""
        return self._call(operation="CreateCloudGroupExternal", query_params=None, body_params=body, error_message="CreateCloudGroupExternal failed", member_cid=member_cid)

    def delete_cloud_groups_external(
        self,
        ids: list[str] | None = Field(default=None, description="Cloud Groups UUIDs to delete"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete Cloud Groups in batch"""
        return self._call(operation="DeleteCloudGroupsExternal", query_params={"ids": ids}, error_message="DeleteCloudGroupsExternal failed", member_cid=member_cid)

    def list_cloud_group_i_ds_external(
        self,
        filter: str | None = Field(default=None, description="A valid FQL filter. Supports filtering groups by: Group properties: name description created_at updated_at Selector properties: cloud_provider account_id region cloud_provider_tag image_registry image_repository image_tag selector.kubernetes_resource.cluster selector.kubernetes_resource.namespace Group tags: business_unit business_impact environment"),
        sort: str | None = Field(default=None, description="A valid sort string."),
        offset: str | None = Field(default=None, description="The starting position of the list operation."),
        limit: str | None = Field(default=None, description="The maximum number of cloud groups to retrieve."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Query Cloud Groups and returns IDs"""
        return self._call(operation="ListCloudGroupIDsExternal", query_params={"filter": filter, "sort": sort, "offset": offset, "limit": limit}, error_message="ListCloudGroupIDsExternal failed", member_cid=member_cid)

    def list_cloud_groups_by_id_external(
        self,
        ids: list[str] | None = Field(default=None, description="`ids` query parameter."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """List Cloud Groups By ID"""
        return self._call(operation="ListCloudGroupsByIDExternal", query_params={"ids": ids}, error_message="ListCloudGroupsByIDExternal failed", member_cid=member_cid)

    def list_cloud_groups_external(
        self,
        filter: str | None = Field(default=None, description="A valid FQL filter. Supports filtering groups by: Group properties: name description created_at updated_at Selector properties: cloud_provider account_id region cloud_provider_tag image_registry image_repository image_tag selector.kubernetes_resource.cluster selector.kubernetes_resource.namespace Group tags: business_unit business_impact environment"),
        sort: str | None = Field(default=None, description="A valid sort string."),
        offset: str | None = Field(default=None, description="The starting position of the list operation."),
        limit: str | None = Field(default=None, description="The maximum number of cloud groups to retrieve."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Query Cloud Groups and returns entities"""
        return self._call(operation="ListCloudGroupsExternal", query_params={"filter": filter, "sort": sort, "offset": offset, "limit": limit}, error_message="ListCloudGroupsExternal failed", member_cid=member_cid)

    def update_cloud_group_external(
        self,
        body: dict = Field(description="Request JSON body for `UpdateCloudGroupExternal` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update Cloud Group"""
        return self._call(operation="UpdateCloudGroupExternal", query_params=None, body_params=body, error_message="UpdateCloudGroupExternal failed", member_cid=member_cid)

    def combined_cloud_risks(
        self,
        filter: str | None = Field(default=None, description="FQL string to filter results in Falcon Query Language (FQL). Supported fields: account_id account_name asset_gcrn asset_id asset_name asset_region asset_type cloud_group cloud_provider first_seen last_seen resolved_at risk_factor rule_id rule_name service_category severity status suppressed_by suppressed_reason tags"),
        sort: str | None = Field(default=None, description="The field to sort on. Use |asc or |desc suffix to specify sort direction.Supported fields: account_id account_name asset_id asset_name asset_region asset_type cloud_provider first_seen last_seen resolved_at rule_name service_category severity status"),
        limit: int | None = Field(default=None, description="The maximum number of items to return. When not specified or 0, 500 is used. When larger than 1000, 1000 is used."),
        offset: int | None = Field(default=None, description="Offset returned risks"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Gets cloud risks with full details based on filters and sort criteria"""
        return self._call(operation="combined_cloud_risks", query_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset}, error_message="combined_cloud_risks failed", member_cid=member_cid)
