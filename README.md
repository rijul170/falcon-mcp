<!-- mcp-name: io.github.rijul170/falcon-mcp -->

# falcon-mcp-extended

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MCP Protocol](https://img.shields.io/badge/MCP%20Protocol-2024--11--05-blue)](https://spec.modelcontextprotocol.io/)
[![Python](https://img.shields.io/badge/python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Tools](https://img.shields.io/badge/tools-1296-purple)](#what-this-adds-over-the-official-server)
[![GitHub Stars](https://img.shields.io/github/stars/rijul170/falcon-mcp?style=social)](https://github.com/rijul170/falcon-mcp)
[![CI](https://github.com/rijul170/falcon-mcp/actions/workflows/python-test.yml/badge.svg)](https://github.com/rijul170/falcon-mcp/actions/workflows/python-test.yml)
[![PyPI](https://img.shields.io/pypi/v/falcon-mcp-extended)](https://pypi.org/project/falcon-mcp-extended/)
[![MCP Registry](https://img.shields.io/badge/MCP%20Registry-active-0A7BBB)](https://registry.modelcontextprotocol.io/v0/servers?search=io.github.rijul170/falcon-mcp)

> [!NOTE]
> **This is a community extension of CrowdStrike's official [falcon-mcp](https://github.com/CrowdStrike/falcon-mcp) server** (MIT licensed). It adds 106 auto-generated API wrapper modules (~904 additional tools) on top of the official curated tool set, for near-complete CrowdStrike Falcon API coverage. This project is **not affiliated with, maintained by, or endorsed by CrowdStrike**. If you only need the curated SOC workflows, use the [official server](https://github.com/CrowdStrike/falcon-mcp); use this project when you need API surface the official server doesn't expose yet.

**For SOC analysts and security engineers:** Stop tab-switching between CrowdStrike, your ticketing system, and your notes. Ask Claude to triage the alert, pull the process tree, check if the hash ran on other hosts, and draft the IR note — all in one conversation.

**falcon-mcp-extended** is a Model Context Protocol (MCP) server that gives AI agents — including Claude — direct, structured access to the CrowdStrike Falcon platform for intelligent security operations.

## What It Does

This server bridges AI assistants and the CrowdStrike Falcon platform, enabling SOC analysts to ask natural-language questions and get answers backed by live Falcon data. It exposes Falcon's detection, investigation, response, and intelligence capabilities as MCP tools, so an AI agent can search detections, pivot through behaviors, contain hosts, and query threat intelligence — all from a single conversation. Designed for both interactive SOC workflows and automated security pipelines, it supports MSSP Flight Control so multi-tenant environments can be queried without switching consoles.

## What This Adds Over the Official Server

| Layer | Module count | Approximate tool count | Enabled by default |
| ------- | ------------- | ------------------------ | -------------------- |
| Curated modules (from upstream, plus additions) | 50 | ~392 | Yes |
| Auto-generated API wrappers (`gen_*`) — **this project's addition** | 106 | ~904 additional | No (opt-in) |

The default mode exposes the curated layer (~392 tools), which covers every major SOC workflow with well-described, ergonomic tools. The full generated layer (total ~1,296 tools) can be enabled with `FALCON_MCP_ENABLE_GENERATED=1` for complete API surface coverage — including Message Center, ODS scans, response/content/device-control policies, installation tokens, MalQuery, FalconX Sandbox, QuickScan Pro, sample uploads, FileVantage, Falcon Complete Dashboard, cloud registration (AWS/Azure/GCP/OCI), Kubernetes admission control, container images/alerts/detections, network scanning, NGSIEM administration, knowledge bases, and much more.

## Features

- **EDR Telemetry** — Search detections, behaviors, and incidents; drill into process execution trees and command-line activity
- **Real Time Response (RTR)** — Initialize RTR sessions, run read-only triage commands (ps, netstat, filehash, reg query), and execute active responder and admin commands with configurable safety gates
- **Threat Intelligence** — Research threat actors, query CrowdStrike indicators, retrieve MITRE ATT&CK reports, and search intelligence reports
- **Custom IOC Management** — Search, create, and delete custom indicators of compromise; manage IOC watchlists
- **Vulnerability Management (Spotlight)** — Query CVE exposure by host, filter by severity or CVE ID, and surface vulnerability assessments
- **Cloud Security** — Kubernetes container visibility, container image vulnerabilities, CSPM asset inventory, and serverless function vulnerability scanning
- **Identity Protection (IDP)** — Entity investigation and identity-based threat analysis
- **MSSP / Flight Control** — List and target child CIDs; pass a per-tool `member_cid` to scope any query to a specific managed tenant
- **Next-Gen SIEM (NGSIEM)** — Execute CQL queries against the Falcon NGSIEM for log-based investigation
- **Host Management** — Query host inventory, login history, network address history, device groups, and online state
- **Firewall & Custom IOA** — Search and manage firewall rules and behavioral detection rule groups
- **Incident Management** — Correlate incidents across hosts, update status, and annotate with investigative notes
- **Scheduled Reports** — List, manage, and download Falcon scheduled report outputs
- **Safety Gates** — Read-only mode suppresses all mutating tools at registration time; a separate destructive policy controls host containment, RTR execution, and account-level deletes

## Prerequisites

- Python 3.11 or later
- CrowdStrike Falcon API credentials (Client ID and Client Secret) with appropriate scopes for the modules you intend to use
- [`uv`](https://docs.astral.sh/uv/) (recommended) or `pip`

## Installation

> [!IMPORTANT]
> Do **not** `pip install falcon-mcp` — that installs CrowdStrike's official package, which does not include the extended module layer. Install this project from source.

### From source (recommended)

```bash
git clone https://github.com/rijul170/falcon-mcp.git
cd falcon-mcp
uv sync --all-extras
uv run falcon-mcp
```

### Via uvx directly from GitHub (no clone required)

```bash
uvx --from git+https://github.com/rijul170/falcon-mcp falcon-mcp
```

### Via pip from GitHub

```bash
pip install git+https://github.com/rijul170/falcon-mcp
```

## Configuration

All configuration is driven by environment variables (or a `.env` file in the working directory). CLI flags mirror every env var and take precedence when both are set.

| Variable | Required | Description | Example |
| --- | --- | --- | --- |
| `FALCON_CLIENT_ID` | Required | CrowdStrike API Client ID | `abc123def456` |
| `FALCON_CLIENT_SECRET` | Required | CrowdStrike API Client Secret | `your-client-secret` |
| `FALCON_BASE_URL` | Required | API endpoint URL for your region | `https://api.crowdstrike.com` |
| `FALCON_MEMBER_CID` | Optional | Default child CID for MSSP Flight Control; targets all queries at that tenant | `ABC123DEF456GHI789` |
| `FALCON_MCP_TRANSPORT` | Optional | Transport protocol: `stdio`, `sse`, or `streamable-http` (default: `stdio`) | `streamable-http` |
| `FALCON_MCP_HOST` | Optional | Bind host for HTTP transports (default: `127.0.0.1`) | `0.0.0.0` |
| `FALCON_MCP_PORT` | Optional | Bind port for HTTP transports (default: `8000`) | `8000` |
| `FALCON_MCP_MODULES` | Optional | Comma-separated list of modules to enable; omit to enable all | `detections,incidents,intel` |
| `FALCON_MCP_ENABLE_GENERATED` | Optional | Set to `1` to load all 106 auto-generated modules (~1,296 tools total) | `1` |
| `FALCON_MCP_READONLY` | Optional | Set to `true` to suppress all mutating tools at startup | `true` |
| `FALCON_MCP_ALLOW_DESTRUCTIVE` | Optional | Set to `true` to enable all destructive tools, or a comma-separated list of specific tool names to allow selectively | `falcon_perform_host_action,falcon_execute_rtr_active_responder_command` |
| `FALCON_MCP_API_KEY` | Optional | API key for `x-api-key` header authentication on HTTP transports | `your-api-key` |
| `FALCON_MCP_STATELESS_HTTP` | Optional | Set to `true` to enable stateless HTTP mode for horizontally-scaled deployments | `true` |
| `FALCON_MCP_DEBUG` | Optional | Set to `true` to enable verbose debug logging | `true` |

**Region base URLs:**

| Region | Base URL |
| -------- | ---------- |
| US-1 | `https://api.crowdstrike.com` |
| US-2 | `https://api.us-2.crowdstrike.com` |
| EU-1 | `https://api.eu-1.crowdstrike.com` |
| GOV-1 | `https://api.laggar.gcw.crowdstrike.com` |

## Claude Code Integration

HTTP mode (streamable-http) is recommended for Claude Code and other AI development environments that support persistent server connections.

**Step 1 — Start the server:**

```bash
FALCON_CLIENT_ID=your-client-id \
FALCON_CLIENT_SECRET=your-client-secret \
FALCON_BASE_URL=https://api.crowdstrike.com \
FALCON_MCP_TRANSPORT=streamable-http \
uv run falcon-mcp
```

**Step 2 — Add to `.claude/settings.json` (project) or `~/.claude/settings.json` (global):**

```json
{
  "mcpServers": {
    "falcon-mcp": {
      "type": "http",
      "url": "http://localhost:8000/mcp"
    }
  }
}
```

For API key-protected deployments, add the header:

```json
{
  "mcpServers": {
    "falcon-mcp": {
      "type": "http",
      "url": "http://localhost:8000/mcp",
      "headers": {
        "x-api-key": "your-api-key"
      }
    }
  }
}
```

## Claude Desktop Integration

Stdio mode works best for Claude Desktop. Credentials are passed directly in the MCP server configuration.

```json
{
  "mcpServers": {
    "falcon-mcp": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/rijul170/falcon-mcp", "falcon-mcp"],
      "env": {
        "FALCON_CLIENT_ID": "your-client-id",
        "FALCON_CLIENT_SECRET": "your-client-secret",
        "FALCON_BASE_URL": "https://api.crowdstrike.com"
      }
    }
  }
}
```

To load credentials from a `.env` file instead of embedding them in the config:

```json
{
  "mcpServers": {
    "falcon-mcp": {
      "command": "uvx",
      "args": ["--env-file", "/path/to/.env", "--from", "git+https://github.com/rijul170/falcon-mcp", "falcon-mcp"]
    }
  }
}
```

## Docker

Build the image locally from the included Dockerfile:

```bash
git clone https://github.com/rijul170/falcon-mcp.git
cd falcon-mcp
docker build -t falcon-mcp-extended .

# Run with a .env file (stdio transport)
docker run -i --rm --env-file /path/to/.env falcon-mcp-extended

# Run with streamable-http transport
docker run --rm -p 8000:8000 --env-file /path/to/.env \
  falcon-mcp-extended --transport streamable-http --host 0.0.0.0
```

## MSSP / Multi-Tenant Usage

The server has first-class support for CrowdStrike Flight Control environments.

**Default tenant targeting:** Set `FALCON_MEMBER_CID` to route all queries to a specific child CID without changing anything else:

```bash
export FALCON_MEMBER_CID="CHILD_CID_HERE"
```

**Per-request tenant targeting:** Every tool that accepts a `member_cid` parameter can override the default at call time. This lets an AI agent query multiple child tenants in a single session without restarting the server:

> "Search for critical detections in tenant ABC123 and compare with tenant XYZ789."

**Flight Control module:** The `flight_control` module provides tools to enumerate all child accounts, list CID groups and user groups, query MSSP role assignments, and manage group membership.

**MSSP API scopes:** The parent CID must have Flight Control API scopes enabled. Child CID API keys are not required when querying through the parent.

## Available Modules

| Module | Key Capabilities |
| -------- | ----------------- |
| `alerts` | Search and manage unified alerts across all Falcon alert types |
| `detections` | Find and analyze EDR detections; retrieve behavior details and process trees |
| `incidents` | Query and correlate security incidents; update status and add investigative notes |
| `hosts` | Search host inventory; get login history, network address history, and online state |
| `intel` | Research threat actors and malware families; query IOC intelligence; retrieve MITRE ATT&CK reports |
| `ioc` | Search, create, and delete custom indicators of compromise |
| `rtr` | Initialize RTR sessions; execute read-only, active responder, and admin commands; manage RTR scripts |
| `spotlight` | Query vulnerability findings by host or CVE ID; access evaluation logic and vulnerability metadata |
| `cloud` | Kubernetes container visibility; container image vulnerabilities; CSPM asset inventory |
| `idp` | Identity entity investigation and identity protection analysis |
| `flight_control` | MSSP Flight Control: list child accounts, CID groups, user groups, and MSSP roles |
| `ngsiem` | Execute CQL queries against the Falcon Next-Gen SIEM |
| `filevantage` | File integrity monitoring — query FIM policy assignments and change events |
| `discover` | Application inventory search; unmanaged and unsanctioned asset discovery |
| `sensor_usage` | Access and analyze sensor deployment and usage data |
| `threat_graph` | Graph-based IOC pivoting: find which hosts ran a given hash or connected to an IP |
| `host_groups` | Manage device groups: create, update, and query host group membership |
| `firewall` | Search and manage firewall rules and rule groups |
| `custom_ioa` | Create and manage Custom IOA behavioral detection rules and rule groups |
| `serverless` | Search for vulnerabilities in serverless functions |
| `scheduled_reports` | List, manage, and download scheduled report executions |

Plus 106 opt-in `gen_*` modules covering the remaining Falcon API surface (enable with `FALCON_MCP_ENABLE_GENERATED=1`). Each tool's description documents the required OAuth2 API scope.

## SOC Quick Start

Once the server is running and connected to Claude, you can start investigating immediately. Example prompts:

**Triage new detections:**
> "Search for new critical and high severity detections from the last 24 hours and summarize the top 5."

**Investigate a specific detection:**
> "Get the full process tree and command-line details for detection ID abc123."

**Contain a compromised host:**
> "Contain host WORKSTATION-42 and add it to the IR-2025-001 tagging group."

**Hunt by IOC:**
> "Which hosts in my environment have executed the hash d41d8cd98f00b204e9800998ecf8427e? Show me the timeline."

**MSSP cross-tenant alert summary:**
> "List all open critical alerts across child tenants ABC123 and XYZ789 and flag any that share the same technique."

**Vulnerability prioritization:**
> "Show me all critical CVEs with a CVSS score above 9.0 affecting internet-facing hosts."

## macOS Persistence (launchd)

To run the server as a persistent background service on macOS, an example launchd plist is provided in the `examples/launchd/` directory. See the template and configuration notes there.

## Cloud Deployment

- [Amazon Bedrock AgentCore](docs/deployment/amazon_bedrock_agentcore.md)
- [Google Cloud Run / Vertex AI](docs/deployment/google_cloud.md)

## Security Considerations

**Read-only mode:** For environments where write access is not required, set `FALCON_MCP_READONLY=true`. This suppresses all mutating tools at registration time — they are never exposed to the AI agent, regardless of what is asked.

**Destructive operation gating:** Even with writes enabled, tools annotated as destructive (host containment, RTR command execution, account-level deletes) are suppressed by default. Enable them explicitly via `FALCON_MCP_ALLOW_DESTRUCTIVE`. The recommended approach is to specify a comma-separated list of specific tool names rather than setting `true` (which arms all ~119 destructive tools):

```bash
# Enable only host containment and RTR active responder
FALCON_MCP_ALLOW_DESTRUCTIVE=falcon_perform_host_action,falcon_batch_execute_active_responder_command
```

**API credential scoping:** Create a dedicated Falcon API client for this server with only the scopes required for your use case. Do not reuse admin-level API keys. Each tool's docstring documents its required API scope.

**Credential storage:** Never embed API credentials in MCP configuration files committed to source control. Use environment variables, a `.env` file outside the repository root, or a secrets manager. For HTTP transports shared across users, enable `FALCON_MCP_API_KEY` to require authentication at the MCP layer in addition to Falcon API authentication.

**Network exposure:** The default HTTP bind address is `127.0.0.1`. Do not bind to `0.0.0.0` in untrusted network environments without enabling API key authentication.

## Contributing

```bash
# Clone and install with dev dependencies
git clone https://github.com/rijul170/falcon-mcp.git
cd falcon-mcp
uv sync --all-extras

# Run tests
uv run pytest
```

Bug reports, feature requests, and pull requests are welcome via [GitHub Issues](https://github.com/rijul170/falcon-mcp/issues). For changes to the curated modules that would also benefit the official server, consider contributing them upstream to [CrowdStrike/falcon-mcp](https://github.com/CrowdStrike/falcon-mcp) as well.

Additional developer documentation:

- [Module Development Guide](docs/development/module_development.md) — how to implement new curated modules
- [Resource Development Guide](docs/development/resource_development.md) — how to implement MCP resources
- [Integration Testing Guide](docs/development/integration_testing.md) — running tests against a live Falcon API
- [End-to-End Testing Guide](docs/development/e2e_testing.md) — full E2E test setup and execution

## Support

This is an independent, community-maintained project. It is **not** an official CrowdStrike product and is not supported by CrowdStrike — do not contact CrowdStrike Technical Support about this project.

For questions, bug reports, and feature requests, please open a [GitHub Issue](https://github.com/rijul170/falcon-mcp/issues).

## Acknowledgements

The curated module layer, server core, and test suite originate from CrowdStrike's official [falcon-mcp](https://github.com/CrowdStrike/falcon-mcp) project (MIT License, Copyright CrowdStrike). This project extends that foundation with auto-generated API coverage. All CrowdStrike and Falcon trademarks belong to CrowdStrike, Inc.

## Related MCP Servers

These three servers cover complementary layers of a security stack — network/log (Alert Logic), endpoint protection (Sophos), and EDR/threat intel (CrowdStrike). Use them together for full-stack AI-powered SOC operations.

| Server | Platform | Highlights |
| -------- | ---------- | ------------ |
| [falcon-mcp-extended](https://github.com/rijul170/falcon-mcp) | CrowdStrike Falcon | EDR telemetry, RTR, threat intel, MSSP Flight Control, 1,296 tools |
| [sophos-central-mcp](https://github.com/rijul170/sophos-central-mcp) | Sophos Central | Endpoint isolation, Live Discover SQL, XDR, email/firewall/DNS, 334 tools |
| [alertlogic-mcp](https://github.com/rijul170/alertlogic-mcp) | Alert Logic MDR | Incident response, SQL log search, SOAR, vulnerability management, 473 tools |

## License

MIT — see [LICENSE](LICENSE). Original code Copyright (c) CrowdStrike; extensions Copyright (c) the falcon-mcp-extended contributors.
