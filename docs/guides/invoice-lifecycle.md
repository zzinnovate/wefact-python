# Invoice Lifecycle

Understanding how invoices move through different states is essential for building reliable integrations with WeFact. This guide covers common patterns and best practices.

## Invoice States

WeFact invoices follow a well-defined lifecycle. Understanding these states helps you build robust integrations that respect business rules.

### Status Values

| Status | Name | Description |
|--------|------|-------------|
| 0 | Draft | Invoice is being prepared, can be edited |
| 2 | Sent | Invoice sent to customer, awaiting payment |
| 3 | Partially Paid | Some payment received, balance outstanding |
| 4 | Paid | Fully paid |
| 8 | Credited | Credit invoice issued (reversal) |

### State Transitions

```
DRAFT (0)
  │
  ├─→ send_by_email() ─→ SENT (2)
  ├─→ block() ─→ (blocked, still draft)
  ├─→ schedule() ─→ (scheduled for auto-send)
  └─→ delete() ─→ (removed)

SENT (2)
  │
  ├─→ part_payment() ─→ PARTIALLY PAID (3)
  ├─→ mark_as_paid() ─→ PAID (4)
  ├─→ send_reminder_by_email() ─→ (reminder sent)
  └─→ credit() ─→ CREDITED (8)

PARTIALLY PAID (3)
  │
  ├─→ part_payment() ─→ (more payments) ─→ PAID (4)
  └─→ mark_as_paid() ─→ PAID (4)

PAID (4)
  │
  ├─→ mark_as_unpaid() ─→ SENT (2)
  └─→ credit() ─→ CREDITED (8)
```

## Common Patterns

### Basic Invoice Creation

Create and send an invoice in one flow:

```python
from wefact import WeFact

client = WeFact(api_key="your_api_key")

# Create invoice
invoice = client.invoices.create(
    DebtorCode="DB10000",
    InvoiceLines=[{
        'Number': 1,
        'Description': 'Consulting services',
        'PriceExcl': 150.00,
        'TaxPercentage': 21
    }]
)

invoice_code = invoice['invoice']['InvoiceCode']

# Send to customer
client.invoices.send_by_email(InvoiceCode=invoice_code)
```

### Processing Payments

Handle partial and full payments:

```python
# Partial payment received
client.invoices.part_payment(
    InvoiceCode="F2024-0001",
    AmountPaid=50.00,
    Date="2024-01-15"
)

# Check remaining balance
invoice = client.invoices.show(InvoiceCode="F2024-0001")
remaining = invoice['invoice']['AmountOpen']

# Mark as fully paid
client.invoices.mark_as_paid(
    InvoiceCode="F2024-0001",
    Date="2024-01-20"
)
```

### Credit Invoice Flow

Issue a credit invoice (reversal) for a paid or sent invoice:

```python
# Original invoice must be sent or paid
credit = client.invoices.credit(
    InvoiceCode="F2024-0001",
    SendEmail="yes"  # Automatically email credit invoice
)

credit_code = credit['invoice']['InvoiceCode']
print(f"Credit invoice created: {credit_code}")
```

### Payment Reminders

Send reminder emails for overdue invoices:

```python
# Invoice must be in Sent or Partially Paid status
client.invoices.send_reminder_by_email(
    InvoiceCode="F2024-0001"
)

# For serious overdue cases
client.invoices.send_summation_by_email(
    InvoiceCode="F2024-0001"
)
```

### Draft Management

Work with draft invoices before sending:

```python
# Create draft
invoice = client.invoices.create(
    DebtorCode="DB10000",
    InvoiceLines=[...]
)

invoice_code = invoice['invoice']['InvoiceCode']

# Edit before sending
client.invoices.edit(
    InvoiceCode=invoice_code,
    Discount=10,  # 10% discount
    TermDays=30   # 30 day payment term
)

# Block from being sent (e.g., awaiting approval)
client.invoices.block(InvoiceCode=invoice_code)

# Later: unblock and send
client.invoices.unblock(InvoiceCode=invoice_code)
client.invoices.send_by_email(InvoiceCode=invoice_code)
```

### Scheduled Sending

Schedule invoices to be sent automatically:

```python
# Create and schedule for future sending
invoice = client.invoices.create(...)
invoice_code = invoice['invoice']['InvoiceCode']

client.invoices.schedule(
    InvoiceCode=invoice_code,
    ScheduledAt="2024-12-31 09:00:00"
)

# Cancel scheduled send if needed
client.invoices.cancel_schedule(InvoiceCode=invoice_code)
```

### Payment Process Management

Pause and resume automatic payment collection:

```python
# Pause payment process (e.g., customer requests delay)
client.invoices.payment_process_pause(
    InvoiceCode="F2024-0001",
    PaymentPausedEndDate="2024-12-31",
    PaymentPausedReason="Customer requested delay",
    DisableOnlinePayment="yes"  # Also disable online payment link
)

# Resume when ready
client.invoices.payment_process_reactivate(
    InvoiceCode="F2024-0001"
)
```

### Working with Attachments

Add supporting documents to invoices:

