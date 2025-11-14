# WeFact Python Wrapper

An unofficial, batteries-included Python client for the WeFact API. Pragmatic, typed where it counts, and intentionally minimal on magic.

Zero dependencies beyond `requests`. Open source, community-friendly, and actively maintained. Not affiliated with WeFact.

## Quick start

Install and make your first call:

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

## Next steps

- Getting Started → [Installation](getting-started/installation.md), [Usage](getting-started/usage.md), [Configuration](getting-started/configuration.md)
- API → [Endpoints](api/endpoints.md), [Parameters](api/parameters.md), [Variables (Enums)](api/variables.md), [Errors](api/errors.md)
- Testing → [CLI Testing Tool](testing/cli-tool.md), [Invoice Endpoints](testing/invoice-endpoints.md)
- Project → [Contributing](project/contributing.md), [Changelog](project/changelog.md), [License](project/license.md), [Security](project/security.md)