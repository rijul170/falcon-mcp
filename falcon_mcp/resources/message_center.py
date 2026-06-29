"""Message Center FQL resources."""

from textwrap import dedent

MESSAGE_CENTER_FQL_DOCUMENTATION = dedent(
    """
    # Message Center / Falcon Complete Cases FQL filter guide

    Use this guide to build the `filter` parameter for `falcon_search_cases` and
    `falcon_search_case_activities`.

    ## Cases fields

    | Field             | Type      | Operators        | Description                          |
    |-------------------|-----------|------------------|--------------------------------------|
    | `id`              | string    | `:`              | Case ID                              |
    | `key`             | string    | `:`              | Case key                             |
    | `title`           | string    | `:`, `~`         | Case title                           |
    | `type`            | string    | `:`              | `fc-detection-question`, `fc-incident-question`, `fc-falcon-product-support`, etc. |
    | `status`          | string    | `:`              | `New`, `In Progress`, `Resolved`, `Closed` |
    | `created_time`    | timestamp | `:`, `>`, `<`    | RFC3339                              |
    | `last_modified_time` | timestamp | `:`, `>`, `<` | RFC3339                              |
    | `user_uuid`       | string    | `:`              | UUID of the case owner               |
    | `detections.id`   | string    | `:`              | Linked detection ID                  |
    | `incidents.id`    | string    | `:`              | Linked incident ID                   |

    ## Activities fields (within `falcon_search_case_activities`)

    | Field             | Type      | Operators        | Description                          |
    |-------------------|-----------|------------------|--------------------------------------|
    | `case_id`         | string    | `:`              | Parent case ID                       |
    | `type`            | string    | `:`              | `comment`, `status-change`, etc.     |
    | `user_uuid`       | string    | `:`              | UUID of the activity author          |
    | `created_time`    | timestamp | `:`, `>`, `<`    | RFC3339                              |

    ## Examples

    - All open Falcon Complete cases:
      `status:'New','In Progress'`
    - Cases linked to a specific detection:
      `detections.id:'abc123...'`
    - Cases updated this week:
      `last_modified_time:>'2025-04-30T00:00:00Z'`

    Combine clauses with `+` (AND) and `,` (OR). Wrap string values in single quotes.
    """
).strip()
