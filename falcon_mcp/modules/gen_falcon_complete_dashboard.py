"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `falcon_complete_dashboard` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenFalconCompleteDashboardModule(GeneratedModuleBase):
    """Generated tools for the Falcon `falcon_complete_dashboard` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_device_count_collection_queries_by_filter, name="get_device_count_collection_queries_by_filter")
        self._add_tool(server=server, method=self.query_alert_ids_by_filter_v2, name="query_alert_ids_by_filter_v2")
        self._add_tool(server=server, method=self.query_allow_list_filter, name="query_allow_list_filter")
        self._add_tool(server=server, method=self.query_block_list_filter, name="query_block_list_filter")
        self._add_tool(server=server, method=self.query_escalations_filter, name="query_escalations_filter")
        self._add_tool(server=server, method=self.query_incident_ids_by_filter, name="query_incident_ids_by_filter")
        self._add_tool(server=server, method=self.query_remediations_filter, name="query_remediations_filter")

    def register_resources(self, server: FastMCP) -> None:
        pass

    def get_device_count_collection_queries_by_filter(
        self,
        limit: int | None = Field(default=None, description="The maximum records to return. [1-500]"),
        sort: str | None = Field(default=None, description="The property to sort on, followed by a dot (.), followed by the sort direction, either 'asc' or 'desc'."),
        filter: str | None = Field(default=None, description="Optional filter and sort criteria in the form of an FQL query. For more information about FQL queries, see [our FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide)."),
        offset: str | None = Field(default=None, description="Starting index of overall result set from which to return ids."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve device count collection Ids that match the provided FQL filter, criteria with scrolling enabled"""
        return self._call(operation="GetDeviceCountCollectionQueriesByFilter", query_params={"limit": limit, "sort": sort, "filter": filter, "offset": offset}, error_message="GetDeviceCountCollectionQueriesByFilter failed", member_cid=member_cid)

    def query_alert_ids_by_filter_v2(
        self,
        limit: int | None = Field(default=None, description="The maximum records to return. [1-500]"),
        sort: str | None = Field(default=None, description="The property to sort on, followed by a dot (.), followed by the sort direction, either 'asc' or 'desc'."),
        filter: str | None = Field(default=None, description="Optional filter and sort criteria in the form of an FQL query. For more information about FQL queries, see [our FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide)."),
        offset: str | None = Field(default=None, description="Starting index of overall result set from which to return ids."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve Alerts Ids for epp, idp and ngsiem that match the provided FQL filter criteria with scrolling enabled"""
        return self._call(operation="QueryAlertIdsByFilterV2", query_params={"limit": limit, "sort": sort, "filter": filter, "offset": offset}, error_message="QueryAlertIdsByFilterV2 failed", member_cid=member_cid)

    def query_allow_list_filter(
        self,
        limit: int | None = Field(default=None, description="The maximum records to return. [1-500]"),
        sort: str | None = Field(default=None, description="The property to sort on, followed by a dot (.), followed by the sort direction, either 'asc' or 'desc'."),
        filter: str | None = Field(default=None, description="Optional filter and sort criteria in the form of an FQL query. For more information about FQL queries, see [our FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide)."),
        offset: str | None = Field(default=None, description="Starting index of overall result set from which to return ids."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve allowlist tickets that match the provided filter criteria with scrolling enabled"""
        return self._call(operation="QueryAllowListFilter", query_params={"limit": limit, "sort": sort, "filter": filter, "offset": offset}, error_message="QueryAllowListFilter failed", member_cid=member_cid)

    def query_block_list_filter(
        self,
        limit: int | None = Field(default=None, description="The maximum records to return. [1-500]"),
        sort: str | None = Field(default=None, description="The property to sort on, followed by a dot (.), followed by the sort direction, either 'asc' or 'desc'."),
        filter: str | None = Field(default=None, description="Optional filter and sort criteria in the form of an FQL query. For more information about FQL queries, see [our FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide)."),
        offset: str | None = Field(default=None, description="Starting index of overall result set from which to return ids."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve block listtickets that match the provided filter criteria with scrolling enabled"""
        return self._call(operation="QueryBlockListFilter", query_params={"limit": limit, "sort": sort, "filter": filter, "offset": offset}, error_message="QueryBlockListFilter failed", member_cid=member_cid)

    def query_escalations_filter(
        self,
        limit: int | None = Field(default=None, description="The maximum records to return. [1-500]"),
        sort: str | None = Field(default=None, description="The property to sort on, followed by a dot (.), followed by the sort direction, either 'asc' or 'desc'."),
        filter: str | None = Field(default=None, description="Optional filter and sort criteria in the form of an FQL query. For more information about FQL queries, see [our FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide)."),
        offset: str | None = Field(default=None, description="Starting index of overall result set from which to return ids."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve escalation tickets that match the provided filter criteria with scrolling enabled"""
        return self._call(operation="QueryEscalationsFilter", query_params={"limit": limit, "sort": sort, "filter": filter, "offset": offset}, error_message="QueryEscalationsFilter failed", member_cid=member_cid)

    def query_incident_ids_by_filter(
        self,
        limit: int | None = Field(default=None, description="The maximum records to return. [1-500]"),
        sort: str | None = Field(default=None, description="The property to sort on, followed by a dot (.), followed by the sort direction, either 'asc' or 'desc'."),
        filter: str | None = Field(default=None, description="Optional filter and sort criteria in the form of an FQL query. For more information about FQL queries, see [our FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide)."),
        offset: str | None = Field(default=None, description="Starting index of overall result set from which to return ids."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve incidents that match the provided filter criteria with scrolling enabled"""
        return self._call(operation="QueryIncidentIdsByFilter", query_params={"limit": limit, "sort": sort, "filter": filter, "offset": offset}, error_message="QueryIncidentIdsByFilter failed", member_cid=member_cid)

    def query_remediations_filter(
        self,
        limit: int | None = Field(default=None, description="The maximum records to return. [1-500]"),
        sort: str | None = Field(default=None, description="The property to sort on, followed by a dot (.), followed by the sort direction, either 'asc' or 'desc'."),
        filter: str | None = Field(default=None, description="Optional filter and sort criteria in the form of an FQL query. For more information about FQL queries, see [our FQL documentation in Falcon](https://falcon.crowdstrike.com/support/documentation/45/falcon-query-language-feature-guide)."),
        offset: str | None = Field(default=None, description="Starting index of overall result set from which to return ids."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve remediation tickets that match the provided filter criteria with scrolling enabled"""
        return self._call(operation="QueryRemediationsFilter", query_params={"limit": limit, "sort": sort, "filter": filter, "offset": offset}, error_message="QueryRemediationsFilter failed", member_cid=member_cid)
