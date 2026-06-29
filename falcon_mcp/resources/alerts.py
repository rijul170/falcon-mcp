"""
Contains Alerts FQL resources.
"""

from falcon_mcp.common.utils import generate_md_table

SEARCH_ALERTS_FQL_FILTERS = [
    ("Name", "Type", "Operators", "Description"),
    ("status", "String", "Yes", "Alert workflow status: 'new', 'in_progress', 'closed', 'reopened'. Ex: status:'new'"),
    ("severity", "Integer", "Yes", "Severity score 1-100. Ex: severity:>=50"),
    ("assigned_to_name", "String", "Yes", "Display name of the assignee. Ex: assigned_to_name:'Jane Doe'"),
    ("assigned_to_uuid", "String", "Yes", "UUID of the assignee."),
    ("product", "String", "Yes", "Source product, e.g. 'epp', 'idp', 'mobile', 'ngsiem'. Ex: product:'epp'"),
    ("pattern_id", "Integer", "Yes", "Detection pattern identifier."),
    ("tactic", "String", "Yes", "MITRE ATT&CK tactic. Ex: tactic:'Defense Evasion'"),
    ("technique", "String", "Yes", "MITRE ATT&CK technique. Ex: technique:'Masquerading'"),
    ("aggregate_id", "String", "Yes", "Groups related alerts (the incident/aggregate they belong to)."),
    ("composite_id", "String", "Yes", "Unique alert composite identifier."),
    ("tags", "String", "Yes", "Alert tags. Ex: tags:'falcon-internal/triage'"),
    ("created_timestamp", "Timestamp", "Yes", "When the alert was created (UTC). Ex: created_timestamp:>'2024-01-01T00:00:00Z'"),
    ("timestamp", "Timestamp", "Yes", "Event timestamp (UTC)."),
]

SEARCH_ALERTS_FQL_DOCUMENTATION = """Falcon Query Language (FQL) - Alerts Guide

=== BASIC SYNTAX ===
property_name:[operator]'value'

=== AVAILABLE OPERATORS ===
• No operator = equals (default)
• ! = not equal to
• >, >=, <, <= = comparisons (integer and timestamp fields)
• ~ = text match (case-insensitive contains)

=== DATA TYPES & SYNTAX ===
• Strings: 'value' (single quotes)
• Integers: 50 (no quotes)
• Timestamps: 'YYYY-MM-DDTHH:MM:SSZ' (ISO 8601, UTC)

=== COMBINING CONDITIONS ===
• + = AND
• , = OR
• ( ) = grouping

=== falcon_search_alerts FQL filter options ===

""" + generate_md_table(SEARCH_ALERTS_FQL_FILTERS) + """

=== EXAMPLE PATTERNS ===
• New high-severity alerts: status:'new'+severity:>=70
• Unassigned EDR alerts: product:'epp'+assigned_to_uuid:''
• Recent alerts for a tactic: tactic:'Defense Evasion'+created_timestamp:>'2024-06-01T00:00:00Z'
• Alerts in an incident: aggregate_id:'inc:abc...'
"""
