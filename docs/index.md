# WeFact Python Wrapper

An unofficial, batteries-included Python client for the WeFact API. Pragmatic, typed where it counts, and intentionally minimal on magic.

**What is WeFact?** [WeFact](https://www.wefact.nl/) is a Dutch invoicing and accounting platform. Create invoices and quotes, process supplier invoices, and maintain real-time insight into your administration.

Maintained by [zzinnovate](https://github.com/zzinnovate). Open source, community-friendly, and actively maintained. Not affiliated with WeFact. For the upstream API, see the official [WeFact API documentation](https://www.wefact.nl/api/).

## Quick start

Available on [PyPI](https://pypi.org/project/wefact-python/). Install and make your first call:

```bash
pip install wefact-python
```

```python
import os
from wefact import WeFact

client = WeFact(api_key=os.getenv('WEFACT_API_KEY'))

# List your latest invoices
result = client.invoices.list(limit=25)
print(result)
```

## Features

- **Minimal dependencies** - Only `requests`, nothing else
- **Type hints** - Better IDE support and fewer runtime errors
- **Direct API mapping** - Mirrors WeFact's controller/action structure
- **Error handling** - Clear exceptions for common failure modes
- **Attachment support** - Base64 encoding/decoding utilities built-in

## Resources

Complete coverage of all 13 WeFact API resources:

Invoices • Credit Invoices • Debtors • Products • Creditors • Groups • Subscriptions • Quotes • Interactions • Tasks • Transactions • Cost Categories • Settings

## Common operations

```python
# Show a debtor
debtor = client.debtors.show(Identifier=5)

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

## Next steps

- Getting Started → [Installation](getting-started/installation.md), [Usage](getting-started/usage.md), [Configuration](getting-started/configuration.md)
- API → [Resources](api/resources.md), [Parameters](api/parameters.md), [Variables (Enums)](api/variables.md), [Errors](api/errors.md)
- Guides → [Invoice Lifecycle](guides/invoice-lifecycle.md)
- Project → [Contributing](project/contributing.md), [Changelog](project/changelog.md), [License](project/license.md), [Security](project/security.md)