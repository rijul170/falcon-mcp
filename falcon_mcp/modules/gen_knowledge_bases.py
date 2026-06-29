"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `knowledge_bases` API service collection
(Charlotte AI Agentic Studio — /agentic-studio/…/knowledge_bases/… endpoints)."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenKnowledgeBasesModule(GeneratedModuleBase):
    """Generated tools for the Falcon `knowledge_bases` collection (Charlotte AI Agentic Studio)."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.entities_knowledge_bases_v1, name="entities_knowledge_bases_v1")
        self._add_tool(server=server, method=self.queries_knowledge_bases_v1, name="queries_knowledge_bases_v1")
        self._add_tool(server=server, method=self.aggregates_knowledge_bases_v1, name="aggregates_knowledge_bases_v1", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_knowledge_bases_create_v1, name="entities_knowledge_bases_create_v1", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_knowledge_bases_update_v1, name="entities_knowledge_bases_update_v1", annotations=WRITE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    # ------------------------------------------------------------------
    # READ operations
    # ------------------------------------------------------------------

    def entities_knowledge_bases_v1(
        self,
        ids: list[str] = Field(description="IDs of knowledge base entities to retrieve (required)."),
        include_deleted: bool | None = Field(default=None, description="Include deleted knowledge bases in the result. Defaults to false."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve knowledge base entities for the provided IDs.

        Scope: Charlotte Ai Agent Definition: READ
        Path: GET /agentic-studio/entities/knowledge_bases/v1
        """
        return self._call(
            operation="entities_knowledge_bases_v1",
            query_params={"ids": ids, "include_deleted": include_deleted},
            error_message="entities_knowledge_bases_v1 failed",
            member_cid=member_cid,
        )

    def queries_knowledge_bases_v1(
        self,
        offset: int | None = Field(default=None, description="Starting index of overall result set from which to return IDs."),
        limit: int | None = Field(default=None, description="Number of IDs to return. Offset + limit should NOT be above 10K."),
        sort: str | None = Field(default=None, description="Order by fields: name, created_at. E.g. 'created_at|desc' or 'name|asc'."),
        filter: str | None = Field(default=None, description="FQL query specifying the filter parameters."),
        include_deleted: bool | None = Field(default=None, description="Include deleted knowledge bases in the result. Defaults to false."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Query knowledge base IDs based on the provided FQL filters.

        Scope: Charlotte Ai Agent Definition: READ
        Path: GET /agentic-studio/queries/knowledge_bases/v1
        """
        return self._call(
            operation="queries_knowledge_bases_v1",
            query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter, "include_deleted": include_deleted},
            error_message="queries_knowledge_bases_v1 failed",
            member_cid=member_cid,
        )

    # ------------------------------------------------------------------
    # WRITE operations
    # ------------------------------------------------------------------

    def aggregates_knowledge_bases_v1(
        self,
        body: dict = Field(description=(
            "Request JSON body for `aggregates_knowledge_bases_v1` per the CrowdStrike API schema (required). "
            "MSA aggregate criteria. Top-level optional fields: date_ranges (array), exclude (string), "
            "extended_bounds (object), field (string), filter (string), filters_spec (object), from (integer), "
            "include (string), interval (string), max_doc_count (integer), min_doc_count (integer), "
            "missing (string), name (string), percents (array), q (string), ranges (array), size (integer), "
            "sort (string), sub_aggregates (array), time_zone (string), type (string)."
        )),
        include_deleted: bool | None = Field(default=None, description="Include deleted knowledge bases in the result. Defaults to false."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Aggregate knowledge bases based on the provided MSA criteria.

        Scope: Charlotte Ai Agent Definition: READ
        Path: POST /agentic-studio/aggregates/knowledge_bases/v1
        """
        return self._call(
            operation="aggregates_knowledge_bases_v1",
            query_params={"include_deleted": include_deleted},
            body_params=body,
            error_message="aggregates_knowledge_bases_v1 failed",
            member_cid=member_cid,
        )

    def entities_knowledge_bases_create_v1(
        self,
        body: dict = Field(description=(
            "Request JSON body for `entities_knowledge_bases_create_v1` per the CrowdStrike API schema (required). "
            "To delete, provide is_deleted=true in the body. "
            "Optional fields: created_at (string), created_by (object), description (string), "
            "embedding_model (string), files_count (integer), id (string), is_deleted (boolean), "
            "name (string), updated_at (string), updated_by (object)."
        )),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create or update a knowledge base. For deletion, provide is_deleted=true in the body.

        Scope: Charlotte Ai Agent Definition: WRITE
        Path: POST /agentic-studio/entities/knowledge_bases/v1
        """
        return self._call(
            operation="entities_knowledge_bases_create_v1",
            body_params=body,
            error_message="entities_knowledge_bases_create_v1 failed",
            member_cid=member_cid,
        )

    def entities_knowledge_bases_update_v1(
        self,
        body: dict = Field(description=(
            "Request JSON body for `entities_knowledge_bases_update_v1` per the CrowdStrike API schema (required). "
            "Optional fields: created_at (string), created_by (object), description (string), "
            "embedding_model (string), files_count (integer), id (string), is_deleted (boolean), "
            "name (string), updated_at (string), updated_by (object)."
        )),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update an existing knowledge base.

        Scope: Charlotte Ai Agent Definition: WRITE
        Path: PATCH /agentic-studio/entities/knowledge_bases/v1
        """
        return self._call(
            operation="entities_knowledge_bases_update_v1",
            body_params=body,
            error_message="entities_knowledge_bases_update_v1 failed",
            member_cid=member_cid,
        )
