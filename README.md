# WeFact Python Wrapper

![GitHub release (latest by date)](https://img.shields.io/github/v/release/zzinnovate/wefact-python)
[![Tests](https://github.com/zzinnovate/wefact-python/actions/workflows/run-tests.yml/badge.svg?branch=main)](https://github.com/zzinnovate/wefact-python/actions/workflows/run-tests.yml)
[![codecov](https://codecov.io/gh/zzinnovate/wefact-python/graph/badge.svg?token=R08526JCXI)](https://codecov.io/gh/zzinnovate/wefact-python)
![Python Version](https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue)

An unofficial, batteries-included Python client for the WeFact API. Pragmatic, typed where it counts, and intentionally minimal on magic.

**Zero dependencies beyond `requests`.** Clean, lightweight, and production-ready.

Maintained by [zzinnovate](https://github.com/zzinnovate) and used in production. Open source, community-friendly, and actively maintained. Not affiliated with WeFact. For the upstream API, see the official [WeFact API documentation](https://www.wefact.nl/api/).

## Requirements

- Python 3.11+

## Install

*(This library is not yet published on PyPI)*

```bash
# Basic installation (library only)
pip install wefact-python

# With CLI testing tool
pip install wefact-python[cli]

# For development (includes CLI, testing, and docs)
pip install -e ".[all]"
```

## Quick start

```python
import os
from wefact import WeFact

client = WeFact(api_key=os.getenv('WEFACT_API_KEY'))

# List your latest invoices
result = client.invoices.list(limit=25)
print(result)
```

## Features

- **Zero dependencies** - Only `requests`, nothing else
- **Type hints** - Better IDE support and fewer runtime errors
- **Direct API mapping** - Mirrors WeFact's controller/action structure
- **Error handling** - Clear exceptions for common failure modes
- **Attachment support** - Base64 encoding/decoding utilities built-in
- **Production-tested** - Used by zzinnovate in client projects

## Resources

Complete coverage of all 13 WeFact API resources:

Invoices • Credit Invoices • Debtors • Products • Creditors • Groups • Subscriptions • Quotes • Interactions • Tasks • Transactions • Cost Categories • Settings

## Common operations

```python
# Show a debtor
debtor = client.debtors.show(Identifier="DB10000")

# Create an invoice
invoice = client.invoices.create(
    DebtorCode="DB10000",
    InvoiceLines=[
        {
            "Number": 1,
            "ProductCode": "P0001",
            "Description": "Service",
            "PriceExcl": 100
        }
    ],
)

# Mark invoice as paid
client.invoices.mark_as_paid(Identifier=invoice["invoice"]["Identifier"])
```

## Documentation

Full documentation covers installation, examples, and implementation details:
- **Getting Started** - Installation, usage, configuration
- **API Reference** - Endpoints, parameters, errors, enums
- **Testing** - CLI testing tool, endpoint examples
- **Project** - Contributing, changelog, security, license

*Documentation will be published at `https://zzinnovate.github.io/wefact-python/` soon.*

## Development

### Installation Options

```bash
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
- Environment variable management

See [docs/testing/cli-tool.md](docs/testing/cli-tool.md) for details.

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
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

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Security

See [SECURITY.md](SECURITY.md) for reporting vulnerabilities and best practices.

## Credits

- [Sjoerd Zaalberg van Zelst](https://github.com/sjoerdzzid) (zzinnovate)
- [All contributors](https://github.com/zzinnovate/wefact-python/graphs/contributors)
- Inspired by [vormkracht10/wefact-php](https://github.com/vormkracht10/wefact-php)

## License

MIT. See [LICENSE](LICENSE).