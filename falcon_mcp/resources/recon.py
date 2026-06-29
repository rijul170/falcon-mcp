"""Falcon Recon FQL resources."""

from textwrap import dedent

RECON_FQL_DOCUMENTATION = dedent(
    """
    # Falcon Recon FQL filter guide

    Use this guide to build the `filter` parameter for `falcon_search_recon_notifications`
    and `falcon_search_recon_rules`.

    ## Notifications fields

    | Field            | Type      | Operators        | Description                          |
    |------------------|-----------|------------------|--------------------------------------|
    | `id`             | string    | `:`              | Notification ID                      |
    | `rule_id`        | string    | `:`              | Source rule ID                       |
    | `rule_name`      | string    | `:`, `~`         | Source rule name                     |
    | `status`         | string    | `:`              | `new`, `in-progress`, `closed-true-positive`, `closed-false-positive` |
    | `priority`       | string    | `:`              | `high`, `medium`, `low`              |
    | `assigned_to_uid`| string    | `:`              | Assignee email                       |
    | `created_date`   | timestamp | `:`, `>`, `<`    | RFC3339                              |
    | `updated_date`   | timestamp | `:`, `>`, `<`    | RFC3339                              |
    | `match_id`       | string    | `:`              | Recon match ID                       |

    ## Rules fields

    | Field            | Type      | Operators        | Description                          |
    |------------------|-----------|------------------|--------------------------------------|
    | `name`           | string    | `:`, `~`         | Rule name                            |
    | `topic`          | string    | `:`              | Rule topic (e.g. `SA_ALIAS`, `SA_VIP`) |
    | `priority`       | string    | `:`              | `high`, `medium`, `low`              |
    | `permissions`    | string    | `:`              | `private`, `public`                  |
    | `created_timestamp` | timestamp | `:`, `>`, `<` | RFC3339                              |

    ## Examples

    - Open high-priority notifications:
      `priority:'high'+status:'new'`
    - Notifications from a particular rule:
      `rule_id:'abc123...'`
    - Public typosquat rules:
      `permissions:'public'+topic:'SA_BRAND_PRODUCT'`

    Combine clauses with `+` (AND) and `,` (OR). Wrap string values in single quotes.
    """
).strip()
