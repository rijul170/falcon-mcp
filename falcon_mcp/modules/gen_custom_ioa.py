"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `custom_ioa` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenCustomIoaModule(GeneratedModuleBase):
    """Generated tools for the Falcon `custom_ioa` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_patterns, name="get_patterns")
        self._add_tool(server=server, method=self.get_rule_groups_mixin0, name="get_rule_groups_mixin0")
        self._add_tool(server=server, method=self.get_rules_mixin0, name="get_rules_mixin0")
        self._add_tool(server=server, method=self.get_rules_get, name="get_rules_get")
        self._add_tool(server=server, method=self.query_patterns, name="query_patterns")
        self._add_tool(server=server, method=self.query_rule_groups_mixin0, name="query_rule_groups_mixin0")
        self._add_tool(server=server, method=self.query_rules_mixin0, name="query_rules_mixin0")
        self._add_tool(server=server, method=self.validate, name="validate", annotations=WRITE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def get_patterns(
        self,
        ids: list[str] = Field(description="The IDs of the entities"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get pattern severities by ID."""
        return self._call(operation="get_patterns", query_params={"ids": ids}, error_message="get_patterns failed", member_cid=member_cid)

    def get_rule_groups_mixin0(
        self,
        ids: list[str] = Field(description="The IDs of the entities"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get rule groups by ID."""
        return self._call(operation="get_rule_groupsMixin0", query_params={"ids": ids}, error_message="get_rule_groupsMixin0 failed", member_cid=member_cid)

    def get_rules_mixin0(
        self,
        ids: list[str] = Field(description="The IDs of the entities"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get rules by ID and optionally with cid and/or version in the following format: `[cid:]ID[:version]`. The max number of IDs is constrained by URL size."""
        return self._call(operation="get_rulesMixin0", query_params={"ids": ids}, error_message="get_rulesMixin0 failed", member_cid=member_cid)

    def get_rules_get(
        self,
        body: dict = Field(description="Request JSON body for `get_rules_get` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get rules by ID and optionally with cid and/or version in the following format: `[cid:]ID[:version]`."""
        return self._call(operation="get_rules_get", query_params=None, body_params=body, error_message="get_rules_get failed", member_cid=member_cid)

    def query_patterns(
        self,
        offset: str | None = Field(default=None, description="Starting index of overall result set from which to return IDs"),
        limit: int | None = Field(default=None, description="Number of IDs to return"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get all pattern severity IDs."""
        return self._call(operation="query_patterns", query_params={"offset": offset, "limit": limit}, error_message="query_patterns failed", member_cid=member_cid)

    def query_rule_groups_mixin0(
        self,
        sort: str | None = Field(default=None, description="Possible order by fields: {created_by, created_on, enabled, modified_by, modified_on, name}"),
        filter: str | None = Field(default=None, description="FQL query specifying the filter parameters. Filter term criteria: [enabled platform name description rules.action_label rules.name rules.description rules.pattern_severity rules.ruletype_name rules.enabled]. Filter range criteria: created_on, modified_on; use any common date format, such as '2010-05-15T14:55:21.892315096Z'."),
        q: str | None = Field(default=None, description="Match query criteria, which includes all the filter string fields"),
        offset: str | None = Field(default=None, description="Starting index of overall result set from which to return IDs"),
        limit: int | None = Field(default=None, description="Number of IDs to return"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Finds all rule group IDs matching the query with optional filter."""
        return self._call(operation="query_rule_groupsMixin0", query_params={"sort": sort, "filter": filter, "q": q, "offset": offset, "limit": limit}, error_message="query_rule_groupsMixin0 failed", member_cid=member_cid)

    def query_rules_mixin0(
        self,
        sort: str | None = Field(default=None, description="Possible order by fields: {rules.created_by, rules.created_on, rules.current_version.action_label, rules.current_version.description, rules.current_version.modified_by, rules.current_version.modified_on, rules.current_version.name, rules.current_version.pattern_severity, rules.enabled, rules.ruletype_name}"),
        filter: str | None = Field(default=None, description="FQL query specifying the filter parameters. Filter term criteria: [enabled platform name description rules.action_label rules.name rules.description rules.pattern_severity rules.ruletype_name rules.enabled]. Filter range criteria: created_on, modified_on; use any common date format, such as '2010-05-15T14:55:21.892315096Z'."),
        q: str | None = Field(default=None, description="Match query criteria, which includes all the filter string fields"),
        offset: str | None = Field(default=None, description="Starting index of overall result set from which to return IDs"),
        limit: int | None = Field(default=None, description="Number of IDs to return"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Finds all rule IDs matching the query with optional filter."""
        return self._call(operation="query_rulesMixin0", query_params={"sort": sort, "filter": filter, "q": q, "offset": offset, "limit": limit}, error_message="query_rulesMixin0 failed", member_cid=member_cid)

    def validate(
        self,
        body: dict = Field(description="Request JSON body for `validate` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Validates field values and checks for matches if a test string is provided."""
        return self._call(operation="validate", query_params=None, body_params=body, error_message="validate failed", member_cid=member_cid)
