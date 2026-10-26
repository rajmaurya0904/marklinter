# MarkLinter

**A documentation linter that verifies internal Markdown relative links, anchor tags, and code snippet include paths across sprawling README repositories.**

Sprawling documentation repos rot fast: relative links point to nowhere after refactoring, headers shift and break anchor hashes, and snippet includes drift out of sync with actual source code. MarkLinter runs in CI or pre-commit to catch broken references instantly, saving maintainers from embarrassing 404s and stale guides.

## Example

<!-- A real command and its REAL pasted output. Run it first. -->

## Install

```bash
pip install -e ".[dev]"
```

## Usage

<!-- The 2-4 commands people actually need, one line each. -->

## How it works

<!-- 3-6 bullets: what it checks, computes or produces. -->

## Limitations

- Does not validate external URLs (http/https) – only checks internal relative links.
- Only processes files with a `.md` extension; other markup formats are ignored.
- Ignores custom URL schemes (e.g., `mailto:`, `tel:`) and treats them as valid.
- Does not verify image existence or alt‑text completeness.
- Path handling is POSIX‑centric; Windows back‑slash paths are not fully supported.
- The linter is not exhaustive – it may miss complex anchor‑hash mismatches in generated headings.


## Development

```bash
pip install -e ".[dev]"
pytest -q
ruff check .
```

## License

MIT -- see [LICENSE](LICENSE).
