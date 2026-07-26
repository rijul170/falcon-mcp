# Contributing

Thank you for your interest in contributing to falcon-mcp-extended!

## How to Contribute

### Reporting Bugs

Before opening a new issue, please search existing issues to avoid duplicates. When reporting a bug, include:

- A clear description of the problem
- Steps to reproduce the behavior
- Expected vs. actual behavior
- Your environment (OS, Python version, MCP client)
- The server version, transport mode, and enabled modules
- Relevant logs or error messages (redact any credentials or sensitive data)

### Suggesting Features

Open a GitHub issue with the label `enhancement`. Describe the use case and why the feature would be valuable to the broader community.

### Submitting Code Changes

1. **Fork** the repository and clone your fork locally.
2. **Create a feature branch** from `master`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**, following the existing code style and conventions.
4. **Add or update tests** if applicable.
5. **Ensure the test suite passes**:
   ```bash
   uv run pytest
   ```
6. **Commit your changes** with a clear, descriptive commit message.
7. **Push** your branch to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
8. **Open a Pull Request** against the `master` branch of this repository.

### Pull Request Guidelines

- Keep PRs focused — one feature or fix per PR.
- Describe what the PR does and why in the PR description.
- Link any related issues using GitHub keywords (e.g., `Closes #123`).
- Be responsive to review feedback.

## Development Setup

```bash
git clone https://github.com/rijul170/falcon-mcp.git
cd falcon-mcp
uv sync --all-extras
```

Run the test suite:

```bash
uv run pytest
```

## Adding Modules

New curated modules should follow the contract described in [docs/development/module_development.md](docs/development/module_development.md).

This project is a community extension of CrowdStrike's official [falcon-mcp](https://github.com/CrowdStrike/falcon-mcp). If a change benefits the upstream curated tool layer rather than just the generated modules here, please consider contributing it there as well.

## Code Style

- Follow the existing Python conventions in the codebase.
- Format with `black` and lint with `ruff` — both are configured in `pyproject.toml`.
- Use meaningful variable and function names.
- Keep functions small and focused on a single responsibility.

## Security

If you discover a security vulnerability, please do **not** open a public issue. Follow the process described in [SECURITY.md](SECURITY.md).

## License

By contributing, you agree that your contributions will be licensed under the same license as this project. See [LICENSE](LICENSE) for details.
