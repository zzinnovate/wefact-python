# API Resources

All resources follow a consistent pattern: standard CRUD methods plus resource-specific operations. Methods accept keyword arguments that map directly to WeFact API parameters.

## Available Resources

```python
client.invoices          # Sales invoices
client.credit_invoices   # Purchase invoices (from suppliers)
client.debtors           # Customers/clients
client.creditors         # Suppliers
client.products          # Products and services
client.groups            # Debtor/creditor groups
client.subscriptions     # Recurring subscriptions
client.quotes            # Price quotations
client.interactions      # Communication logs
client.tasks             # Task management
client.transactions      # Bank transactions
client.cost_categories   # Expense categories
client.settings          # Account settings
```

## Common Methods

Most resources support these standard operations:

```python
# List with pagination
client.invoices.list(limit=100, offset=0)

# Get single record by ID or code
client.invoices.show(Identifier="5")           # Using numeric ID
client.invoices.show(InvoiceCode="INV10000")   # Using formatted code

# Create new record
client.invoices.create(DebtorCode="DB10000", ...)

# Update existing record
client.invoices.edit(Identifier="5", ...)

# Delete record
client.invoices.delete(Identifier="5")
```

---

## Invoices

Full invoice lifecycle management with 25+ operations.

### CRUD Operations

```python
# List invoices
client.invoices.list(limit=100, offset=0)

# Get invoice by ID
client.invoices.show(Identifier="5")

# Or use the formatted invoice code
client.invoices.show(InvoiceCode="INV10000")

# Create invoice
client.invoices.create(
    DebtorCode="DB10000",
    InvoiceLines=[
        {
            "Number": 1,
            "ProductCode": "P0001",
            "Description": "Service",
            "PriceExcl": 100
        }
    ]
)

# Update invoice
client.invoices.edit(Identifier="5", Description="Updated")

# Delete invoice
client.invoices.delete(Identifier="5")
```

### Payment Management

```python
# Create credit invoice
client.invoices.credit(Identifier="5")

# Register partial payment
client.invoices.part_payment(
    Identifier="5",
    AmountPaid=50.00,
    PayDate="2025-01-15"
)

# Mark as paid
client.invoices.mark_as_paid(
    Identifier="5",
    PayDate="2025-01-15",
    PaymentMethod="bank"
)

# Mark as unpaid (reverse payment)
client.invoices.mark_as_unpaid(Identifier="5")
```

### Email Operations

```python
# Send invoice
client.invoices.send_by_email(Identifier="5")

# Send payment reminder
client.invoices.send_reminder_by_email(Identifier="5")

# Send collection notice
client.invoices.send_summation_by_email(Identifier="5")
```

### Document Operations

```python
# Download PDF (returns Base64 encoded)
response = client.invoices.download(Identifier="5")
pdf_content = response['invoice']['Base64']
```

### State Management

```python
# Block draft invoice (prevents sending)
client.invoices.block(Identifier="5")

# Unblock
client.invoices.unblock(Identifier="5")

# Schedule send
client.invoices.schedule(
    Identifier="5",
    ScheduledAt="2025-08-01 09:00:00"
)

# Cancel schedule
client.invoices.cancel_schedule(Identifier="5")

# Pause payment process
client.invoices.payment_process_pause(
    Identifier="5",
    PaymentPausedEndDate="2025-12-31",
    PaymentPausedReason="Customer requested"
)

# Reactivate payment process
client.invoices.payment_process_reactivate(Identifier="5")
```

### Line Management

```python
# Add invoice line
client.invoices.invoice_line_add(
    Identifier="5",
    InvoiceLines=[
        {
            "ProductCode": "P0002",
            "PriceExcl": 25.00
        }
    ]
)

# Delete invoice line
client.invoices.invoice_line_delete(
    Identifier="5",
    InvoiceLines=[{"Identifier": "12"}]  # Line ID
)

# Reorder lines
client.invoices.sort_lines(
    Identifier="5",
    InvoiceLines=[
        {"Identifier": "13"},
        {"Identifier": "12"}
    ]
)
```

### Attachments

