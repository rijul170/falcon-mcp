"""Users FQL resources."""

from textwrap import dedent

SEARCH_USERS_FQL_DOCUMENTATION = dedent(
    """
    # Users FQL filter guide

    Use this guide to build the `filter` parameter for the `falcon_search_users` tool.

    ## Common fields

    | Field             | Type      | Operators        | Description                          |
    |-------------------|-----------|------------------|--------------------------------------|
    | `uid`             | string    | `:`, `~`         | User email / login (e.g. `jane@x.com`) |
    | `first_name`      | string    | `:`, `~`         | First name                           |
    | `last_name`       | string    | `:`, `~`         | Last name                            |
    | `cid`             | string    | `:`              | Customer ID                          |
    | `status`          | string    | `:`              | `active`, `disabled`, `pending`      |
    | `created_at`      | timestamp | `:`, `>`, `<`    | RFC3339                              |
    | `last_login_at`   | timestamp | `:`, `>`, `<`    | RFC3339                              |
    | `assigned_cids`   | string    | `:`              | (Flight Control) Member CID UUID     |

    ## Examples

    - Active admins:
      `status:'active'+roles:'falconadministrator'`
    - Users who haven't logged in this quarter:
      `last_login_at:<'2025-02-01T00:00:00Z'`
    - All users in one domain:
      `uid:~'@example.com'`

    Combine clauses with `+` (AND) and `,` (OR). Wrap string values in single quotes.
    """
).strip()
