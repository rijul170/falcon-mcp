"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `identity_protection` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenIdentityProtectionModule(GeneratedModuleBase):
    """Generated tools for the Falcon `identity_protection` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_sensor_details, name="get_sensor_details")
        self._add_tool(server=server, method=self.get_sensor_aggregates, name="get_sensor_aggregates")
        self._add_tool(server=server, method=self.query_sensors_by_filter, name="query_sensors_by_filter")
        self._add_tool(server=server, method=self.post_graphql, name="post_graphql", annotations=WRITE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def get_sensor_aggregates(
        self,
        body: dict = Field(description="Aggregate query body per the CrowdStrike API schema. Supports fields: date_ranges, exclude, field, filter, from, include, interval, min_doc_count, missing, name, q, ranges, size, sort, sub_aggregates, time_zone, type."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get aggregate device-level sensor statistics (POST /identity-protection/aggregates/devices/GET/v1).

        Use for dashboarding: count sensors by OS platform, status, version, site, or any
        keyword field. Supports histogram, terms, and date_range aggregation types.
        Requires: Identity Protection Entities: READ scope.
        """
        return self._call(operation="GetSensorAggregates", query_params=None, body_params=body, error_message="GetSensorAggregates failed", member_cid=member_cid)

    def get_sensor_details(
        self,
        body: dict = Field(description="Request JSON body for `GetSensorDetails` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get details on one or more sensors by providing device IDs in a POST body. Supports up to a maximum of 5000 IDs."""
        return self._call(operation="GetSensorDetails", query_params=None, body_params=body, error_message="GetSensorDetails failed", member_cid=member_cid)

    def query_sensors_by_filter(
        self,
        offset: int | None = Field(default=None, description="The offset to start retrieving records from"),
        limit: int | None = Field(default=None, description="The maximum records to return. [1-200]"),
        sort: str | None = Field(default=None, description="The property to sort by (e.g. status.desc or hostname.asc)"),
        filter: str | None = Field(default=None, description="The filter expression that should be used to limit the results"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for sensors in your environment by hostname, IP, and other criteria."""
        return self._call(operation="QuerySensorsByFilter", query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter}, error_message="QuerySensorsByFilter failed", member_cid=member_cid)

    def post_graphql(
        self,
        body: dict = Field(description="Request JSON body for `post_graphql` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Identity Protection GraphQL API. Allows to retrieve entities, timeline activities, identity-based incidents and security assessment. Allows to perform actions on entities and identity-based incidents."""
        return self._call(operation="post_graphql", query_params=None, body_params=body, error_message="post_graphql failed", member_cid=member_cid)
