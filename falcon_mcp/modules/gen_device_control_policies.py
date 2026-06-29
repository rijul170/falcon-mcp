"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `device_control_policies` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenDeviceControlPoliciesModule(GeneratedModuleBase):
    """Generated tools for the Falcon `device_control_policies` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_default_device_control_policies, name="get_default_device_control_policies")
        self._add_tool(server=server, method=self.get_default_device_control_settings, name="get_default_device_control_settings")
        self._add_tool(server=server, method=self.get_device_control_policies_v2, name="get_device_control_policies_v2")
        self._add_tool(server=server, method=self.query_device_control_policies, name="query_device_control_policies")
        self._add_tool(server=server, method=self.query_device_control_policy_members, name="query_device_control_policy_members")
        self._add_tool(server=server, method=self.patch_device_control_policies_v2, name="patch_device_control_policies_v2", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.post_device_control_policies_v2, name="post_device_control_policies_v2", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_default_device_control_policies, name="update_default_device_control_policies", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_default_device_control_settings, name="update_default_device_control_settings", annotations=WRITE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def get_default_device_control_policies(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve the configuration for a Default Device Control Policy"""
        return self._call(operation="getDefaultDeviceControlPolicies", query_params=None, error_message="getDefaultDeviceControlPolicies failed", member_cid=member_cid)

    def get_default_device_control_settings(
        self,
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get default device control settings (USB and Bluetooth)"""
        return self._call(operation="getDefaultDeviceControlSettings", query_params=None, error_message="getDefaultDeviceControlSettings failed", member_cid=member_cid)

    def get_device_control_policies_v2(
        self,
        ids: list[str] = Field(description="The IDs of the policies to get"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get device control policies for the given filter criteria. (USB and Bluetooth)"""
        return self._call(operation="getDeviceControlPoliciesV2", query_params={"ids": ids}, error_message="getDeviceControlPoliciesV2 failed", member_cid=member_cid)

    def patch_device_control_policies_v2(
        self,
        body: dict = Field(description="Request JSON body for `patchDeviceControlPoliciesV2` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update device control policy base (USB and Bluetooth)"""
        return self._call(operation="patchDeviceControlPoliciesV2", query_params=None, body_params=body, error_message="patchDeviceControlPoliciesV2 failed", member_cid=member_cid)

    def post_device_control_policies_v2(
        self,
        body: dict = Field(description="Request JSON body for `postDeviceControlPoliciesV2` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create/clone a device control policy (USB and Bluetooth)"""
        return self._call(operation="postDeviceControlPoliciesV2", query_params=None, body_params=body, error_message="postDeviceControlPoliciesV2 failed", member_cid=member_cid)

    def query_device_control_policies(
        self,
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results"),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        limit: int | None = Field(default=None, description="The maximum records to return. [1-5000]"),
        sort: str | None = Field(default=None, description="The property to sort by"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for Device Control Policies in your environment by providing an FQL filter and paging details. Returns a set of Device Control Policy IDs which match the filter criteria"""
        return self._call(operation="queryDeviceControlPolicies", query_params={"filter": filter, "offset": offset, "limit": limit, "sort": sort}, error_message="queryDeviceControlPolicies failed", member_cid=member_cid)

    def query_device_control_policy_members(
        self,
        id: str | None = Field(default=None, description="The ID of the Device Control Policy to search for members of"),
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results"),
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        limit: int | None = Field(default=None, description="The maximum records to return. [1-5000]"),
        sort: str | None = Field(default=None, description="The property to sort by"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for members of a Device Control Policy in your environment by providing an FQL filter and paging details. Returns a set of Agent IDs which match the filter criteria"""
        return self._call(operation="queryDeviceControlPolicyMembers", query_params={"id": id, "filter": filter, "offset": offset, "limit": limit, "sort": sort}, error_message="queryDeviceControlPolicyMembers failed", member_cid=member_cid)

    def update_default_device_control_policies(
        self,
        body: dict = Field(description="Request JSON body for `updateDefaultDeviceControlPolicies` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update the configuration for a Default Device Control Policy"""
        return self._call(operation="updateDefaultDeviceControlPolicies", query_params=None, body_params=body, error_message="updateDefaultDeviceControlPolicies failed", member_cid=member_cid)

    def update_default_device_control_settings(
        self,
        body: dict = Field(description="Request JSON body for `updateDefaultDeviceControlSettings` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update the configuration for Default Device Control Settings"""
        return self._call(operation="updateDefaultDeviceControlSettings", query_params=None, body_params=body, error_message="updateDefaultDeviceControlSettings failed", member_cid=member_cid)
