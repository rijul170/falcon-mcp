# Security Policy

## Reporting a vulnerability

If you discover a security issue in falcon-mcp-extended, please **do not open a
public issue**. Instead, report it privately via GitHub's
[private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability)
on this repository (Security → Report a vulnerability). Include a description,
affected version/commit, and reproduction steps. Please allow reasonable time
for a fix before any public disclosure.

## Handling credentials (operator guidance)

This server talks to your CrowdStrike Falcon tenant with a real API client.
Treat it accordingly:

- **Never commit credentials.** `.env` is git‑ignored. Keep it that way, and
  keep `FALCON_CLIENT_ID` / `FALCON_CLIENT_SECRET` out of MCP client config
  files that live in source control.
- **Prefer a dedicated, least‑privilege API client** over an admin-level one.
  Each tool documents its required OAuth2 API scope — grant only the scopes the
  modules you actually enable need.
- **Point `FALCON_BASE_URL` at your own region.** Credentials issued in one
  Falcon cloud will not authenticate against another.
- **Bind to localhost.** `FALCON_MCP_HOST` defaults to `127.0.0.1`. If you must
  expose the HTTP transport, put it behind an authenticated reverse proxy and
  set `FALCON_MCP_API_KEY` so the MCP layer requires its own auth on top of
  Falcon's.
- **Keep destructive tools off by default.** `FALCON_MCP_ALLOW_DESTRUCTIVE` is
  unset unless you opt in. Prefer a comma‑separated allowlist of specific tool
  names over `true`, which arms every destructive tool at once — host
  containment, RTR command execution, account-level deletes.
- **Use read-only mode where writes aren't needed.** `FALCON_MCP_READONLY=true`
  suppresses all mutating tools at registration time; they are never exposed to
  the AI client, regardless of what it is asked.
- **Scope MSSP access deliberately.** `FALCON_MEMBER_CID` targets every query at
  one child CID. Flight Control scopes on the parent CID reach all managed
  tenants, so set the member CID explicitly rather than relying on defaults.

## Scope

This project is an independent API client, and a community extension of
CrowdStrike's official [falcon-mcp](https://github.com/CrowdStrike/falcon-mcp).
It is **not affiliated with, maintained by, or endorsed by CrowdStrike** —
please do not contact CrowdStrike support about this project. Vulnerabilities in
the CrowdStrike Falcon platform itself should be reported to CrowdStrike
directly.
