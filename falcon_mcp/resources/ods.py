"""On-Demand Scanning FQL resources."""

from textwrap import dedent

ODS_FQL_DOCUMENTATION = dedent(
    """
    # On-Demand Scanning (ODS) FQL filter guide

    Use this guide to build the `filter` parameter for ODS search tools.

    ## Scans (`falcon_search_ods_scans`)

    | Field             | Type      | Operators        | Description                          |
    |-------------------|-----------|------------------|--------------------------------------|
    | `id`              | string    | `:`              | Scan ID                              |
    | `description`     | string    | `:`, `~`         | Description                          |
    | `status`          | string    | `:`              | `pending`, `running`, `complete`, `cancelled`, `failed` |
    | `initiated_from`  | string    | `:`              | Source (e.g. `falcon-mcp`, `console`) |
    | `created_on`      | timestamp | `:`, `>`, `<`    | RFC3339                              |
    | `started_on`      | timestamp | `:`, `>`, `<`    | RFC3339                              |
    | `completed_on`    | timestamp | `:`, `>`, `<`    | RFC3339                              |
    | `host_groups`     | string    | `:`              | Host group ID                        |
    | `hosts`           | string    | `:`              | Host AID                             |

    ## Host scans (`falcon_search_ods_host_scans`)

    | Field             | Type      | Operators        | Description                          |
    |-------------------|-----------|------------------|--------------------------------------|
    | `host_id`         | string    | `:`              | Host AID                             |
    | `scan_id`         | string    | `:`              | Parent scan ID                       |
    | `host_scan_status`| string    | `:`              | Per-host status                      |
    | `started_on`      | timestamp | `:`, `>`, `<`    | RFC3339                              |
    | `completed_on`    | timestamp | `:`, `>`, `<`    | RFC3339                              |

    ## Malicious files

    | Field             | Type      | Operators        | Description                          |
    |-------------------|-----------|------------------|--------------------------------------|
    | `host_id`         | string    | `:`              | Host AID where file was found        |
    | `file_path`       | string    | `:`, `~`         | File path                            |
    | `hash`            | string    | `:`              | SHA256                               |
    | `quarantined`     | bool      | `:`              | Whether quarantined                  |

    Combine clauses with `+` (AND) and `,` (OR). Wrap string values in single quotes.
    """
).strip()
