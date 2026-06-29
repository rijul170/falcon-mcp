"""
Incidents module for Falcon MCP Server

This module provides tools for accessing and analyzing CrowdStrike Falcon incidents.
"""

from typing import Any

from mcp.server import FastMCP
from mcp.server.fastmcp.resources import TextResource
from mcp.types import ToolAnnotations
from pydantic import AnyUrl, Field

from falcon_mcp.modules.base import BaseModule
from falcon_mcp.resources.incidents import (
    CROWD_SCORE_FQL_DOCUMENTATION,
    SEARCH_BEHAVIORS_FQL_DOCUMENTATION,
    SEARCH_INCIDENTS_FQL_DOCUMENTATION,
)


class IncidentsModule(BaseModule):
    """Module for accessing and analyzing CrowdStrike Falcon incidents."""

    def register_tools(self, server: FastMCP) -> None:
        """Register tools with the MCP server.

        Args:
            server: MCP server instance
        """
        # Register tools
        self._add_tool(
            server=server,
            method=self.show_crowd_score,
            name="show_crowd_score",
        )

        self._add_tool(
            server=server,
            method=self.search_incidents,
            name="search_incidents",
        )

        self._add_tool(
            server=server,
            method=self.get_incident_details,
            name="get_incident_details",
        )

        self._add_tool(
            server=server,
            method=self.search_behaviors,
            name="search_behaviors",
        )

        self._add_tool(
            server=server,
            method=self.get_behavior_details,
            name="get_behavior_details",
        )

        self._add_tool(
            server=server,
            method=self.update_incidents,
            name="update_incidents",
            annotations=ToolAnnotations(
                readOnlyHint=False,
                destructiveHint=False,
                idempotentHint=False,
                openWorldHint=True,
            ),
        )

    def register_resources(self, server: FastMCP) -> None:
        """Register resources with the MCP server.

        Args:
            server: MCP server instance
        """
        crowd_score_fql_resource = TextResource(
            uri=AnyUrl("falcon://incidents/crowd-score/fql-guide"),
            name="falcon_show_crowd_score_fql_guide",
            description="Contains the guide for the `filter` param of the `falcon_show_crowd_score` tool.",
            text=CROWD_SCORE_FQL_DOCUMENTATION,
        )

        search_incidents_fql_resource = TextResource(
            uri=AnyUrl("falcon://incidents/search/fql-guide"),
            name="falcon_search_incidents_fql_guide",
            description="Contains the guide for the `filter` param of the `falcon_search_incidents` tool.",
            text=SEARCH_INCIDENTS_FQL_DOCUMENTATION,
        )

        search_behaviors_fql_resource = TextResource(
            uri=AnyUrl("falcon://incidents/behaviors/fql-guide"),
            name="falcon_search_behaviors_fql_guide",
            description="Contains the guide for the `filter` param of the `falcon_search_behaviors` tool.",
            text=SEARCH_BEHAVIORS_FQL_DOCUMENTATION,
        )

        self._add_resource(
            server,
            crowd_score_fql_resource,
        )
        self._add_resource(
            server,
            search_incidents_fql_resource,
        )
        self._add_resource(
            server,
            search_behaviors_fql_resource,
        )

    def show_crowd_score(
        self,
        filter: str | None = Field(
            default=None,
            description="FQL Syntax formatted string used to limit the results. IMPORTANT: use the `falcon://incidents/crowd-score/fql-guide` resource when building this filter parameter.",
        ),
        limit: int = Field(
            default=10,
            ge=1,
            le=2500,
            description="Maximum number of records to return. (Max: 2500)",
        ),
        offset: int | None = Field(
            default=None,
            description="Starting index of overall result set from which to return ids.",
        ),
        sort: str | None = Field(
            default=None,
            description="The property to sort by. (Ex: modified_timestamp.desc)",
            examples={"modified_timestamp.desc"},
        ),
    ) -> dict[str, Any]:
        """View calculated CrowdScores and security posture metrics for your environment.

        IMPORTANT: You must use the `falcon://incidents/crowd-score/fql-guide` resource when you need to use the `filter` parameter.
        This resource contains the guide on how to build the FQL `filter` parameter for the `falcon_show_crowd_score` tool.
        """
        api_response = self._base_search_api_call(
            operation="CrowdScore",
            search_params={
                "filter": filter,
                "limit": limit,
                "offset": offset,
                "sort": sort,
            },
            error_message="Failed to get crowd score",
        )

        # Check if we received an error response
        if self._is_error(api_response):
            # Return the error response as is
            return api_response

        # Initialize result with all scores
        result = {
            "average_score": 0,
            "average_adjusted_score": 0,
            "scores": api_response,  # Include all the scores in the result
        }

        if api_response:  # If we have scores (list of score objects)
            score_sum = 0
            adjusted_score_sum = 0
            count = len(api_response)

            for item in api_response:
                score_sum += item.get("score", 0)
                adjusted_score_sum += item.get("adjusted_score", 0)

            if count > 0:
                # Round to ensure integer output
                result["average_score"] = round(score_sum / count)
                result["average_adjusted_score"] = round(adjusted_score_sum / count)

        return result

    def search_incidents(
        self,
        filter: str | None = Field(
            default=None,
            description="FQL Syntax formatted string used to limit the results. IMPORTANT: use the `falcon://incidents/search/fql-guide` resource when building this filter parameter.",
        ),
        limit: int = Field(
            default=10,
            ge=1,
            le=500,
            description="Maximum number of records to return. (Max: 500)",
        ),
        offset: int | None = Field(
            default=None,
            description="Starting index of overall result set from which to return ids.",
        ),
        sort: str | None = Field(
            default=None,
            description="The property to sort by. FQL syntax. Ex: state.asc, name.desc",
        ),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID to scope this call to a specific child tenant. Obtain child CIDs from `falcon_list_child_accounts`. Leave unset to use the parent account scope.",
        ),
    ) -> list[dict[str, Any]]:
        """Find and analyze security incidents to understand coordinated activity in your environment.

        IMPORTANT: You must use the `falcon://incidents/search/fql-guide` resource when you need to use the `filter` parameter.
        This resource contains the guide on how to build the FQL `filter` parameter for the `falcon_search_incidents` tool.
        """
        incident_ids = self._base_query(
            operation="QueryIncidents",
            filter=filter,
            limit=limit,
            offset=offset,
            sort=sort,
            member_cid=member_cid,
        )

        if self._is_error(incident_ids):
            return [incident_ids]

        if incident_ids:
            return self._get_incident_details_scoped(incident_ids, member_cid=member_cid)

        return []

    def get_incident_details(
        self,
        ids: list[str] = Field(description="Incident ID(s) to retrieve."),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID to scope this call to a specific child tenant. Obtain child CIDs from `falcon_list_child_accounts`. Leave unset to use the parent account scope.",
        ),
    ) -> list[dict[str, Any]]:
        """Get comprehensive incident details to understand attack patterns and coordinated activities.

        This tool returns comprehensive incident details for one or more incident IDs.
        Use this when you already have specific incident IDs and need their full details.
        For searching/discovering incidents, use the `falcon_search_incidents` tool instead.
        """
        return self._get_incident_details_scoped(ids, member_cid=member_cid)

    def search_behaviors(
        self,
        filter: str | None = Field(
            default=None,
            description="FQL Syntax formatted string used to limit the results. IMPORTANT: use the `falcon://incidents/behaviors/fql-guide` resource when building this filter parameter.",
        ),
        limit: int = Field(
            default=10,
            ge=1,
            le=500,
            description="Maximum number of records to return. (Max: 500)",
        ),
        offset: int | None = Field(
            default=None,
            description="Starting index of overall result set from which to return ids.",
        ),
        sort: str | None = Field(
            default=None,
            description="The property to sort by. (Ex: modified_timestamp.desc)",
        ),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID to scope this call to a specific child tenant. Obtain child CIDs from `falcon_list_child_accounts`. Leave unset to use the parent account scope.",
        ),
    ) -> list[dict[str, Any]]:
        """Find and analyze behaviors to understand suspicious activity in your environment.

        Use this when you need to find behaviors matching certain criteria rather than retrieving specific behaviors by ID.
        For retrieving details of known behavior IDs, use falcon_get_behavior_details instead.

        IMPORTANT: You must use the `falcon://incidents/behaviors/fql-guide` resource when you need to use the `filter` parameter.
        This resource contains the guide on how to build the FQL `filter` parameter for the `falcon_search_behaviors` tool.
        """
        behavior_ids = self._base_query(
            operation="QueryBehaviors",
            filter=filter,
            limit=limit,
            offset=offset,
            sort=sort,
            member_cid=member_cid,
        )

        if self._is_error(behavior_ids):
            return [behavior_ids]

        if behavior_ids:
            return self._get_behavior_details_scoped(behavior_ids, member_cid=member_cid)

        return []

    def get_behavior_details(
        self,
        ids: list[str] = Field(description="Behavior ID(s) to retrieve."),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID to scope this call to a specific child tenant. Obtain child CIDs from `falcon_list_child_accounts`. Leave unset to use the parent account scope.",
        ),
    ) -> list[dict[str, Any]]:
        """Get detailed behavior information to understand attack techniques and tactics.

        Use this when you already know the specific behavior ID(s) and need to retrieve their details.
        For searching behaviors based on criteria, use the `falcon_search_behaviors` tool instead.
        """
        return self._get_behavior_details_scoped(ids, member_cid=member_cid)

    def _get_incident_details_scoped(
        self, ids: list[str], member_cid: str | None = None
    ) -> list[dict[str, Any]]:
        incidents = self._base_get_by_ids(
            operation="GetIncidents",
            ids=ids,
            member_cid=member_cid,
        )
        if self._is_error(incidents):
            return [incidents]
        return incidents

    def _get_behavior_details_scoped(
        self, ids: list[str], member_cid: str | None = None
    ) -> list[dict[str, Any]]:
        behaviors = self._base_get_by_ids(
            operation="GetBehaviors",
            ids=ids,
            member_cid=member_cid,
        )
        if self._is_error(behaviors):
            return [behaviors]
        return behaviors

    def update_incidents(
        self,
        ids: list[str] = Field(
            description="Incident ID(s) to update. Obtain from `falcon_search_incidents` or `falcon_get_incident_details`.",
        ),
        status: str | None = Field(
            default=None,
            description="New status for the incident(s): `new`, `reopened`, `in_progress`, `closed`.",
            examples=["new", "reopened", "in_progress", "closed"],
        ),
        assignee_uuid: str | None = Field(
            default=None,
            description="UUID of the analyst to assign the incident(s) to.",
        ),
        unassign: bool = Field(
            default=False,
            description="Set to True to remove the current assignee from the incident(s).",
        ),
        add_tag: str | None = Field(
            default=None,
            description="Tag to add to the incident(s).",
        ),
        remove_tag: str | None = Field(
            default=None,
            description="Tag to remove from the incident(s).",
        ),
        comment: str | None = Field(
            default=None,
            description="Analyst comment to add to the incident(s).",
        ),
        member_cid: str | None = Field(
            default=None,
            description="Optional child CID to scope this call to a specific child tenant. Obtain child CIDs from `falcon_list_child_accounts`. Leave unset to use the parent account scope.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Update status, assignment, tags, or comments on one or more incidents.

        Status codes map to: new (20), reopened (25), in_progress (30), closed (40).
        Use this to close out resolved incidents, assign to analysts, or add investigation notes.
        Supports bulk updates across multiple incident IDs in a single call.
        """
        status_map = {"new": "20", "reopened": "25", "in_progress": "30", "closed": "40"}

        action_parameters = []
        if status is not None:
            action_parameters.append({"name": "update_status", "value": status_map.get(status, status)})
        if assignee_uuid is not None:
            action_parameters.append({"name": "assign_incident", "value": assignee_uuid})
        if unassign:
            action_parameters.append({"name": "unassign", "value": ""})
        if add_tag is not None:
            action_parameters.append({"name": "add_tag", "value": add_tag})
        if remove_tag is not None:
            action_parameters.append({"name": "remove_tag", "value": remove_tag})
        if comment is not None:
            action_parameters.append({"name": "add_comment", "value": comment})

        return self._base_query_api_call(
            operation="PerformIncidentAction",
            body_params={
                "ids": ids,
                "action_parameters": action_parameters,
            },
            error_message="Failed to update incidents",
            member_cid=member_cid,
        )

    def _base_query(
        self,
        operation: str,
        filter: str | None = None,
        limit: int = 100,
        offset: int | None = None,
        sort: str | None = None,
        member_cid: str | None = None,
    ) -> list[str] | dict[str, Any]:
        return self._base_search_api_call(
            operation=operation,
            search_params={
                "filter": filter,
                "limit": limit,
                "offset": offset,
                "sort": sort,
            },
            error_message="Failed to perform operation",
            member_cid=member_cid,
        )
