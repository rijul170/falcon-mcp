"""Sensor Download FQL resources."""

from textwrap import dedent

SEARCH_SENSOR_INSTALLERS_FQL_DOCUMENTATION = dedent(
    """
    # Sensor Installers FQL filter guide

    Use this guide to build the `filter` parameter for `falcon_search_sensor_installers`.

    ## Common fields

    | Field           | Type      | Operators        | Description                                  |
    |-----------------|-----------|------------------|----------------------------------------------|
    | `platform`      | string    | `:`              | `windows`, `mac`, `linux`                    |
    | `os`            | string    | `:`, `~`         | OS name (e.g. `Windows 10`, `Ubuntu`)        |
    | `os_version`    | string    | `:`, `~`         | OS version (e.g. `1903`, `22.04`)            |
    | `architectures` | string    | `:`              | `x86_64`, `arm64`                            |
    | `version`       | string    | `:`, `~`         | Sensor version (e.g. `7.20`)                 |
    | `release_date`  | timestamp | `:`, `>`, `<`    | RFC3339                                      |
    | `sha256`        | string    | `:`              | SHA256 of the installer                      |
    | `name`          | string    | `:`, `~`         | Installer file name                          |

    ## Examples

    - Latest Windows installers:
      `platform:'windows'`
    - Linux installers for Ubuntu 22.04 x86_64:
      `platform:'linux'+os:'Ubuntu'+os_version:'22.04'+architectures:'x86_64'`
    - Installers released in the last 30 days:
      `release_date:>'2025-04-07T00:00:00Z'`

    Combine clauses with `+` (AND) and `,` (OR). Wrap string values in single quotes.
    """
).strip()
