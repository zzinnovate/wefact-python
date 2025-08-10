# Usage

This client maps WeFact controllers to Python resources. Methods accept keyword arguments that become form data in requests.

## Initialize

```python
from wefact import WeFact

client = WeFact(api_key="your-api-key")
```

## Invoices

```python
# List (with basic pagination)
invoices = client.invoices.list(limit=50, offset=0)

# Create
invoice = client.invoices.create(
    DebtorCode="DB10000",
    InvoiceLines=[{"Number": 1, "ProductCode": "P0001", "Description": "Service", "PriceExcl": 100}],
)

# Show
full = client.invoices.show(Identifier=invoice["invoice"]["Identifier"])  # nested by controller name

# Mark as paid
client.invoices.mark_as_paid(Identifier=full["invoice"]["Identifier"])
```

## Debtors

```python
client.debtors.list(limit=25)
client.debtors.create(CompanyName="ACME BV")
client.debtors.edit(Identifier="DB10000", CompanyName="ACME B.V.")
client.debtors.show(Identifier="DB10000")
# delete is not available for this resource
```

## Creditors, Products, Groups, Subscriptions

```python
client.creditors.list()
client.products.create(ProductName="Widget", ProductKeyPhrase="WGT-001", PriceExcl=9.99)
client.groups.create(Type="debtor", GroupName="VIP")
client.subscriptions.terminate(Identifier="SUB123")
```

## Error handling

```python
from wefact.exceptions import ClientError, ServerError, AuthenticationError, NotFoundError, ValidationError

try:
    client.invoices.list()
except AuthenticationError:
    print("Invalid API key")
except NotFoundError:
    print("Endpoint not found")
except (ValidationError, ClientError, ServerError) as e:
    print(f"API error: {e}")
```

For available operations per resource, see [Endpoints](../api/endpoints.md).