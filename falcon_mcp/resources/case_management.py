"""NGSIEM Case Management FQL resources."""

from textwrap import dedent

CASE_MANAGEMENT_FQL_DOCUMENTATION = dedent(
    """
    # NGSIEM Cases FQL filter guide

    Use this guide to build the `filter` parameter for `falcon_search_ngsiem_cases`.

    ## Cases fields

    | Field                   | Type      | Operators        | Description                          |
    |-------------------------|-----------|------------------|--------------------------------------|
    | `name`                  | string    | `:`, `~`         | Case name                            |
    | `description`           | string    | `:`, `~`         | Case description                     |
    | `severity`              | int       | `:`, `>`, `<`    | 1-5 (5 = critical)                   |
    | `status`                | string    | `:`              | `New`, `In Progress`, `Resolved`, etc. |
    | `tags`                  | string    | `:`              | Tag value                            |
    | `assigned_to_user_uuid` | string    | `:`              | Assignee UUID                        |
    | `created_at`            | timestamp | `:`, `>`, `<`    | RFC3339                              |
    | `updated_at`            | timestamp | `:`, `>`, `<`    | RFC3339                              |
    | `evidence.alerts.id`    | string    | `:`              | Linked alert ID                      |
    | `evidence.events.id`    | string    | `:`              | Linked event ID                      |

    ## Examples

    - All open critical cases:
      `severity:5+status:'New','In Progress'`
    - Cases tagged with a runbook:
      `tags:'runbook-abc'`
    - Cases that link a specific alert:
      `evidence.alerts.id:'abc123...'`

    Combine clauses with `+` (AND) and `,` (OR). Wrap string values in single quotes.
    """
).strip()
