# Contributing

Thanks for taking the time to contribute. This project aims to be small, sharp, and well-tested. PRs that keep that spirit are very welcome.

## TL;DR

- Fork → branch → commit small, focused changes → add tests → open a PR.
- Keep public API changes minimal and documented.
- Tests should pass locally.

## Development setup

This repo uses a standard Python toolchain with pytest and MkDocs:

- Install runtime deps and dev tools
  - From PyPI users install only runtime deps automatically.
  - For local dev, install extras from `requirements.txt` as needed.

```bash
python -m pip install -r requirements.txt
```

Run tests:

```bash
pytest
```

Serve docs locally:

```bash
mkdocs serve
```

## Workflow

1. Fork and clone:
   ```bash
   git clone https://github.com/your-username/wefact-python.git
   cd wefact-python
   ```
2. Create a feature branch:
   ```bash
   git checkout -b feat/short-slug
   ```
3. Make changes with tests. Put tests under `tests/`.
4. Run the suite until green.
5. Commit with a clear message:
   ```bash
   git commit -m "feat(invoice): add mark_as_paid helper"
   ```
6. Push and open a PR against `main`.

## Code style

- Prefer small, composable functions and explicit names.
- Keep public method names aligned with WeFact controller/actions.
- Raise the existing exceptions from `wefact.exceptions`.
- Avoid breaking changes unless there’s a compelling reason (and document them).

## Tests

- Add tests for new behavior and bug fixes.
- Include at least one happy-path test and one edge case.
- Use fixtures in `tests/conftest.py` when appropriate.

## Docs

- Update `docs/` when behavior or configuration changes.
- Keep examples minimal and runnable.

## Releasing (maintainers)

- Update `CHANGELOG.md`.
- Bump version in `pyproject.toml`.
- Tag and publish to PyPI.

Thank you for making the project better.