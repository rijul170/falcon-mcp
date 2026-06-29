"""Installation Tokens FQL resources."""

from textwrap import dedent

SEARCH_INSTALLATION_TOKENS_FQL_DOCUMENTATION = dedent(
    """
    # Installation Tokens FQL filter guide

    Use this guide to build the `filter` parameter for the
    `falcon_search_installation_tokens` tool.

    ## Common fields

    | Field                | Type      | Operators        | Description                                |
    |----------------------|-----------|------------------|--------------------------------------------|
    | `label`              | string    | `:`, `~`         | Token label                                |
    | `value`              | string    | `:`              | The token value (rarely useful in filters) |
    | `revoked`            | bool      | `:`              | `true` if revoked, `false` if active       |
    | `expires_timestamp`  | timestamp | `:`, `>`, `<`    | RFC3339                                    |
    | `created_timestamp`  | timestamp | `:`, `>`, `<`    | RFC3339                                    |
    | `created_by`         | string    | `:`              | UUID of creating user                      |
    | `modified_timestamp` | timestamp | `:`, `>`, `<`    | RFC3339                                    |
    | `modified_by`        | string    | `:`              | UUID of last modifier                      |

    ## Examples

    - Active tokens only: `revoked:false`
    - Tokens expiring in the next 30 days:
      `revoked:false+expires_timestamp:<'2025-06-06T00:00:00Z'`
    - All tokens labelled for a particular project:
      `label:~'project-acme'`

    Combine clauses with `+` (AND) and `,` (OR). Wrap string values in single quotes.
    """
).strip()
