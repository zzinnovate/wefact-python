# WeFact Python Wrapper

A pragmatic Python wrapper around the WeFact controller/action API. Thin transport, explicit resource methods, and predictable errors.

Manage invoices, debtors, creditors, products, groups, subscriptions, settings, and cost categories with a consistent client surface.

## Quick start

Install and make your first call:

```bash
pip install wefact-python
```

```python
from wefact import WeFact

client = WeFact(api_key="your-api-key")
invoices = client.invoices.list(limit=10)
```

## What’s inside

- High-level resources: invoices, debtors, creditors, products, groups, subscriptions, settings, cost categories
- Clear, typed exceptions for common error classes

## Next steps

- Getting Started → [Installation](getting-started/installation.md), [Usage](getting-started/usage.md), [Configuration](getting-started/configuration.md)
- API → [Endpoints](api/endpoints.md), [Errors](api/errors.md)
- Project → [Contributing](project/contributing.md), [Changelog](project/changelog.md), [License](project/license.md), [Security](project/security.md)