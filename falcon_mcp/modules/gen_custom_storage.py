"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `custom_storage` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenCustomStorageModule(GeneratedModuleBase):
    """Generated tools for the Falcon `custom_storage` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_object, name="get_object")
        self._add_tool(server=server, method=self.get_object_metadata, name="get_object_metadata")
        self._add_tool(server=server, method=self.get_versioned_object, name="get_versioned_object")
        self._add_tool(server=server, method=self.get_versioned_object_metadata, name="get_versioned_object_metadata")
        self._add_tool(server=server, method=self.list_collections, name="list_collections")
        self._add_tool(server=server, method=self.list_objects, name="list_objects")
        self._add_tool(server=server, method=self.list_objects_by_version, name="list_objects_by_version")
        self._add_tool(server=server, method=self.put_object, name="put_object", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_object, name="delete_object", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_versioned_object, name="delete_versioned_object", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.describe_collections, name="describe_collections", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.search_objects, name="search_objects", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.search_objects_by_version, name="search_objects_by_version", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def delete_object(
        self,
        collection_name: str = Field(description="`collection_name` path parameter (required)."),
        object_key: str = Field(description="`object_key` path parameter (required)."),
        dry_run: bool | None = Field(default=None, description="If false, run the operation as normal. If true, validate that the request *would* succeed, but don't execute it."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete the specified object"""
        return self._call(operation="DeleteObject", query_params={"dry_run": dry_run}, path_params={"collection_name": collection_name, "object_key": object_key}, error_message="DeleteObject failed", member_cid=member_cid)

    def delete_versioned_object(
        self,
        collection_name: str = Field(description="`collection_name` path parameter (required)."),
        object_key: str = Field(description="`object_key` path parameter (required)."),
        collection_version: str = Field(description="`collection_version` path parameter (required)."),
        dry_run: bool | None = Field(default=None, description="If false, run the operation as normal. If true, validate that the request *would* succeed, but don't execute it."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete the specified versioned object"""
        return self._call(operation="DeleteVersionedObject", query_params={"dry_run": dry_run}, path_params={"collection_name": collection_name, "object_key": object_key, "collection_version": collection_version}, error_message="DeleteVersionedObject failed", member_cid=member_cid)

    def describe_collections(
        self,
        names: list[str] = Field(description="A set of collection names"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Fetch metadata about one or more existing collections"""
        return self._call(operation="DescribeCollections", query_params={"names": names}, error_message="DescribeCollections failed", member_cid=member_cid)

    def get_object(
        self,
        collection_name: str = Field(description="`collection_name` path parameter (required)."),
        object_key: str = Field(description="`object_key` path parameter (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get the bytes for the specified object"""
        return self._call(operation="GetObject", query_params=None, path_params={"collection_name": collection_name, "object_key": object_key}, error_message="GetObject failed", member_cid=member_cid)

    def get_object_metadata(
        self,
        collection_name: str = Field(description="`collection_name` path parameter (required)."),
        object_key: str = Field(description="`object_key` path parameter (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get the metadata for the specified object"""
        return self._call(operation="GetObjectMetadata", query_params=None, path_params={"collection_name": collection_name, "object_key": object_key}, error_message="GetObjectMetadata failed", member_cid=member_cid)

    def get_versioned_object(
        self,
        collection_name: str = Field(description="`collection_name` path parameter (required)."),
        object_key: str = Field(description="`object_key` path parameter (required)."),
        collection_version: str = Field(description="`collection_version` path parameter (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get the bytes for the specified object"""
        return self._call(operation="GetVersionedObject", query_params=None, path_params={"collection_name": collection_name, "object_key": object_key, "collection_version": collection_version}, error_message="GetVersionedObject failed", member_cid=member_cid)

    def get_versioned_object_metadata(
        self,
        collection_name: str = Field(description="`collection_name` path parameter (required)."),
        object_key: str = Field(description="`object_key` path parameter (required)."),
        collection_version: str = Field(description="`collection_version` path parameter (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get the metadata for the specified object"""
        return self._call(operation="GetVersionedObjectMetadata", query_params=None, path_params={"collection_name": collection_name, "object_key": object_key, "collection_version": collection_version}, error_message="GetVersionedObjectMetadata failed", member_cid=member_cid)

    def list_collections(
        self,
        end: str | None = Field(default=None, description="The end key to end listing to"),
        limit: int | None = Field(default=None, description="The limit of results to return"),
        start: str | None = Field(default=None, description="The start key to start listing from"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """List available collection names in alphabetical order"""
        return self._call(operation="ListCollections", query_params={"end": end, "limit": limit, "start": start}, error_message="ListCollections failed", member_cid=member_cid)

    def list_objects(
        self,
        collection_name: str = Field(description="`collection_name` path parameter (required)."),
        end: str | None = Field(default=None, description="The end key to end listing to"),
        limit: int | None = Field(default=None, description="The limit of results to return"),
        start: str | None = Field(default=None, description="The start key to start listing from"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """List the object keys in the specified collection in alphabetical order"""
        return self._call(operation="ListObjects", query_params={"end": end, "limit": limit, "start": start}, path_params={"collection_name": collection_name}, error_message="ListObjects failed", member_cid=member_cid)

    def list_objects_by_version(
        self,
        collection_name: str = Field(description="`collection_name` path parameter (required)."),
        collection_version: str = Field(description="`collection_version` path parameter (required)."),
        end: str | None = Field(default=None, description="The end key to end listing to"),
        limit: int | None = Field(default=None, description="The limit of results to return"),
        start: str | None = Field(default=None, description="The start key to start listing from"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """List the object keys in the specified collection in alphabetical order"""
        return self._call(operation="ListObjectsByVersion", query_params={"end": end, "limit": limit, "start": start}, path_params={"collection_name": collection_name, "collection_version": collection_version}, error_message="ListObjectsByVersion failed", member_cid=member_cid)

    def put_object(
        self,
        collection_name: str = Field(description="`collection_name` path parameter (required)."),
        object_key: str = Field(description="`object_key` path parameter (required)."),
        body: dict = Field(description="Request JSON body for `PutObject` per the CrowdStrike API schema (required)."),
        dry_run: bool | None = Field(default=None, description="If false, run the operation as normal. If true, validate that the request *would* succeed, but don't execute it."),
        schema_version: str | None = Field(default=None, description="The version of the collection schema"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Put the specified new object at the given key or overwrite an existing object at the given key"""
        return self._call(operation="PutObject", query_params={"dry_run": dry_run, "schema_version": schema_version}, path_params={"collection_name": collection_name, "object_key": object_key}, body_params=body, error_message="PutObject failed", member_cid=member_cid)

    def search_objects(
        self,
        collection_name: str = Field(description="`collection_name` path parameter (required)."),
        filter: str = Field(description="The filter to limit the returned results."),
        limit: int | None = Field(default=None, description="The limit of results to return"),
        offset: int | None = Field(default=None, description="The offset of results to return"),
        sort: str | None = Field(default=None, description="The sort order for the returned results."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for objects that match the specified filter criteria (returns metadata, not actual objects)"""
        return self._call(operation="SearchObjects", query_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort}, path_params={"collection_name": collection_name}, error_message="SearchObjects failed", member_cid=member_cid)

    def search_objects_by_version(
        self,
        collection_name: str = Field(description="`collection_name` path parameter (required)."),
        collection_version: str = Field(description="`collection_version` path parameter (required)."),
        filter: str = Field(description="The filter to limit the returned results."),
        limit: int | None = Field(default=None, description="The limit of results to return"),
        offset: int | None = Field(default=None, description="The offset of results to return"),
        sort: str | None = Field(default=None, description="The sort order for the returned results."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for objects that match the specified filter criteria (returns metadata, not actual objects)"""
        return self._call(operation="SearchObjectsByVersion", query_params={"filter": filter, "limit": limit, "offset": offset, "sort": sort}, path_params={"collection_name": collection_name, "collection_version": collection_version}, error_message="SearchObjectsByVersion failed", member_cid=member_cid)
