# Invoice Endpoints - Complete Testing Guide

## 📋 All 25 Invoice Endpoints

### ✅ Verified Implementation Status

All **25 invoice endpoints** are fully implemented in the WeFact Python wrapper (`wefact/resources.py`).

| # | Endpoint | Method Name | Status | Dependencies |
|---|----------|-------------|--------|--------------|
| 1 | `show` | `show()` | ✅ | None |
| 2 | `list` | `list()` | ✅ | None |
| 3 | `add` | `create()` | ✅ | None |
| 4 | `edit` | `edit()` | ✅ | None |
| 5 | `delete` | `delete()` | ✅ | Draft only |
| 6 | `credit` | `credit()` | ✅ | Must be sent |
| 7 | `partpayment` | `part_payment()` | ✅ | Must be sent |
| 8 | `markaspaid` | `mark_as_paid()` | ✅ | Not draft |
| 9 | `markasunpaid` | `mark_as_unpaid()` | ✅ | Must be paid |
| 10 | `sendbyemail` | `send_by_email()` | ✅ | Draft → Sent |
| 11 | `sendreminderbyemail` | `send_reminder_by_email()` | ✅ | Must be sent |
| 12 | `sendsummationbyemail` | `send_summation_by_email()` | ✅ | Must be sent |
| 13 | `download` | `download()` | ✅ | None |
| 14 | `block` | `block()` | ✅ | Draft only |
| 15 | `unblock` | `unblock()` | ✅ | Blocked draft |
| 16 | `schedule` | `schedule()` | ✅ | Draft only |
| 17 | `cancel-schedule` | `cancel_schedule()` | ✅ | Scheduled draft |
| 18 | `payment-process/pause` | `payment_process_pause()` | ✅ | Sent/Part paid |
| 19 | `payment-process/reactivate` | `payment_process_reactivate()` | ✅ | Paused invoice |
| 20 | `sortlines` | `sort_lines()` | ✅ | None |
| 21 | `invoiceline/add` | `invoice_line_add()` | ✅ | None |
| 22 | `invoiceline/delete` | `invoice_line_delete()` | ✅ | None |
| 23 | `attachment/add` | `attachment_add()` | ✅ | None |
| 24 | `attachment/delete` | `attachment_delete()` | ✅ | None |
| 25 | `attachment/download` | `attachment_download()` | ✅ | None |

## 🔄 Invoice State Machine

```
┌─────────┐
│  DRAFT  │──── edit() ────────────┐
│ (0)     │                        │
└────┬────┘                        ▼
     │                         ┌─────────┐
     │                         │ UPDATED │
     │                         │ DRAFT   │
     │                         └────┬────┘
     │                              │
     ├── block() ──────► BLOCKED ◄──┘
     │                     │
     │                  unblock()
     │                     │
     ├── schedule() ──► SCHEDULED
     │                     │
     │              cancel_schedule()
     │                     │
     ├◄────────────────────┘
     │
     ├── send_by_email() ──┐
     │                     │
     ▼                     ▼
┌─────────┐          ┌─────────┐
│  SENT   │◄─────────│ SENT    │
│  (2)    │          │         │
└────┬────┘          └────┬────┘
     │                    │
     ├── send_reminder_by_email()
     │                    │
     ├── send_summation_by_email()
     │                    │
     ├── part_payment() ──┤
     │                    │
     ▼                    ▼
┌──────────────┐   ┌─────────┐
│ PARTIALLY    │   │  PAID   │
│ PAID (3)     │──►│  (4)    │
└──────┬───────┘   └────┬────┘
       │                │
       ├── mark_as_paid()
       │                │
       ├── payment_process_pause() ──► PAUSED
       │                                  │
       │                    payment_process_reactivate()
       │                                  │
       ├◄─────────────────────────────────┘
       │
       ├── mark_as_unpaid() ──► SENT (2)
       │
       ├── credit() ────────────► CREDIT INVOICE (8)
       │
       └── download() (Available at any stage)
```

## 📝 Testing Workflow

The `InvoiceTester` class implements a comprehensive 17-step lifecycle test:

### Draft Phase
1. **Create** - Create draft invoice
2. **Edit** - Modify invoice (discount, term)
3. **Add Line** - Add additional invoice lines
4. **Block** - Block draft invoice
5. **Unblock** - Remove block
6. **Schedule** - Schedule for future sending
7. **Cancel Schedule** - Remove schedule

### Active Phase (After Sending)
8. **Send by Email** - Change status to SENT
9. **Send Reminder** - Email payment reminder
10. **Send Summation** - Email summation notice
11. **Part Payment** - Process partial payment
12. **Mark as Paid** - Set to PAID status
13. **Mark as Unpaid** - Revert to SENT
14. **Pause Payment** - Pause payment process
15. **Reactivate Payment** - Resume payment process
16. **Download** - Get PDF
17. **Credit** - Create credit invoice

