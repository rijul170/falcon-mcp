"""Fusion Workflows FQL resources."""

from textwrap import dedent

WORKFLOWS_FQL_DOCUMENTATION = dedent(
    """
    # Fusion SOAR Workflows FQL filter guide

    Use this guide to build the `filter` parameter for workflow search tools.

    ## Definitions fields

    | Field             | Type      | Operators        | Description                          |
    |-------------------|-----------|------------------|--------------------------------------|
    | `id`              | string    | `:`              | Definition ID                        |
    | `name`            | string    | `:`, `~`         | Workflow name                        |
    | `description`     | string    | `:`, `~`         | Workflow description                 |
    | `enabled`         | bool      | `:`              | `true` or `false`                    |
    | `trigger.id`      | string    | `:`              | Trigger ID                           |
    | `created_by`      | string    | `:`              | UUID of creating user                |
    | `created`         | timestamp | `:`, `>`, `<`    | RFC3339                              |
    | `last_modified`   | timestamp | `:`, `>`, `<`    | RFC3339                              |

    ## Executions fields

    | Field             | Type      | Operators        | Description                          |
    |-------------------|-----------|------------------|--------------------------------------|
    | `definition_id`   | string    | `:`              | Definition ID                        |
    | `definition_name` | string    | `:`              | Definition name                      |
    | `status`          | string    | `:`              | `Running`, `Completed`, `Failed`, `Cancelled` |
    | `start_timestamp` | timestamp | `:`, `>`, `<`    | RFC3339                              |
    | `end_timestamp`   | timestamp | `:`, `>`, `<`    | RFC3339                              |

    ## Examples

    - All enabled workflows:
      `enabled:true`
    - Failed executions in the last 24 h:
      `status:'Failed'+start_timestamp:>'2025-05-06T00:00:00Z'`

    Combine clauses with `+` (AND) and `,` (OR). Wrap string values in single quotes.
    """
).strip()
