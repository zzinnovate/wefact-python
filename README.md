# WeFact Python Wrapper

![GitHub release (latest by date)](https://img.shields.io/github/v/release/zzinnovate/wefact-python)
[![Tests](https://github.com/zzinnovate/wefact-python/actions/workflows/run-tests.yml/badge.svg?branch=main)](https://github.com/zzinnovate/wefact-python/actions/workflows/run-tests.yml)
[![codecov](https://codecov.io/github/zzinnovate/wefact-python/branch/main/graph/badge.svg)](https://codecov.io/github/zzinnovate/wefact-python)
![Python Version](https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue)

An unofficial, batteries-included Python client for the WeFact API. Pragmatic, typed where it counts, and intentionally minimal on magic.

This project is maintained by [zzinnovate](https://github.com/zzinnovate) and is not affiliated with WeFact. For the upstream API, see the official [WeFact API documentation](https://www.wefact.nl/api/).

## Requirements

- Python 3.11+ (dropped 3.8–3.10 before first public release to align with supported ecosystem and newer typing features)

## Install

*(This library is not yet published on PyPI)*

```bash
# pip install wefact-python
```

## Quick start

```python
from wefact import WeFact

client = WeFact(api_key="your-api-key")

# List your latest invoices
result = client.invoices.list(limit=25)
print(result)
```

## What you get

- First-class resources: invoices, debtors, creditors, products, groups, subscriptions, settings, cost categories
- Clear exceptions for common failure modes
- A thin, predictable layer over WeFact’s controller/action API

## Common operations

```python
# Show a debtor
debtor = client.debtors.show(Identifier="DB10000")

# Create an invoice
invoice = client.invoices.create(
	DebtorCode="DB10000",
	InvoiceLines=[{"Number": 1, "ProductCode": "P0001", "Description": "Service", "PriceExcl": 100}],
)

# Mark invoice as paid
client.invoices.mark_as_paid(Identifier=invoice["invoice"]["Identifier"])  # API returns nested objects
```

## Documentation

Head over to the docs for installation notes, examples, and deep dives:
- Getting Started → Installation, Usage, Configuration
- API → Endpoints and Errors
- Project → Contributing, Changelog, Security, License

*the docs are not yet published...*

```python
# https://zzinnovate.github.io/wefact-python/
```

## Development

### Running Tests

```bash
# Install dependencies (if not already done)
pip install -e ".[dev]"

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

## Changelog

See [CHANGELOG](CHANGELOG.md).

## Contributing

See [CONTRIBUTING](CONTRIBUTING.md).

## Security

See [SECURITY](SECURITY.md).

## Credits

- [Sjoerd Zaalberg van Zelst](https://github.com/sjoerdzzid) (zzinnovate)
- [All contributors](https://github.com/zzinnovate/wefact-python/graphs/contributors)
- Inspired by [vormkracht10/wefact-php](https://github.com/vormkracht10/wefact-php)

## License

MIT. See [LICENSE](LICENSE).