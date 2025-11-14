# Contributing

Thanks for taking the time to contribute. This project aims to be small, sharp, and well-tested. PRs that keep that spirit are very welcome.

## TL;DR

- Fork → branch → commit small, focused changes → add tests → open a PR
- Keep public API changes minimal and documented
- Tests should pass locally
- Use the CLI tool to test against a real WeFact environment

## Development Setup

### Installation

```bash
# Clone the repository
git clone https://github.com/zzinnovate/wefact-python.git
cd wefact-python

# Install with all development dependencies (CLI, testing, docs)
pip install -e ".[all]"

# Or install specific groups
pip install -e ".[cli]"      # CLI testing tool only
pip install -e ".[dev]"      # Testing tools only
pip install -e ".[docs]"     # Documentation tools only
```

### CLI Testing Tool

Test endpoints interactively against a real WeFact environment:

```bash
# Run the CLI tool
python -m wefact_cli

# Or after installation
wefact-test
```

The CLI provides:
- Interactive API endpoint testing
- Dummy data generation for testing
- Nifty terminal UI
- Environment variable management

See [docs/testing/cli-tool.md](docs/testing/cli-tool.md) for details.

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage (terminal report)
pytest --cov=wefact --cov-report=term-missing

# HTML coverage report (open htmlcov/index.html)
pytest --cov=wefact --cov-report=html

# Run specific test file
pytest tests/test_invoices.py
```

### Building Documentation

```bash
# Serve docs locally with live reload
mkdocs serve

# Build static site
mkdocs build
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

## Code Style

- **Small, composable functions** - Keep functions focused on a single responsibility
- **Explicit names** - Method names should clearly describe what they do
- **Align with WeFact API** - Public methods match WeFact's controller/action pattern (e.g., `list`, `show`, `create`, `edit`, `delete`, `mark_as_paid`)
- **Use existing exceptions** - Raise exceptions from `wefact.exceptions` (e.g., `ValidationError`, `AuthenticationError`, `NotFoundError`)
- **Use enums for readability** - Provide enums in `wefact.enums` for API values (e.g., `PricePeriod.MONTHLY`, `TaskStatus.IN_PROGRESS`, `PaymentMethod.IDEAL`) instead of Dutch abbreviations
- **Avoid breaking changes** - Maintain backward compatibility unless there's a compelling reason

Example with enums:
```python
from wefact.enums import PricePeriod, TaskStatus

# Good - readable and IDE-friendly
product = client.products.create(
    ProductName="Hosting",
    PricePeriod=PricePeriod.MONTHLY
)

# Avoid - unclear abbreviations
product = client.products.create(
    ProductName="Hosting",
    PricePeriod='m'  # What does 'm' mean?
)
```

## Tests

- **Add tests for all changes** - New features and bug fixes require tests
- **Mock API calls** - Use `pytest-mock` to mock `requests.post` responses
- **Cover happy path and edge cases** - Include at least one success test and one failure/edge case
- **Use fixtures** - Leverage fixtures from `tests/conftest.py` (e.g., `api_client`, `sample_invoice`)
- **Test naming** - Use descriptive names: `test_create_invoice`, `test_list_invoices_with_filters`

Example test pattern:
```python
def test_create_invoice(client, mocker):
    mock_response = {'status': 'success', 'invoice': {'Identifier': 'INV10000'}}
    mocker.patch('wefact.request.requests.post', return_value=type('R', (), {
        'status_code': 200,
        'json': staticmethod(lambda: mock_response)
    })())
    response = client.invoices.create(DebtorCode='DB10000', InvoiceLines=[...])
    assert response['status'] == 'success'
```

## Documentation

- **Update docs** when behavior or configuration changes
- **Keep examples runnable** - Code examples should work as-is
- **Document new resources** - Add to `docs/api/` when adding new endpoints
- **Update CHANGELOG.md** - Document all notable changes

## Releasing (maintainers)

- Update `CHANGELOG.md`.
- Bump version in `pyproject.toml`.
- Tag and publish to PyPI.

Thank you for making the project better.