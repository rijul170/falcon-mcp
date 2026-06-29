"""
API scope definitions and utilities for Falcon MCP Server

This module provides API scope definitions and related utilities for the Falcon MCP server.
"""

from .logging import get_logger

logger = get_logger(__name__)

# Map of API operations to required scopes
# This can be expanded as more modules and operations are added
API_SCOPE_REQUIREMENTS = {
    # Alerts operations (migrated from detections)
    "GetQueriesAlertsV2": ["Alerts:read"],
    "PostEntitiesAlertsV2": ["Alerts:read"],
    # Hosts operations
    "QueryDevicesByFilter": ["Hosts:read"],
    "PostDeviceDetailsV2": ["Hosts:read"],
    # Incidents operations
    "QueryIncidents": ["Incidents:read"],
    "CrowdScore": ["Incidents:read"],
    "GetIncidents": ["Incidents:read"],
    "GetBehaviors": ["Incidents:read"],
    "QueryBehaviors": ["Incidents:read"],
    # Intel operations
    "QueryIntelActorEntities": ["Actors (Falcon Intelligence):read"],
    "QueryIntelIndicatorEntities": ["Indicators (Falcon Intelligence):read"],
    "QueryIntelReportEntities": ["Reports (Falcon Intelligence):read"],
    "GetMitreReport": ["Actors (Falcon Intelligence):read"],
    # IOC operations
    "indicator_search_v1": ["IOC Management:read"],
    "indicator_get_v1": ["IOC Management:read"],
    "indicator_create_v1": ["IOC Management:write"],
    "indicator_delete_v1": ["IOC Management:write"],
    # Firewall Management operations
    "query_rules": ["Firewall Management:read"],
    "get_rules": ["Firewall Management:read"],
    "query_rule_groups": ["Firewall Management:read"],
    "get_rule_groups": ["Firewall Management:read"],
    "query_policy_rules": ["Firewall Management:read"],
    "create_rule_group": ["Firewall Management:write"],
    "delete_rule_groups": ["Firewall Management:write"],
    # Spotlight operations
    "combinedQueryVulnerabilities": ["Vulnerabilities:read"],
    # Discover operations
    "combined_applications": ["Assets:read"],
    "combined_hosts": ["Assets:read"],
    # Cloud operations
    "ReadContainerCombined": ["Falcon Container Image:read"],
    "ReadContainerCount": ["Falcon Container Image:read"],
    "ReadCombinedVulnerabilities": ["Falcon Container Image:read"],
    # CSPM Assets operations
    "cloud_security_assets_queries": ["Cloud Security API Assets:read"],
    "cloud_security_assets_entities_get": ["Cloud Security API Assets:read"],
    # Identity Protection operations
    "api_preempt_proxy_post_graphql": [
        "Identity Protection Entities:read",
        "Identity Protection Timeline:read",
        "Identity Protection Detections:read",
        "Identity Protection Assessment:read",
        "Identity Protection GraphQL:write",
    ],
    # Sensor Usage operations
    "GetSensorUsageWeekly": ["Sensor Usage:read"],
    # Serverless operations
    "GetCombinedVulnerabilitiesSARIF": ["Falcon Container Image:read"],
    # Scheduled Reports operations
    "scheduled_reports_query": ["Scheduled Reports:read"],
    "scheduled_reports_get": ["Scheduled Reports:read"],
    "scheduled_reports_launch": ["Scheduled Reports:read"],
    # Report Executions operations (same scope as Scheduled Reports)
    "report_executions_query": ["Scheduled Reports:read"],
    "report_executions_get": ["Scheduled Reports:read"],
    "report_executions_download_get": ["Scheduled Reports:read"],
    # NGSIEM operations
    "StartSearchV1": ["NGSIEM:write"],
    "GetSearchStatusV1": ["NGSIEM:read"],
    "StopSearchV1": ["NGSIEM:write"],
    # Real Time Response operations
    "RTR_ListAllSessions": ["Real time response:read"],
    "RTR_ListSessions": ["Real time response:read"],
    "RTR_InitSession": ["Real time response:read"],
    "RTR_DeleteSession": ["Real time response:read"],
    "RTR_PulseSession": ["Real time response:read"],
    "RTR_CheckCommandStatus": ["Real time response:read"],
    "RTR_ExecuteCommand": ["Real time response:read"],
    "RTR_ListFilesV2": ["Real time response:write"],
    # Custom IOA operations
    "query_rule_groups_full": ["Custom IOA Rules:read"],
    "query_platformsMixin0": ["Custom IOA Rules:read"],
    "get_platformsMixin0": ["Custom IOA Rules:read"],
    "query_rule_types": ["Custom IOA Rules:read"],
    "get_rule_types": ["Custom IOA Rules:read"],
    "create_rule_groupMixin0": ["Custom IOA Rules:write"],
    "update_rule_groupMixin0": ["Custom IOA Rules:write"],
    "delete_rule_groupsMixin0": ["Custom IOA Rules:write"],
    "create_rule": ["Custom IOA Rules:write"],
    "update_rules_v2": ["Custom IOA Rules:write"],
    "delete_rules": ["Custom IOA Rules:write"],
    # Host Group operations
    "queryHostGroups": ["Host Groups:read"],
    "queryCombinedGroupMembers": ["Host Groups:read"],
    "getHostGroups": ["Host Groups:read"],
    "createHostGroups": ["Host Groups:write"],
    "updateHostGroups": ["Host Groups:write"],
    "deleteHostGroups": ["Host Groups:write"],
    "performGroupAction": ["Host Groups:write"],
    # Prevention Policy operations
    "queryCombinedPreventionPolicies": ["Prevention Policies:read"],
    "queryCombinedPreventionPolicyMembers": ["Prevention Policies:read"],
    "createPreventionPolicies": ["Prevention Policies:write"],
    "updatePreventionPolicies": ["Prevention Policies:write"],
    "deletePreventionPolicies": ["Prevention Policies:write"],
    "performPreventionPoliciesAction": ["Prevention Policies:write"],
    "setPreventionPoliciesPrecedence": ["Prevention Policies:write"],
    # Sensor Update Policy operations
    "queryCombinedSensorUpdatePoliciesV2": ["Sensor update policies:read"],
    "queryCombinedSensorUpdatePolicyMembers": ["Sensor update policies:read"],
    "queryCombinedSensorUpdateBuilds": ["Sensor update policies:read"],
    "createSensorUpdatePoliciesV2": ["Sensor update policies:write"],
    "updateSensorUpdatePoliciesV2": ["Sensor update policies:write"],
    "deleteSensorUpdatePolicies": ["Sensor update policies:write"],
    "performSensorUpdatePoliciesAction": ["Sensor update policies:write"],
    "setSensorUpdatePoliciesPrecedence": ["Sensor update policies:write"],
    "revealUninstallToken": ["Sensor update policies:write"],
    # RTR Response Policy operations
    "queryCombinedRTResponsePolicies": ["Response Policies:read"],
    "queryCombinedRTResponsePolicyMembers": ["Response Policies:read"],
    "createRTResponsePolicies": ["Response Policies:write"],
    "updateRTResponsePolicies": ["Response Policies:write"],
    "deleteRTResponsePolicies": ["Response Policies:write"],
    "performRTResponsePoliciesAction": ["Response Policies:write"],
    "setRTResponsePoliciesPrecedence": ["Response Policies:write"],
    # User Management operations
    "queryUserV1": ["User Management:read"],
    "retrieveUsersGETV1": ["User Management:read"],
    "combinedUserRolesV1": ["User Management:read"],
    "queriesRolesV1": ["User Management:read"],
    "entitiesRolesV1": ["User Management:read"],
    "userRolesActionV1": ["User Management:write"],
    # Installation Tokens operations
    "tokens_query": ["Installation Tokens:read"],
    "tokens_read": ["Installation Tokens:read"],
    "customer_settings_read": ["Installation Tokens:read"],
    "tokens_create": ["Installation Tokens:write"],
    "tokens_update": ["Installation Tokens:write"],
    "tokens_delete": ["Installation Tokens:write"],
    # Zero Trust Assessment operations
    "getAssessmentV1": ["Zero Trust Assessment:read"],
    # getCombinedAssessmentsQuery requires Configuration Assessment (confirmed by live 403
    # validation: ZTA-only credentials got 403 here while genuine ZTA ops returned 200),
    # even though it is also called from the zero_trust module.
    "getCombinedAssessmentsQuery": ["Configuration Assessment:read"],
    "getAssessmentsByScoreV1": ["Zero Trust Assessment:read"],
    "getAuditV1": ["Zero Trust Assessment:read"],
    # Device Control Policy operations
    "queryCombinedDeviceControlPolicies": ["Device Control Policies:read"],
    "queryCombinedDeviceControlPolicyMembers": ["Device Control Policies:read"],
    "createDeviceControlPolicies": ["Device Control Policies:write"],
    "updateDeviceControlPolicies": ["Device Control Policies:write"],
    "deleteDeviceControlPolicies": ["Device Control Policies:write"],
    "performDeviceControlPoliciesAction": ["Device Control Policies:write"],
    "setDeviceControlPoliciesPrecedence": ["Device Control Policies:write"],
    # Sensor Download operations
    "GetCombinedSensorInstallersByQueryV3": ["Sensor Download:read"],
    "GetSensorInstallersEntitiesV3": ["Sensor Download:read"],
    "GetSensorInstallersCCIDByQuery": ["Sensor Download:read"],
    # Falcon for IT operations
    "ITAutomationGetTasksByQuery": ["Falcon for IT:read"],
    "ITAutomationGetTasks": ["Falcon for IT:read"],
    "ITAutomationGetTaskExecutionsByQuery": ["Falcon for IT:read"],
    "ITAutomationGetTaskExecution": ["Falcon for IT:read"],
    "ITAutomationGetTaskExecutionHostStatus": ["Falcon for IT:read"],
    "ITAutomationGetExecutionResults": ["Falcon for IT:read"],
    "ITAutomationCombinedScheduledTasks": ["Falcon for IT:read"],
    "ITAutomationQueryPolicies": ["Falcon for IT:read"],
    "ITAutomationCancelTaskExecution": ["Falcon for IT:write"],
    # Recon operations
    "QueryNotificationsV1": ["Falcon Intelligence Recon:read"],
    "GetNotificationsV1": ["Falcon Intelligence Recon:read"],
    "UpdateNotificationsV1": ["Falcon Intelligence Recon:write"],
    "DeleteNotificationsV1": ["Falcon Intelligence Recon:write"],
    "QueryRulesV1": ["Falcon Intelligence Recon:read"],
    "GetRulesV1": ["Falcon Intelligence Recon:read"],
    "CreateRulesV1": ["Falcon Intelligence Recon:write"],
    "UpdateRulesV1": ["Falcon Intelligence Recon:write"],
    "DeleteRulesV1": ["Falcon Intelligence Recon:write"],
    # Message Center operations
    "QueryCasesIdsByFilter": ["Message Center:read"],
    "GetCaseEntitiesByIDs": ["Message Center:read"],
    "QueryActivityByCaseID": ["Message Center:read"],
    "GetCaseActivityByIds": ["Message Center:read"],
    "CreateCaseV2": ["Message Center:write"],
    "CaseAddActivity": ["Message Center:write"],
    # Fusion Workflows operations
    "WorkflowDefinitionsCombined": ["Workflow:read"],
    "WorkflowExecutionsCombined": ["Workflow:read"],
    "WorkflowTriggersCombined": ["Workflow:read"],
    "WorkflowActivitiesCombined": ["Workflow:read"],
    "WorkflowExecutionResults": ["Workflow:read"],
    "WorkflowExecute": ["Workflow:write"],
    "WorkflowExecutionsAction": ["Workflow:write"],
    # NGSIEM Case Management operations
    "queries_cases_get_v1": ["Case Management:read"],
    "entities_cases_post_v2": ["Case Management:read"],
    "entities_cases_put_v2": ["Case Management:write"],
    "entities_cases_patch_v2": ["Case Management:write"],
    "entities_case_tags_post_v1": ["Case Management:write"],
    "entities_case_tags_delete_v1": ["Case Management:write"],
    "entities_alert_evidence_post_v1": ["Case Management:write"],
    "entities_event_evidence_post_v1": ["Case Management:write"],
    # Threat Graph operations
    "queries_edgetypes_get": ["Threatgraph:read"],
    "combined_edges_get": ["Threatgraph:read"],
    "combined_ran_on_get": ["Threatgraph:read"],
    "combined_summary_get": ["Threatgraph:read"],
    "entities_vertices_getv2": ["Threatgraph:read"],
    # ODS operations
    "query_scans": ["On Demand Scans (ODS):read"],
    "get_scans_by_scan_ids_v2": ["On Demand Scans (ODS):read"],
    "query_scan_host_metadata": ["On Demand Scans (ODS):read"],
    "get_scan_host_metadata_by_ids": ["On Demand Scans (ODS):read"],
    "query_scheduled_scans": ["On Demand Scans (ODS):read"],
    "get_scheduled_scans_by_scan_ids": ["On Demand Scans (ODS):read"],
    "query_malicious_files": ["On Demand Scans (ODS):read"],
    "get_malicious_files_by_ids": ["On Demand Scans (ODS):read"],
    "create_scan": ["On Demand Scans (ODS):write"],
    "cancel_scans": ["On Demand Scans (ODS):write"],
    # NGSIEM content + data connections
    "ListLookupFiles": ["NGSIEM:read"],
    "ListParsers": ["NGSIEM:read"],
    "ListSavedQueries": ["NGSIEM:read"],
    "ListDashboards": ["NGSIEM:read"],
    "ExternalListDataConnections": ["NGSIEM Data Connections API:read"],
    "ExternalListDataConnectors": ["NGSIEM Data Connections API:read"],
    "ExternalGetDataConnectionStatus": ["NGSIEM Data Connections API:read"],
    # Alerts operations (unified alerts module)
    "GetQueriesAlertsV2": ["Alerts:read"],
    "PostEntitiesAlertsV2": ["Alerts:read"],
    "PostAggregatesAlertsV2": ["Alerts:read"],
    "PatchEntitiesAlertsV3": ["Alerts:write"],
    # Event Streams operations
    "listAvailableStreamsOAuth2": ["Event streams:read"],
    "refreshActiveStreamSession": ["Event streams:read"],
    # Quarantine operations
    "QueryQuarantineFiles": ["Quarantined Files:read"],
    "GetQuarantineFiles": ["Quarantined Files:read"],
    "UpdateQuarantinedDetectsByIds": ["Quarantined Files:write"],
    # ML Exclusions operations
    "queryMLExclusionsV1": ["Machine Learning Exclusions:read"],
    "getMLExclusionsV1": ["Machine Learning Exclusions:read"],
    "createMLExclusionsV1": ["Machine Learning Exclusions:write"],
    "updateMLExclusionsV1": ["Machine Learning Exclusions:write"],
    "deleteMLExclusionsV1": ["Machine Learning Exclusions:write"],
    # IOA Exclusions operations
    "queryIOAExclusionsV1": ["IOA Exclusions:read"],
    "getIOAExclusionsV1": ["IOA Exclusions:read"],
    "createIOAExclusionsV1": ["IOA Exclusions:write"],
    "updateIOAExclusionsV1": ["IOA Exclusions:write"],
    "deleteIOAExclusionsV1": ["IOA Exclusions:write"],
    # MalQuery operations
    "GetMalQueryQuotasV1": ["MalQuery:read"],
    "GetMalQueryMetadataV1": ["MalQuery:read"],
    "GetMalQueryRequestV1": ["MalQuery:read"],
    "PostMalQueryExactSearchV1": ["MalQuery:write"],
    "PostMalQueryHuntV1": ["MalQuery:write"],
    "PostMalQueryFuzzySearchV1": ["MalQuery:write"],
    # Falcon Sandbox (FalconX) operations
    "QueryReports": ["Sandbox (Falcon Intelligence):read"],
    "GetReports": ["Sandbox (Falcon Intelligence):read"],
    "GetSummaryReports": ["Sandbox (Falcon Intelligence):read"],
    "Submit": ["Sandbox (Falcon Intelligence):write"],
    # Tailored Intelligence operations
    "QueryEvents": ["Tailored Intelligence (Typosquatting):read"],
    "GetEventsEntities": ["Tailored Intelligence (Typosquatting):read"],
    "QueryRules": ["Tailored Intelligence (Typosquatting):read"],
    "GetRulesEntities": ["Tailored Intelligence (Typosquatting):read"],
    # --- Mutation-enablement coverage (migrated + newly added modules) ---
    # RTR batch sessions/commands + custom script & put-file management.
    # NOTE: script/put-file library management maps to the RTR Administrator
    # scope "Real time response (admin)"; session + read-only commands use
    # "Real time response".
    "BatchInitSessions": ["Real time response:read"],
    "BatchRefreshSessions": ["Real time response:read"],
    "BatchCmd": ["Real time response:read"],
    "BatchGetCmd": ["Real time response:write"],
    "BatchActiveResponderCmd": ["Real time response:write"],
    "BatchAdminCmd": ["Real time response (admin):write"],
    "RTR_GetFalconScripts": ["Real time response:read"],
    "RTR_ListFalconScripts": ["Real time response:read"],
    "RTR_GetScriptsV2": ["Real time response (admin):write"],
    "RTR_ListScripts": ["Real time response (admin):write"],
    "RTR_CreateScriptsV2": ["Real time response (admin):write"],
    "RTR_UpdateScriptsV2": ["Real time response (admin):write"],
    "RTR_DeleteScripts": ["Real time response (admin):write"],
    "RTR_ListPut_Files": ["Real time response (admin):write"],
    "RTR_GetPut_FilesV2": ["Real time response (admin):write"],
    "RTR_DeletePut_Files": ["Real time response (admin):write"],
    # Host migration (Falcon Flight Control host migration jobs)
    "GetHostMigrationIDsV1": ["Host Migration:read"],
    "GetHostMigrationsV1": ["Host Migration:read"],
    "GetMigrationIDsV1": ["Host Migration:read"],
    "GetMigrationsV1": ["Host Migration:read"],
    "GetMigrationDestinationsV1": ["Host Migration:read"],
    "CreateMigrationV1": ["Host Migration:write"],
    "HostMigrationsActionsV1": ["Host Migration:write"],
    "MigrationsActionsV1": ["Host Migration:write"],
    # SaaS security (Falcon Shield) — dismiss actions are writes
    "DismissAffectedEntityV3": ["Falcon Shield:write"],
    "DismissSecurityCheckV3": ["Falcon Shield:write"],
    # NGSIEM external data connections
    "ExternalGetDataConnectionToken": ["NGSIEM Data Connections API:read"],
    "ExternalCreateDataConnection": ["NGSIEM Data Connections API:write"],
    "ExternalUpdateDataConnectionStatus": ["NGSIEM Data Connections API:write"],
    "ExternalRegenerateDataConnectionToken": ["NGSIEM Data Connections API:write"],
    "ExternalDeleteDataConnection": ["NGSIEM Data Connections API:write"],
    # Hosts — online state (read); containment/actions + tagging (write)
    "GetOnlineState_V1": ["Hosts:read"],
    "PerformActionV2": ["Hosts:write"],
    "UpdateDeviceTags": ["Hosts:write"],
    # Incidents — actions (assign/tag/comment/status) are writes
    "PerformIncidentAction": ["Incidents:write"],
    # Fusion SOAR workflows — export/view human input (read); import/update/execute (write)
    "WorkflowDefinitionsExport": ["Workflow:read"],
    "WorkflowGetHumanInputV1": ["Workflow:read"],
    "WorkflowDefinitionsImport": ["Workflow:write"],
    "WorkflowDefinitionsUpdate": ["Workflow:write"],
    "WorkflowMockExecute": ["Workflow:write"],
    "WorkflowUpdateHumanInputV1": ["Workflow:write"],
    # Flight Control (MSSP) — CID groups, user groups, role assignments
    "getChildren": ["Flight Control:read"],
    "queryChildren": ["Flight Control:read"],
    "queryCIDGroups": ["Flight Control:read"],
    "queryCIDGroupMembers": ["Flight Control:read"],
    "getCIDGroupById": ["Flight Control:read"],
    "getCIDGroupMembersBy": ["Flight Control:read"],
    "queryUserGroups": ["Flight Control:read"],
    "queryUserGroupMembers": ["Flight Control:read"],
    "getUserGroupsByID": ["Flight Control:read"],
    "getUserGroupMembersByID": ["Flight Control:read"],
    "queryRoles": ["Flight Control:read"],
    "getRolesByID": ["Flight Control:read"],
    "createCIDGroups": ["Flight Control:write"],
    "updateCIDGroups": ["Flight Control:write"],
    "deleteCIDGroups": ["Flight Control:write"],
    "addCIDGroupMembers": ["Flight Control:write"],
    "deleteCIDGroupMembersV2": ["Flight Control:write"],
    "createUserGroups": ["Flight Control:write"],
    "updateUserGroups": ["Flight Control:write"],
    "deleteUserGroups": ["Flight Control:write"],
    "addUserGroupMembers": ["Flight Control:write"],
    "deleteUserGroupMembers": ["Flight Control:write"],
    "addRole": ["Flight Control:write"],
    "deletedRoles": ["Flight Control:write"],
    # Installation tokens — audit event reads
    "audit_events_query": ["Installation Tokens:read"],
    "audit_events_read": ["Installation Tokens:read"],
    # Content update policies
    "queryCombinedContentUpdatePolicies": ["Content Update:read"],
    "queryCombinedContentUpdatePolicyMembers": ["Content Update:read"],
    "queryPinnableContentVersions": ["Content Update:read"],
    "createContentUpdatePolicies": ["Content Update:write"],
    "updateContentUpdatePolicies": ["Content Update:write"],
    "deleteContentUpdatePolicies": ["Content Update:write"],
    "performContentUpdatePoliciesAction": ["Content Update:write"],
    "setContentUpdatePoliciesPrecedence": ["Content Update:write"],
    # Firewall management — policy writes (rule/rule-group reads already mapped)
    "createFirewallPolicies": ["Firewall Management:write"],
    "updateFirewallPolicies": ["Firewall Management:write"],
    "deleteFirewallPolicies": ["Firewall Management:write"],
    "performFirewallPoliciesAction": ["Firewall Management:write"],
    "setFirewallPoliciesPrecedence": ["Firewall Management:write"],
    "update_rule_group": ["Firewall Management:write"],
    # Sensor visibility exclusions
    "querySensorVisibilityExclusionsV1": ["Sensor Visibility Exclusions:read"],
    "getSensorVisibilityExclusionsV1": ["Sensor Visibility Exclusions:read"],
    "createSVExclusionsV1": ["Sensor Visibility Exclusions:write"],
    "updateSensorVisibilityExclusionsV1": ["Sensor Visibility Exclusions:write"],
    "deleteSensorVisibilityExclusionsV1": ["Sensor Visibility Exclusions:write"],
    # User management — create/update/delete/actions
    "createUserV1": ["User Management:write"],
    "updateUserV1": ["User Management:write"],
    "deleteUserV1": ["User Management:write"],
    "userActionV1": ["User Management:write"],
    # Identity Protection policy rules (preempt proxy / Enforcement scope)
    "get_policy_rules": ["Identity Protection Enforcement:read"],
    "get_policy_rules_query": ["Identity Protection Enforcement:read"],
    "post_policy_rules": ["Identity Protection Enforcement:write"],
    "delete_policy_rules": ["Identity Protection Enforcement:write"],
    # Case management — notification groups, SLAs, templates
    "queries_notification_groups_get_v1": ["Case Management:read"],
    "entities_notification_groups_get_v1": ["Case Management:read"],
    "entities_notification_groups_post_v1": ["Case Management:write"],
    "entities_notification_groups_patch_v1": ["Case Management:write"],
    "entities_notification_groups_delete_v1": ["Case Management:write"],
    "queries_slas_get_v1": ["Case Management:read"],
    "entities_slas_get_v1": ["Case Management:read"],
    "entities_slas_post_v1": ["Case Management:write"],
    "entities_slas_patch_v1": ["Case Management:write"],
    "entities_slas_delete_v1": ["Case Management:write"],
    "queries_templates_get_v1": ["Case Management:read"],
    "entities_templates_get_v1": ["Case Management:read"],
    "entities_templates_export_get_v1": ["Case Management:read"],
    "entities_templates_post_v1": ["Case Management:write"],
    "entities_templates_patch_v1": ["Case Management:write"],
    "entities_templates_delete_v1": ["Case Management:write"],
    "entities_templates_import_post_v1": ["Case Management:write"],
    # Next-Gen SIEM correlation rules
    "queries_rules_get_v1": ["Correlation Rules:read"],
    "entities_rules_get_v2": ["Correlation Rules:read"],
    "entities_rules_post_v1": ["Correlation Rules:write"],
    "entities_rules_patch_v1": ["Correlation Rules:write"],
    "entities_rules_delete_v1": ["Correlation Rules:write"],
    # Falcon Data Replicator (FDR) schema — all read
    "fdrschema_queries_event_get": ["Falcon Data Replicator:read"],
    "fdrschema_combined_event_get": ["Falcon Data Replicator:read"],
    "fdrschema_entities_event_get": ["Falcon Data Replicator:read"],
    "fdrschema_queries_field_get": ["Falcon Data Replicator:read"],
    "fdrschema_entities_field_get": ["Falcon Data Replicator:read"],
    # Spotlight configuration assessment (getCombinedAssessmentsQuery shares the
    # Zero Trust Assessment mapping above; rule details require Configuration Assessment)
    "getRuleDetails": ["Configuration Assessment:read"],
    # Device control policy — class config patch
    "patchDeviceControlPoliciesClassesV1": ["Device Control Policies:write"],
    # Sensor update policy — kernel-compatibility reads
    "queryCombinedSensorUpdateKernels": ["Sensor update policies:read"],
    "querySensorUpdateKernelsDistinct": ["Sensor update policies:read"],
    # Scheduled reports — retry execution (documented under Read)
    "report_executions_retry": ["Scheduled Reports:read"],
    # FileVantage (File Integrity Monitoring) operations
    "highVolumeQueryChanges": ["Falcon FileVantage:read"],
    "queryChanges": ["Falcon FileVantage:read"],
    "getChanges": ["Falcon FileVantage:read"],
    "queryPolicies": ["Falcon FileVantage:read"],
    "getPolicies": ["Falcon FileVantage:read"],
    "queryRuleGroups": ["Falcon FileVantage:read"],
    "getRuleGroups": ["Falcon FileVantage:read"],
    "getRules": ["Falcon FileVantage:read"],
    "queryScheduledExclusions": ["Falcon FileVantage:read"],
    "getScheduledExclusions": ["Falcon FileVantage:read"],
    "queryActionsMixin0": ["Falcon FileVantage:read"],
    "getActionsMixin0": ["Falcon FileVantage:read"],
    # Change content uses the separate FileVantage Content read scope
    "getContents": ["Falcon FileVantage Content:read"],
    # FileVantage writes (policies, rule groups, rules, scheduled exclusions, signals)
    "createPolicies": ["Falcon FileVantage:write"],
    "updatePolicies": ["Falcon FileVantage:write"],
    "deletePolicies": ["Falcon FileVantage:write"],
    "updatePolicyHostGroups": ["Falcon FileVantage:write"],
    "updatePolicyPrecedence": ["Falcon FileVantage:write"],
    "updatePolicyRuleGroups": ["Falcon FileVantage:write"],
    "createRuleGroups": ["Falcon FileVantage:write"],
    "updateRuleGroups": ["Falcon FileVantage:write"],
    "deleteRuleGroups": ["Falcon FileVantage:write"],
    "updateRuleGroupPrecedence": ["Falcon FileVantage:write"],
    "createRules": ["Falcon FileVantage:write"],
    "updateRules": ["Falcon FileVantage:write"],
    "deleteRules": ["Falcon FileVantage:write"],
    "createScheduledExclusions": ["Falcon FileVantage:write"],
    "updateScheduledExclusions": ["Falcon FileVantage:write"],
    "deleteScheduledExclusions": ["Falcon FileVantage:write"],
    "signalChangesExternal": ["Falcon FileVantage:write"],
    "startActions": ["Falcon FileVantage:write"],
    # Add more mappings as needed
}


def get_required_scopes(operation: str | None) -> list[str]:
    """Get the required API scopes for a specific operation.

    Args:
        operation: The API operation name

    Returns:
        List[str]: List of required API scopes
    """
    if operation is None:
        return []
    return API_SCOPE_REQUIREMENTS.get(operation, [])


# Merge auto-generated scope hints (one entry per operation wrapped by the
# generated gen_* modules). Hand-curated entries above take precedence.
try:  # pragma: no cover - generated file may be absent before first generation
    from .api_scopes_generated import GENERATED_SCOPE_REQUIREMENTS

    API_SCOPE_REQUIREMENTS = {**GENERATED_SCOPE_REQUIREMENTS, **API_SCOPE_REQUIREMENTS}
except ImportError:
    pass
