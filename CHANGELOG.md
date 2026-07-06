# Changelog

## 0.9.0-extended (2026-06-30)

First release of **falcon-mcp-extended**, a community extension of CrowdStrike's official [falcon-mcp](https://github.com/CrowdStrike/falcon-mcp) v0.9.0.

### Added on top of upstream v0.9.0

* 106 auto-generated `gen_*` API wrapper modules (~904 additional tools; ~1,296 total), opt-in via `FALCON_MCP_ENABLE_GENERATED=1`
* Auto-generated per-operation API scope hints (`api_scopes_generated.py`) plus curated scope mappings for all generated operations
* Additional curated host tools: device login history and network address history

### Changed

* Rebranded as an independent community extension: honest attribution, non-affiliation notice, and install instructions that don't collide with the official PyPI package
* Package distribution renamed to `falcon-mcp-extended` (the `falcon-mcp` name on PyPI belongs to CrowdStrike's official server)

## Upstream history

For the history of the underlying server through v0.9.0, see the official
[CrowdStrike falcon-mcp changelog](https://github.com/CrowdStrike/falcon-mcp/blob/main/CHANGELOG.md).