```python
# Add attachment
client.invoices.attachment_add(
    ReferenceIdentifier="5",
    Filename="contract.pdf",
    Base64="<base64_encoded_content>"
)

# Download attachment
response = client.invoices.attachment_download(
    ReferenceIdentifier="5",
    Filename="contract.pdf"
)

# Delete attachment
client.invoices.attachment_delete(
    ReferenceIdentifier="5",
    Filename="contract.pdf"
)
```

---

## Credit Invoices

Purchase invoices received from suppliers.

### CRUD Operations

```python
client.credit_invoices.list(limit=100)
client.credit_invoices.show(Identifier="8")
client.credit_invoices.create(CreditorCode="CR10000", ...)
client.credit_invoices.edit(Identifier="8", ...)
client.credit_invoices.delete(Identifier="8")
```

### Payment Management

```python
# Partial payment
client.credit_invoices.part_payment(
    Identifier="8",
    AmountPaid=100.00
)

# Mark as paid
client.credit_invoices.mark_as_paid(Identifier="8")
```

### Line Management

```python
# Add lines
client.credit_invoices.credit_invoice_line_add(
    Identifier="8",
    CreditInvoiceLines=[...]
)

# Delete lines
client.credit_invoices.credit_invoice_line_delete(
    Identifier="8",
    CreditInvoiceLines=[{"Identifier": "15"}]
)
```

### Attachments

Same pattern as invoices: `attachment_add()`, `attachment_delete()`, `attachment_download()`

---

## Debtors

Customer/client management.

!!! note
    Delete is not available for debtors.

### CRUD Operations

```python
client.debtors.list(limit=100)
client.debtors.show(Identifier="25")
client.debtors.create(
    DebtorCode="DB10000",
    CompanyName="Acme Inc",
    EmailAddress="info@acme.com"
)
client.debtors.edit(Identifier="25", EmailAddress="new@acme.com")
# delete() raises ClientError
```

### Extra Contacts

```python
# Add contact
client.debtors.extra_client_contact_add(
    Identifier="25",
    EmailAddress="john@acme.com",
    FirstName="John",
    LastName="Doe"
)

# Edit contact
client.debtors.extra_client_contact_edit(
    Identifier="25",
    ContactIdentifier="3",
    EmailAddress="john.doe@acme.com"
)

# Delete contact
client.debtors.extra_client_contact_delete(
    Identifier="25",
    ContactIdentifier="3"
)
```

### Attachments

Same pattern: `attachment_add()`, `attachment_delete()`, `attachment_download()`

---

## Creditors

Supplier management.

### Operations

```python
client.creditors.list(limit=100)
client.creditors.show(Identifier="18")
client.creditors.create(CreditorCode="CR10000", CompanyName="Supplier Co")
client.creditors.edit(Identifier="18", ...)
client.creditors.delete(Identifier="18")
```

### Attachments

Same pattern: `attachment_add()`, `attachment_delete()`, `attachment_download()`

---

## Products

Product and service catalog.

### Operations

```python
client.products.list(limit=100)
client.products.show(Identifier="42")
client.products.create(
    ProductName="Hosting",
    ProductKeyPhrase="hosting",
    PriceExcl=9.99
)
client.products.edit(Identifier="42", PriceExcl=12.99)
client.products.delete(Identifier="42")
```

---

## Groups

Debtor/creditor grouping for organization.

### Operations

```python
client.groups.list(limit=100)
client.groups.show(Identifier="7")
client.groups.create(Type="debtor", GroupName="VIP Clients")
client.groups.edit(Identifier="7", GroupName="Key Accounts")
client.groups.delete(Identifier="7")
```

---

## Subscriptions

Recurring subscription management.

!!! note
    Delete is not available. Use `terminate()` instead.

### Operations

```python
client.subscriptions.list(limit=100)
client.subscriptions.show(Identifier="12")
client.subscriptions.create(DebtorCode="DB10000", ...)
client.subscriptions.edit(Identifier="12", ...)

# Terminate subscription (not delete)
client.subscriptions.terminate(
    Identifier="12",
    TerminationDate="2025-12-31"
)
```

---

## Quotes

Price quotation management.

### CRUD Operations

