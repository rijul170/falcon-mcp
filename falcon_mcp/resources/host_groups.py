"""Host Groups FQL resources."""

from textwrap import dedent

SEARCH_HOST_GROUPS_FQL_DOCUMENTATION = dedent(
    """
    # Host Groups FQL filter guide

    Use this guide to build the `filter` parameter for the `falcon_search_host_groups` tool.

    ## Common fields

    | Field                | Type      | Operators        | Description                                  |
    |----------------------|-----------|------------------|----------------------------------------------|
    | `name`               | string    | `:`, `~`         | Group name (case-sensitive; `~` for wildcard) |
    | `description`        | string    | `:`, `~`         | Group description                            |
    | `group_type`         | string    | `:`              | `static` or `dynamic`                        |
    | `assignment_rule`    | string    | `:`, `~`         | The FQL rule used by dynamic groups          |
    | `created_by`         | string    | `:`              | UUID of creating user                        |
    | `created_timestamp`  | timestamp | `:`, `>`, `<`    | RFC3339 (e.g. `2025-01-01T00:00:00Z`)        |
    | `modified_by`        | string    | `:`              | UUID of last modifier                        |
    | `modified_timestamp` | timestamp | `:`, `>`, `<`    | RFC3339                                      |

    ## Examples

    - Production groups:
      `name:'Production*'`
    - All dynamic groups modified this week:
      `group_type:'dynamic'+modified_timestamp:>'2025-04-30T00:00:00Z'`
    - Groups created by a specific user:
      `created_by:'7c2f...'`

    ## Notes

    - Combine clauses with `+` (AND) and `,` (OR).
    - Use single quotes around string values.
    - For static groups, `assignment_rule` will be empty.
    """
).strip()
