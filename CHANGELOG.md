# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

- Initial release of MarkLinter.
- Added basic linting for internal Markdown links, anchor tags, and code snippet includes.
- Provided CLI entry point `marklinter`.
- Included tests for smoke testing.

## [0.1.0] - 2026-10-27

- First public release.
- Features:
-   * Verify relative Markdown links.
-   * Check anchor tag consistency.
-   * Validate code snippet include paths.
-   * Report errors with file and line number.
-   * Exit with non‑zero status on failures.
-   * Configurable via `marklinter.toml`.
-   * Supports pre‑commit integration.
-   * CI workflow added.
-   * Documentation updated.

---

This project follows [Semantic Versioning](https://semver.org/).
