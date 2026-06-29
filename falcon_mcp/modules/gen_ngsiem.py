"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `ngsiem` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenNgsiemModule(GeneratedModuleBase):
    """Generated tools for the Falcon `ngsiem` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.external_get_data_connection_by_id, name="external_get_data_connection_by_id")
        self._add_tool(server=server, method=self.external_list_connector_configs, name="external_list_connector_configs")
        self._add_tool(server=server, method=self.get_dashboard_template, name="get_dashboard_template")
        self._add_tool(server=server, method=self.get_lookup_file, name="get_lookup_file")
        self._add_tool(server=server, method=self.get_lookup_from_package_v1, name="get_lookup_from_package_v1")
        self._add_tool(server=server, method=self.get_lookup_from_package_with_namespace_v1, name="get_lookup_from_package_with_namespace_v1")
        self._add_tool(server=server, method=self.get_lookup_v1, name="get_lookup_v1")
        self._add_tool(server=server, method=self.get_parser, name="get_parser")
        self._add_tool(server=server, method=self.get_parser_template, name="get_parser_template")
        self._add_tool(server=server, method=self.get_saved_query_template, name="get_saved_query_template")
        self._add_tool(server=server, method=self.bulk_install_parsers, name="bulk_install_parsers", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.create_parser, name="create_parser", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.external_create_connector_config, name="external_create_connector_config", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.external_patch_connector_config, name="external_patch_connector_config", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.external_update_data_connection, name="external_update_data_connection", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.install_parser, name="install_parser", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_parser, name="update_parser", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.update_parser_auto_update_policy, name="update_parser_auto_update_policy", annotations=WRITE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_dashboard, name="delete_dashboard", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_lookup_file, name="delete_lookup_file", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_parser, name="delete_parser", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.delete_saved_query, name="delete_saved_query", annotations=DESTRUCTIVE_ANNOTATIONS)
        self._add_tool(server=server, method=self.external_delete_connector_configs, name="external_delete_connector_configs", annotations=DESTRUCTIVE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def bulk_install_parsers(
        self,
        body: dict = Field(description="Request JSON body for `BulkInstallParsers` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Installs multiple CrowdStrike-managed out-of-the-box (OOTB) parsers into the customer's repository in a single operation. This endpoint provisions multiple pre-built parsers with their specific versions for the requesting customer ID (CID). The parsers are installed as-is and cannot be modified by the customer. Requires an array of parsers with parser_id and version in the request body. Maximum 100 parsers per request."""
        return self._call(operation="BulkInstallParsers", query_params=None, body_params=body, error_message="BulkInstallParsers failed", member_cid=member_cid)

    def create_parser(
        self,
        body: dict = Field(description="Request JSON body for `CreateParser` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create Parser in NGSIEM. This endpoint has been deprecated in favour of the POST /entities/parsers-template/v1 API."""
        return self._call(operation="CreateParser", query_params=None, body_params=body, error_message="CreateParser failed", member_cid=member_cid)

    def delete_dashboard(
        self,
        ids: str | None = Field(default=None, description="dashboard ID value"),
        search_domain: str | None = Field(default=None, description="name of search domain (view or repo)"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete Dashboard in NGSIEM"""
        return self._call(operation="DeleteDashboard", query_params={"ids": ids, "search_domain": search_domain}, error_message="DeleteDashboard failed", member_cid=member_cid)

    def delete_lookup_file(
        self,
        filename: str | None = Field(default=None, description="lookup file filename"),
        search_domain: str | None = Field(default=None, description="name of search domain (view or repo)"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete Lookup File in NGSIEM"""
        return self._call(operation="DeleteLookupFile", query_params={"filename": filename, "search_domain": search_domain}, error_message="DeleteLookupFile failed", member_cid=member_cid)

    def delete_parser(
        self,
        ids: str | None = Field(default=None, description="parser ID value"),
        repository: str | None = Field(default=None, description="name of repository"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete Parser in NGSIEM"""
        return self._call(operation="DeleteParser", query_params={"ids": ids, "repository": repository}, error_message="DeleteParser failed", member_cid=member_cid)

    def delete_saved_query(
        self,
        ids: str | None = Field(default=None, description="saved query ID value"),
        search_domain: str | None = Field(default=None, description="name of search domain (view or repo)"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete Saved Query in NGSIEM"""
        return self._call(operation="DeleteSavedQuery", query_params={"ids": ids, "search_domain": search_domain}, error_message="DeleteSavedQuery failed", member_cid=member_cid)

    def external_create_connector_config(
        self,
        body: dict = Field(description="Request JSON body for `ExternalCreateConnectorConfig` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Create a new configuration for a data connector"""
        return self._call(operation="ExternalCreateConnectorConfig", query_params=None, body_params=body, error_message="ExternalCreateConnectorConfig failed", member_cid=member_cid)

    def external_delete_connector_configs(
        self,
        connector_id: str = Field(description="Unique identifier of the connector"),
        ids: list[str] = Field(description="Unique identifiers of the config(s) to delete"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Delete data connection config"""
        return self._call(operation="ExternalDeleteConnectorConfigs", query_params={"connector_id": connector_id, "ids": ids}, error_message="ExternalDeleteConnectorConfigs failed", member_cid=member_cid)

    def external_get_data_connection_by_id(
        self,
        ids: list[str] = Field(description="Unique identifier of the data connection"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get data connection by ID"""
        return self._call(operation="ExternalGetDataConnectionByID", query_params={"ids": ids}, error_message="ExternalGetDataConnectionByID failed", member_cid=member_cid)

    def external_list_connector_configs(
        self,
        ids: str = Field(description="Unique identifier of the data connector"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """List configurations for a data connector"""
        return self._call(operation="ExternalListConnectorConfigs", query_params={"ids": ids}, error_message="ExternalListConnectorConfigs failed", member_cid=member_cid)

    def external_patch_connector_config(
        self,
        ids: str = Field(description="Unique id of the config to update"),
        body: dict = Field(description="Request JSON body for `ExternalPatchConnectorConfig` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Patch configurations for a data connector"""
        return self._call(operation="ExternalPatchConnectorConfig", query_params={"ids": ids}, body_params=body, error_message="ExternalPatchConnectorConfig failed", member_cid=member_cid)

    def external_update_data_connection(
        self,
        ids: str = Field(description="Unique identifier of the data connection"),
        body: dict = Field(description="Request JSON body for `ExternalUpdateDataConnection` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update a data connection"""
        return self._call(operation="ExternalUpdateDataConnection", query_params={"ids": ids}, body_params=body, error_message="ExternalUpdateDataConnection failed", member_cid=member_cid)

    def get_dashboard_template(
        self,
        ids: str | None = Field(default=None, description="dashboard ID value"),
        search_domain: str | None = Field(default=None, description="name of search domain (view or repo)"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve Dashboard in NGSIEM as LogScale YAML Template"""
        return self._call(operation="GetDashboardTemplate", query_params={"ids": ids, "search_domain": search_domain}, error_message="GetDashboardTemplate failed", member_cid=member_cid)

    def get_lookup_file(
        self,
        filename: str | None = Field(default=None, description="lookup file filename"),
        search_domain: str | None = Field(default=None, description="name of search domain (view or repo)"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve Lookup File in NGSIEM"""
        return self._call(operation="GetLookupFile", query_params={"filename": filename, "search_domain": search_domain}, error_message="GetLookupFile failed", member_cid=member_cid)

    def get_lookup_from_package_v1(
        self,
        repository: str = Field(description="`repository` path parameter (required)."),
        package: str = Field(description="`package` path parameter (required)."),
        filename: str = Field(description="`filename` path parameter (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Download lookup file in package from NGSIEM"""
        return self._call(operation="GetLookupFromPackageV1", query_params=None, path_params={"repository": repository, "package": package, "filename": filename}, error_message="GetLookupFromPackageV1 failed", member_cid=member_cid)

    def get_lookup_from_package_with_namespace_v1(
        self,
        repository: str = Field(description="`repository` path parameter (required)."),
        namespace: str = Field(description="`namespace` path parameter (required)."),
        package: str = Field(description="`package` path parameter (required)."),
        filename: str = Field(description="`filename` path parameter (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Download lookup file in namespaced package from NGSIEM"""
        return self._call(operation="GetLookupFromPackageWithNamespaceV1", query_params=None, path_params={"repository": repository, "namespace": namespace, "package": package, "filename": filename}, error_message="GetLookupFromPackageWithNamespaceV1 failed", member_cid=member_cid)

    def get_lookup_v1(
        self,
        repository: str = Field(description="`repository` path parameter (required)."),
        filename: str = Field(description="`filename` path parameter (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Download lookup file from NGSIEM"""
        return self._call(operation="GetLookupV1", query_params=None, path_params={"repository": repository, "filename": filename}, error_message="GetLookupV1 failed", member_cid=member_cid)

    def get_parser(
        self,
        ids: str | None = Field(default=None, description="parser ID value"),
        repository: str | None = Field(default=None, description="name of repository"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve Parser in NGSIEM. This endpoint has been deprecated in favour of the GET /entities/parsers-template/v1 API."""
        return self._call(operation="GetParser", query_params={"ids": ids, "repository": repository}, error_message="GetParser failed", member_cid=member_cid)

    def get_parser_template(
        self,
        ids: str | None = Field(default=None, description="parser ID value"),
        repository: str | None = Field(default=None, description="name of repository"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve Parser in NGSIEM as LogScale YAML Template"""
        return self._call(operation="GetParserTemplate", query_params={"ids": ids, "repository": repository}, error_message="GetParserTemplate failed", member_cid=member_cid)

    def get_saved_query_template(
        self,
        ids: str | None = Field(default=None, description="saved query ID value"),
        search_domain: str | None = Field(default=None, description="name of search domain (view or repo)"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve Saved Query in NGSIEM as LogScale YAML Template"""
        return self._call(operation="GetSavedQueryTemplate", query_params={"ids": ids, "search_domain": search_domain}, error_message="GetSavedQueryTemplate failed", member_cid=member_cid)

    def install_parser(
        self,
        body: dict = Field(description="Request JSON body for `InstallParser` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Installs a CrowdStrike-managed out-of-the-box (OOTB) parser into the customer's repository. This endpoint provisions a pre-built parser with a specific version for the requesting customer ID (CID). The parser is installed as-is and cannot be modified by the customer. Requires parser_id and version in the request body."""
        return self._call(operation="InstallParser", query_params=None, body_params=body, error_message="InstallParser failed", member_cid=member_cid)

    def update_parser(
        self,
        body: dict = Field(description="Request JSON body for `UpdateParser` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Update Parser in NGSIEM. Please note that name changes are not supported, but rather should be created as a new parser. This endpoint has been deprecated in favour of the PATCH /entities/parsers-template/v1 API."""
        return self._call(operation="UpdateParser", query_params=None, body_params=body, error_message="UpdateParser failed", member_cid=member_cid)

    def update_parser_auto_update_policy(
        self,
        body: dict = Field(description="Request JSON body for `UpdateParserAutoUpdatePolicy` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Updates a parser auto update policy - 'on' enables auto-updates, 'off' disables them"""
        return self._call(operation="UpdateParserAutoUpdatePolicy", query_params=None, body_params=body, error_message="UpdateParserAutoUpdatePolicy failed", member_cid=member_cid)
