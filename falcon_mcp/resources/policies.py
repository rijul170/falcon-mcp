"""Shared FQL guide for policy modules (prevention, sensor update, RTR response)."""

from textwrap import dedent

POLICY_FQL_DOCUMENTATION = dedent(
    """
    # Policy FQL filter guide

    Use this guide to build the `filter` parameter for prevention/sensor-update/RTR
    policy search tools. The same fields apply to all three policy types.

    ## Common fields

    | Field                 | Type      | Operators        | Description                          |
    |-----------------------|-----------|------------------|--------------------------------------|
    | `name`                | string    | `:`, `~`         | Policy name                          |
    | `description`         | string    | `:`, `~`         | Policy description                   |
    | `platform_name`       | string    | `:`              | `Windows`, `Mac`, `Linux`            |
    | `enabled`             | bool      | `:`              | `true` or `false`                    |
    | `precedence`          | int       | `:`, `>`, `<`    | Lower numbers = higher precedence    |
    | `created_by`          | string    | `:`              | UUID of creating user                |
    | `created_timestamp`   | timestamp | `:`, `>`, `<`    | RFC3339                              |
    | `modified_by`         | string    | `:`              | UUID of last modifier                |
    | `modified_timestamp`  | timestamp | `:`, `>`, `<`    | RFC3339                              |
    | `groups.id`           | string    | `:`              | Assigned host group ID               |
    | `groups.name`         | string    | `:`              | Assigned host group name             |

    ## Examples

    - Enabled Windows policies: `enabled:true+platform_name:'Windows'`
    - Policies with the production host group:
      `groups.name:'Production*'`
    - Policies modified after a date:
      `modified_timestamp:>'2025-04-01T00:00:00Z'`

    Combine clauses with `+` (AND) and `,` (OR). Wrap string values in single quotes.
    """
).strip()
