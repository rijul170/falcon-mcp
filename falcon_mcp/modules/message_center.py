"""
Message Center module for Falcon MCP Server.

Provides tools for working with CrowdStrike Falcon Complete cases (search/details,
activities, create case, post comments).
"""

from typing import Any

from mcp.server import FastMCP
from mcp.server.fastmcp.resources import TextResource
from mcp.types import ToolAnnotations
from pydantic import AnyUrl, Field

from falcon_mcp.common.errors import _format_error_response
from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule
from falcon_mcp.resources.message_center import MESSAGE_CENTER_FQL_DOCUMENTATION

logger = get_logger(__name__)

WRITE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True,
)


class MessageCenterModule(BaseModule):
    """Module for CrowdStrike Falcon Message Center (Complete cases)."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.search_cases, name="search_cases")
        self._add_tool(server=server, method=self.get_case_details, name="get_case_details")
        self._add_tool(server=server, method=self.search_case_activities, name="search_case_activities")
        self._add_tool(server=server, method=self.get_case_activities, name="get_case_activities")
        self._add_tool(
            server=server, method=self.create_case, name="create_case",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.add_case_comment, name="add_case_comment",
            annotations=WRITE_ANNOTATIONS,
        )

    def register_resources(self, server: FastMCP) -> None:
        self._add_resource(server, TextResource(
            uri=AnyUrl("falcon://message-center/fql-guide"),
            name="falcon_message_center_fql_guide",
            description="FQL filter guide for Message Center search tools.",
            text=MESSAGE_CENTER_FQL_DOCUMENTATION,
        ))

    def search_cases(
        self,
        filter: str | None = Field(default=None, description="FQL filter; see `falcon://message-center/fql-guide`."),
        limit: int = Field(default=10, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
        q: str | None = Field(default=None, description="Free-text query."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search Falcon Complete cases and return their details."""
        ids = self._base_search_api_call(
            operation="QueryCasesIdsByFilter",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort, "q": q},
            error_message="Failed to search cases",
        )
        if self._is_error(ids):
            if filter:
                return self._format_fql_error_response([ids], filter, MESSAGE_CENTER_FQL_DOCUMENTATION)
            return [ids]
        if not ids:
            if filter:
                return self._format_fql_error_response([], filter, MESSAGE_CENTER_FQL_DOCUMENTATION)
            return []
        details = self._base_get_by_ids(operation="GetCaseEntitiesByIDs", ids=ids, id_key="ids")
        if self._is_error(details):
            return [details]
        return details

    def get_case_details(
        self,
        ids: list[str] = Field(description="Case IDs."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get full case details for the given case IDs."""
        if not ids:
            return []
        return self._base_get_by_ids(operation="GetCaseEntitiesByIDs", ids=ids, id_key="ids")

    def search_case_activities(
        self,
        case_id: str = Field(description="Case ID to query activities for."),
        filter: str | None = Field(default=None, description="Optional FQL filter on activities."),
        limit: int = Field(default=10, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
        q: str | None = Field(default=None, description="Free-text query."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """List activity IDs on a case (returns IDs only - call get_case_activities for details)."""
        result = self._base_search_api_call(
            operation="QueryActivityByCaseID",
            search_params={
                "case_id": case_id, "filter": filter, "limit": limit,
                "offset": offset, "sort": sort, "q": q,
            },
            error_message="Failed to query case activities",
        )
        if self._is_error(result):
            return [result]
        return result

    def get_case_activities(
        self,
        ids: list[str] = Field(description="Activity IDs."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get full activity details for the given activity IDs."""
        if not ids:
            return []
        return self._base_get_by_ids(operation="GetCaseActivityByIds", ids=ids, id_key="ids")

    def create_case(
        self,
        title: str = Field(description="Case title."),
        body: str = Field(description="Case body / description."),
        case_type: str = Field(
            description="Case type. Common values: 'fc-detection-question', 'fc-incident-question', 'fc-falcon-product-support'.",
        ),
        user_uuid: str = Field(description="UUID of the user creating the case."),
        detections: list[dict[str, Any]] | None = Field(
            default=None,
            description="Optional list of related detections, each `{id, product, url}`.",
        ),
        incidents: list[dict[str, Any]] | None = Field(
            default=None,
            description="Optional list of related incidents, each `{id, url}`.",
        ),
    ) -> list[dict[str, Any]]:
        """Open a new Falcon Complete case."""
        if not title or not body:
            return [_format_error_response(
                "`title` and `body` are required.", operation="CreateCaseV2",
            )]
        payload: dict[str, Any] = {
            "title": title, "body": body, "type": case_type, "user_uuid": user_uuid,
        }
        if detections:
            payload["detections"] = detections
        if incidents:
            payload["incidents"] = incidents
        result = self._base_query_api_call(
            operation="CreateCaseV2",
            body_params=payload,
            error_message="Failed to create case",
        )
        if self._is_error(result):
            return [result]
        return result

    def add_case_comment(
        self,
        case_id: str = Field(description="Case ID."),
        comment: str = Field(description="Comment content."),
        user_uuid: str = Field(description="UUID of the user posting the comment."),
    ) -> list[dict[str, Any]]:
        """Post a comment to a case (only `type=comment` activities are permitted via API)."""
        if not comment:
            return [_format_error_response(
                "`comment` is required.", operation="CaseAddActivity",
            )]
        payload = {
            "case_id": case_id,
            "body": comment,
            "type": "comment",
            "user_uuid": user_uuid,
        }
        result = self._base_query_api_call(
            operation="CaseAddActivity",
            body_params=payload,
            error_message="Failed to post case comment",
        )
        if self._is_error(result):
            return [result]
        return result
