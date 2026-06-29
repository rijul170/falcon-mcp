"""
FileVantage module for Falcon MCP Server.

Provides tools for CrowdStrike Falcon FileVantage — File Integrity Monitoring (FIM).
Covers change monitoring (file/registry change records), FileVantage policies, rule
groups, monitoring rules, scheduled exclusions, and change actions.

Requires the "Falcon FileVantage" API scope (read/write); retrieving change *content*
additionally requires the "Falcon FileVantage Content" read scope.
"""

from typing import Any

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.errors import _format_error_response
from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule

logger = get_logger(__name__)

WRITE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True,
)
# Deletes are irreversible; startActions can "purge" change records permanently.
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True,
)

_VALID_ACTIONS = ("suppress", "unsuppress", "purge")


class FileVantageModule(BaseModule):
    """Module for CrowdStrike Falcon FileVantage (File Integrity Monitoring)."""

    def register_tools(self, server: FastMCP) -> None:
        # --- Reads ---
        self._add_tool(server=server, method=self.search_filevantage_changes, name="search_filevantage_changes")
        self._add_tool(server=server, method=self.get_filevantage_change_details, name="get_filevantage_change_details")
        self._add_tool(server=server, method=self.get_filevantage_change_content, name="get_filevantage_change_content")
        self._add_tool(server=server, method=self.search_filevantage_policies, name="search_filevantage_policies")
        self._add_tool(server=server, method=self.get_filevantage_policy_details, name="get_filevantage_policy_details")
        self._add_tool(server=server, method=self.search_filevantage_rule_groups, name="search_filevantage_rule_groups")
        self._add_tool(server=server, method=self.get_filevantage_rule_group_details, name="get_filevantage_rule_group_details")
        self._add_tool(server=server, method=self.get_filevantage_rule_details, name="get_filevantage_rule_details")
        self._add_tool(server=server, method=self.search_filevantage_scheduled_exclusions, name="search_filevantage_scheduled_exclusions")
        self._add_tool(server=server, method=self.get_filevantage_scheduled_exclusion_details, name="get_filevantage_scheduled_exclusion_details")
        self._add_tool(server=server, method=self.search_filevantage_actions, name="search_filevantage_actions")
        self._add_tool(server=server, method=self.get_filevantage_action_details, name="get_filevantage_action_details")

        # --- Writes (non-destructive) ---
        for method, name in (
            (self.create_filevantage_policy, "create_filevantage_policy"),
            (self.update_filevantage_policy, "update_filevantage_policy"),
            (self.update_filevantage_policy_host_groups, "update_filevantage_policy_host_groups"),
            (self.update_filevantage_policy_precedence, "update_filevantage_policy_precedence"),
            (self.update_filevantage_policy_rule_groups, "update_filevantage_policy_rule_groups"),
            (self.create_filevantage_rule_group, "create_filevantage_rule_group"),
            (self.update_filevantage_rule_group, "update_filevantage_rule_group"),
            (self.update_filevantage_rule_group_precedence, "update_filevantage_rule_group_precedence"),
            (self.create_filevantage_rule, "create_filevantage_rule"),
            (self.update_filevantage_rule, "update_filevantage_rule"),
            (self.create_filevantage_scheduled_exclusion, "create_filevantage_scheduled_exclusion"),
            (self.update_filevantage_scheduled_exclusion, "update_filevantage_scheduled_exclusion"),
            (self.signal_filevantage_changes, "signal_filevantage_changes"),
        ):
            self._add_tool(server=server, method=method, name=name, annotations=WRITE_ANNOTATIONS)

        # --- Destructive ---
        for method, name in (
            (self.start_filevantage_action, "start_filevantage_action"),
            (self.delete_filevantage_policies, "delete_filevantage_policies"),
            (self.delete_filevantage_rule_groups, "delete_filevantage_rule_groups"),
            (self.delete_filevantage_rules, "delete_filevantage_rules"),
            (self.delete_filevantage_scheduled_exclusions, "delete_filevantage_scheduled_exclusions"),
        ):
            self._add_tool(server=server, method=method, name=name, annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    # ------------------------------------------------------------------ Reads

    def search_filevantage_changes(
        self,
        filter: str | None = Field(
            default=None,
            description=(
                "FQL filter over change records. Common fields: `action_timestamp`, "
                "`host.name`, `host.platform_name`, `rule_id`, `severity`, `change_type`, "
                "`ingestion_timestamp`."
            ),
        ),
        limit: int = Field(default=100, ge=1, le=500, description="Max change IDs to return."),
        offset: int | None = Field(default=None, description="Offset for pagination."),
        sort: str | None = Field(
            default=None,
            description="Sort expression, e.g. `action_timestamp|desc`, `severity|asc`.",
        ),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search FileVantage change records and return full change details.

        This is the core FIM surface: unauthorized/observed file and registry changes.
        Uses the high-volume changes endpoint for scalable pagination.
        """
        ids = self._base_search_api_call(
            operation="highVolumeQueryChanges",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search FileVantage changes",
            member_cid=member_cid,
        )
        if self._is_error(ids):
            return [ids]
        if not ids:
            return []
        return self._base_query_api_call(
            operation="getChanges",
            query_params={"ids": ids},
            error_message="Failed to get FileVantage change details",
            member_cid=member_cid,
        )

    def get_filevantage_change_details(
        self,
        ids: list[str] = Field(description="Change IDs. Obtain from `falcon_search_filevantage_changes`."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get full details for specific FileVantage change records by ID."""
        if not ids:
            return []
        return self._base_query_api_call(
            operation="getChanges",
            query_params={"ids": ids},
            error_message="Failed to get FileVantage change details",
            member_cid=member_cid,
        )

    def get_filevantage_change_content(
        self,
        id: str = Field(description="A single change ID to retrieve before/after content for."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get the captured before/after content of a FileVantage change.

        Requires the separate "Falcon FileVantage Content" read scope.
        """
        if not id:
            return [_format_error_response("`id` is required.", operation="getContents")]
        return self._base_query_api_call(
            operation="getContents",
            query_params={"id": id},
            error_message="Failed to get FileVantage change content",
            member_cid=member_cid,
        )

    def search_filevantage_policies(
        self,
        type: str = Field(
            description="Policy platform. One of: `Windows`, `Linux`, `Mac`.",
            examples=["Windows", "Linux", "Mac"],
        ),
        filter: str | None = Field(default=None, description="Optional FQL filter."),
        limit: int = Field(default=100, ge=1, le=500, description="Max policy IDs."),
        offset: int | None = Field(default=None, description="Offset for pagination."),
        sort: str | None = Field(default=None, description="Sort expression, e.g. `precedence|asc`."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search FileVantage policies for a platform and return full policy details."""
        ids = self._base_search_api_call(
            operation="queryPolicies",
            search_params={"type": type, "filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search FileVantage policies",
            member_cid=member_cid,
        )
        if self._is_error(ids):
            return [ids]
        if not ids:
            return []
        return self._base_query_api_call(
            operation="getPolicies",
            query_params={"ids": ids},
            error_message="Failed to get FileVantage policy details",
            member_cid=member_cid,
        )

    def get_filevantage_policy_details(
        self,
        ids: list[str] = Field(description="Policy IDs. Obtain from `falcon_search_filevantage_policies`."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get full details for specific FileVantage policies by ID."""
        if not ids:
            return []
        return self._base_query_api_call(
            operation="getPolicies",
            query_params={"ids": ids},
            error_message="Failed to get FileVantage policy details",
            member_cid=member_cid,
        )

    def search_filevantage_rule_groups(
        self,
        type: str = Field(
            description="Rule group type, e.g. `WindowsFiles`, `WindowsRegistry`, `LinuxFiles`, `MacFiles`.",
        ),
        limit: int = Field(default=100, ge=1, le=500, description="Max rule group IDs."),
        offset: int | None = Field(default=None, description="Offset for pagination."),
        sort: str | None = Field(default=None, description="Sort expression."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search FileVantage rule groups of a given type and return full details."""
        ids = self._base_search_api_call(
            operation="queryRuleGroups",
            search_params={"type": type, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search FileVantage rule groups",
            member_cid=member_cid,
        )
        if self._is_error(ids):
            return [ids]
        if not ids:
            return []
        return self._base_query_api_call(
            operation="getRuleGroups",
            query_params={"ids": ids},
            error_message="Failed to get FileVantage rule group details",
            member_cid=member_cid,
        )

    def get_filevantage_rule_group_details(
        self,
        ids: list[str] = Field(description="Rule group IDs. Obtain from `falcon_search_filevantage_rule_groups`."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get full details (including assigned rule IDs) for FileVantage rule groups by ID."""
        if not ids:
            return []
        return self._base_query_api_call(
            operation="getRuleGroups",
            query_params={"ids": ids},
            error_message="Failed to get FileVantage rule group details",
            member_cid=member_cid,
        )

    def get_filevantage_rule_details(
        self,
        rule_group_id: str = Field(description="The rule group the rules belong to."),
        ids: list[str] = Field(description="Rule IDs within the rule group (from the rule group's assigned rules)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get full details for specific FileVantage monitoring rules within a rule group."""
        if not ids:
            return []
        return self._base_query_api_call(
            operation="getRules",
            query_params={"rule_group_id": rule_group_id, "ids": ids},
            error_message="Failed to get FileVantage rule details",
            member_cid=member_cid,
        )

    def search_filevantage_scheduled_exclusions(
        self,
        policy_id: str = Field(description="The FileVantage policy to list scheduled exclusions for."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search a policy's scheduled exclusions and return full details."""
        ids = self._base_search_api_call(
            operation="queryScheduledExclusions",
            search_params={"policy_id": policy_id},
            error_message="Failed to search FileVantage scheduled exclusions",
            member_cid=member_cid,
        )
        if self._is_error(ids):
            return [ids]
        if not ids:
            return []
        return self._base_query_api_call(
            operation="getScheduledExclusions",
            query_params={"policy_id": policy_id, "ids": ids},
            error_message="Failed to get FileVantage scheduled exclusion details",
            member_cid=member_cid,
        )

    def get_filevantage_scheduled_exclusion_details(
        self,
        policy_id: str = Field(description="The policy the scheduled exclusions belong to."),
        ids: list[str] = Field(description="Scheduled exclusion IDs."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get full details for specific FileVantage scheduled exclusions."""
        if not ids:
            return []
        return self._base_query_api_call(
            operation="getScheduledExclusions",
            query_params={"policy_id": policy_id, "ids": ids},
            error_message="Failed to get FileVantage scheduled exclusion details",
            member_cid=member_cid,
        )

    def search_filevantage_actions(
        self,
        filter: str | None = Field(default=None, description="Optional FQL filter over change actions."),
        limit: int = Field(default=100, ge=1, le=500, description="Max action IDs."),
        offset: int | None = Field(default=None, description="Offset for pagination."),
        sort: str | None = Field(default=None, description="Sort expression."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search FileVantage change actions (suppress/unsuppress/purge workflow) and return details."""
        ids = self._base_search_api_call(
            operation="queryActionsMixin0",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search FileVantage actions",
            member_cid=member_cid,
        )
        if self._is_error(ids):
            return [ids]
        if not ids:
            return []
        return self._base_query_api_call(
            operation="getActionsMixin0",
            query_params={"ids": ids},
            error_message="Failed to get FileVantage action details",
            member_cid=member_cid,
        )

    def get_filevantage_action_details(
        self,
        ids: list[str] = Field(description="Action IDs. Obtain from `falcon_search_filevantage_actions`."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get full details for specific FileVantage change actions by ID."""
        if not ids:
            return []
        return self._base_query_api_call(
            operation="getActionsMixin0",
            query_params={"ids": ids},
            error_message="Failed to get FileVantage action details",
            member_cid=member_cid,
        )

    # ----------------------------------------------------------------- Writes

    def create_filevantage_policy(
        self,
        name: str = Field(description="Policy name (unique per platform)."),
        platform: str = Field(description="Platform: `Windows`, `Linux`, or `Mac`.", examples=["Windows"]),
        description: str | None = Field(default=None, description="Policy description."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Create a FileVantage policy. New policies are created disabled and with no rule groups."""
        body: dict[str, Any] = {"name": name, "platform": platform}
        if description is not None:
            body["description"] = description
        return self._write(operation="createPolicies", error_message="Failed to create FileVantage policy", body_params=body, member_cid=member_cid)

    def update_filevantage_policy(
        self,
        id: str = Field(description="Policy ID to update."),
        name: str | None = Field(default=None, description="Updated name."),
        description: str | None = Field(default=None, description="Updated description."),
        enabled: bool | None = Field(default=None, description="Enable or disable the policy."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Update a FileVantage policy's name, description, or enabled state."""
        body: dict[str, Any] = {"id": id}
        if name is not None:
            body["name"] = name
        if description is not None:
            body["description"] = description
        if enabled is not None:
            body["enabled"] = enabled
        return self._write(operation="updatePolicies", error_message="Failed to update FileVantage policy", body_params=body, member_cid=member_cid)

    def update_filevantage_policy_host_groups(
        self,
        policy_id: str = Field(description="Policy to modify host-group assignment for."),
        action: str = Field(description="`assign` or `unassign`.", examples=["assign", "unassign"]),
        ids: list[str] = Field(description="Host group IDs to assign/unassign."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Assign or unassign host groups to/from a FileVantage policy."""
        return self._write(operation="updatePolicyHostGroups", error_message="Failed to update FileVantage policy host groups",
            query_params={"policy_id": policy_id, "action": action, "ids": ids}, member_cid=member_cid,
        )

    def update_filevantage_policy_precedence(
        self,
        ids: list[str] = Field(description="Policy IDs in the desired precedence order (highest first)."),
        type: str = Field(description="Platform: `Windows`, `Linux`, or `Mac`."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Set the evaluation precedence of FileVantage policies for a platform (full ordered list)."""
        return self._write(operation="updatePolicyPrecedence", error_message="Failed to update FileVantage policy precedence",
            query_params={"ids": ids, "type": type}, member_cid=member_cid,
        )

    def update_filevantage_policy_rule_groups(
        self,
        policy_id: str = Field(description="Policy to modify rule-group assignment for."),
        action: str = Field(description="`assign` or `unassign`.", examples=["assign", "unassign"]),
        ids: list[str] = Field(description="Rule group IDs to assign/unassign."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Assign or unassign rule groups to/from a FileVantage policy."""
        return self._write(operation="updatePolicyRuleGroups", error_message="Failed to update FileVantage policy rule groups",
            query_params={"policy_id": policy_id, "action": action, "ids": ids}, member_cid=member_cid,
        )

    def create_filevantage_rule_group(
        self,
        name: str = Field(description="Rule group name."),
        type: str = Field(description="Rule group type, e.g. `WindowsFiles`, `WindowsRegistry`, `LinuxFiles`, `MacFiles`."),
        description: str | None = Field(default=None, description="Rule group description."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Create a FileVantage rule group (a reusable container of monitoring rules)."""
        body: dict[str, Any] = {"name": name, "type": type}
        if description is not None:
            body["description"] = description
        return self._write(operation="createRuleGroups", error_message="Failed to create FileVantage rule group", body_params=body, member_cid=member_cid)

    def update_filevantage_rule_group(
        self,
        id: str = Field(description="Rule group ID to update."),
        name: str | None = Field(default=None, description="Updated name."),
        description: str | None = Field(default=None, description="Updated description."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Update a FileVantage rule group's name or description."""
        body: dict[str, Any] = {"id": id}
        if name is not None:
            body["name"] = name
        if description is not None:
            body["description"] = description
        return self._write(operation="updateRuleGroups", error_message="Failed to update FileVantage rule group", body_params=body, member_cid=member_cid)

    def update_filevantage_rule_group_precedence(
        self,
        rule_group_id: str = Field(description="Rule group whose rule precedence is being set."),
        ids: list[str] = Field(description="Rule IDs in the desired precedence order."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Set the precedence order of rules within a FileVantage rule group (full ordered list)."""
        return self._write(operation="updateRuleGroupPrecedence", error_message="Failed to update FileVantage rule group precedence",
            query_params={"rule_group_id": rule_group_id, "ids": ids}, member_cid=member_cid,
        )

    def create_filevantage_rule(
        self,
        rule_group_id: str = Field(description="Rule group the rule belongs to."),
        path: str = Field(description="File/registry path to monitor."),
        severity: str = Field(description="Severity: `Low`, `Medium`, `High`, or `Critical`."),
        type: str = Field(description="Rule type matching the rule group, e.g. `File`, `Directory`, `RegistryKey`, `RegistryValue`."),
        depth: str | None = Field(default=None, description="Monitoring depth, e.g. `1`, `2`, `ANY`."),
        include: str | None = Field(default=None, description="Include glob/pattern (files/keys to include)."),
        exclude: str | None = Field(default=None, description="Exclude glob/pattern."),
        precedence: int | None = Field(default=None, description="Rule precedence within the group."),
        description: str | None = Field(default=None, description="Rule description."),
        watch_settings: dict[str, Any] | None = Field(
            default=None,
            description=(
                "Optional advanced flags merged into the rule body, e.g. "
                "{'watch_write_file_changes': true, 'watch_delete_file_changes': true, "
                "'enable_content_capture': false, 'include_users': 'admin'}."
            ),
        ),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Create a FileVantage monitoring rule inside a rule group."""
        body: dict[str, Any] = {
            "rule_group_id": rule_group_id, "path": path, "severity": severity, "type": type,
        }
        for k, v in (("depth", depth), ("include", include), ("exclude", exclude),
                     ("precedence", precedence), ("description", description)):
            if v is not None:
                body[k] = v
        if watch_settings:
            body.update(watch_settings)
        return self._write(operation="createRules", error_message="Failed to create FileVantage rule", body_params=body, member_cid=member_cid)

    def update_filevantage_rule(
        self,
        id: str = Field(description="Rule ID to update."),
        rule_group_id: str = Field(description="Rule group the rule belongs to."),
        severity: str | None = Field(default=None, description="Updated severity."),
        path: str | None = Field(default=None, description="Updated path."),
        depth: str | None = Field(default=None, description="Updated monitoring depth."),
        include: str | None = Field(default=None, description="Updated include pattern."),
        exclude: str | None = Field(default=None, description="Updated exclude pattern."),
        precedence: int | None = Field(default=None, description="Updated precedence."),
        description: str | None = Field(default=None, description="Updated description."),
        watch_settings: dict[str, Any] | None = Field(
            default=None, description="Optional advanced watch_* / capture flags merged into the body.",
        ),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Update a FileVantage monitoring rule."""
        body: dict[str, Any] = {"id": id, "rule_group_id": rule_group_id}
        for k, v in (("severity", severity), ("path", path), ("depth", depth), ("include", include),
                     ("exclude", exclude), ("precedence", precedence), ("description", description)):
            if v is not None:
                body[k] = v
        if watch_settings:
            body.update(watch_settings)
        return self._write(operation="updateRules", error_message="Failed to update FileVantage rule", body_params=body, member_cid=member_cid)

    def create_filevantage_scheduled_exclusion(
        self,
        policy_id: str = Field(description="Policy the exclusion applies to."),
        name: str = Field(description="Scheduled exclusion name."),
        schedule_start: str | None = Field(default=None, description="Start timestamp (RFC3339)."),
        schedule_end: str | None = Field(default=None, description="End timestamp (RFC3339). Omit for indefinite."),
        timezone: str | None = Field(default=None, description="IANA timezone, e.g. `America/New_York`."),
        description: str | None = Field(default=None, description="Description."),
        processes: str | None = Field(default=None, description="Process pattern(s) to exclude."),
        users: str | None = Field(default=None, description="User pattern(s) to exclude."),
        repeated: dict[str, Any] | None = Field(
            default=None,
            description=(
                "Optional recurrence object, e.g. {'frequency':'weekly','start_time':'09:00',"
                "'end_time':'17:00','weekly_days':['Monday','Tuesday'],'all_day':false}."
            ),
        ),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Create a scheduled exclusion (suppresses expected changes during a window) on a policy."""
        body: dict[str, Any] = {"policy_id": policy_id, "name": name}
        for k, v in (("schedule_start", schedule_start), ("schedule_end", schedule_end),
                     ("timezone", timezone), ("description", description), ("processes", processes),
                     ("users", users), ("repeated", repeated)):
            if v is not None:
                body[k] = v
        return self._write(operation="createScheduledExclusions", error_message="Failed to create FileVantage scheduled exclusion", body_params=body, member_cid=member_cid)

    def update_filevantage_scheduled_exclusion(
        self,
        id: str = Field(description="Scheduled exclusion ID to update."),
        policy_id: str = Field(description="Policy the exclusion belongs to."),
        name: str | None = Field(default=None, description="Updated name."),
        description: str | None = Field(default=None, description="Updated description."),
        users: str | None = Field(default=None, description="Updated user pattern(s)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Update a FileVantage scheduled exclusion."""
        body: dict[str, Any] = {"id": id, "policy_id": policy_id}
        for k, v in (("name", name), ("description", description), ("users", users)):
            if v is not None:
                body[k] = v
        return self._write(operation="updateScheduledExclusions", error_message="Failed to update FileVantage scheduled exclusion", body_params=body, member_cid=member_cid)

    def signal_filevantage_changes(
        self,
        ids: list[str] = Field(description="Change IDs to emit external workflow signals for."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Emit external (Fusion workflow) signals for the specified FileVantage changes."""
        if not ids:
            return [_format_error_response("`ids` is required.", operation="signalChangesExternal")]
        return self._write(operation="signalChangesExternal", error_message="Failed to signal FileVantage changes", body_params={"ids": ids}, member_cid=member_cid)

    # ------------------------------------------------------------- Destructive

    def start_filevantage_action(
        self,
        change_ids: list[str] = Field(description="Change IDs to act on."),
        operation: str = Field(
            description="Action: `suppress`, `unsuppress`, or `purge`. `purge` permanently deletes change records.",
            examples=["suppress", "unsuppress", "purge"],
        ),
        comment: str | None = Field(default=None, description="Audit comment."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Suppress, unsuppress, or PURGE FileVantage change records.

        `purge` is irreversible — it permanently deletes the change records.
        """
        if not change_ids:
            return [_format_error_response("`change_ids` is required.", operation="startActions")]
        if operation not in _VALID_ACTIONS:
            return [_format_error_response(
                f"`operation` must be one of {_VALID_ACTIONS}.", operation="startActions",
            )]
        body: dict[str, Any] = {"change_ids": change_ids, "operation": operation}
        if comment is not None:
            body["comment"] = comment
        return self._write(operation="startActions", error_message="Failed to start FileVantage action", body_params=body, member_cid=member_cid)

    def delete_filevantage_policies(
        self,
        ids: list[str] = Field(description="Policy IDs to delete."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Delete FileVantage policies by ID."""
        if not ids:
            return [_format_error_response("`ids` is required.", operation="deletePolicies")]
        return self._write(operation="deletePolicies", error_message="Failed to delete FileVantage policies", query_params={"ids": ids}, member_cid=member_cid)

    def delete_filevantage_rule_groups(
        self,
        ids: list[str] = Field(description="Rule group IDs to delete."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Delete FileVantage rule groups by ID."""
        if not ids:
            return [_format_error_response("`ids` is required.", operation="deleteRuleGroups")]
        return self._write(operation="deleteRuleGroups", error_message="Failed to delete FileVantage rule groups", query_params={"ids": ids}, member_cid=member_cid)

    def delete_filevantage_rules(
        self,
        rule_group_id: str = Field(description="Rule group the rules belong to."),
        ids: list[str] = Field(description="Rule IDs to delete."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Delete FileVantage monitoring rules from a rule group."""
        if not ids:
            return [_format_error_response("`ids` is required.", operation="deleteRules")]
        return self._write(operation="deleteRules", error_message="Failed to delete FileVantage rules",
            query_params={"rule_group_id": rule_group_id, "ids": ids}, member_cid=member_cid,
        )

    def delete_filevantage_scheduled_exclusions(
        self,
        policy_id: str = Field(description="Policy the exclusions belong to."),
        ids: list[str] = Field(description="Scheduled exclusion IDs to delete."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Delete FileVantage scheduled exclusions from a policy."""
        if not ids:
            return [_format_error_response("`ids` is required.", operation="deleteScheduledExclusions")]
        return self._write(operation="deleteScheduledExclusions", error_message="Failed to delete FileVantage scheduled exclusions",
            query_params={"policy_id": policy_id, "ids": ids}, member_cid=member_cid,
        )

    # ----------------------------------------------------------------- Helper

    def _write(
        self,
        operation: str,
        error_message: str,
        *,
        body_params: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
        member_cid: str | None = None,
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Run a mutating call and normalize errors to a single-item list."""
        result = self._base_query_api_call(
            operation=operation,
            body_params=body_params,
            query_params=query_params,
            error_message=error_message,
            member_cid=member_cid,
        )
        if self._is_error(result):
            return [result]
        return result
