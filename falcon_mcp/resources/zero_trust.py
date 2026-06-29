"""Zero Trust Assessment FQL resources."""

from textwrap import dedent

ZTA_FQL_DOCUMENTATION = dedent(
    """
    # Zero Trust Assessment FQL filter guide

    Use this guide to build the `filter` parameter for ZTA search tools.

    ## Common fields

    | Field                | Type      | Operators        | Description                                |
    |----------------------|-----------|------------------|--------------------------------------------|
    | `aid`                | string    | `:`              | Host AID                                   |
    | `cid`                | string    | `:`              | Customer ID                                |
    | `score`              | int       | `:`, `>`, `<`    | Overall ZTA score (0-100)                  |
    | `os.score`           | int       | `:`, `>`, `<`    | OS hardening score                         |
    | `sensor_config.score`| int       | `:`, `>`, `<`    | Sensor configuration score                 |
    | `account.score`      | int       | `:`, `>`, `<`    | Account/identity score                     |
    | `event_timestamp`    | timestamp | `:`, `>`, `<`    | When the assessment was computed (RFC3339) |
    | `assessment_items.id`| string    | `:`              | Specific assessment item ID                |
    | `platform`           | string    | `:`              | windows / mac / linux                      |

    ## Examples

    - Hosts below 50 overall score:
      `score:<50`
    - Windows hosts with OS hardening problems:
      `platform:'windows'+os.score:<70`
    - Recently assessed hosts:
      `event_timestamp:>'2025-04-30T00:00:00Z'`

    Combine clauses with `+` (AND) and `,` (OR). Wrap string values in single quotes.
    """
).strip()
