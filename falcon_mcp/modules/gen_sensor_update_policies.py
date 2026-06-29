"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `sensor_update_policies` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenSensorUpdatePoliciesModule(GeneratedModuleBase):
    """Generated tools for the Falcon `sensor_update_policies` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_sensor_update_policies_v2, name="get_sensor_update_policies_v2")
        self._add_tool(server=server, method=self.query_sensor_update_policies, name="query_sensor_update_policies")
        self._add_tool(server=server, method=self.query_sensor_update_policy_members, name="query_sensor_update_policy_members")
        self._add_tool(server=server, method=self.increment_uninstall_token, name="increment_uninstall_token", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def get_sensor_update_policies_v2(
        self,
        ids: list[str] = Field(description="The IDs of the Sensor Update Policies to return"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve a set of Sensor Update Policies with additional support for uninstall protection by specifying their IDs"""
        return self._call(operation="getSensorUpdatePoliciesV2", query_params={"ids": ids}, error_message="getSensorUpdatePoliciesV2 failed", member_cid=member_cid)

    def increment_uninstall_token(
        self,
        body: dict = Field(description="Request JSON body for `incrementUninstallToken` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Increments a bulk maintenance token."""
        return self._call(operation="incrementUninstallToken", query_params=None, body_params=body, error_message="incrementUninstallToken failed", member_cid=member_cid)

    def query_sensor_update_policies(
        self,
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results"),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        limit: int | None = Field(default=None, description="The maximum records to return. [1-5000]"),
        sort: str | None = Field(default=None, description="The property to sort by"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for Sensor Update Policies in your environment by providing an FQL filter and paging details. Returns a set of Sensor Update Policy IDs which match the filter criteria"""
        return self._call(operation="querySensorUpdatePolicies", query_params={"filter": filter, "offset": offset, "limit": limit, "sort": sort}, error_message="querySensorUpdatePolicies failed", member_cid=member_cid)

    def query_sensor_update_policy_members(
        self,
        id: str | None = Field(default=None, description="The ID of the Sensor Update Policy to search for members of"),
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results"),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        limit: int | None = Field(default=None, description="The maximum records to return. [1-5000]"),
        sort: str | None = Field(default=None, description="The property to sort by"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for members of a Sensor Update Policy in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria"""
        return self._call(operation="querySensorUpdatePolicyMembers", query_params={"id": id, "filter": filter, "offset": offset, "limit": limit, "sort": sort}, error_message="querySensorUpdatePolicyMembers failed", member_cid=member_cid)
