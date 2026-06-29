"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `exposure_management` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenExposureManagementModule(GeneratedModuleBase):
    """Generated tools for the Falcon `exposure_management` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.blob_download_external_assets, name="blob_download_external_assets")
        self._add_tool(server=server, method=self.blob_preview_external_assets, name="blob_preview_external_assets")
        self._add_tool(server=server, method=self.combined_ecosystem_subsidiaries, name="combined_ecosystem_subsidiaries")
        self._add_tool(server=server, method=self.get_ecosystem_subsidiaries, name="get_ecosystem_subsidiaries")
        self._add_tool(server=server, method=self.get_external_assets, name="get_external_assets")
        self._add_tool(server=server, method=self.query_ecosystem_subsidiaries, name="query_ecosystem_subsidiaries")
        self._add_tool(server=server, method=self.query_external_assets_v2, name="query_external_assets_v2")
        self._add_tool(server=server, method=self.patch_external_assets, name="patch_external_assets", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.post_external_assets_inventory_v1, name="post_external_assets_inventory_v1", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_external_assets, name="delete_external_assets", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def blob_download_external_assets(
        self,
        assetId: str = Field(description="The Asset ID"),
        hash: str = Field(description="The File Hash"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Download the entire contents of the blob. The relative link to this endpoint is returned in the GET /entities/external-assets/v1 request."""
        return self._call(operation="blob_download_external_assets", query_params={"assetId": assetId, "hash": hash}, error_message="blob_download_external_assets failed", member_cid=member_cid)

    def blob_preview_external_assets(
        self,
        assetId: str = Field(description="The Asset ID"),
        hash: str = Field(description="The File Hash"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Download a preview of the blob. The relative link to this endpoint is returned in the GET /entities/external-assets/v1 request."""
        return self._call(operation="blob_preview_external_assets", query_params={"assetId": assetId, "hash": hash}, error_message="blob_preview_external_assets failed", member_cid=member_cid)

    def combined_ecosystem_subsidiaries(
        self,
        offset: int | None = Field(default=None, description="Starting index of result set from which to return subsidiaries"),
        limit: int | None = Field(default=None, description="The maximum number of subsidiaries to return in the response."),
        filter: str | None = Field(default=None, description="Filter ecosystem subsidiaries"),
        sort: str | None = Field(default=None, description="The field by which to sort the list of subsidiaries. Possible values:<ul><li>name</li><li>primary_domain</li></ul></br>Sort order can be specified by appending 'asc' or 'desc' to the field name (e.g. 'name|asc' or 'primary_domain|desc')."),
        version_id: str | None = Field(default=None, description="The version ID of the ecosystem subsidiaries data, represented as a hash string. This parameter is required to ensure data consistency and prevent stale data. If a new version of the ecosystem subsidiaries data is written, the version ID will be updated. By including this parameter in the request, the client can ensure that the response will be invalidated if a new version is written."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves a list of ecosystem subsidiaries with their detailed information."""
        return self._call(operation="combined_ecosystem_subsidiaries", query_params={"offset": offset, "limit": limit, "filter": filter, "sort": sort, "version_id": version_id}, error_message="combined_ecosystem_subsidiaries failed", member_cid=member_cid)

    def delete_external_assets(
        self,
        ids: list[str] = Field(description="One or more asset IDs (max: 100)."),
        body: dict = Field(description="Request JSON body for `delete_external_assets` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete multiple external assets."""
        return self._call(operation="delete_external_assets", query_params={"ids": ids}, body_params=body, error_message="delete_external_assets failed", member_cid=member_cid)

    def get_ecosystem_subsidiaries(
        self,
        ids: list[str] = Field(description="One or more asset IDs (max: 100). Find ecosystem subsidiary IDs with GET /fem/entities/ecosystem-subsidiaries/v1"),
        version_id: str | None = Field(default=None, description="The version ID of the ecosystem subsidiaries data, represented as a hash string. This parameter is required to ensure data consistency and prevent stale data. If a new version of the ecosystem subsidiaries data is written, the version ID will be updated. By including this parameter in the request, the client can ensure that the response will be invalidated if a new version is written."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves detailed information about ecosystem subsidiaries by ID."""
        return self._call(operation="get_ecosystem_subsidiaries", query_params={"ids": ids, "version_id": version_id}, error_message="get_ecosystem_subsidiaries failed", member_cid=member_cid)

    def get_external_assets(
        self,
        ids: list[str] = Field(description="One or more asset IDs (max: 100). Find asset IDs with GET /fem/queries/external-assets/v1"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get details on external assets by providing one or more IDs."""
        return self._call(operation="get_external_assets", query_params={"ids": ids}, error_message="get_external_assets failed", member_cid=member_cid)

    def patch_external_assets(
        self,
        body: dict = Field(description="Request JSON body for `patch_external_assets` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update the details of external assets."""
        return self._call(operation="patch_external_assets", query_params=None, body_params=body, error_message="patch_external_assets failed", member_cid=member_cid)

    def post_external_assets_inventory_v1(
        self,
        body: dict = Field(description="Request JSON body for `post_external_assets_inventory_v1` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Add external assets for external asset scanning."""
        return self._call(operation="post_external_assets_inventory_v1", query_params=None, body_params=body, error_message="post_external_assets_inventory_v1 failed", member_cid=member_cid)

    def query_ecosystem_subsidiaries(
        self,
        offset: int | None = Field(default=None, description="Starting index of result set from which to return subsidiaries"),
        limit: int | None = Field(default=None, description="The maximum number of IDs to return in the response."),
        filter: str | None = Field(default=None, description="Filter ecosystem subsidiaries"),
        sort: str | None = Field(default=None, description="The field by which to sort the list of IDs. Possible values:<ul><li>name</li><li>primary_domain</li></ul></br>Sort order can be specified by appending 'asc' or 'desc' to the field name (e.g. 'name|asc' or 'primary_domain|desc')."),
        version_id: str | None = Field(default=None, description="The version ID of the ecosystem subsidiaries data, represented as a hash string. This parameter is required to ensure data consistency and prevent stale data. If a new version of the ecosystem subsidiaries data is written, the version ID will be updated. By including this parameter in the request, the client can ensure that the response will be invalidated if a new version is written."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves a list of IDs for ecosystem subsidiaries. Use these IDs with the /entities/ecosystem-subsidiaries/v1 endpoints."""
        return self._call(operation="query_ecosystem_subsidiaries", query_params={"offset": offset, "limit": limit, "filter": filter, "sort": sort, "version_id": version_id}, error_message="query_ecosystem_subsidiaries failed", member_cid=member_cid)

    def query_external_assets_v2(
        self,
        after: str | None = Field(default=None, description="A pagination token used with the limit parameter to manage pagination of results. On your first request, don't provide an after token. On subsequent requests, provide the after token from the previous response to continue from that place in the results."),
        limit: int | None = Field(default=None, description="number of IDs to return."),
        sort: str | None = Field(default=None, description="Order by fields."),
        filter: str | None = Field(default=None, description="Filter assets using an FQL query. Common filter options include:<ul><li>asset_type:'ip'</li><li>last_seen_timestamp:>'now-7d'</li></ul> </br>Available filter fields that support exact match: asset_id, asset_type, confidence, connectivity_status, criticality, criticality_description, criticality_timestamp, criticality_username, data_providers, discovered_by, dns_domain.fqdn, dns_domain.isps, dns_domain.parent_domain, dns_domain.resolved_ips, dns_domain.services.applications.category, dns_domain.services.applications.cpe, dns_domain.services.applications.name, dns_domain.services.applications.vendor, dns_domain.services.applications.version, dns_domain.services.cloud_provider, dns_domain.services.cpes, dns_domain.services.hosting_provider, dns_domain.services.last_seen, dns_domain.services.platform_name, dns_domain.services.port, dns_domain.services.protocol, dns_domain.services.protocol_port, dns_domain.services.status, dns_domain.services.status_code, dns_domain.services.transport, dns_domain.type, first_seen, id, internet_exposure, ip.asn, ip.cloud_provider, ip.cloud_vm.description, ip.cloud_vm.instance_id, ip.cloud_vm.lifecycle, ip.cloud_vm.mac_address, ip.cloud_vm.owner_id, ip.cloud_vm.platform, ip.cloud_vm.private_ip, ip.cloud_vm.public_ip, ip.cloud_vm.region, ip.cloud_vm.security_groups, ip.cloud_vm.source, ip.cloud_vm.status, ip.fqdns, ip.ip_address, ip.isp, ip.location.area_code, ip.location.city, ip.location.country_code, ip.location.country_name, ip.location.postal_code, ip.location.region_code, ip.location.region_name, ip.location.timezone, ip.ptr, ip.aid, ip.services.applications.category, ip.services.applications.cpe, ip.services.applications.name, ip.services.applications.vendor, ip.services.applications.version, ip.services.cloud_provider, ip.services.cpes, ip.services.first_seen, ip.services.last_seen, ip.services.platform_name, ip.services.port, ip.services.protocol, ip.services.protocol_port, ip.services.status, ip.services.status_code, ip.services.transport, last_seen, manual, perimeter, subsidiaries.id, subsidiaries.name, triage.action, triage.assigned_to, triage.status, triage.updated_by, triage.updated_timestamp </br>Available filter fields that supports wildcard (*): asset_id, asset_type, confidence, connectivity_status, criticality, criticality_username, data_providers, discovered_by, dns_domain.fqdn, dns_domain.isps, dns_domain.parent_domain, dns_domain.resolved_ips, dns_domain.services.applications.category, dns_domain.services.applications.cpe, dns_domain.services.applications.name, dns_domain.services.applications.vendor, dns_domain.services.applications.version, dns_domain.services.cloud_provider, dns_domain.services.cpes, dns_domain.services.hosting_provider, dns_domain.services.id, dns_domain.services.platform_name, dns_domain.services.port, dns_domain.services.protocol, dns_domain.services.protocol_port, dns_domain.services.status, dns_domain.services.status_code, dns_domain.services.transport, dns_domain.type, id, internet_exposure, ip.asn, ip.cloud_vm.instance_id, ip.cloud_vm.lifecycle, ip.cloud_vm.mac_address, ip.cloud_vm.owner_id, ip.cloud_vm.platform, ip.cloud_vm.private_ip, ip.cloud_vm.public_ip, ip.cloud_vm.region, ip.cloud_vm.security_groups, ip.cloud_vm.source, ip.cloud_vm.status, ip.fqdns, ip.ip_address, ip.isp, ip.location.area_code, ip.location.city, ip.location.country_code, ip.location.country_name, ip.location.postal_code, ip.location.region_code, ip.location.region_name, ip.location.timezone, ip.ptr, ip.aid, ip.services.applications.category, ip.services.applications.cpe, ip.services.applications.name, ip.services.applications.vendor, ip.services.applications.version, ip.services.cloud_provider, ip.services.cpes, ip.services.platform_name, ip.services.port, ip.services.protocol, ip.services.protocol_port, ip.services.status, ip.services.status_code, ip.services.transport, manual, perimeter, subsidiaries.id, subsidiaries.name, triage.action, triage.assigned_to, triage.status, triage.updated_by </br>Available filter fields that supports in ([v1, v2]): asset_id, asset_type, confidence, connectivity_status, criticality, criticality_username, data_providers, discovered_by, dns_domain.fqdn, dns_domain.isps, dns_domain.parent_domain, dns_domain.services.applications.category, dns_domain.services.applications.cpe, dns_domain.services.applications.name, dns_domain.services.applications.vendor, dns_domain.services.applications.version, dns_domain.services.cloud_provider, dns_domain.services.cpes, dns_domain.services.id, dns_domain.services.platform_name, dns_domain.services.port, dns_domain.services.protocol, dns_domain.services.protocol_port, dns_domain.services.status, dns_domain.services.status_code, dns_domain.services.transport, dns_domain.type, id, internet_exposure, ip.asn, ip.cloud_vm.instance_id, ip.cloud_vm.lifecycle, ip.cloud_vm.mac_address, ip.cloud_vm.owner_id, ip.cloud_vm.platform, ip.cloud_vm.region, ip.cloud_vm.security_groups, ip.cloud_vm.source, ip.cloud_vm.status, ip.fqdns, ip.isp, ip.location.area_code, ip.location.city, ip.location.country_code, ip.location.country_name, ip.location.postal_code, ip.location.region_code, ip.location.region_name, ip.location.timezone, ip.ptr, ip.aid, ip.services.applications.category, ip.services.applications.cpe, ip.services.applications.name, ip.services.applications.vendor, ip.services.applications.version, ip.services.cloud_provider, ip.services.cpes, ip.services.platform_name, ip.services.port, ip.services.protocol, ip.services.protocol_port, ip.services.status, ip.services.status_code, ip.services.transport, manual, perimeter, subsidiaries.id, subsidiaries.name, triage.action, triage.assigned_to, triage.status, triage.updated_by </br>Available filter fields that supports range comparisons (>, <, >=, <=): criticality_timestamp, dns_domain.resolved_ips, dns_domain.services.first_seen, dns_domain.services.last_seen, dns_domain.services.port, dns_domain.services.status_code, first_seen, ip.cloud_vm.private_ip, ip.cloud_vm.public_ip, ip.ip_address, ip.services.first_seen, ip.services.last_seen, ip.services.port, ip.services.status_code, last_seen, triage.updated_timestamp </br>All filter fields and operations supports negation (!)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get a list of external asset IDs that match the provided filter conditions. Use these IDs with the /entities/external-assets/v1 endpoint"""
        return self._call(operation="query_external_assets_v2", query_params={"after": after, "limit": limit, "sort": sort, "filter": filter}, error_message="query_external_assets_v2 failed", member_cid=member_cid)
