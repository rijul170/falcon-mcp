"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `mobile_enrollment` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenMobileEnrollmentModule(GeneratedModuleBase):
    """Generated tools for the Falcon `mobile_enrollment` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.request_device_enrollment_v4, name="request_device_enrollment_v4", annotations=WRITE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def request_device_enrollment_v4(
        self,
        body: dict = Field(description="Request JSON body for `RequestDeviceEnrollmentV4` per the CrowdStrike API schema (required)."),
        action_name: str | None = Field(default=None, description="Action to perform"),
        filter: str | None = Field(default=None, description="FQL filter"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Trigger on-boarding process for a mobile device"""
        return self._call(operation="RequestDeviceEnrollmentV4", query_params={"action_name": action_name, "filter": filter}, body_params=body, error_message="RequestDeviceEnrollmentV4 failed", member_cid=member_cid)
