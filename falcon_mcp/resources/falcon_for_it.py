"""Falcon for IT (F4IT) FQL resources."""

from textwrap import dedent

F4IT_FQL_DOCUMENTATION = dedent(
    """
    # Falcon for IT FQL filter guide

    Use this guide to build the `filter` parameter for F4IT search tools.

    ## Tasks (`falcon_search_f4it_tasks`)

    | Field           | Type      | Operators        | Description                          |
    |-----------------|-----------|------------------|--------------------------------------|
    | `id`            | string    | `:`              | Task ID                              |
    | `name`          | string    | `:`, `~`         | Task name                            |
    | `description`   | string    | `:`, `~`         | Task description                     |
    | `task_type`     | string    | `:`              | `live-query`, `scheduled`, etc.      |
    | `query_language`| string    | `:`              | `osquery`, `falconscript`            |
    | `created_by`    | string    | `:`              | UUID of creating user                |
    | `created_time`  | timestamp | `:`, `>`, `<`    | RFC3339                              |

    ## Task Executions (`falcon_search_f4it_task_executions`)

    | Field             | Type      | Operators        | Description                        |
    |-------------------|-----------|------------------|------------------------------------|
    | `id`              | string    | `:`              | Execution ID                       |
    | `task_id`         | string    | `:`              | Parent task ID                     |
    | `status`          | string    | `:`              | `pending`, `running`, `complete`    |
    | `start_time`      | timestamp | `:`, `>`, `<`    | RFC3339                            |
    | `end_time`        | timestamp | `:`, `>`, `<`    | RFC3339                            |
    | `triggered_by`    | string    | `:`              | UUID of triggering user            |

    ## Examples

    - Failed executions in the last day:
      `status:'failed'+start_time:>'2025-05-06T00:00:00Z'`
    - All osquery tasks:
      `query_language:'osquery'`

    Combine clauses with `+` (AND) and `,` (OR). Wrap string values in single quotes.
    """
).strip()
