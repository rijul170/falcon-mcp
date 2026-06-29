"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `knowledge_base_audit_events` API service collection
(Charlotte AI Agentic Studio — /agentic-studio/…/knowledge_base_audit_events/… endpoints)."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenKnowledgeBaseAuditEventsModule(GeneratedModuleBase):
    """Generated tools for the Falcon `knowledge_base_audit_events` collection (Charlotte AI Agentic Studio)."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.combined_knowledge_base_audit_events_v1, name="combined_knowledge_base_audit_events_v1")
        self._add_tool(server=server, method=self.entities_knowledge_base_audit_events_v1, name="entities_knowledge_base_audit_events_v1")
        self._add_tool(server=server, method=self.queries_knowledge_base_audit_events_v1, name="queries_knowledge_base_audit_events_v1")
        self._add_tool(server=server, method=self.aggregates_knowledge_base_audit_events_v1, name="aggregates_knowledge_base_audit_events_v1", annotations=WRITE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    # ------------------------------------------------------------------
    # READ operations
    # ------------------------------------------------------------------

    def combined_knowledge_base_audit_events_v1(
        self,
        knowledge_base_id: str | None = Field(default=None, description="ID of the knowledge base to filter audit events for."),
        offset: int | None = Field(default=None, description="Starting index of overall result set from which to return events."),
        limit: int | None = Field(default=None, description="Maximum number of events to return."),
        sort: str | None = Field(default=None, description="Sort order specification. E.g. 'created_at|desc'."),
        filter: str | None = Field(default=None, description="FQL query for filtering audit events."),
        include_deleted: bool | None = Field(default=None, description="Include audit events for deleted knowledge bases. Defaults to false."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get knowledge base audit events with full event details and pagination.

        Returns the complete audit event objects (not just IDs). Use this for an enriched
        view without a subsequent entities lookup.

        Scope: Charlotte Ai Agent Definition: READ
        Path: GET /agentic-studio/combined/knowledge_base_audit_events/v1
        """
        return self._call(
            operation="combined_knowledge_base_audit_events_v1",
            query_params={
                "knowledge_base_id": knowledge_base_id,
                "offset": offset,
                "limit": limit,
                "sort": sort,
                "filter": filter,
                "include_deleted": include_deleted,
            },
            error_message="combined_knowledge_base_audit_events_v1 failed",
            member_cid=member_cid,
        )

    def entities_knowledge_base_audit_events_v1(
        self,
        knowledge_base_id: str | None = Field(default=None, description="ID of the knowledge base to scope the lookup."),
        ids: list[str] | None = Field(default=None, description="IDs of audit event entities to retrieve."),
        include_deleted: bool | None = Field(default=None, description="Include audit events for deleted knowledge bases. Defaults to false."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve knowledge base audit event entities by their IDs.

        Scope: Charlotte Ai Agent Definition: READ
        Path: GET /agentic-studio/entities/knowledge_base_audit_events/v1
        """
        return self._call(
            operation="entities_knowledge_base_audit_events_v1",
            query_params={"knowledge_base_id": knowledge_base_id, "ids": ids, "include_deleted": include_deleted},
            error_message="entities_knowledge_base_audit_events_v1 failed",
            member_cid=member_cid,
        )

    def queries_knowledge_base_audit_events_v1(
        self,
        knowledge_base_id: str | None = Field(default=None, description="ID of the knowledge base to scope the query."),
        offset: int | None = Field(default=None, description="Starting index of overall result set from which to return IDs."),
        limit: int | None = Field(default=None, description="Maximum number of IDs to return."),
        sort: str | None = Field(default=None, description="Sort order specification. E.g. 'created_at|desc'."),
        filter: str | None = Field(default=None, description="FQL query for filtering audit event IDs."),
        include_deleted: bool | None = Field(default=None, description="Include audit events for deleted knowledge bases. Defaults to false."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Query knowledge base audit event IDs with pagination and filtering.

        Returns a list of event IDs. Follow up with entities_knowledge_base_audit_events_v1
        to retrieve full event details, or use combined_knowledge_base_audit_events_v1 directly.

        Scope: Charlotte Ai Agent Definition: READ
        Path: GET /agentic-studio/queries/knowledge_base_audit_events/v1
        """
        return self._call(
            operation="queries_knowledge_base_audit_events_v1",
            query_params={
                "knowledge_base_id": knowledge_base_id,
                "offset": offset,
                "limit": limit,
                "sort": sort,
                "filter": filter,
                "include_deleted": include_deleted,
            },
            error_message="queries_knowledge_base_audit_events_v1 failed",
            member_cid=member_cid,
        )

    # ------------------------------------------------------------------
    # WRITE operations (POST body required by API, read-only in intent)
    # ------------------------------------------------------------------

    def aggregates_knowledge_base_audit_events_v1(
        self,
        body: dict = Field(description=(
            "Request JSON body for `aggregates_knowledge_base_audit_events_v1` per the CrowdStrike API schema (required). "
            "MSA aggregate criteria. Top-level optional fields: date_ranges (array), exclude (string), "
            "extended_bounds (object), field (string), filter (string), filters_spec (object), from (integer), "
            "include (string), interval (string), max_doc_count (integer), min_doc_count (integer), "
            "missing (string), name (string), percents (array), q (string), ranges (array), size (integer), "
            "sort (string), sub_aggregates (array), time_zone (string), type (string)."
        )),
        include_deleted: bool | None = Field(default=None, description="Include audit events for deleted knowledge bases. Defaults to false."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Aggregate knowledge base audit events based on the provided MSA criteria.

        Scope: Charlotte Ai Agent Definition: READ
        Path: POST /agentic-studio/aggregates/knowledge_base_audit_events/v1
        """
        return self._call(
            operation="aggregates_knowledge_base_audit_events_v1",
            query_params={"include_deleted": include_deleted},
            body_params=body,
            error_message="aggregates_knowledge_base_audit_events_v1 failed",
            member_cid=member_cid,
        )
