# Contributing

Thank you for your interest in contributing to falcon-mcp-extended! This is an independent, community-maintained project (not affiliated with CrowdStrike).

## How to contribute

1. Find an issue you'd like to address, or open a new one describing the bug or feature first so it can be discussed.
2. Fork the repository and clone your fork.
3. Create a branch for your change: `git checkout -b your-branch-name`.
4. Set up the development environment:

   ```bash
   uv sync --all-extras
   ```

5. Make your changes. Follow the existing code style; use [Google-style docstrings](https://google.github.io/styleguide/pyguide.html#docstrings) for new functions.
6. Lint and test before pushing:

   ```bash
   uv run ruff check .
   uv run pytest
   ```

7. Commit using [Conventional Commits](https://www.conventionalcommits.org/) (e.g. `fix: handle empty FQL filter in search_hosts`), push, and open a pull request against `master`.

## Guidelines

- **New tools/modules:** curated modules live in `falcon_mcp/modules/`; auto-generated modules (`gen_*`) are produced by `scripts/generate_falcon_modules.py` — regenerate rather than hand-editing them.
- **API scope mappings:** every `operation="..."` used in a module must have an entry in `falcon_mcp/common/api_scopes.py` (curated) or `api_scopes_generated.py` (generated). The test suite enforces this.
- **Tool annotations:** set `readOnlyHint` / `destructiveHint` correctly — the read-only and destructive gating features depend on them.
- **Tests:** add or update tests under `tests/` for any behavior change.

## Upstream changes

Improvements to the curated modules, server core, or common utilities may also benefit the official [CrowdStrike/falcon-mcp](https://github.com/CrowdStrike/falcon-mcp) project — consider contributing them upstream as well.

## Code of Conduct

All contributors are expected to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