```python
import base64

# Read and encode file
with open('contract.pdf', 'rb') as f:
    pdf_content = base64.b64encode(f.read()).decode('utf-8')

# Attach to invoice
client.invoices.attachment_add(
    ReferenceIdentifier=invoice_id,  # Numeric ID, not InvoiceCode
    Filename="contract.pdf",
    Base64=pdf_content
)

# Download attachment later
result = client.invoices.attachment_download(
    ReferenceIdentifier=invoice_id,
    Filename="contract.pdf"
)

# Save downloaded file
if result['status'] == 'success':
    content = base64.b64decode(result['attachment']['Base64'])
    with open('downloaded.pdf', 'wb') as f:
        f.write(content)

# Remove attachment
client.invoices.attachment_delete(
    ReferenceIdentifier=invoice_id,
    Filename="contract.pdf"
)
```

### Downloading PDFs

Retrieve invoice PDFs programmatically:

```python
result = client.invoices.download(InvoiceCode="F2024-0001")

if result['status'] == 'success':
    # PDF is base64 encoded
    pdf_base64 = result['invoice']['Base64']
    filename = result['invoice']['Filename']
    
    # Decode and save
    import base64
    pdf_content = base64.b64decode(pdf_base64)
    
    with open(filename, 'wb') as f:
        f.write(pdf_content)
```

## Important Constraints

### Status Requirements

Different operations require specific invoice states:

| Operation | Required Status | Notes |
|-----------|----------------|-------|
| `edit()` | Draft (0) | Cannot edit sent invoices |
| `delete()` | Draft (0) | Cannot delete sent invoices |
| `block()` | Draft (0) | Only blocks drafts from sending |
| `schedule()` | Draft (0) | Only drafts can be scheduled |
| `send_by_email()` | Draft (0) | Transitions to Sent (2) |
| `send_reminder_by_email()` | Sent/Partial (2, 3) | Cannot remind on paid invoices |
| `part_payment()` | Sent/Partial (2, 3) | Cannot pay draft invoices |
| `mark_as_paid()` | Sent/Partial (2, 3) | Cannot mark drafts as paid |
| `mark_as_unpaid()` | Paid (4) | Reverts to Sent (2) |
| `credit()` | Sent or higher | Cannot credit drafts |
| `download()` | Any | Always available |

### Common Mistakes

**Cannot credit a draft invoice**
```python
# ❌ This will fail
invoice = client.invoices.create(...)
client.invoices.credit(InvoiceCode=invoice_code)

# ✅ Send first
client.invoices.send_by_email(InvoiceCode=invoice_code)
client.invoices.credit(InvoiceCode=invoice_code)
```

**Cannot edit a sent invoice**
```python
# ❌ This will fail
client.invoices.send_by_email(InvoiceCode=invoice_code)
client.invoices.edit(InvoiceCode=invoice_code, Discount=10)

# ✅ Edit before sending
client.invoices.edit(InvoiceCode=invoice_code, Discount=10)
client.invoices.send_by_email(InvoiceCode=invoice_code)
```

**Cannot delete a sent invoice**
```python
# ❌ Cannot delete sent invoices
client.invoices.send_by_email(InvoiceCode=invoice_code)
client.invoices.delete(InvoiceCode=invoice_code)

# ✅ Use credit invoice instead
client.invoices.credit(InvoiceCode=invoice_code)
```

## Complete Example

See `examples/invoice_lifecycle.py` for a complete working example that demonstrates:

- Creating an invoice
- Sending it by email
- Marking it as paid
- Creating a credit invoice
- Downloading the PDF

Run it with:

```bash
export WEFACT_API_KEY="your_api_key"
python examples/invoice_lifecycle.py
```

## Reference

### All Invoice Methods

The `client.invoices` resource provides 25 methods covering the complete invoice lifecycle:

#### CRUD Operations

- **`list()`** - List invoices with pagination
- **`show()`** - Get single invoice details
- **`create()`** - Create new invoice
- **`edit()`** - Modify draft invoice
- **`delete()`** - Delete draft invoice

#### Status Changes

- **`send_by_email()`** - Send draft invoice to customer
- **`mark_as_paid()`** - Mark invoice as fully paid
- **`mark_as_unpaid()`** - Revert paid invoice to sent
- **`part_payment()`** - Record partial payment

#### Payment Communication

- **`send_reminder_by_email()`** - Send payment reminder
- **`send_summation_by_email()`** - Send summation notice

#### Draft Management

- **`block()`** - Prevent draft from being sent
- **`unblock()`** - Remove sending block
- **`schedule()`** - Schedule automatic sending
- **`cancel_schedule()`** - Cancel scheduled sending

#### Payment Process

- **`payment_process_pause()`** - Temporarily stop collection
- **`payment_process_reactivate()`** - Resume collection

#### Additional Operations

- **`credit()`** - Create credit invoice (reversal)
- **`download()`** - Get invoice PDF
- **`sort_lines()`** - Reorder invoice lines
- **`invoice_line_add()`** - Add line item
- **`invoice_line_delete()`** - Remove line item

#### Attachments

- **`attachment_add()`** - Upload file to invoice
- **`attachment_download()`** - Download attached file
- **`attachment_delete()`** - Remove attachment

For parameter details, see the [WeFact API documentation](https://developer.wefact.com/invoice/show).
