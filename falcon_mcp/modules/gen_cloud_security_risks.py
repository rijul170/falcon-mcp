"""AUTO-GENERATED module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon
`cloud-security-risks` API service collection.

Coverage notes
--------------
combined_cloud_risks (GET /cloud-security-risks/combined/cloud-risks/v1)
    Already present in ``gen_cloud_security.py``
    (GenCloudSecurityModule.combined_cloud_risks). Intentionally omitted here
    to avoid duplicate tool registration.

cloud_security_timeline_risks_enriched
    (GET /cloud-security-timeline/entities/cloud-risks-enriched-timeline/v1)
    NOT present in FalconPy 1.6.1. Called via the UberClass ``override``
    mechanism ("GET,<path>") so no FalconPy update is required.

Rate limit: 500 requests/minute/CID (HTTP 429 on breach).
Scope required: Cloud Security API Risks: READ
"""

from typing import Any

from mcp.server import FastMCP
from pydantic import Field

from falcon_mcp.common.errors import handle_api_response
from falcon_mcp.common.generated_base import GeneratedModuleBase
from falcon_mcp.common.utils import prepare_api_parameters

# Endpoint not yet in FalconPy 1.6.1 — dispatched via UberClass override.
_ENRICHED_TIMELINE_OVERRIDE = (
    "GET,/cloud-security-timeline/entities/cloud-risks-enriched-timeline/v1"
)


class GenCloudSecurityRisksModule(GeneratedModuleBase):
    """Generated tools for the Falcon `cloud-security-risks` collection.

    Exposes ``cloud_security_timeline_risks_enriched``, which returns the
    enriched asset risk timeline for a given GCRN. Because this endpoint is
    absent from FalconPy 1.6.1, the call is dispatched via the FalconPy
    UberClass ``override`` kwarg rather than a named operation ID.
    """

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(
            server=server,
            method=self.cloud_security_timeline_risks_enriched,
            name="cloud_security_timeline_risks_enriched",
        )

    def register_resources(self, server: FastMCP) -> None:
        pass

    def cloud_security_timeline_risks_enriched(
        self,
        id: str = Field(
            description=(
                "The GCRN (Global Cloud Resource Name) of the cloud asset whose enriched "
                "risk timeline you want to retrieve. Obtain GCRNs from "
                "`cloud_security_assets_combined_application_findings` or other asset "
                "discovery tools."
            ),
        ),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID for MSSP scoping.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Return the enriched asset risk timeline for a cloud asset.

        Retrieves a chronological timeline of cloud security risk events for the
        specified asset, enriched with context such as rule details, severity
        changes, and suppression history.

        Rate limited to 500 requests per minute per CID. Exceeding this limit
        returns HTTP 429 (Too Many Requests).

        Scope required: Cloud Security API Risks: READ

        This operation targets
        ``/cloud-security-timeline/entities/cloud-risks-enriched-timeline/v1``
        which is not yet in FalconPy 1.6.1. It is dispatched via the FalconPy
        UberClass ``override`` parameter so no SDK update is needed.
        """
        # Build query parameters (strips None values).
        prepared = prepare_api_parameters({"id": id})

        # Dispatch via override because the operation ID is not in FalconPy 1.6.1.
        response = self.client.command_for(
            # The first positional arg becomes api_operation; because override is
            # provided, FalconPy ignores the operation ID lookup and uses the raw
            # HTTP method + path from the override string instead.
            "cloud_security_timeline_risks_enriched",
            member_cid=member_cid,
            parameters=prepared,
            override=_ENRICHED_TIMELINE_OVERRIDE,
        )

        return handle_api_response(
            response,
            operation="cloud_security_timeline_risks_enriched",
            error_message="cloud_security_timeline_risks_enriched failed",
            default_result=[],
        )