### Attachment Workflow
- **Add Attachment** - Upload file (base64)
- **Download Attachment** - Retrieve file
- **Delete Attachment** - Remove file

## 🎯 Usage Examples

### Basic Usage
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

# Send invoice
client.invoices.send_by_email(
    InvoiceCode=invoice['invoice']['InvoiceCode']
)

# Process payment
client.invoices.part_payment(
    InvoiceCode=invoice['invoice']['InvoiceCode'],
    AmountPaid=50.00
)

# Mark as paid
client.invoices.mark_as_paid(
    InvoiceCode=invoice['invoice']['InvoiceCode']
)

# Create credit invoice
client.invoices.credit(
    InvoiceCode=invoice['invoice']['InvoiceCode']
)
```

### Advanced: Payment Process Management
```python
# Pause payment process
client.invoices.payment_process_pause(
    InvoiceCode="F2024-0001",
    PaymentPausedEndDate="2024-12-31",
    PaymentPausedReason="Customer requested delay",
    DisableOnlinePayment="yes"
)

# Reactivate later
client.invoices.payment_process_reactivate(
    InvoiceCode="F2024-0001"
)
```

### Working with Attachments
```python
import base64

# Read file
with open('document.pdf', 'rb') as f:
    pdf_content = base64.b64encode(f.read()).decode('utf-8')

# Add attachment
client.invoices.attachment_add(
    ReferenceIdentifier=1,
    Filename="contract.pdf",
    Base64=pdf_content
)

# Download attachment
result = client.invoices.attachment_download(
    ReferenceIdentifier=1,
    Filename="contract.pdf"
)

# Save downloaded file
if result['status'] == 'success':
    content = base64.b64decode(result['attachment']['Base64'])
    with open('downloaded.pdf', 'wb') as f:
        f.write(content)
```

## 🧪 Running Comprehensive Tests

### Setup: Initialize Test Data

Before running invoice tests, initialize dummy data which creates a test debtor:

```bash
python wefact_cli/cli.py
# Select: Initialize Dummy Data
# Enter your test email when prompted
```

This creates a permanent test debtor with your test email address. All invoice lifecycle tests will use this debtor, ensuring emails are sent to your test address (not real customers!).

### Using the CLI

```bash
# Run full lifecycle test
python wefact_cli/cli.py
# Select: Test Invoice Endpoints → Full Lifecycle Test

# Run attachment workflow test
python wefact_cli/cli.py
# Select: Test Invoice Endpoints → Attachment Workflow Test
```

### Programmatic Usage

```python
from wefact import WeFact
from wefact_cli.endpoints.invoice_tester import InvoiceTester

client = WeFact(api_key="your_api_key")
tester = InvoiceTester(client)

# Uses the test debtor from dummy data initialization
results = tester.test_full_lifecycle()

# Or specify a different debtor
results = tester.test_full_lifecycle(debtor_code='DB10000')
```

See `examples/test_invoice_lifecycle.py` for a complete example.

**Note:** Each test run creates NEW invoices for testing. The test debtor persists across test runs.

## ⚠️ Important Notes

### Status Dependencies
- **Draft operations** (edit, block, schedule): Only work on Status = 0
- **Email operations** (send_reminder, send_summation): Require Status ≥ 2
- **Payment operations** (part_payment, mark_as_paid): Require Status ≥ 2
- **Credit**: Works best on SENT or PAID invoices
- **Delete**: Only works on DRAFT invoices

### Common Pitfalls
1. **Cannot credit draft** - Must send invoice first
2. **Cannot block sent invoice** - Only drafts can be blocked
3. **Cannot delete sent invoice** - Use `credit()` instead
4. **Part payment auto-marks as paid** - If amount equals outstanding
5. **Scheduled invoices auto-send** - Cannot manually send scheduled invoices

### Best Practices
1. Always check invoice status before operations
2. Use `show()` to get current state
3. Handle errors gracefully (status dependencies)
4. Test on sandbox/development environment first
5. Use meaningful reference numbers for tracking

## 🔍 Debugging

Enable detailed logging in the CLI:
```python
from wefact_cli.endpoints.invoice_tester import InvoiceTester

tester = InvoiceTester(client)
results = tester.test_full_lifecycle(debtor_code='DB10000')

# Check individual results
for endpoint, result in results.items():
    if not result.success:
        print(f"Failed: {endpoint} - {result.message}")
        print(f"Response: {result.response}")
```

## 📚 API Documentation Reference

All endpoints documented at: https://developer.wefact.com/invoice/

- State transitions: Check "Verplichte velden" for requirements
- Error messages: In Dutch, returned in `response['error']`
- Success messages: In `response['success']` array