```python
client.quotes.list(limit=100)
client.quotes.show(Identifier="9")
client.quotes.create(
    DebtorCode="DB10000",
    PriceQuoteLines=[
        {
            "Description": "Setup",
            "PriceExcl": 50.00
        }
    ]
)
client.quotes.edit(Identifier="9", Reference="2025-001")
client.quotes.delete(Identifier="9")
```

### Email & Documents

```python
# Send quote
client.quotes.send_by_email(Identifier="9")

# Download PDF
response = client.quotes.download(Identifier="9")
```

### Scheduling

```python
# Schedule send
client.quotes.schedule(
    Identifier="9",
    ScheduledAt="2025-08-15 09:00:00"
)

# Cancel schedule
client.quotes.cancel_schedule(Identifier="9")
```

### Status Management

```python
# Accept quote
client.quotes.accept(Identifier="9")

# Decline quote
client.quotes.decline(Identifier="9")

# Archive quote
client.quotes.archive(Identifier="9")
```

### Line Management

```python
# Add line
client.quotes.price_quote_line_add(
    Identifier="9",
    PriceQuoteLines=[{"Description": "Support", "PriceExcl": 25}]
)

# Delete line
client.quotes.price_quote_line_delete(
    Identifier="9",
    PriceQuoteLines=[{"Identifier": "22"}]
)

# Reorder lines
client.quotes.sort_lines(
    Identifier="9",
    PriceQuoteLines=[{"Identifier": "23"}, {"Identifier": "22"}]
)
```

### Attachments

Same pattern: `attachment_add()`, `attachment_delete()`, `attachment_download()`

---

## Interactions

Communication and interaction logging.

### Operations

```python
client.interactions.list(limit=100)
client.interactions.show(Identifier="14")
client.interactions.create(
    DebtorCode="DB10000",
    Subject="Onboarding call",
    Note="Discussed requirements"
)
client.interactions.edit(Identifier="14", Subject="Follow-up call")
client.interactions.delete(Identifier="14")
```

### Attachments

Same pattern: `attachment_add()`, `attachment_delete()`, `attachment_download()`

---

## Tasks

Task management and tracking.

### Operations

```python
client.tasks.list(limit=100)
client.tasks.show(Identifier="6")
client.tasks.create(
    DebtorCode="DB10000",
    Subject="Call back customer"
)
client.tasks.edit(Identifier="6", Subject="Updated task")
client.tasks.delete(Identifier="6")
```

### Status Management

```python
# Change status (0=Open, 1=Closed)
client.tasks.change_status(Identifier="6", Status=1)
```

### Attachments

Same pattern: `attachment_add()`, `attachment_delete()`, `attachment_download()`

---

## Transactions

Bank transaction management and invoice matching.

### Operations

```python
client.transactions.list(limit=100)
client.transactions.show(Identifier="31")
client.transactions.create(...)
client.transactions.edit(Identifier="31", ...)
client.transactions.delete(Identifier="31")
```

### Matching

```python
# Match transaction to invoices
client.transactions.match(
    Identifier="31",
    InvoiceIdentifiers=["5", "6"]
)

# Ignore transaction
client.transactions.ignore(Identifier="31")
```

---

## Cost Categories

Expense category management.

!!! note
    Cost categories use the `settings` controller internally but have a dedicated resource.

### Operations

```python
client.cost_categories.list(limit=100)
client.cost_categories.show(Identifier="10")
client.cost_categories.create(Title="Cloud Infrastructure")
client.cost_categories.edit(Identifier="10", Title="Infrastructure")
client.cost_categories.delete(Identifier="10")
```

---

## Settings

Account settings retrieval.

!!! note
    Only `list()` is available. Individual CRUD operations raise `ClientError`.

### Operations

```python
# Get all settings
settings = client.settings.list()

# show(), create(), edit(), delete() raise ClientError
```

---

## Response Structure

Most detail responses nest data under the controller name:

```python
response = client.invoices.show(Identifier="INV10000")
# Returns: {'status': 'success', 'invoice': {...}}

invoice_data = response['invoice']
```

List responses use plural form:

```python
response = client.invoices.list(limit=10)
# Returns: {'status': 'success', 'invoices': [...], 'total': 42}

invoices = response['invoices']
```