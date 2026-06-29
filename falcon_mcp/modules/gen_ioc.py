"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `ioc` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenIocModule(GeneratedModuleBase):
    """Generated tools for the Falcon `ioc` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_indicators_report, name="get_indicators_report")
        self._add_tool(server=server, method=self.indicator_aggregate_v1, name="indicator_aggregate_v1")
        self._add_tool(server=server, method=self.action_get_v1, name="action_get_v1")
        self._add_tool(server=server, method=self.action_query_v1, name="action_query_v1")
        self._add_tool(server=server, method=self.indicator_combined_v1, name="indicator_combined_v1")
        self._add_tool(server=server, method=self.indicator_get_device_count_v1, name="indicator_get_device_count_v1")
        self._add_tool(server=server, method=self.indicator_get_devices_ran_on_v1, name="indicator_get_devices_ran_on_v1")
        self._add_tool(server=server, method=self.indicator_get_processes_ran_on_v1, name="indicator_get_processes_ran_on_v1")
        self._add_tool(server=server, method=self.entities_processes, name="entities_processes")
        self._add_tool(server=server, method=self.ioc_type_query_v1, name="ioc_type_query_v1")
        self._add_tool(server=server, method=self.platform_query_v1, name="platform_query_v1")
        self._add_tool(server=server, method=self.severity_query_v1, name="severity_query_v1")
        self._add_tool(server=server, method=self.indicator_update_v1, name="indicator_update_v1", annotations=WRITE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def indicator_aggregate_v1(
        self,
        body: dict = Field(description="Request JSON body for `indicator_aggregate_v1` per the CrowdStrike API schema. Supports date_ranges, exclude, field, filter, from, include, interval, min_doc_count, missing, name, q, ranges, size, sort, sub_aggregates, time_zone, type."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get aggregate query result on Indicators resource."""
        return self._call(operation="indicator_aggregate_v1", query_params=None, body_params=body, error_message="indicator_aggregate_v1 failed", member_cid=member_cid)

    def entities_processes(
        self,
        ids: list[str] = Field(description="ProcessID for entities to look up. These are returned by indicator_get_processes_ran_on_v1."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """For the provided ProcessID retrieve the process details."""
        return self._call(operation="entities_processes", query_params={"ids": ids}, error_message="entities_processes failed", member_cid=member_cid)

    def get_indicators_report(
        self,
        body: dict = Field(description="Request JSON body for `GetIndicatorsReport` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Launch an indicators report creation job"""
        return self._call(operation="GetIndicatorsReport", query_params=None, body_params=body, error_message="GetIndicatorsReport failed", member_cid=member_cid)

    def action_get_v1(
        self,
        ids: list[str] | None = Field(default=None, description="The ids of the Actions to retrieve"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get Actions by ids."""
        return self._call(operation="action_get_v1", query_params={"ids": ids}, error_message="action_get_v1 failed", member_cid=member_cid)

    def action_query_v1(
        self,
        offset: str | None = Field(default=None, description="Starting index of overall result set from which to return ids."),
        limit: int | None = Field(default=None, description="Number of ids to return."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Query Actions."""
        return self._call(operation="action_query_v1", query_params={"offset": offset, "limit": limit}, error_message="action_query_v1 failed", member_cid=member_cid)

    def indicator_combined_v1(
        self,
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results."),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from. Offset and After params are mutually exclusive. If none provided then scrolling will be used by default. To access more than 10k iocs, use the 'after' parameter instead of 'offset'."),
        limit: int | None = Field(default=None, description="The maximum records to return."),
        sort: str | None = Field(default=None, description="The sort expression that should be used to sort the results."),
        after: str | None = Field(default=None, description="A pagination token used with the limit parameter to manage pagination of results. On your first request, don't provide an 'after' token. On subsequent requests, provide the 'after' token from the previous response to continue from that place in the results. To access more than 10k indicators, use the 'after' parameter instead of 'offset'."),
        from_parent: bool | None = Field(default=None, description="The filter for returning either only indicators for the request customer or its MSSP parents"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get Combined for Indicators."""
        return self._call(operation="indicator_combined_v1", query_params={"filter": filter, "offset": offset, "limit": limit, "sort": sort, "after": after, "from_parent": from_parent}, error_message="indicator_combined_v1 failed", member_cid=member_cid)

    def indicator_get_device_count_v1(
        self,
        type: str = Field(description="The type of the indicator. Valid types include: sha256: A hex-encoded sha256 hash string. Length - min: 64, max: 64. md5: A hex-encoded md5 hash string. Length - min 32, max: 32. domain: A domain name. Length - min: 1, max: 200. ipv4: An IPv4 address. Must be a valid IP address. ipv6: An IPv6 address. Must be a valid IP address."),
        value: str = Field(description="The string representation of the indicator"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get the number of devices the indicator has run on"""
        return self._call(operation="indicator_get_device_count_v1", query_params={"type": type, "value": value}, error_message="indicator_get_device_count_v1 failed", member_cid=member_cid)

    def indicator_get_devices_ran_on_v1(
        self,
        type: str = Field(description="The type of the indicator. Valid types include: sha256: A hex-encoded sha256 hash string. Length - min: 64, max: 64. md5: A hex-encoded md5 hash string. Length - min 32, max: 32. domain: A domain name. Length - min: 1, max: 200. ipv4: An IPv4 address. Must be a valid IP address. ipv6: An IPv6 address. Must be a valid IP address."),
        value: str = Field(description="The string representation of the indicator"),
        limit: str | None = Field(default=None, description="The maximum number of results to return. Use with the offset parameter to manage pagination of results."),
        offset: str | None = Field(default=None, description="The first process to return, where 0 is the latest offset. Use with the limit parameter to manage pagination of results."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get the IDs of devices the indicator has run on"""
        return self._call(operation="indicator_get_devices_ran_on_v1", query_params={"type": type, "value": value, "limit": limit, "offset": offset}, error_message="indicator_get_devices_ran_on_v1 failed", member_cid=member_cid)

    def indicator_get_processes_ran_on_v1(
        self,
        type: str = Field(description="The type of the indicator. Valid types include: sha256: A hex-encoded sha256 hash string. Length - min: 64, max: 64. md5: A hex-encoded md5 hash string. Length - min 32, max: 32. domain: A domain name. Length - min: 1, max: 200. ipv4: An IPv4 address. Must be a valid IP address. ipv6: An IPv6 address. Must be a valid IP address."),
        value: str = Field(description="The string representation of the indicator"),
        device_id: str = Field(description="Specify a host's ID to return only processes from that host. Get a host's ID from GET /devices/queries/devices/v1, the Falcon console, or the Streaming API."),
        limit: str | None = Field(default=None, description="The maximum number of results to return. Use with the offset parameter to manage pagination of results."),
        offset: str | None = Field(default=None, description="The first process to return, where 0 is the latest offset. Use with the limit parameter to manage pagination of results."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get the number of processes the indicator has run on"""
        return self._call(operation="indicator_get_processes_ran_on_v1", query_params={"type": type, "value": value, "device_id": device_id, "limit": limit, "offset": offset}, error_message="indicator_get_processes_ran_on_v1 failed", member_cid=member_cid)

    def indicator_update_v1(
        self,
        body: dict = Field(description="Request JSON body for `indicator_update_v1` per the CrowdStrike API schema (required)."),
        retrodetects: bool | None = Field(default=None, description="Whether to submit to retrodetects"),
        ignore_warnings: bool | None = Field(default=None, description="Set to true to ignore warnings and add all IOCs"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update Indicators."""
        return self._call(operation="indicator_update_v1", query_params={"retrodetects": retrodetects, "ignore_warnings": ignore_warnings}, body_params=body, error_message="indicator_update_v1 failed", member_cid=member_cid)

    def ioc_type_query_v1(
        self,
        offset: str | None = Field(default=None, description="Starting index of overall result set from which to return ids."),
        limit: int | None = Field(default=None, description="Number of ids to return."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Query IOC Types."""
        return self._call(operation="ioc_type_query_v1", query_params={"offset": offset, "limit": limit}, error_message="ioc_type_query_v1 failed", member_cid=member_cid)

    def platform_query_v1(
        self,
        offset: str | None = Field(default=None, description="Starting index of overall result set from which to return ids."),
        limit: int | None = Field(default=None, description="Number of ids to return."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Query Platforms."""
        return self._call(operation="platform_query_v1", query_params={"offset": offset, "limit": limit}, error_message="platform_query_v1 failed", member_cid=member_cid)

    def severity_query_v1(
        self,
        offset: str | None = Field(default=None, description="Starting index of overall result set from which to return ids."),
        limit: int | None = Field(default=None, description="Number of ids to return."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Query Severities."""
        return self._call(operation="severity_query_v1", query_params={"offset": offset, "limit": limit}, error_message="severity_query_v1 failed", member_cid=member_cid)
