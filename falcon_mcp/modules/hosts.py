"""
Hosts module for Falcon MCP Server

This module provides tools for accessing and managing CrowdStrike Falcon hosts/devices.
"""

from textwrap import dedent
from typing import Any

from mcp.server import FastMCP
from mcp.server.fastmcp.resources import TextResource
from mcp.types import ToolAnnotations
from pydantic import AnyUrl, Field

from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule
from falcon_mcp.resources.hosts import SEARCH_HOSTS_FQL_DOCUMENTATION

logger = get_logger(__name__)


class HostsModule(BaseModule):
    """Module for accessing and managing CrowdStrike Falcon hosts/devices."""

    def register_tools(self, server: FastMCP) -> None:
        """Register tools with the MCP server.

        Args:
            server: MCP server instance
        """
        # Register tools
        self._add_tool(
            server=server,
            method=self.search_hosts,
            name="search_hosts",
        )

        self._add_tool(
            server=server,
            method=self.get_host_details,
            name="get_host_details",
        )

        self._add_tool(
            server=server,
            method=self.perform_host_action,
            name="perform_host_action",
            annotations=ToolAnnotations(
                readOnlyHint=False,
                destructiveHint=True,
                idempotentHint=False,
                openWorldHint=True,
            ),
        )

        self._add_tool(
            server=server,
            method=self.get_host_online_state,
            name="get_host_online_state",
        )

        self._add_tool(
            server=server,
            method=self.scroll_hosts,
            name="scroll_hosts",
        )

        self._add_tool(
            server=server,
            method=self.update_host_tags,
            name="update_host_tags",
            annotations=ToolAnnotations(
                readOnlyHint=False,
                destructiveHint=False,
                idempotentHint=False,
                openWorldHint=True,
            ),
        )

        self._add_tool(server=server, method=self.get_device_login_history, name="get_device_login_history")
        self._add_tool(server=server, method=self.get_device_network_address_history, name="get_device_network_address_history")
        self._add_tool(server=server, method=self.list_host_retention_policy_info, name="list_host_retention_policy_info")
        self._add_tool(server=server, method=self.get_log_collector_policy_info, name="get_log_collector_policy_info")

    def register_resources(self, server: FastMCP) -> None:
        """Register resources with the MCP server.

        Args:
            server: MCP server instance
        """
        search_hosts_fql_resource = TextResource(
            uri=AnyUrl("falcon://hosts/search/fql-guide"),
            name="falcon_search_hosts_fql_guide",
            description="Contains the guide for the `filter` param of the `falcon_search_hosts` tool.",
            text=SEARCH_HOSTS_FQL_DOCUMENTATION,
        )

        self._add_resource(
            server,
            search_hosts_fql_resource,
        )

    def search_hosts(
        self,
        filter: str | None = Field(
            default=None,
            description="FQL Syntax formatted string used to limit the results. IMPORTANT: use the `falcon://hosts/search/fql-guide` resource when building this filter parameter.",
            examples={"platform_name:'Windows'", "hostname:'PC*'"},
        ),
        limit: int = Field(
            default=10,
            ge=1,
            le=5000,
            description="The maximum records to return. [1-5000]",
        ),
        offset: int | None = Field(
            default=None,
            description="The offset to start retrieving records from.",
        ),
        sort: str | None = Field(
            default=None,
            description=dedent("""
                Sort hosts using these options:

                hostname: Host name/computer name
                last_seen: Timestamp when the host was last seen
                first_seen: Timestamp when the host was first seen
                modified_timestamp: When the host record was last modified
                platform_name: Operating system platform
                agent_version: CrowdStrike agent version
                os_version: Operating system version
                external_ip: External IP address

                Sort either asc (ascending) or desc (descending).
                Both formats are supported: 'hostname.desc' or 'hostname|desc'

                Examples: 'hostname.asc', 'last_seen.desc', 'platform_name.asc'
            """).strip(),
            examples={"hostname.asc", "last_seen.desc"},
        ),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID to scope this call to a specific child tenant. Obtain child CIDs from `falcon_list_child_accounts`. Leave unset to use the parent account scope.",
        ),
    ) -> list[dict[str, Any]]:
        """Search for hosts in your CrowdStrike environment.

        IMPORTANT: You must use the `falcon://hosts/search/fql-guide` resource when you need to use the `filter` parameter.
        This resource contains the guide on how to build the FQL `filter` parameter for the `falcon_search_hosts` tool.
        """
        device_ids = self._base_search_api_call(
            operation="QueryDevicesByFilter",
            search_params={
                "filter": filter,
                "limit": limit,
                "offset": offset,
                "sort": sort,
            },
            error_message="Failed to search hosts",
            member_cid=member_cid,
        )

        if self._is_error(device_ids):
            return [device_ids]

        if device_ids:
            details = self._base_get_by_ids(
                operation="PostDeviceDetailsV2",
                ids=device_ids,
                id_key="ids",
                member_cid=member_cid,
            )

            if self._is_error(details):
                return [details]

            return details

        return []

    def get_host_details(
        self,
        ids: list[str] = Field(
            description="Host device IDs to retrieve details for. You can get device IDs from the search_hosts operation, the Falcon console, or the Streaming API. Maximum: 5000 IDs per request."
        ),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID to scope this call to a specific child tenant. Obtain child CIDs from `falcon_list_child_accounts`. Leave unset to use the parent account scope.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Retrieve detailed information for specified host device IDs.

        This tool returns comprehensive host details for one or more device IDs.
        Use this when you already have specific device IDs and need their full details.
        For searching/discovering hosts, use the `falcon_search_hosts` tool instead.
        """
        logger.debug("Getting host details for IDs: %s", ids)

        if not ids:
            return []

        return self._base_get_by_ids(
            operation="PostDeviceDetailsV2",
            ids=ids,
            id_key="ids",
            member_cid=member_cid,
        )

    def scroll_hosts(
        self,
        filter: str | None = Field(
            default=None,
            description="FQL Syntax filter. IMPORTANT: use the `falcon://hosts/search/fql-guide` resource when building this parameter.",
        ),
        limit: int = Field(
            default=100,
            ge=1,
            le=5000,
            description="Maximum host IDs to return per page (max 5000). Use with `after` for cursor-based pagination.",
        ),
        sort: str | None = Field(
            default=None,
            description="Sort expression. Examples: `hostname.asc`, `last_seen.desc`.",
        ),
        after: str | None = Field(
            default=None,
            description="Pagination cursor from a previous `falcon_scroll_hosts` response. Omit for the first page.",
        ),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID to scope this call to a specific child tenant.",
        ),
    ) -> dict[str, Any]:
        """Scroll through hosts using cursor-based pagination for large estates (>10k hosts).

        Unlike `falcon_search_hosts` which uses offset pagination, this tool uses an `after`
        cursor that scales to estates of any size. Returns host details plus a `next_after`
        cursor — pass that value as `after` in the next call to get the next page.
        When `next_after` is null, you have reached the last page.
        """
        from falcon_mcp.common.utils import prepare_api_parameters

        params = prepare_api_parameters({"filter": filter, "limit": limit, "sort": sort, "after": after})
        response = self.client.command_for("QueryDevicesByFilterScroll", member_cid=member_cid, parameters=params)

        if not isinstance(response, dict) or response.get("status_code") not in (200, None):
            body = response.get("body", {}) if isinstance(response, dict) else {}
            errors = body.get("errors", [])
            return {"error": errors[0].get("message", "Scroll failed") if errors else "Scroll failed"}

        body = response.get("body", {})
        ids = body.get("resources", []) or []
        pagination = body.get("meta", {}).get("pagination", {})
        next_after = pagination.get("after")
        total = pagination.get("total")

        if not ids:
            return {"hosts": [], "next_after": None, "total": total}

        details = self._base_get_by_ids(
            operation="PostDeviceDetailsV2",
            ids=ids,
            id_key="ids",
            member_cid=member_cid,
        )
        if self._is_error(details):
            return {"error": details, "next_after": next_after, "total": total}

        return {"hosts": details, "next_after": next_after, "total": total, "returned": len(ids)}

    def perform_host_action(
        self,
        device_ids: list[str] = Field(
            description="Host device IDs (AIDs) to perform the action on. Obtain from `falcon_search_hosts`.",
        ),
        action: str = Field(
            description=dedent("""
                Action to perform on the specified hosts:
                • contain — Network-isolate the host (blocks all traffic except Falcon sensor)
                • lift_containment — Remove network containment from the host
                • hide_host — Hide the host from the Falcon console (sensor remains active)
                • unhide_host — Restore a hidden host to the Falcon console
                • detection_suppress — Suppress future detections for the host
                • detection_unsuppress — Re-enable detections for the host
            """).strip(),
            examples=["contain", "lift_containment", "hide_host", "unhide_host", "detection_suppress", "detection_unsuppress"],
        ),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID to scope this call to a specific child tenant. Obtain child CIDs from `falcon_list_child_accounts`. Leave unset to use the parent account scope.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Perform a containment or visibility action on one or more hosts.

        IMPORTANT: `contain` isolates a host from the network — only Falcon sensor traffic
        is allowed. Confirm intent before containing production systems. Use `lift_containment`
        to restore normal network access after investigation.
        """
        return self._base_query_api_call(
            operation="PerformActionV2",
            query_params={"action_name": action},
            body_params={"ids": device_ids},
            error_message=f"Failed to perform host action '{action}'",
            member_cid=member_cid,
        )

    def get_host_online_state(
        self,
        ids: list[str] = Field(
            description="Host device IDs (AIDs) to check online state for. Obtain from `falcon_search_hosts`.",
        ),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID to scope this call to a specific child tenant. Obtain child CIDs from `falcon_list_child_accounts`. Leave unset to use the parent account scope.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Check the current online/offline state of one or more hosts.

        Returns per-host state: online, offline, or unknown. Useful before initiating
        RTR sessions or containment to confirm reachability.
        """
        return self._base_get_by_ids(
            operation="GetOnlineState_V1",
            ids=ids,
            id_key="ids",
            use_params=True,
            member_cid=member_cid,
        )

    def update_host_tags(
        self,
        device_ids: list[str] = Field(
            description="Host device IDs (AIDs) to tag. Obtain from `falcon_search_hosts`.",
        ),
        tags: list[str] = Field(
            description="Falcon Grouping Tags to add or remove. Format: `FalconGroupingTags/tag-name`. Example: `['FalconGroupingTags/IR-2024-001', 'FalconGroupingTags/quarantine']`.",
            examples=[["FalconGroupingTags/IR-2024-001"], ["FalconGroupingTags/quarantine"]],
        ),
        action: str = Field(
            default="add",
            description="Tag action: `add` to attach tags, `remove` to detach tags.",
        ),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID to scope this call to a specific child tenant. Obtain child CIDs from `falcon_list_child_accounts`. Leave unset to use the parent account scope.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Add or remove Falcon Grouping Tags on one or more hosts.

        Tags are used to group hosts for policy assignment, reporting, and filtering.
        Tags must use the `FalconGroupingTags/` prefix.
        """
        return self._base_query_api_call(
            operation="UpdateDeviceTags",
            body_params={
                "action": action,
                "device_ids": device_ids,
                "tags": tags,
            },
            error_message="Failed to update host tags",
            member_cid=member_cid,
        )

    def get_device_login_history(
        self,
        device_ids: list[str] = Field(
            description="Host device IDs (AIDs) to retrieve login history for. Maximum 10 IDs per request. Obtain from `falcon_search_hosts`.",
        ),
        limit: int | None = Field(
            default=None,
            description="Maximum number of login events to return per device [1-100].",
        ),
        from_time: str | None = Field(
            default=None,
            description="Inclusive start of the time window (ISO 8601, e.g. '2024-01-01T00:00:00Z').",
        ),
        to_time: str | None = Field(
            default=None,
            description="Inclusive end of the time window (ISO 8601, e.g. '2024-01-02T00:00:00Z').",
        ),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID to scope this call to a specific child tenant.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Retrieve recent interactive login sessions for one or more hosts.

        Returns login history including usernames, login timestamps, and login types.
        Critical for IR investigations: use this to identify who was logged in during
        a suspected incident window and trace lateral movement via account activity.
        Maximum 10 device IDs per request.
        """
        from falcon_mcp.common.utils import prepare_api_parameters

        params = prepare_api_parameters({"limit": limit, "from": from_time, "to": to_time})
        response = self.client.command_for(
            "QueryDeviceLoginHistoryV2",
            member_cid=member_cid,
            parameters=params,
            data={"device_ids": device_ids},
        )
        if not isinstance(response, dict) or response.get("status_code") not in (200, None):
            body = response.get("body", {}) if isinstance(response, dict) else {}
            errors = body.get("errors", [])
            return {"error": errors[0].get("message", "Login history query failed") if errors else "Login history query failed"}

        return (response.get("body") or {}).get("resources") or []

    def get_device_network_address_history(
        self,
        device_ids: list[str] = Field(
            description="Host device IDs (AIDs) to retrieve network address history for. Obtain from `falcon_search_hosts`.",
        ),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID to scope this call to a specific child tenant.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Retrieve the historical IP and MAC address records for one or more hosts.

        Returns timestamped records of IP and MAC address changes. Critical for IR:
        use this to trace lateral movement by pivoting on historical IPs, identify
        VPN/NAT assignment patterns, and correlate network events to specific hosts.
        """
        response = self.client.command_for(
            "QueryGetNetworkAddressHistoryV1",
            member_cid=member_cid,
            data={"device_ids": device_ids},
        )
        if not isinstance(response, dict) or response.get("status_code") not in (200, None):
            body = response.get("body", {}) if isinstance(response, dict) else {}
            errors = body.get("errors", [])
            return {"error": errors[0].get("message", "Network address history query failed") if errors else "Network address history query failed"}

        return (response.get("body") or {}).get("resources") or []

    def list_host_retention_policy_info(
        self,
        sample_size: int = Field(
            default=50,
            ge=1,
            le=500,
            description="Number of hosts to sample for retention policy distribution.",
        ),
        filter: str | None = Field(
            default=None,
            description="Optional FQL filter to narrow the host sample (e.g. `platform_name:'Windows'`).",
        ),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID for MSSP child tenant scoping.",
        ),
    ) -> dict[str, Any]:
        """Report the host retention policy distribution across hosts in a tenant.

        NOTE: Host Retention Policy write operations are NOT available via the
        CrowdStrike API. Policy assignment must be done via the Falcon Console UI.
        This tool is READ-ONLY — it samples hosts and aggregates their
        `device_policies.host_retention` field into a distribution summary.
        """
        from falcon_mcp.common.utils import prepare_api_parameters
        params = prepare_api_parameters({"limit": sample_size, "filter": filter})
        id_resp = self.client.command_for("QueryDevicesByFilter", member_cid=member_cid, parameters=params)
        if not isinstance(id_resp, dict) or id_resp.get("status_code") not in (200, None):
            return {"error": "Failed to query devices for host retention sampling"}
        device_ids = (id_resp.get("body") or {}).get("resources") or []
        if not device_ids:
            return {
                "note": "READ-ONLY: Host Retention Policy write operations are not available via the CrowdStrike API.",
                "distribution": {},
                "sample_size": 0,
            }
        details = self._base_get_by_ids(
            operation="PostDeviceDetailsV2", ids=device_ids, id_key="ids", member_cid=member_cid,
        )
        if self._is_error(details):
            return {"error": details}
        distribution: dict[str, int] = {}
        for host in details if isinstance(details, list) else []:
            retention = (host.get("device_policies") or {}).get("host_retention") or {}
            name = retention.get("policy_name") or retention.get("name") or retention.get("policy_id") or "unassigned"
            distribution[name] = distribution.get(name, 0) + 1
        return {
            "note": "READ-ONLY: Host Retention Policy write operations are not available via the CrowdStrike API.",
            "distribution": distribution,
            "sample_size": len(details) if isinstance(details, list) else 0,
        }

    def get_log_collector_policy_info(
        self,
        sample_size: int = Field(
            default=50,
            ge=1,
            le=500,
            description="Number of hosts to sample for log collector policy distribution.",
        ),
        filter: str | None = Field(
            default=None,
            description="Optional FQL filter to narrow the host sample.",
        ),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID for MSSP child tenant scoping.",
        ),
    ) -> dict[str, Any]:
        """Report the Falcon LogScale Collector policy distribution across hosts.

        Samples host device details and extracts the `device_policies.logscale-collector`
        field to show which log collector policy is applied per host. Useful for auditing
        LogScale Collector deployment coverage across a tenant.
        """
        from falcon_mcp.common.utils import prepare_api_parameters
        params = prepare_api_parameters({"limit": sample_size, "filter": filter})
        id_resp = self.client.command_for("QueryDevicesByFilter", member_cid=member_cid, parameters=params)
        if not isinstance(id_resp, dict) or id_resp.get("status_code") not in (200, None):
            return {"error": "Failed to query devices for log collector sampling"}
        device_ids = (id_resp.get("body") or {}).get("resources") or []
        if not device_ids:
            return {"distribution": {}, "sample_size": 0}
        details = self._base_get_by_ids(
            operation="PostDeviceDetailsV2", ids=device_ids, id_key="ids", member_cid=member_cid,
        )
        if self._is_error(details):
            return {"error": details}
        distribution: dict[str, int] = {}
        for host in details if isinstance(details, list) else []:
            policies = host.get("device_policies") or {}
            collector = policies.get("logscale-collector") or policies.get("log-collector") or {}
            name = collector.get("policy_name") or collector.get("name") or collector.get("policy_id") or "unassigned"
            distribution[name] = distribution.get(name, 0) + 1
        return {
            "distribution": distribution,
            "sample_size": len(details) if isinstance(details, list) else 0,
        }
