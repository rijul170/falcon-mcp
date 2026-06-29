"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `hosts` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenHostsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `hosts` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.combined_devices_by_filter, name="combined_devices_by_filter")
        self._add_tool(server=server, method=self.combined_hidden_devices_by_filter, name="combined_hidden_devices_by_filter")
        self._add_tool(server=server, method=self.get_device_details_v2, name="get_device_details_v2")
        self._add_tool(server=server, method=self.query_device_login_history_v2, name="query_device_login_history_v2")
        self._add_tool(server=server, method=self.query_get_network_address_history_v1, name="query_get_network_address_history_v1")
        self._add_tool(server=server, method=self.query_hidden_devices, name="query_hidden_devices")
        self._add_tool(server=server, method=self.entities_perform_action, name="entities_perform_action", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def combined_devices_by_filter(
        self,
        offset: str | None = Field(default=None, description="The offset to page from, provided from the previous call as the 'next' value, for the next result set. For the first call, do not supply an offset."),
        limit: int | None = Field(default=None, description="The maximum records to return. [1-10000]"),
        sort: str | None = Field(default=None, description="The property to sort by (e.g. status.desc or hostname.asc). If not specified, the default sort will be device_id.asc. This should be supplied for each consecutive call."),
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results. This should be supplied for each consecutive call."),
        fields: str | None = Field(default=None, description="The fields to return, comma delimited if specifying more than one field. For example: fields=hostname,device_id would return device records only containing the hostname and device_id"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for hosts in your environment by platform, hostname, IP, and other criteria. Returns full device records."""
        return self._call(operation="CombinedDevicesByFilter", query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter, "fields": fields}, error_message="CombinedDevicesByFilter failed", member_cid=member_cid)

    def combined_hidden_devices_by_filter(
        self,
        offset: str | None = Field(default=None, description="The offset to page from, provided from the previous call as the 'next' value, for the next result set. For the first call, do not supply an offset."),
        limit: int | None = Field(default=None, description="The maximum records to return. [1-10000]"),
        sort: str | None = Field(default=None, description="The property to sort by (e.g. status.desc or hostname.asc). If not specified, the default sort will be device_id.asc. This should be supplied for each consecutive call."),
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results. This should be supplied for each consecutive call."),
        fields: str | None = Field(default=None, description="The fields to return, comma delimited if specifying more than one field. For example: fields=hostname,device_id would return device records only containing the hostname and device_id"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for hidden hosts in your environment by platform, hostname, IP, and other criteria. Returns full device records."""
        return self._call(operation="CombinedHiddenDevicesByFilter", query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter, "fields": fields}, error_message="CombinedHiddenDevicesByFilter failed", member_cid=member_cid)

    def get_device_details_v2(
        self,
        ids: list[str] = Field(description="The host agentIDs used to get details on"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get details on one or more hosts by providing host IDs as a query parameter. Supports up to a maximum 100 IDs."""
        return self._call(operation="GetDeviceDetailsV2", query_params={"ids": ids}, error_message="GetDeviceDetailsV2 failed", member_cid=member_cid)

    def query_device_login_history_v2(
        self,
        body: dict = Field(description="Request JSON body for `QueryDeviceLoginHistoryV2` per the CrowdStrike API schema (required)."),
        limit: int | None = Field(default=None, description="The maximum number of results to return [1-100]."),
        from_: str | None = Field(default=None, description="The inclusive beginning of the time window to search."),
        to: str | None = Field(default=None, description="The inclusive end of the time window to search."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve details about recent interactive login sessions for a set of devices powered by the Host Timeline. A max of 10 device ids can be specified"""
        return self._call(operation="QueryDeviceLoginHistoryV2", query_params={"limit": limit, "from": from_, "to": to}, body_params=body, error_message="QueryDeviceLoginHistoryV2 failed", member_cid=member_cid)

    def query_get_network_address_history_v1(
        self,
        body: dict = Field(description="Request JSON body for `QueryGetNetworkAddressHistoryV1` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve history of IP and MAC addresses of devices."""
        return self._call(operation="QueryGetNetworkAddressHistoryV1", query_params=None, body_params=body, error_message="QueryGetNetworkAddressHistoryV1 failed", member_cid=member_cid)

    def query_hidden_devices(
        self,
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        limit: int | None = Field(default=None, description="The maximum records to return. [1-5000]"),
        sort: str | None = Field(default=None, description="The property to sort by (e.g. status.desc or hostname.asc)"),
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve hidden hosts that match the provided filter criteria."""
        return self._call(operation="QueryHiddenDevices", query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter}, error_message="QueryHiddenDevices failed", member_cid=member_cid)

    def entities_perform_action(
        self,
        ids: list[str] = Field(description="Entity IDs (e.g. prevention policy IDs) to perform the action on. These are NOT host device IDs or host group IDs — use falcon_perform_host_action for host containment."),
        action_name: str = Field(description="The action to perform on the entities (e.g. 'add-group-policy', 'remove-group-policy')."),
        body: dict = Field(description="Request JSON body for `entities_perform_action` per the CrowdStrike API schema. Contains action-specific payload fields."),
        disable_hostname_check: bool | None = Field(default=None, description="Disable hostname check on add-member operations."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Perform a policy group action on specified entity IDs (POST /devices/entities/group-actions/v1). NOTE: This endpoint acts on policy/group entity IDs, NOT on host device IDs. For host containment use falcon_perform_host_action instead."""
        return self._call(operation="entities_perform_action", query_params={"ids": ids, "action_name": action_name, "disable_hostname_check": disable_hostname_check}, body_params=body, error_message="entities_perform_action failed", member_cid=member_cid)
