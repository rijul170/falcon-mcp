"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `firewall_management` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenFirewallManagementModule(GeneratedModuleBase):
    """Generated tools for the Falcon `firewall_management` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_events, name="get_events")
        self._add_tool(server=server, method=self.get_firewall_fields, name="get_firewall_fields")
        self._add_tool(server=server, method=self.get_network_locations, name="get_network_locations")
        self._add_tool(server=server, method=self.get_network_locations_details, name="get_network_locations_details")
        self._add_tool(server=server, method=self.get_platforms, name="get_platforms")
        self._add_tool(server=server, method=self.get_policy_containers, name="get_policy_containers")
        self._add_tool(server=server, method=self.query_events, name="query_events")
        self._add_tool(server=server, method=self.query_firewall_fields, name="query_firewall_fields")
        self._add_tool(server=server, method=self.query_network_locations, name="query_network_locations")
        self._add_tool(server=server, method=self.query_platforms, name="query_platforms")
        self._add_tool(server=server, method=self.create_network_locations, name="create_network_locations", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.create_rule_group_validation, name="create_rule_group_validation", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_network_locations, name="update_network_locations", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_network_locations_metadata, name="update_network_locations_metadata", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_network_locations_precedence, name="update_network_locations_precedence", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_rule_group_validation, name="update_rule_group_validation", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.upsert_network_locations, name="upsert_network_locations", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.validate_filepath_pattern, name="validate_filepath_pattern", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_network_locations, name="delete_network_locations", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_policy_container_v1, name="update_policy_container_v1", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def create_network_locations(
        self,
        body: dict = Field(description="Request JSON body for `create_network_locations` per the CrowdStrike API schema (required)."),
        clone_id: str | None = Field(default=None, description="A network location ID from which to copy location. If this is provided then the body of the request is ignored."),
        add_fw_rules: bool | None = Field(default=None, description="A boolean to determine whether the cloned location needs to be added to the same firewall rules that original location is added to."),
        comment: str | None = Field(default=None, description="Audit log comment for this action"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create new network locations provided, and return the ID."""
        return self._call(operation="create_network_locations", query_params={"clone_id": clone_id, "add_fw_rules": add_fw_rules, "comment": comment}, body_params=body, error_message="create_network_locations failed", member_cid=member_cid)

    def create_rule_group_validation(
        self,
        body: dict = Field(description="Request JSON body for `create_rule_group_validation` per the CrowdStrike API schema (required)."),
        clone_id: str | None = Field(default=None, description="A rule group ID from which to copy rules. If this is provided then the 'rules' property of the body is ignored."),
        library: str | None = Field(default=None, description="If this flag is set to true then the rules will be cloned from the clone_id from the CrowdStrike Firewall Rule Groups Library."),
        comment: str | None = Field(default=None, description="Audit log comment for this action"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Validates the request of creating a new rule group on a platform for a customer with a name and description"""
        return self._call(operation="create_rule_group_validation", query_params={"clone_id": clone_id, "library": library, "comment": comment}, body_params=body, error_message="create_rule_group_validation failed", member_cid=member_cid)

    def delete_network_locations(
        self,
        ids: list[str] = Field(description="The IDs of the network locations to be deleted"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete network location entities by ID."""
        return self._call(operation="delete_network_locations", query_params={"ids": ids}, error_message="delete_network_locations failed", member_cid=member_cid)

    def get_events(
        self,
        ids: list[str] = Field(description="The events to retrieve, identified by ID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get events entities by ID and optionally version"""
        return self._call(operation="get_events", query_params={"ids": ids}, error_message="get_events failed", member_cid=member_cid)

    def get_firewall_fields(
        self,
        ids: list[str] = Field(description="The IDs of the rule types to retrieve"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get the firewall field specifications by ID"""
        return self._call(operation="get_firewall_fields", query_params={"ids": ids}, error_message="get_firewall_fields failed", member_cid=member_cid)

    def get_network_locations(
        self,
        ids: list[str] = Field(description="The events to retrieve, identified by ID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get a summary of network locations entities by ID"""
        return self._call(operation="get_network_locations", query_params={"ids": ids}, error_message="get_network_locations failed", member_cid=member_cid)

    def get_network_locations_details(
        self,
        ids: list[str] = Field(description="The events to retrieve, identified by ID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get network locations entities by ID"""
        return self._call(operation="get_network_locations_details", query_params={"ids": ids}, error_message="get_network_locations_details failed", member_cid=member_cid)

    def get_platforms(
        self,
        ids: list[str] = Field(description="The IDs of the platforms to retrieve"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get platforms by ID, e.g., windows or mac or droid"""
        return self._call(operation="get_platforms", query_params={"ids": ids}, error_message="get_platforms failed", member_cid=member_cid)

    def get_policy_containers(
        self,
        ids: list[str] = Field(description="The policy container(s) to retrieve, identified by policy ID"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get policy container entities by policy ID"""
        return self._call(operation="get_policy_containers", query_params={"ids": ids}, error_message="get_policy_containers failed", member_cid=member_cid)

    def query_events(
        self,
        sort: str | None = Field(default=None, description="Possible order by fields:"),
        filter: str | None = Field(default=None, description="FQL query specifying the filter parameters. Filter term criteria: enabled, platform, name, description, etc TODO. Filter range criteria: created_on, modified_on; use any common date format, such as '2010-05-15T14:55:21.892315096Z'."),
        q: str | None = Field(default=None, description="Match query criteria, which includes all the filter string fields, plus TODO"),
        offset: str | None = Field(default=None, description="Starting index of overall result set from which to return ids."),
        after: str | None = Field(default=None, description="A pagination token used with the limit parameter to manage pagination of results. On your first request, don't provide an after token. On subsequent requests, provide the after token from the previous response to continue from that place in the results."),
        limit: int | None = Field(default=None, description="Number of ids to return."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Find all event IDs matching the query with filter"""
        return self._call(operation="query_events", query_params={"sort": sort, "filter": filter, "q": q, "offset": offset, "after": after, "limit": limit}, error_message="query_events failed", member_cid=member_cid)

    def query_firewall_fields(
        self,
        platform_id: str | None = Field(default=None, description="Get fields configuration for this platform"),
        offset: str | None = Field(default=None, description="Starting index of overall result set from which to return ids."),
        limit: int | None = Field(default=None, description="Number of ids to return."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get the firewall field specification IDs for the provided platform"""
        return self._call(operation="query_firewall_fields", query_params={"platform_id": platform_id, "offset": offset, "limit": limit}, error_message="query_firewall_fields failed", member_cid=member_cid)

    def query_network_locations(
        self,
        sort: str | None = Field(default=None, description="Possible order by fields:"),
        filter: str | None = Field(default=None, description="FQL query specifying the filter parameters. Filter term criteria: name"),
        q: str | None = Field(default=None, description="Match query criteria, which includes all the filter string fields"),
        offset: str | None = Field(default=None, description="Starting index of overall result set from which to return ids."),
        after: str | None = Field(default=None, description="A pagination token used with the limit parameter to manage pagination of results. On your first request, don't provide an after token. On subsequent requests, provide the after token from the previous response to continue from that place in the results."),
        limit: int | None = Field(default=None, description="Number of ids to return."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get a list of network location IDs"""
        return self._call(operation="query_network_locations", query_params={"sort": sort, "filter": filter, "q": q, "offset": offset, "after": after, "limit": limit}, error_message="query_network_locations failed", member_cid=member_cid)

    def query_platforms(
        self,
        offset: str | None = Field(default=None, description="Starting index of overall result set from which to return ids."),
        limit: int | None = Field(default=None, description="Number of ids to return."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get the list of platform names"""
        return self._call(operation="query_platforms", query_params={"offset": offset, "limit": limit}, error_message="query_platforms failed", member_cid=member_cid)

    def update_network_locations(
        self,
        body: dict = Field(description="Request JSON body for `update_network_locations` per the CrowdStrike API schema (required)."),
        comment: str | None = Field(default=None, description="Audit log comment for this action"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Updates the network locations provided, and return the ID."""
        return self._call(operation="update_network_locations", query_params={"comment": comment}, body_params=body, error_message="update_network_locations failed", member_cid=member_cid)

    def update_network_locations_metadata(
        self,
        body: dict = Field(description="Request JSON body for `update_network_locations_metadata` per the CrowdStrike API schema (required)."),
        comment: str | None = Field(default=None, description="Audit log comment for this action"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Updates the network locations metadata such as polling_intervals for the cid"""
        return self._call(operation="update_network_locations_metadata", query_params={"comment": comment}, body_params=body, error_message="update_network_locations_metadata failed", member_cid=member_cid)

    def update_network_locations_precedence(
        self,
        body: dict = Field(description="Request JSON body for `update_network_locations_precedence` per the CrowdStrike API schema (required)."),
        comment: str | None = Field(default=None, description="Audit log comment for this action"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Updates the network locations precedence according to the list of ids provided."""
        return self._call(operation="update_network_locations_precedence", query_params={"comment": comment}, body_params=body, error_message="update_network_locations_precedence failed", member_cid=member_cid)

    def update_policy_container_v1(
        self,
        body: dict = Field(description="Request JSON body for `update_policy_container_v1` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update an identified policy container. WARNING: This endpoint is deprecated in favor of v2, using this endpoint could disable your local logging setting."""
        return self._call(operation="update_policy_container_v1", query_params=None, body_params=body, error_message="update_policy_container_v1 failed", member_cid=member_cid)

    def update_rule_group_validation(
        self,
        body: dict = Field(description="Request JSON body for `update_rule_group_validation` per the CrowdStrike API schema (required)."),
        comment: str | None = Field(default=None, description="Audit log comment for this action"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Validates the request of updating name, description, or enabled status of a rule group, or create, edit, delete, or reorder rules"""
        return self._call(operation="update_rule_group_validation", query_params={"comment": comment}, body_params=body, error_message="update_rule_group_validation failed", member_cid=member_cid)

    def upsert_network_locations(
        self,
        body: dict = Field(description="Request JSON body for `upsert_network_locations` per the CrowdStrike API schema (required)."),
        comment: str | None = Field(default=None, description="Audit log comment for this action"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Updates the network locations provided, and return the ID."""
        return self._call(operation="upsert_network_locations", query_params={"comment": comment}, body_params=body, error_message="upsert_network_locations failed", member_cid=member_cid)

    def validate_filepath_pattern(
        self,
        body: dict = Field(description="Request JSON body for `validate_filepath_pattern` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Validates that the test pattern matches the executable filepath glob pattern."""
        return self._call(operation="validate_filepath_pattern", query_params=None, body_params=body, error_message="validate_filepath_pattern failed", member_cid=member_cid)
