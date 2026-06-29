"""Threat Graph reference."""

from textwrap import dedent

THREAT_GRAPH_GUIDE = dedent(
    """
    # Threat Graph reference

    Threat Graph models entities (vertices) and the relationships between them
    (edges). Tools in this module take a vertex ID, an indicator, or a vertex type
    to return either edges, summaries, or full metadata.

    ## Common vertex types

    - `device` - host
    - `process` - executed process
    - `file` - on-disk file
    - `hash_sha256`, `hash_md5` - file hashes
    - `ipv4`, `ipv6`, `domain` - network indicators
    - `indicator` - external IOC
    - `incident`, `detection` - findings
    - `legacy_detection` - pre-Alerts detection
    - `actor` - threat actor (intel)
    - `accessory`, `kerberos_ticket`, `idp_session` - identity entities
    - `any-vertex` - wildcard for vertex lookups

    The full list is large; pass any string the API accepts.

    ## Scopes

    - `device` - within one host
    - `customer` - across the CID
    - `global` - across all CrowdStrike telemetry (where authorized)
    - `cspm` - cloud posture
    - `cwpp` - cloud workload protection

    ## Edge types (a small sample)

    Use `falcon_list_threat_graph_edge_types` for the live list. Examples:

    - `parent_processes`, `child_processes`
    - `module_files`, `injected_into_processes`
    - `dns_requests`, `network_connections`
    - `module_loads`, `command_history`

    ## Indicator types for `ran_on`

    `sha256`, `md5`, `ipv4`, `ipv6`, `domain`.
    """
).strip()
