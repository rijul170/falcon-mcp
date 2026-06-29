"""
NGSIEM Case Management module for Falcon MCP Server.

Provides tools for searching/getting/creating/updating NGSIEM cases and managing tags
and evidence (alerts/events) attached to them.
"""

from typing import Any

from mcp.server import FastMCP
from mcp.server.fastmcp.resources import TextResource
from mcp.types import ToolAnnotations
from pydantic import AnyUrl, Field

from falcon_mcp.common.errors import _format_error_response
from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule
from falcon_mcp.resources.case_management import CASE_MANAGEMENT_FQL_DOCUMENTATION

logger = get_logger(__name__)

WRITE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True,
)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True,
)


class CaseManagementModule(BaseModule):
    """Module for CrowdStrike NGSIEM Case Management."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.search_ngsiem_cases, name="search_ngsiem_cases")
        self._add_tool(server=server, method=self.get_ngsiem_case_details, name="get_ngsiem_case_details")
        self._add_tool(
            server=server, method=self.create_ngsiem_case, name="create_ngsiem_case",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.update_ngsiem_case, name="update_ngsiem_case",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.add_ngsiem_case_tags, name="add_ngsiem_case_tags",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.remove_ngsiem_case_tags, name="remove_ngsiem_case_tags",
            annotations=DESTRUCTIVE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.attach_alert_evidence, name="attach_alert_evidence",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.attach_event_evidence, name="attach_event_evidence",
            annotations=WRITE_ANNOTATIONS,
        )
        # Notification groups
        self._add_tool(server=server, method=self.search_notification_groups, name="search_notification_groups")
        self._add_tool(server=server, method=self.get_notification_groups, name="get_notification_groups")
        self._add_tool(server=server, method=self.create_notification_group, name="create_notification_group", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_notification_group, name="update_notification_group", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_notification_groups, name="delete_notification_groups", annotations=DESTRUCTIVE_ANNOTATIONS)
        # SLAs
        self._add_tool(server=server, method=self.search_case_slas, name="search_case_slas")
        self._add_tool(server=server, method=self.get_case_sla, name="get_case_sla")
        self._add_tool(server=server, method=self.create_case_sla, name="create_case_sla", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_case_sla, name="update_case_sla", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_case_slas, name="delete_case_slas", annotations=DESTRUCTIVE_ANNOTATIONS)
        # Templates
        self._add_tool(server=server, method=self.search_case_templates, name="search_case_templates")
        self._add_tool(server=server, method=self.get_case_template, name="get_case_template")
        self._add_tool(server=server, method=self.create_case_template, name="create_case_template", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_case_template, name="update_case_template", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_case_templates, name="delete_case_templates", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.export_case_template, name="export_case_template")
        self._add_tool(server=server, method=self.import_case_template, name="import_case_template", annotations=WRITE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        self._add_resource(server, TextResource(
            uri=AnyUrl("falcon://ngsiem-cases/fql-guide"),
            name="falcon_ngsiem_cases_fql_guide",
            description="FQL filter guide for NGSIEM case search.",
            text=CASE_MANAGEMENT_FQL_DOCUMENTATION,
        ))

    def search_ngsiem_cases(
        self,
        filter: str | None = Field(default=None, description="FQL filter; see `falcon://ngsiem-cases/fql-guide`."),
        limit: int = Field(default=10, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
        q: str | None = Field(default=None, description="Free-text query."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search NGSIEM cases and return their full details."""
        ids = self._base_search_api_call(
            operation="queries_cases_get_v1",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort, "q": q},
            error_message="Failed to search NGSIEM cases",
        )
        if self._is_error(ids):
            if filter:
                return self._format_fql_error_response([ids], filter, CASE_MANAGEMENT_FQL_DOCUMENTATION)
            return [ids]
        if not ids:
            if filter:
                return self._format_fql_error_response([], filter, CASE_MANAGEMENT_FQL_DOCUMENTATION)
            return []
        details = self._base_get_by_ids(operation="entities_cases_post_v2", ids=ids, id_key="ids")
        if self._is_error(details):
            return [details]
        return details

    def get_ngsiem_case_details(
        self,
        ids: list[str] = Field(description="Case IDs."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get full case details for the given case IDs."""
        if not ids:
            return []
        return self._base_get_by_ids(operation="entities_cases_post_v2", ids=ids, id_key="ids")

    def create_ngsiem_case(
        self,
        name: str = Field(description="Case name."),
        description: str | None = Field(default=None, description="Case description."),
        severity: int = Field(default=3, ge=1, le=5, description="Severity 1-5."),
        status: str | None = Field(default=None, description="Case status (e.g. 'New', 'In Progress')."),
        assigned_to_user_uuid: str | None = Field(default=None, description="UUID of the assignee."),
        tags: list[str] | None = Field(default=None, description="Tags to attach."),
        alert_ids: list[str] | None = Field(default=None, description="Linked alert IDs."),
        event_ids: list[str] | None = Field(default=None, description="Linked event IDs."),
        template_id: str | None = Field(default=None, description="Optional template ID."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Create an NGSIEM case (operation_id `entities_cases_put_v2`)."""
        body: dict[str, Any] = {"name": name, "severity": severity}
        if description is not None:
            body["description"] = description
        if status is not None:
            body["status"] = status
        if assigned_to_user_uuid is not None:
            body["assigned_to_user_uuid"] = assigned_to_user_uuid
        if tags is not None:
            body["tags"] = tags
        evidence: dict[str, Any] = {}
        if alert_ids:
            evidence["alerts"] = [{"id": a} for a in alert_ids]
        if event_ids:
            evidence["events"] = [{"id": e} for e in event_ids]
        if evidence:
            body["evidence"] = evidence
        if template_id:
            body["template"] = {"id": template_id}
        result = self._base_query_api_call(
            operation="entities_cases_put_v2",
            body_params=body,
            error_message="Failed to create NGSIEM case",
        )
        if self._is_error(result):
            return [result]
        return result

    def update_ngsiem_case(
        self,
        id: str = Field(description="Case ID."),
        name: str | None = Field(default=None, description="New name."),
        description: str | None = Field(default=None, description="New description."),
        severity: int | None = Field(default=None, ge=1, le=5, description="Severity 1-5."),
        status: str | None = Field(default=None, description="New status."),
        assigned_to_user_uuid: str | None = Field(default=None, description="New assignee UUID."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Update an NGSIEM case (operation_id `entities_cases_patch_v2`)."""
        body: dict[str, Any] = {"id": id}
        if name is not None:
            body["name"] = name
        if description is not None:
            body["description"] = description
        if severity is not None:
            body["severity"] = severity
        if status is not None:
            body["status"] = status
        if assigned_to_user_uuid is not None:
            body["assigned_to_user_uuid"] = assigned_to_user_uuid
        if len(body) == 1:
            return [_format_error_response(
                "Provide at least one field to update.",
                operation="entities_cases_patch_v2",
            )]
        result = self._base_query_api_call(
            operation="entities_cases_patch_v2",
            body_params=body,
            error_message="Failed to update NGSIEM case",
        )
        if self._is_error(result):
            return [result]
        return result

    def add_ngsiem_case_tags(
        self,
        id: str = Field(description="Case ID."),
        tags: list[str] = Field(description="Tags to add."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Add tags to an NGSIEM case."""
        if not tags:
            return [_format_error_response(
                "`tags` is required.", operation="entities_case_tags_post_v1",
            )]
        result = self._base_query_api_call(
            operation="entities_case_tags_post_v1",
            body_params={"id": id, "tags": tags},
            error_message="Failed to add case tags",
        )
        if self._is_error(result):
            return [result]
        return result

    def remove_ngsiem_case_tags(
        self,
        id: str = Field(description="Case ID."),
        tags: list[str] = Field(description="Tags to remove."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Remove tags from an NGSIEM case (DELETE with id + tag query params)."""
        if not tags:
            return [_format_error_response(
                "`tags` is required.", operation="entities_case_tags_delete_v1",
            )]
        result = self._base_query_api_call(
            operation="entities_case_tags_delete_v1",
            query_params={"id": id, "tag": tags},
            error_message="Failed to remove case tags",
        )
        if self._is_error(result):
            return [result]
        return result

    def attach_alert_evidence(
        self,
        case_id: str = Field(description="Case ID."),
        alert_ids: list[str] = Field(description="Alert IDs to attach as evidence."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Attach alert evidence to an NGSIEM case."""
        if not alert_ids:
            return [_format_error_response(
                "`alert_ids` is required.", operation="entities_alert_evidence_post_v1",
            )]
        body = {"id": case_id, "alerts": [{"id": a} for a in alert_ids]}
        result = self._base_query_api_call(
            operation="entities_alert_evidence_post_v1",
            body_params=body,
            error_message="Failed to attach alert evidence",
        )
        if self._is_error(result):
            return [result]
        return result

    def attach_event_evidence(
        self,
        case_id: str = Field(description="Case ID."),
        event_ids: list[str] = Field(description="Event IDs to attach as evidence."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Attach event evidence to an NGSIEM case."""
        if not event_ids:
            return [_format_error_response(
                "`event_ids` is required.", operation="entities_event_evidence_post_v1",
            )]
        body = {"id": case_id, "events": [{"id": e} for e in event_ids]}
        result = self._base_query_api_call(
            operation="entities_event_evidence_post_v1",
            body_params=body,
            error_message="Failed to attach event evidence",
        )
        if self._is_error(result):
            return [result]
        return result

    # --- Notification groups -----------------------------------------------

    def search_notification_groups(
        self,
        filter: str | None = Field(default=None, description="FQL filter."),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search case notification groups and return full details.

        Notification groups define who gets alerted when a case is created or updated.
        """
        ids = self._base_search_api_call(
            operation="queries_notification_groups_get_v1",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search notification groups",
        )
        if self._is_error(ids):
            return [ids]
        if not ids:
            return []
        details = self._base_get_by_ids(
            operation="entities_notification_groups_get_v1", ids=ids, use_params=True,
        )
        if self._is_error(details):
            return [details]
        return details

    def get_notification_groups(
        self,
        ids: list[str] = Field(description="Notification group IDs."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get notification group details by ID."""
        if not ids:
            return []
        return self._base_get_by_ids(
            operation="entities_notification_groups_get_v1", ids=ids, use_params=True,
        )

    def create_notification_group(
        self,
        name: str = Field(description="Group name."),
        user_uuids: list[str] | None = Field(default=None, description="User UUIDs to include in this group."),
        notification_settings: dict[str, Any] | None = Field(
            default=None,
            description="Notification channel settings (e.g., email, Slack). Format is connector-specific.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Create a case notification group."""
        body: dict[str, Any] = {"name": name}
        if user_uuids is not None:
            body["user_uuids"] = user_uuids
        if notification_settings is not None:
            body["notification_settings"] = notification_settings
        result = self._base_query_api_call(
            operation="entities_notification_groups_post_v1",
            body_params=body,
            error_message="Failed to create notification group",
        )
        if self._is_error(result):
            return [result]
        return result

    def update_notification_group(
        self,
        id: str = Field(description="Notification group ID."),
        name: str | None = Field(default=None, description="New name."),
        user_uuids: list[str] | None = Field(default=None, description="Replacement user UUID list."),
        notification_settings: dict[str, Any] | None = Field(default=None, description="Updated notification settings."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Update a case notification group."""
        body: dict[str, Any] = {"id": id}
        if name is not None:
            body["name"] = name
        if user_uuids is not None:
            body["user_uuids"] = user_uuids
        if notification_settings is not None:
            body["notification_settings"] = notification_settings
        if len(body) == 1:
            return [_format_error_response(
                "Provide at least one field to update.", operation="entities_notification_groups_patch_v1",
            )]
        result = self._base_query_api_call(
            operation="entities_notification_groups_patch_v1",
            body_params=body,
            error_message="Failed to update notification group",
        )
        if self._is_error(result):
            return [result]
        return result

    def delete_notification_groups(
        self,
        ids: list[str] = Field(description="Notification group IDs to delete."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Delete case notification groups by ID."""
        if not ids:
            return [_format_error_response("`ids` is required.", operation="entities_notification_groups_delete_v1")]
        result = self._base_query_api_call(
            operation="entities_notification_groups_delete_v1",
            query_params={"ids": ids},
            error_message="Failed to delete notification groups",
        )
        if self._is_error(result):
            return [result]
        return result

    # --- SLAs --------------------------------------------------------------

    def search_case_slas(
        self,
        filter: str | None = Field(default=None, description="FQL filter."),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search case SLA definitions and return full details."""
        ids = self._base_search_api_call(
            operation="queries_slas_get_v1",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search case SLAs",
        )
        if self._is_error(ids):
            return [ids]
        if not ids:
            return []
        details = self._base_get_by_ids(
            operation="entities_slas_get_v1", ids=ids, use_params=True,
        )
        if self._is_error(details):
            return [details]
        return details

    def get_case_sla(
        self,
        ids: list[str] = Field(description="SLA IDs."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get case SLA details by ID."""
        if not ids:
            return []
        return self._base_get_by_ids(operation="entities_slas_get_v1", ids=ids, use_params=True)

    def create_case_sla(
        self,
        sla_body: dict[str, Any] = Field(
            description=(
                "SLA definition object. Typical fields: `name` (str), `duration_minutes` (int), "
                "`severity_levels` (list of severity ints), `case_types` (list of case type strings). "
                "Example: {\"name\": \"P1 SLA\", \"duration_minutes\": 240, \"severity_levels\": [1, 2]}"
            ),
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Create a case SLA definition."""
        result = self._base_query_api_call(
            operation="entities_slas_post_v1",
            body_params=sla_body,
            error_message="Failed to create case SLA",
        )
        if self._is_error(result):
            return [result]
        return result

    def update_case_sla(
        self,
        id: str = Field(description="SLA ID to update."),
        sla_body: dict[str, Any] = Field(
            description="Updated SLA fields. Must include `id`. All provided fields will be replaced.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Update a case SLA definition."""
        body = {**sla_body, "id": id}
        result = self._base_query_api_call(
            operation="entities_slas_patch_v1",
            body_params=body,
            error_message="Failed to update case SLA",
        )
        if self._is_error(result):
            return [result]
        return result

    def delete_case_slas(
        self,
        ids: list[str] = Field(description="SLA IDs to delete."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Delete case SLA definitions by ID."""
        if not ids:
            return [_format_error_response("`ids` is required.", operation="entities_slas_delete_v1")]
        result = self._base_query_api_call(
            operation="entities_slas_delete_v1",
            query_params={"ids": ids},
            error_message="Failed to delete case SLAs",
        )
        if self._is_error(result):
            return [result]
        return result

    # --- Case templates ----------------------------------------------------

    def search_case_templates(
        self,
        filter: str | None = Field(default=None, description="FQL filter."),
        limit: int = Field(default=20, ge=1, le=500, description="Max records."),
        offset: int = Field(default=0, ge=0, description="Offset."),
        sort: str | None = Field(default=None, description="Sort expression."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search case templates and return full details."""
        ids = self._base_search_api_call(
            operation="queries_templates_get_v1",
            search_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
            error_message="Failed to search case templates",
        )
        if self._is_error(ids):
            return [ids]
        if not ids:
            return []
        details = self._base_get_by_ids(
            operation="entities_templates_get_v1", ids=ids, use_params=True,
        )
        if self._is_error(details):
            return [details]
        return details

    def get_case_template(
        self,
        ids: list[str] = Field(description="Template IDs."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Get case template details by ID."""
        if not ids:
            return []
        return self._base_get_by_ids(operation="entities_templates_get_v1", ids=ids, use_params=True)

    def create_case_template(
        self,
        template_body: dict[str, Any] = Field(
            description=(
                "Template definition object. Typical fields: `name` (str), `description` (str), "
                "`case_type` (str), `severity` (int), `fields` (list of field dicts). "
                "Example: {\"name\": \"Phishing Template\", \"case_type\": \"incident\", \"severity\": 2}"
            ),
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Create a case template."""
        result = self._base_query_api_call(
            operation="entities_templates_post_v1",
            body_params=template_body,
            error_message="Failed to create case template",
        )
        if self._is_error(result):
            return [result]
        return result

    def update_case_template(
        self,
        id: str = Field(description="Template ID to update."),
        template_body: dict[str, Any] = Field(
            description="Updated template fields. `id` will be merged automatically.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Update a case template."""
        body = {**template_body, "id": id}
        result = self._base_query_api_call(
            operation="entities_templates_patch_v1",
            body_params=body,
            error_message="Failed to update case template",
        )
        if self._is_error(result):
            return [result]
        return result

    def delete_case_templates(
        self,
        ids: list[str] = Field(description="Template IDs to delete."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Delete case templates by ID."""
        if not ids:
            return [_format_error_response("`ids` is required.", operation="entities_templates_delete_v1")]
        result = self._base_query_api_call(
            operation="entities_templates_delete_v1",
            query_params={"ids": ids},
            error_message="Failed to delete case templates",
        )
        if self._is_error(result):
            return [result]
        return result

    def export_case_template(
        self,
        id: str = Field(description="Template ID to export. Obtain from `falcon_search_case_templates`."),
    ) -> dict[str, Any]:
        """Export a case template as JSON.

        Returns the template definition suitable for backup or importing into another CID.
        """
        from falcon_mcp.common.errors import handle_api_response
        response = self.client.command_for("entities_templates_export_get_v1", parameters={"id": id})
        if not isinstance(response, dict):
            return {"error": "Unexpected response format"}
        status = response.get("status_code")
        if status not in (200, None):
            return handle_api_response(
                response, operation="entities_templates_export_get_v1",
                error_message="Failed to export case template", default_result={},
            )
        body = response.get("body", {})
        if isinstance(body, (bytes, bytearray)):
            import json
            try:
                return json.loads(body.decode("utf-8"))
            except Exception:
                return {"template_data": body.decode("utf-8", errors="replace")}
        return body if isinstance(body, dict) else {"template_data": str(body)}

    def import_case_template(
        self,
        template_body: dict[str, Any] = Field(
            description="Template definition to import. Use the output from `falcon_export_case_template` as the source.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Import a case template from a definition object.

        Creates a new template from the provided definition. Useful for replicating templates
        across CIDs or restoring from a backup exported via `falcon_export_case_template`.
        """
        result = self._base_query_api_call(
            operation="entities_templates_import_post_v1",
            body_params=template_body,
            error_message="Failed to import case template",
        )
        if self._is_error(result):
            return [result]
        return result
