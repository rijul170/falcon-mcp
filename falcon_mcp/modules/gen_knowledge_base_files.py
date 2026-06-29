"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `knowledge_base_files` API service collection
(Charlotte AI Agentic Studio — /agentic-studio/…/knowledge_base_files/… endpoints)."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenKnowledgeBaseFilesModule(GeneratedModuleBase):
    """Generated tools for the Falcon `knowledge_base_files` collection (Charlotte AI Agentic Studio)."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.entities_knowledge_base_files_download_v1, name="entities_knowledge_base_files_download_v1")
        self._add_tool(server=server, method=self.entities_knowledge_base_files_v1, name="entities_knowledge_base_files_v1")
        self._add_tool(server=server, method=self.queries_knowledge_base_files_v1, name="queries_knowledge_base_files_v1")
        self._add_tool(server=server, method=self.entities_knowledge_base_files_update_v1, name="entities_knowledge_base_files_update_v1", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_knowledge_base_files_create_v1, name="entities_knowledge_base_files_create_v1", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.entities_knowledge_base_files_delete_v1, name="entities_knowledge_base_files_delete_v1", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    # ------------------------------------------------------------------
    # READ operations
    # ------------------------------------------------------------------

    def entities_knowledge_base_files_download_v1(
        self,
        knowledge_base_id: str = Field(description="ID of the knowledge base that owns the file (required)."),
        id: str = Field(description="ID of the knowledge base file entity to download (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Download a knowledge base file entity for the provided ID.

        Scope: Charlotte Ai Agent Definition: READ
        Path: GET /agentic-studio/entities/knowledge_base_files/download/v1
        """
        return self._call(
            operation="entities_knowledge_base_files_download_v1",
            query_params={"knowledge_base_id": knowledge_base_id, "id": id},
            error_message="entities_knowledge_base_files_download_v1 failed",
            member_cid=member_cid,
        )

    def entities_knowledge_base_files_v1(
        self,
        knowledge_base_id: str = Field(description="ID of the knowledge base that owns the files (required)."),
        ids: list[str] = Field(description="IDs of knowledge base file entities to retrieve (required)."),
        include_deleted: bool | None = Field(default=None, description="Include deleted files in the result. Defaults to false."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve knowledge base file entities for the provided IDs.

        Scope: Charlotte Ai Agent Definition: READ
        Path: GET /agentic-studio/entities/knowledge_base_files/v1
        """
        return self._call(
            operation="entities_knowledge_base_files_v1",
            query_params={"knowledge_base_id": knowledge_base_id, "ids": ids, "include_deleted": include_deleted},
            error_message="entities_knowledge_base_files_v1 failed",
            member_cid=member_cid,
        )

    def queries_knowledge_base_files_v1(
        self,
        knowledge_base_id: str = Field(description="ID of the knowledge base to query files within (required)."),
        offset: int | None = Field(default=None, description="Starting index of overall result set from which to return IDs."),
        limit: int | None = Field(default=None, description="Number of IDs to return. Offset + limit should NOT be above 10K."),
        filter: str | None = Field(default=None, description="FQL query specifying the filter parameters."),
        include_deleted: bool | None = Field(default=None, description="Include deleted files in the result. Defaults to false."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Query knowledge base file IDs based on the provided FQL filters.

        Scope: Charlotte Ai Agent Definition: READ
        Path: GET /agentic-studio/queries/knowledge_base_files/v1
        """
        return self._call(
            operation="queries_knowledge_base_files_v1",
            query_params={"knowledge_base_id": knowledge_base_id, "offset": offset, "limit": limit, "filter": filter, "include_deleted": include_deleted},
            error_message="queries_knowledge_base_files_v1 failed",
            member_cid=member_cid,
        )

    # ------------------------------------------------------------------
    # WRITE operations
    # ------------------------------------------------------------------

    def entities_knowledge_base_files_update_v1(
        self,
        id: str = Field(description="File identifier to update (required)."),
        file_description: str | None = Field(default=None, description="Updated description for the file."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update an existing file in a knowledge base. Supports updating file content and optionally its description.

        Note: This endpoint uses multipart/form-data. The id and file_description are form fields.
        File content updates may require direct API access — pass id and file_description; file binary
        upload is not supported through the MCP tool layer.

        Scope: Charlotte Ai Agent Definition: WRITE
        Path: PUT /agentic-studio/entities/knowledge_base_files/v1
        """
        return self._call(
            operation="entities_knowledge_base_files_update_v1",
            body_params={"id": id, "file_description": file_description},
            error_message="entities_knowledge_base_files_update_v1 failed",
            member_cid=member_cid,
        )

    def entities_knowledge_base_files_create_v1(
        self,
        knowledge_base_id: str = Field(description="ID of the knowledge base to upload the file into (required)."),
        file_description: str | None = Field(default=None, description="Optional description for the uploaded file."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Upload a file to a knowledge base.

        Note: This endpoint uses multipart/form-data. Actual file binary upload is not supported
        through the MCP tool layer; use this tool to initiate the operation or pass metadata.
        The knowledge_base_id is a required query parameter; file and file_description are form fields.

        Scope: Charlotte Ai Agent Definition: WRITE
        Path: POST /agentic-studio/entities/knowledge_base_files/v1
        """
        return self._call(
            operation="entities_knowledge_base_files_create_v1",
            query_params={"knowledge_base_id": knowledge_base_id},
            body_params={"file_description": file_description},
            error_message="entities_knowledge_base_files_create_v1 failed",
            member_cid=member_cid,
        )

    # ------------------------------------------------------------------
    # DESTRUCTIVE operations
    # ------------------------------------------------------------------

    def entities_knowledge_base_files_delete_v1(
        self,
        knowledge_base_id: str = Field(description="ID of the knowledge base that owns the file (required)."),
        id: str = Field(description="ID of the document/file to delete (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete a document from a knowledge base.

        Scope: Charlotte Ai Agent Definition: WRITE
        Path: DELETE /agentic-studio/entities/knowledge_base_files/v1
        """
        return self._call(
            operation="entities_knowledge_base_files_delete_v1",
            query_params={"knowledge_base_id": knowledge_base_id, "id": id},
            error_message="entities_knowledge_base_files_delete_v1 failed",
            member_cid=member_cid,
        )
