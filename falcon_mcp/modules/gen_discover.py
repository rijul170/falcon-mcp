"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `discover` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenDiscoverModule(GeneratedModuleBase):
    """Generated tools for the Falcon `discover` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_accounts, name="get_accounts")
        self._add_tool(server=server, method=self.get_applications, name="get_applications")
        self._add_tool(server=server, method=self.get_hosts, name="get_hosts")
        self._add_tool(server=server, method=self.get_iot_hosts, name="get_iot_hosts")
        self._add_tool(server=server, method=self.get_logins, name="get_logins")
        self._add_tool(server=server, method=self.query_accounts, name="query_accounts")
        self._add_tool(server=server, method=self.query_applications, name="query_applications")
        self._add_tool(server=server, method=self.query_hosts, name="query_hosts")
        self._add_tool(server=server, method=self.query_iot_hosts_v2, name="query_iot_hosts_v2")
        self._add_tool(server=server, method=self.query_logins, name="query_logins")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def get_accounts(
        self,
        ids: list[str] = Field(description="One or more account IDs (max: 100). Find account IDs with GET /discover/queries/accounts/v1"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get details on accounts by providing one or more IDs."""
        return self._call(operation="get_accounts", query_params={"ids": ids}, error_message="get_accounts failed", member_cid=member_cid)

    def get_applications(
        self,
        ids: list[str] = Field(description="The IDs of applications to retrieve. (Min: 1, Max: 100)"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get details on applications by providing one or more IDs."""
        return self._call(operation="get_applications", query_params={"ids": ids}, error_message="get_applications failed", member_cid=member_cid)

    def get_hosts(
        self,
        ids: list[str] = Field(description="One or more asset IDs (max: 100). Find asset IDs with GET /discover/queries/hosts/v1"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get details on assets by providing one or more IDs."""
        return self._call(operation="get_hosts", query_params={"ids": ids}, error_message="get_hosts failed", member_cid=member_cid)

    def get_iot_hosts(
        self,
        ids: list[str] = Field(description="One or more asset IDs (max: 100). Find asset IDs with GET /discover/queries/iot-hosts/v1"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get details on IoT assets by providing one or more IDs."""
        return self._call(operation="get_iot_hosts", query_params={"ids": ids}, error_message="get_iot_hosts failed", member_cid=member_cid)

    def get_logins(
        self,
        ids: list[str] = Field(description="One or more login IDs (max: 100). Find login IDs with GET /discover/queries/logins/v1"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get details on logins by providing one or more IDs."""
        return self._call(operation="get_logins", query_params={"ids": ids}, error_message="get_logins failed", member_cid=member_cid)

    def query_accounts(
        self,
        offset: int | None = Field(default=None, description="An offset used with the limit parameter to manage pagination of results. On your first request, don’t provide an offset. On subsequent requests, add previous offset with the previous limit to continue from that place in the results."),
        limit: int | None = Field(default=None, description="The number of account IDs to return in this response (min: 1, max: 100, default: 100). Use with the offset parameter to manage pagination of results."),
        sort: str | None = Field(default=None, description="Sort accounts by their properties. A single sort field is allowed. Common sort options include: <ul><li>username|asc</li><li>last_failed_login_timestamp|desc</li></ul>"),
        filter: str | None = Field(default=None, description="Filter accounts using an FQL query. Common filter options include:<ul><li>account_type :'Local'</li><li>admin_privileges:'Yes'</li><li>first_seen_timestamp:<'now-7d'</li><li>last_successful_login_type:'Terminal server'</li></ul> Available filter fields that support exact match: id, cid, user_sid, account_name, username, account_type, admin_privileges, first_seen_timestamp, last_successful_login_type, last_successful_login_timestamp, last_successful_login_hostname, last_successful_login_remote_ip, last_successful_login_host_country, last_successful_login_host_city, login_domain, last_failed_login_type, last_failed_login_timestamp, last_failed_login_hostname, password_last_set_timestamp, local_admin_privileges Available filter fields that supports wildcard (*): id, cid, user_sid, account_name, username, account_type, admin_privileges, last_successful_login_type, last_successful_login_hostname, last_successful_login_remote_ip, last_successful_login_host_country, last_successful_login_host_city, login_domain, last_failed_login_type, last_failed_login_hostname, local_admin_privileges Available filter fields that supports range comparisons (>, <, >=, <=): first_seen_timestamp, last_successful_login_timestamp,last_failed_login_timestamp, password_last_set_timestamp All filter fields and operations supports negation (!)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for accounts in your environment by providing an FQL (Falcon Query Language) filter and paging details. Returns a set of account IDs which match the filter criteria."""
        return self._call(operation="query_accounts", query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter}, error_message="query_accounts failed", member_cid=member_cid)

    def query_applications(
        self,
        offset: int | None = Field(default=None, description="An offset used with the limit parameter to manage pagination of results. On your first request, don’t provide an offset. On subsequent requests, add previous offset with the previous limit to continue from that place in the results."),
        limit: int | None = Field(default=None, description="The number of application ids to return in this response (Min: 1, Max: 100, Default: 100)."),
        sort: str | None = Field(default=None, description="Sort applications by their properties. A single sort field is allowed."),
        filter: str | None = Field(default=None, description="Search for applications in your environment by providing an FQL filter. Available filter fields that support exact match: name, version, vendor, name_vendor, name_vendor_version, first_seen_timestamp, installation_timestamp, architectures, installation_paths, versioning_scheme, groups, is_normalized, last_used_user_sid, last_used_user_name, last_used_file_name, last_used_file_hash, last_used_timestamp, last_updated_timestamp, is_suspicious, category, host.id, host.platform_name, host.hostname, cid, host.os_version, host.machine_domain, host.ou, host.site_name, host.country, host.current_mac_address, host.current_network_prefix, host.tags, host.groups, host.product_type_desc, host.kernel_version, host.system_manufacturer, host.internet_exposure, host.agent_version, host.external_ip, host.aid Available filter fields that supports wildcard (*): name, version, vendor, name_vendor, name_vendor_version, architectures, installation_paths, groups, last_used_user_sid, last_used_user_name, last_used_file_name, last_used_file_hash, host.platform_name, host.hostname, cid, host.os_version, host.machine_domain, host.ou, host.site_name, host.country, host.current_mac_address, host.current_network_prefix, host.tags, host.groups, host.product_type_desc, host.kernel_version, host.system_manufacturer, host.internet_exposure, host.agent_version, host.external_ip, host.aid Available filter fields that supports range comparisons (>, <, >=, <=): first_seen_timestamp, installation_timestamp, last_used_timestamp, last_updated_timestamp All filter fields and operations supports negation (!)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for applications in your environment by providing an FQL filter and paging details. returns a set of application IDs which match the filter criteria."""
        return self._call(operation="query_applications", query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter}, error_message="query_applications failed", member_cid=member_cid)

    def query_hosts(
        self,
        offset: int | None = Field(default=None, description="An offset used with the limit parameter to manage pagination of results. On your first request, don’t provide an offset. On subsequent requests, add previous offset with the previous limit to continue from that place in the results."),
        limit: int | None = Field(default=None, description="The number of asset IDs to return in this response (min: 1, max: 100, default: 100). Use with the offset parameter to manage pagination of results."),
        sort: str | None = Field(default=None, description="Sort assets by their properties. A single sort field is allowed. Common sort options include: <ul><li>hostname|asc</li><li>product_type_desc|desc</li></ul>"),
        filter: str | None = Field(default=None, description="Filter assets using an FQL query. Common filter options include:<ul><li>entity_type:'m anaged'</li><li>product_type_desc:'Workstation'</li><li>platform_name:'Windows'</li><li>last_seen_timestamp:>' now-7d'</li></ul> Available filter fields that support exact match: id, aid, entity_type, country, city, platform_name, os_version, kernel_version, product_type_desc, tags, groups, agent_version, system_product_name, system_manufacturer, system_serial_number, bios_manufacturer, bios_version, ou, machine_domain, site_name, external_ip, hostname, local_ips_count, network_interfaces.local_ip, network_interfaces.mac_address, network_interfaces.interface_alias, network_interfaces.interface_description, network_interfaces.network_prefix, last_discoverer_aid, discoverer_count, discoverer_aids, discoverer_tags, discoverer_platform_names, discoverer_product_type_descs, confidence, internet_exposure, os_is_eol, data_providers, data_providers_count, mac_addresses, local_ip_addresses, reduced_functionality_mode, number_of_disk_drives, processor_package_count, physical_core_count, logical_core_count, total_disk_space, disk_sizes.disk_name, disk_sizes.disk_space, cpu_processor_name, total_memory, encryption_status, encrypted_drives, encrypted_drives_count, unencrypted_drives, unencrypted_drives_count, os_security.secure_boot_requested_status, os_security.device_guard_status, os_security.device_guard_status, os_security.device_guard_status, os_security.system_guard_status, os_security.credential_guard_status, os_security.iommu_protection_status, os_security.secure_boot_enabled_status, os_security.uefi_memory_protection_status, os_security.virtualization_based_security_status, os_security.kernel_dma_protection_status, total_bios_files, bios_hashes_data.sha256_hash, bios_hashes_data.measurement_type, bios_id, average_processor_usage, average_memory_usage, average_memory_usage_pct, max_processor_usage, max_memory_usage, max_memory_usage_pct, used_disk_space, used_disk_space_pct, available_disk_space, available_disk_space_pct, mount_storage_info.mount_path, mount_storage_info.used_space, mount_storage_info.available_space, form_factor, servicenow_id, owned_by, managed_by, assigned_to, department, fqdn, used_for, object_guid, object_sid, ad_user_account_control, account_enabled, creation_timestamp, email, os_service_pack, location, state, cpu_manufacturer, discovering_by, scan_details.scan_id, scan_details.schedule_id Available filter fields that supports wildcard (*): id, aid, entity_type, country, city, platform_name, os_version, kernel_version, product_type_desc, tags, groups, agent_version, system_product_name, system_manufacturer, system_serial_number, bios_manufacturer, bios_version, ou, machine_domain, site_name, external_ip, hostname, network_interfaces.local_ip, network_interfaces.mac_address, network_interfaces.interface_alias, network_interfaces.interface_description, network_interfaces.network_prefix, last_discoverer_aid, discoverer_aids, discoverer_tags, discoverer_platform_names, discoverer_product_type_descs, confidence, internet_exposure, os_is_eol, data_providers, mac_addresses, local_ip_addresses, reduced_functionality_mode, disk_sizes.disk_name, cpu_processor_name, encryption_status, encrypted_drives, unencrypted_drives, os_security.secure_boot_requested_status, os_security.device_guard_status, os_security.device_guard_status, os_security.device_guard_status, os_security.system_guard_status, os_security.credential_guard_status, os_security.iommu_protection_status, os_security.secure_boot_enabled_status, os_security.uefi_memory_protection_status, os_security.virtualization_based_security_status, os_security.kernel_dma_protection_status, bios_hashes_data.sha256_hash, bios_hashes_data.measurement_type, bios_id, mount_storage_info.mount_path, form_factor, servicenow_id, owned_by, managed_by, assigned_to, department, fqdn, used_for, object_guid, object_sid, account_enabled, email, os_service_pack, location, state, cpu_manufacturer, discovering_by, scan_details.scan_id, scan_details.schedule_id Available filter fields that supports range comparisons (>, <, >=, <=): first_seen_timestamp, last_seen_timestamp, local_ips_count, discoverer_count, confidence, number_of_disk_drives, processor_package_count, physical_core_count, data_providers_count, logical_core_count, total_disk_space, disk_sizes.disk_space, total_memory, encrypted_drives_count, unencrypted_drives_count, total_bios_files, average_processor_usage, average_memory_usage, average_memory_usage_pct, max_processor_usage, max_memory_usage, max_memory_usage_pct, used_disk_space, used_disk_space_pct, available_disk_space, available_disk_space_pct, mount_storage_info.used_space, mount_storage_info.available_space, ad_user_account_control, creation_timestamp, scan_details.scan_date, vulnerability_assessment_date All filter fields and operations supports negation (!)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for assets in your environment by providing an FQL (Falcon Query Language) filter and paging details. Returns a set of asset IDs which match the filter criteria."""
        return self._call(operation="query_hosts", query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter}, error_message="query_hosts failed", member_cid=member_cid)

    def query_iot_hosts_v2(
        self,
        after: str | None = Field(default=None, description="A pagination token used with the limit parameter to manage pagination of results. On your first request, don't provide an after token. On subsequent requests, provide the after token from the previous response to continue from that place in the results."),
        limit: int | None = Field(default=None, description="The number of asset IDs to return in this response (min: 1, max: 100, default: 100). Use with the after parameter to manage pagination of results."),
        sort: str | None = Field(default=None, description="Sort assets by their properties. A single sort field is allowed. Common sort options include: <ul><li>hostname|asc</li><li>product_type_desc|desc</li></ul>"),
        filter: str | None = Field(default=None, description="Filter assets using an FQL query. Common filter options include:<ul><li>entity_type:'m anaged'</li><li>product_type_desc:'Workstation'</li><li>platform_name:'Windows'</li><li>last_seen_timestamp:>' now-7d'</li></ul> Available filter fields that support exact match: device_family, device_class, device_type, device_mode, business_criticality, line_of_business, virtual_zone, subnet, purdue_level, vlan, local_ip_addresses, mac_addresses, physical_connections_count, data_providers Available filter fields that supports wildcard (*): device_family, device_class, device_type, device_mode, business_criticality, line_of_business, virtual_zone, subnet, purdue_level, vlan, local_ip_addresses, mac_addresses, data_providers Available filter fields that supports range comparisons (>, <, >=, <=): physical_connections_count All filter fields and operations supports negation (!)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for IoT assets in your environment by providing an FQL (Falcon Query Language) filter and paging details. Returns a set of asset IDs which match the filter criteria."""
        return self._call(operation="query_iot_hostsV2", query_params={"after": after, "limit": limit, "sort": sort, "filter": filter}, error_message="query_iot_hostsV2 failed", member_cid=member_cid)

    def query_logins(
        self,
        offset: int | None = Field(default=None, description="An offset used with the limit parameter to manage pagination of results. On your first request, don’t provide an offset. On subsequent requests, add previous offset with the previous limit to continue from that place in the results."),
        limit: int | None = Field(default=None, description="The number of login IDs to return in this response (min: 1, max: 100, default: 100). Use with the offset parameter to manage pagination of results."),
        sort: str | None = Field(default=None, description="Sort logins by their properties. A single sort field is allowed. Common sort options include: <ul><li>account_name|asc</li><li>login_timestamp|desc</li></ul>"),
        filter: str | None = Field(default=None, description="Filter logins using an FQL query. Common filter options include:<ul><li>account_type:' Local'</li><li>login_type:'Interactive'</li><li>first_seen_timestamp:<'now-7d'</li><li>admin_privileges:'No'</li></ul> Available filter fields that support exact match: id, cid, login_status, account_id, host_id, user_sid, aid, account_name, username, hostname, account_type, login_type, login_timestamp, login_domain, admin_privileges, local_admin_privileges, local_ip, remote_ip, host_country, host_city, is_suspicious, failure_description, login_event_count, aggregation_time_interval Available filter fields that supports wildcard (*): id, cid, login_status, account_id, host_id, user_sid, aid, account_name, username, hostname, account_type, login_type, login_domain, admin_privileges, local_admin_privileges, local_ip, remote_ip, host_country, host_city, failure_description, aggregation_time_interval Available filter fields that supports range comparisons (>, <, >=, <=): login_timestamp, login_event_count All filter fields and operations supports negation (!)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for logins in your environment by providing an FQL (Falcon Query Language) filter and paging details. Returns a set of login IDs which match the filter criteria."""
        return self._call(operation="query_logins", query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter}, error_message="query_logins failed", member_cid=member_cid)
