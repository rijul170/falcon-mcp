"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via
scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon `intel` API service collection."""

from mcp.server import FastMCP
from mcp.types import ToolAnnotations
from pydantic import Field

from falcon_mcp.common.generated_base import GeneratedModuleBase

WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=True, openWorldHint=True)


class GenIntelModule(GeneratedModuleBase):
    """Generated tools for the Falcon `intel` collection."""

    def register_tools(self, server: FastMCP) -> None:
        self._add_tool(server=server, method=self.get_intel_actor_entities, name="get_intel_actor_entities")
        self._add_tool(server=server, method=self.get_intel_indicator_entities, name="get_intel_indicator_entities")
        self._add_tool(server=server, method=self.get_intel_report_entities, name="get_intel_report_entities")
        self._add_tool(server=server, method=self.get_intel_report_pdf, name="get_intel_report_pdf")
        self._add_tool(server=server, method=self.get_intel_rule_entities, name="get_intel_rule_entities")
        self._add_tool(server=server, method=self.get_intel_rule_file, name="get_intel_rule_file")
        self._add_tool(server=server, method=self.get_latest_intel_rule_file, name="get_latest_intel_rule_file")
        self._add_tool(server=server, method=self.get_malware_entities, name="get_malware_entities")
        self._add_tool(server=server, method=self.get_malware_mitre_report, name="get_malware_mitre_report")
        self._add_tool(server=server, method=self.get_vulnerabilities, name="get_vulnerabilities")
        self._add_tool(server=server, method=self.query_intel_actor_ids, name="query_intel_actor_ids")
        self._add_tool(server=server, method=self.query_intel_indicator_ids, name="query_intel_indicator_ids")
        self._add_tool(server=server, method=self.query_intel_report_ids, name="query_intel_report_ids")
        self._add_tool(server=server, method=self.query_intel_rule_ids, name="query_intel_rule_ids")
        self._add_tool(server=server, method=self.query_malware, name="query_malware")
        self._add_tool(server=server, method=self.query_malware_entities, name="query_malware_entities")
        self._add_tool(server=server, method=self.query_mitre_attacks, name="query_mitre_attacks")
        self._add_tool(server=server, method=self.query_mitre_attacks_for_malware, name="query_mitre_attacks_for_malware")
        self._add_tool(server=server, method=self.query_vulnerabilities, name="query_vulnerabilities")
        self._add_tool(server=server, method=self.post_mitre_attacks, name="post_mitre_attacks", annotations=WRITE_ANNOTATIONS)

    def register_resources(self, server: FastMCP) -> None:
        pass

    def get_intel_actor_entities(
        self,
        ids: list[str] = Field(description="The IDs of the actors you want to retrieve."),
        fields: list[str] | None = Field(default=None, description="The fields to return, or a predefined set of fields in the form of the collection name surrounded by two underscores like: __<collection>__. Ex: slug __full__. Defaults to __basic__."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve specific actors using their actor IDs."""
        return self._call(operation="GetIntelActorEntities", query_params={"ids": ids, "fields": fields}, error_message="GetIntelActorEntities failed", member_cid=member_cid)

    def get_intel_indicator_entities(
        self,
        body: dict = Field(description="Request JSON body for `GetIntelIndicatorEntities` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve specific indicators using their indicator IDs."""
        return self._call(operation="GetIntelIndicatorEntities", query_params=None, body_params=body, error_message="GetIntelIndicatorEntities failed", member_cid=member_cid)

    def get_intel_report_entities(
        self,
        ids: list[str] = Field(description="The IDs of the reports you want to retrieve."),
        fields: list[str] | None = Field(default=None, description="The fields to return, or a predefined set of fields in the form of the collection name surrounded by two underscores like: __<collection>__. Ex: slug __full__. Defaults to __basic__."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve specific reports using their report IDs."""
        return self._call(operation="GetIntelReportEntities", query_params={"ids": ids, "fields": fields}, error_message="GetIntelReportEntities failed", member_cid=member_cid)

    def get_intel_report_pdf(
        self,
        id: str | None = Field(default=None, description="The ID of the report you want to download as a PDF."),
        ids: str | None = Field(default=None, description="The ID of the report you want to download as a PDF. This parameter is used only if no id parameter given."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Return a Report PDF attachment"""
        return self._call(operation="GetIntelReportPDF", query_params={"id": id, "ids": ids}, error_message="GetIntelReportPDF failed", member_cid=member_cid)

    def get_intel_rule_entities(
        self,
        ids: list[str] = Field(description="The ids of rules to return."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieve details for rule sets for the specified ids."""
        return self._call(operation="GetIntelRuleEntities", query_params={"ids": ids}, error_message="GetIntelRuleEntities failed", member_cid=member_cid)

    def get_intel_rule_file(
        self,
        id: int = Field(description="The ID of the rule set."),
        format: str | None = Field(default=None, description="Choose the format you want the rule set in. Valid formats are zip and gzip. Defaults to zip."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Download earlier rule sets."""
        return self._call(operation="GetIntelRuleFile", query_params={"id": id, "format": format}, error_message="GetIntelRuleFile failed", member_cid=member_cid)

    def get_latest_intel_rule_file(
        self,
        type: str = Field(description="The rule news report type. Accepted values: snort-suricata-master snort-suricata-update snort-suricata-changelog yara-master yara-update yara-changelog common-event-format netwitness cql-master cql-update cql-changelog"),
        format: str | None = Field(default=None, description="Choose the format you want the rule set in. Valid formats are zip and gzip. Defaults to zip."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Download the latest rule set."""
        return self._call(operation="GetLatestIntelRuleFile", query_params={"type": type, "format": format}, error_message="GetLatestIntelRuleFile failed", member_cid=member_cid)

    def get_malware_entities(
        self,
        ids: list[str] = Field(description="Malware family name in lower case with spaces, dots and slashes replaced with dashes"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get malware entities for specified ids."""
        return self._call(operation="GetMalwareEntities", query_params={"ids": ids}, error_message="GetMalwareEntities failed", member_cid=member_cid)

    def get_malware_mitre_report(
        self,
        id: str = Field(description="Malware family name in lower case with spaces replaced with dashes"),
        format: str = Field(description="Supported report formats: CSV, JSON or JSON_NAVIGATOR"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Export Mitre ATT&CK information for a given malware family."""
        return self._call(operation="GetMalwareMitreReport", query_params={"id": id, "format": format}, error_message="GetMalwareMitreReport failed", member_cid=member_cid)

    def get_vulnerabilities(
        self,
        body: dict = Field(description="Request JSON body for `GetVulnerabilities` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get vulnerabilities"""
        return self._call(operation="GetVulnerabilities", query_params=None, body_params=body, error_message="GetVulnerabilities failed", member_cid=member_cid)

    def post_mitre_attacks(
        self,
        body: dict = Field(description="Request JSON body for `PostMitreAttacks` per the CrowdStrike API schema (required)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Retrieves report and observable IDs associated with the given actor and attacks"""
        return self._call(operation="PostMitreAttacks", query_params=None, body_params=body, error_message="PostMitreAttacks failed", member_cid=member_cid)

    def query_intel_actor_ids(
        self,
        offset: int | None = Field(default=None, description="Set the starting row number to return actors IDs from. Defaults to 0."),
        limit: int | None = Field(default=None, description="Set the number of actor IDs to return. The value must be between 1 and 5000."),
        sort: str | None = Field(default=None, description="Order fields in ascending or descending order. Ex: created_date|asc."),
        filter: str | None = Field(default=None, description="Filter your query by specifying FQL filter parameters. Filter parameters include: actor_type, animal_classifier, capabilities, capability, capability.id, capability.slug, capability.value, created_date, description, ecrime_kill_chain.attribution, ecrime_kill_chain.crimes, ecrime_kill_chain.customers, ecrime_kill_chain.marketing, ecrime_kill_chain.monetization, ecrime_kill_chain.services_offered, ecrime_kill_chain.services_used, ecrime_kill_chain.technical_tradecraft, ecrime_kill_chain.victims, first_activity_date, group, group.id, group.slug, group.value, id, kill_chain.actions_and_objectives, kill_chain.actions_on_objectives, kill_chain.command_and_control, kill_chain.delivery, kill_chain.exploitation, kill_chain.installation, kill_chain.objectives, kill_chain.reconnaissance, kill_chain.weaponization, known_as, last_activity_date, last_modified_date, motivations, motivations.id, motivations.slug, motivations.value, name, objectives, origins, origins.id, origins.slug, origins.value, region, region.id, region.slug, region.value, short_description, slug, status, target_countries, target_countries.id, target_countries.slug, target_countries.value, target_industries, target_industries.id, target_industries.slug, target_industries.value, target_regions, target_regions.id, target_regions.slug, target_regions.value."),
        q: str | None = Field(default=None, description="Perform a generic substring search across all fields."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get actor IDs that match provided FQL filters."""
        return self._call(operation="QueryIntelActorIds", query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter, "q": q}, error_message="QueryIntelActorIds failed", member_cid=member_cid)

    def query_intel_indicator_ids(
        self,
        offset: int | None = Field(default=None, description="Set the starting row number to return indicator IDs from. Defaults to 0."),
        limit: int | None = Field(default=None, description="Set the number of indicator IDs to return. The number must be between 1 and 10000"),
        sort: str | None = Field(default=None, description="Order fields in ascending or descending order. Ex: published_date|asc."),
        filter: str | None = Field(default=None, description="Filter your query by specifying FQL filter parameters. Filter parameters include: _marker, actors, deleted, domain_types, id, indicator, ip_address_types, kill_chains, labels, labels.created_on, labels.last_valid_on, labels.name, last_updated, malicious_confidence, malware_families, published_date, reports, reports.slug, scope, targets, threat_types, type, vulnerabilities."),
        q: str | None = Field(default=None, description="Perform a generic substring search across all fields."),
        include_deleted: bool | None = Field(default=None, description="If true, include both published and deleted indicators in the response. Defaults to false."),
        include_relations: bool | None = Field(default=None, description="If true, include related indicators in the response. Defaults to true."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get indicators IDs that match provided FQL filters."""
        return self._call(operation="QueryIntelIndicatorIds", query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter, "q": q, "include_deleted": include_deleted, "include_relations": include_relations}, error_message="QueryIntelIndicatorIds failed", member_cid=member_cid)

    def query_intel_report_ids(
        self,
        offset: int | None = Field(default=None, description="Set the starting row number to return report IDs from. Defaults to 0."),
        limit: int | None = Field(default=None, description="Set the number of report IDs to return. The value must be between 1 and 5000."),
        sort: str | None = Field(default=None, description="Order fields in ascending or descending order. Ex: created_date|asc."),
        filter: str | None = Field(default=None, description="Filter your query by specifying FQL filter parameters. Filter parameters include: actors, actors.animal_classifier, actors.id, actors.name, actors.slug, actors.url, created_date, description, id, last_modified_date, malware, malware.community_identifiers, malware.family_name, malware.slug, motivations, motivations.id, motivations.slug, motivations.value, name, name.raw, short_description, slug, sub_type, sub_type.id, sub_type.name, sub_type.slug, summary, tags, tags.id, tags.slug, tags.value, target_countries, target_countries.id, target_countries.slug, target_countries.value, target_industries, target_industries.id, target_industries.slug, target_industries.value, type, type.id, type.name, type.slug, url."),
        q: str | None = Field(default=None, description="Perform a generic substring search across all fields."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get report IDs that match provided FQL filters."""
        return self._call(operation="QueryIntelReportIds", query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter, "q": q}, error_message="QueryIntelReportIds failed", member_cid=member_cid)

    def query_intel_rule_ids(
        self,
        type: str = Field(description="The rule news report type. Accepted values: snort-suricata-master snort-suricata-update snort-suricata-changelog yara-master yara-update yara-changelog common-event-format netwitness cql-master cql-update cql-changelog"),
        offset: int | None = Field(default=None, description="Set the starting row number to return reports from. Defaults to 0."),
        limit: int | None = Field(default=None, description="The number of rule IDs to return. Defaults to 10."),
        sort: str | None = Field(default=None, description="Order fields in ascending or descending order. Ex: created_date|asc."),
        name: list[str] | None = Field(default=None, description="Search by rule title."),
        description: list[str] | None = Field(default=None, description="Substring match on description field."),
        tags: list[str] | None = Field(default=None, description="Search for rule tags."),
        min_created_date: int | None = Field(default=None, description="Filter results to those created on or after a certain date."),
        max_created_date: str | None = Field(default=None, description="Filter results to those created on or before a certain date."),
        q: str | None = Field(default=None, description="Perform a generic substring search across all fields."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Search for rule IDs that match provided filter criteria."""
        return self._call(operation="QueryIntelRuleIds", query_params={"offset": offset, "limit": limit, "sort": sort, "name": name, "type": type, "description": description, "tags": tags, "min_created_date": min_created_date, "max_created_date": max_created_date, "q": q}, error_message="QueryIntelRuleIds failed", member_cid=member_cid)

    def query_malware(
        self,
        offset: int | None = Field(default=None, description="Set the starting row number to return malware IDs from. Defaults to 0."),
        limit: int | None = Field(default=None, description="Set the number of malware IDs to return. The value must be between 1 and 5000."),
        sort: str | None = Field(default=None, description="Order fields in ascending or descending order. Ex: created_date|asc."),
        filter: str | None = Field(default=None, description="Filter your query by specifying FQL filter parameters."),
        q: str | None = Field(default=None, description="Perform a generic substring search across all fields."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get malware family names that match provided FQL filters."""
        return self._call(operation="QueryMalware", query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter, "q": q}, error_message="QueryMalware failed", member_cid=member_cid)

    def query_malware_entities(
        self,
        offset: int | None = Field(default=None, description="Set the starting row number to return malware IDs from. Defaults to 0."),
        limit: int | None = Field(default=None, description="Set the number of malware IDs to return. The value must be between 1 and 5000."),
        sort: str | None = Field(default=None, description="Order fields in ascending or descending order. Ex: created_date|asc."),
        filter: str | None = Field(default=None, description="Filter your query by specifying FQL filter parameters."),
        q: str | None = Field(default=None, description="Perform a generic substring search across all fields."),
        fields: list[str] | None = Field(default=None, description="The fields to return"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get malware entities that match provided FQL filters."""
        return self._call(operation="QueryMalwareEntities", query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter, "q": q, "fields": fields}, error_message="QueryMalwareEntities failed", member_cid=member_cid)

    def query_mitre_attacks(
        self,
        id: str | None = Field(default=None, description="The actor ID(derived from the actor's name) for which to retrieve a list of attacks, for example: fancy-bear. Only one value is allowed"),
        ids: list[str] | None = Field(default=None, description="The actor ID(derived from the actor's name) for which to retrieve a list of attacks, for example: fancy-bear. Multiple values are allowed"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Gets MITRE tactics and techniques for the given actor, returning concatenation of id and tactic and technique ids, example: fancy-bear_TA0011_T1071"""
        return self._call(operation="QueryMitreAttacks", query_params={"id": id, "ids": ids}, error_message="QueryMitreAttacks failed", member_cid=member_cid)

    def query_mitre_attacks_for_malware(
        self,
        ids: list[str] = Field(description="Malware family name in lower case with spaces replaced with dashes"),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Gets MITRE tactics and techniques for the given malware"""
        return self._call(operation="QueryMitreAttacksForMalware", query_params={"ids": ids}, error_message="QueryMitreAttacksForMalware failed", member_cid=member_cid)

    def query_vulnerabilities(
        self,
        offset: str | None = Field(default=None, description="Starting index of result set from which to return IDs."),
        limit: int | None = Field(default=None, description="Number of IDs to return."),
        sort: str | None = Field(default=None, description="Order by fields."),
        filter: str | None = Field(default=None, description="FQL query specifying the filter parameters. Filter parameters include: _all, affected_products.product, affected_products.vendor, community_identifiers, cve, cvss_v3_base, cvss_v3_base.score, cvss_v3_base.severity, exploit_status, publish_date, related_actors, related_actors.animal_classifier, related_actors.name, related_reports.serial_id, related_reports.title, related_threats, related_threats.name, severity, updated_timestamp."),
        q: str | None = Field(default=None, description="Match phrase_prefix query criteria; included fields: _all (all filter string fields indexed)."),
        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),
    ) -> list[dict] | dict:
        """Get vulnerabilities IDs"""
        return self._call(operation="QueryVulnerabilities", query_params={"offset": offset, "limit": limit, "sort": sort, "filter": filter, "q": q}, error_message="QueryVulnerabilities failed", member_cid=member_cid)
