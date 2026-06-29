"""
Host Migration module for Falcon MCP Server.

Provides tools for managing sensor registration migrations between child CIDs
in an MSSP environment. Use this to move hosts from one tenant to another.
"""

from textwrap import dedent
from typing import Any

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.logging import get_logger
from falcon_mcp.modules.base import BaseModule

logger = get_logger(__name__)

WRITE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True,
)

DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(
    readOnlyHint=False, destructiveHint=True, idempotentHint=False, openWorldHint=True,
)


class HostMigrationModule(BaseModule):
    """Module for managing sensor migrations between CrowdStrike child CIDs."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.search_migrations, name="search_migrations")
        self._add_tool(server=server, method=self.get_migration_details, name="get_migration_details")
        self._add_tool(
            server=server, method=self.get_migration_destinations, name="get_migration_destinations",
        )
        self._add_tool(
            server=server, method=self.create_migration, name="create_migration",
            annotations=WRITE_ANNOTATIONS,
        )
        self._add_tool(
            server=server, method=self.perform_migration_action, name="perform_migration_action",
            annotations=DESTRUCTIVE_ANNOTATIONS,
        )
        self._add_tool(server=server, method=self.search_host_migrations, name="search_host_migrations")
        self._add_tool(server=server, method=self.get_host_migrations, name="get_host_migrations")
        self._add_tool(
            server=server, method=self.remove_hosts_from_migration, name="remove_hosts_from_migration",
            annotations=WRITE_ANNOTATIONS,
        )

    def search_migrations(
        self,
        filter: str | None = Field(
            default=None,
            description=dedent("""
                FQL filter to narrow results. Valid fields:
                migration_status, created_by, created_time, name, id, migration_id, target_cid, status.
                Example: "status:'pending'+target_cid:'<CID>'"
            """).strip(),
        ),
        sort: str | None = Field(
            default=None,
            description="Sort expression. Examples: `created_time|desc`, `name|asc`, `status|asc`.",
            examples=["created_time|desc", "name|asc"],
        ),
        limit: int = Field(
            default=20, ge=1, le=10000,
            description="Maximum number of migration job IDs to return (max 10000).",
        ),
        offset: int | None = Field(default=None, description="Pagination offset."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search and list host migration jobs.

        Returns migration job IDs and fetches their full details. Use this to discover
        existing migration jobs, filter by status or target CID, and track progress.
        """
        ids = self._base_search_api_call(
            operation="GetMigrationIDsV1",
            search_params={"filter": filter, "sort": sort, "limit": limit, "offset": offset},
            error_message="Failed to search migrations",
        )
        if self._is_error(ids):
            return [ids]
        if not ids:
            return []
        return self._get_migrations_by_ids(ids)

    def get_migration_details(
        self,
        ids: list[str] = Field(
            description="Migration job IDs to retrieve details for. Obtain from `falcon_search_migrations`.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Retrieve full details for one or more migration jobs by ID."""
        if not ids:
            return []
        return self._get_migrations_by_ids(ids)

    def get_migration_destinations(
        self,
        device_ids: list[str] | None = Field(
            default=None,
            description="Host device IDs (AIDs) to find valid destination CIDs for. Use this or `filter`.",
        ),
        filter: str | None = Field(
            default=None,
            description="FQL filter to select source hosts. Use this or `device_ids`.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Find valid destination CIDs available for a set of hosts.

        Use this before creating a migration to discover which child CIDs can receive
        the target hosts. Provide either `device_ids` or an FQL `filter` to select source hosts.
        """
        if device_ids:
            body: dict[str, Any] = {"resources": [{"device_ids": device_ids}]}
        else:
            body = {"filter": filter}

        return self._base_query_api_call(
            operation="GetMigrationDestinationsV1",
            body_params=body,
            error_message="Failed to get migration destinations",
        )

    def create_migration(
        self,
        name: str = Field(
            description="Human-readable name for the migration job.",
        ),
        target_cid: str = Field(
            description="Destination child CID to migrate hosts into. Obtain valid CIDs from `falcon_get_migration_destinations`.",
        ),
        device_ids: list[str] | None = Field(
            default=None,
            description="Specific host AIDs to include in the migration. Use this or `filter`.",
        ),
        filter: str | None = Field(
            default=None,
            description="FQL filter to select hosts for the migration. Use this or `device_ids`.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Create a new host migration job.

        Creates a migration job that moves sensor registrations from the current CID to `target_cid`.
        After creation, use `falcon_perform_migration_action` with action `start_migration` to begin.
        The migration does NOT start automatically — it must be explicitly started.
        """
        resource: dict[str, Any] = {"name": name, "target_cid": target_cid}
        if device_ids is not None:
            resource["device_ids"] = device_ids
        if filter is not None:
            resource["filter"] = filter

        return self._base_query_api_call(
            operation="CreateMigrationV1",
            body_params={"resources": [resource]},
            error_message="Failed to create migration job",
        )

    def perform_migration_action(
        self,
        migration_id: str = Field(
            description="Migration job ID to act on. Obtain from `falcon_search_migrations`.",
        ),
        action: str = Field(
            description=dedent("""
                Action to perform on the migration job:
                • start_migration — Begin the migration (moves sensors to target CID)
                • cancel_migration — Cancel an in-progress migration
                • delete_migration — Permanently delete a migration job
                • rename_migration — Rename the migration job (requires `new_name`)
            """).strip(),
            examples=["start_migration", "cancel_migration", "delete_migration", "rename_migration"],
        ),
        new_name: str | None = Field(
            default=None,
            description="New name for the migration job. Required when `action` is `rename_migration`.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Perform a lifecycle action on a migration job.

        IMPORTANT: `start_migration` irreversibly begins moving sensor registrations.
        Confirm the correct target CID and host list before starting. Use `cancel_migration`
        to stop an in-progress migration, or `delete_migration` to remove the job entirely.
        """
        action_parameters = []
        if action == "rename_migration" and new_name:
            action_parameters.append({"name": "name", "value": new_name})

        body: dict[str, Any] = {"ids": [migration_id]}
        if action_parameters:
            body["action_parameters"] = action_parameters

        return self._base_query_api_call(
            operation="MigrationsActionsV1",
            query_params={"action_name": action},
            body_params=body,
            error_message=f"Failed to perform migration action '{action}'",
        )

    def search_host_migrations(
        self,
        migration_id: str = Field(
            description="Migration job ID to search host entries within. Obtain from `falcon_search_migrations`.",
        ),
        filter: str | None = Field(
            default=None,
            description=dedent("""
                FQL filter for host migrations. Valid fields:
                target_cid, id, created_time, host_migration_id, hostgroups, status,
                source_cid, migration_id, groups, static_host_groups, hostname.
                Example: "status:'failed'"
            """).strip(),
        ),
        sort: str | None = Field(
            default=None,
            description="Sort expression. Examples: `hostname|asc`, `status|desc`, `created_time|desc`.",
        ),
        limit: int = Field(
            default=20, ge=1, le=10000,
            description="Maximum host migration IDs to return (max 10000).",
        ),
        offset: int | None = Field(default=None, description="Pagination offset."),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Search host entries within a migration job.

        Returns per-host migration records showing individual host status
        (pending, in_progress, complete, failed). Filter by status to find failed migrations.
        """
        ids = self._base_search_api_call(
            operation="GetHostMigrationIDsV1",
            search_params={
                "id": migration_id,
                "filter": filter,
                "sort": sort,
                "limit": limit,
                "offset": offset,
            },
            error_message="Failed to search host migrations",
        )
        if self._is_error(ids):
            return [ids]
        if not ids:
            return []
        return self._get_host_migration_details(ids)

    def get_host_migrations(
        self,
        ids: list[str] = Field(
            description="Host migration entry IDs to retrieve. Obtain from `falcon_search_host_migrations`.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Retrieve details for specific host migration entries by ID."""
        if not ids:
            return []
        return self._get_host_migration_details(ids)

    def remove_hosts_from_migration(
        self,
        migration_id: str = Field(
            description="Migration job ID to remove hosts from. Obtain from `falcon_search_migrations`.",
        ),
        host_migration_ids: list[str] | None = Field(
            default=None,
            description="Host migration entry IDs to remove. Obtain from `falcon_search_host_migrations`. Use this or `filter`.",
        ),
        filter: str | None = Field(
            default=None,
            description="FQL filter to select host migration entries to remove. Use this or `host_migration_ids`.",
        ),
    ) -> list[dict[str, Any]] | dict[str, Any]:
        """Remove specific hosts from a migration job before it starts.

        Only works on migrations that have not yet started. Use to refine the host list
        after creating a migration job.
        """
        resource: dict[str, Any] = {}
        if host_migration_ids:
            resource["ids"] = host_migration_ids
        if filter:
            resource["filter"] = filter

        return self._base_query_api_call(
            operation="HostMigrationsActionsV1",
            query_params={"id": migration_id, "action_name": "remove_hosts"},
            body_params={"resources": [resource]} if resource else {"resources": [{}]},
            error_message="Failed to remove hosts from migration",
        )

    def _get_migrations_by_ids(self, ids: list[str]) -> list[dict[str, Any]] | dict[str, Any]:
        result = self._base_get_by_ids(
            operation="GetMigrationsV1",
            ids=ids,
            id_key="ids",
            use_params=True,
        )
        if self._is_error(result):
            return [result]
        return result

    def _get_host_migration_details(self, ids: list[str]) -> list[dict[str, Any]] | dict[str, Any]:
        result = self._base_query_api_call(
            operation="GetHostMigrationsV1",
            body_params={"resources": [{"ids": ids}]},
            error_message="Failed to get host migration details",
        )
        if self._is_error(result):
            return [result]
        return result
