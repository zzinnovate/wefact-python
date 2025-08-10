# Resources and operations

The client exposes Python resources that map to WeFact controllers. Methods accept keyword arguments posted as form data. Responses are JSON objects; most detail responses are nested under the controller name (for example, `{ "invoice": { ... } }`).

Tip: Parameter shapes shown here are illustrative. For full matrices, consult the official WeFact API reference.

## invoices

| Method | Description | Example |
|---|---|---|
| `list(limit=..., offset=...)` | List invoices with pagination. | ``client.invoices.list(limit=100, offset=0)`` |
| `show(Identifier=...)` | Get a single invoice by identifier/code. | ``client.invoices.show(Identifier="INV10000")`` |
| `create(DebtorCode=..., InvoiceLines=[...])` | Create a new invoice. | ``client.invoices.create(DebtorCode="DB10000", InvoiceLines=[{"Number":1,"ProductCode":"P0001","PriceExcl":100}])`` |
| `edit(Identifier=..., ...)` | Update an invoice. | ``client.invoices.edit(Identifier="INV10000", Description="Updated")`` |
| `delete(Identifier=...)` | Delete an invoice. | ``client.invoices.delete(Identifier="INV10000")`` |
| `credit(...)` | Create a credit invoice. | ``client.invoices.credit(Identifier="INV10000")`` |
| `part_payment(...)` | Register a partial payment. | ``client.invoices.part_payment(Identifier="INV10000", Amount=10.0)`` |
| `mark_as_paid(...)` | Mark as paid. | ``client.invoices.mark_as_paid(Identifier="INV10000")`` |
| `mark_as_unpaid(...)` | Revert paid status. | ``client.invoices.mark_as_unpaid(Identifier="INV10000")`` |
| `send_by_email(...)` | Send the invoice by email. | ``client.invoices.send_by_email(Identifier="INV10000")`` |
| `send_reminder_by_email(...)` | Send a reminder by email. | ``client.invoices.send_reminder_by_email(Identifier="INV10000")`` |
| `send_summation_by_email(...)` | Send a summation by email. | ``client.invoices.send_summation_by_email(Identifier="INV10000")`` |
| `download(...)` | Download the invoice PDF. | ``client.invoices.download(Identifier="INV10000")`` |
| `block(...)` | Block the invoice from reminders. | ``client.invoices.block(Identifier="INV10000")`` |
| `unblock(...)` | Unblock the invoice. | ``client.invoices.unblock(Identifier="INV10000")`` |
| `schedule(...)` | Schedule sending. | ``client.invoices.schedule(Identifier="INV10000", Date="2025-08-01")`` |
| `cancel_schedule(...)` | Cancel scheduled sending. | ``client.invoices.cancel_schedule(Identifier="INV10000")`` |
| `payment_process_pause(...)` | Pause payment process. | ``client.invoices.payment_process_pause(Identifier="INV10000")`` |
| `payment_process_reactivate(...)` | Reactivate payment process. | ``client.invoices.payment_process_reactivate(Identifier="INV10000")`` |
| `sort_lines(...)` | Reorder invoice lines. | ``client.invoices.sort_lines(Identifier="INV10000", LineNumbers=[2,1])`` |
| `invoice_line_add(...)` | Add an invoice line. | ``client.invoices.invoice_line_add(Identifier="INV10000", InvoiceLine={"ProductCode":"P0001","PriceExcl":25})`` |
| `invoice_line_delete(...)` | Remove an invoice line. | ``client.invoices.invoice_line_delete(Identifier="INV10000", LineNumber=1)`` |
| `attachment_add(...)` | Upload an attachment to an invoice. | ``client.invoices.attachment_add(Identifier="INV10000", FileName="x.pdf", FileData="<base64>")`` |
| `attachment_delete(...)` | Delete an invoice attachment. | ``client.invoices.attachment_delete(Identifier="INV10000", AttachmentGuid="ATT-1")`` |
| `attachment_download(...)` | Download an attachment. | ``client.invoices.attachment_download(Identifier="INV10000", AttachmentGuid="ATT-1")`` |

Example:

```python
client.invoices.create(
  DebtorCode="DB10000",
  InvoiceLines=[{"Number": 1, "ProductCode": "P0001", "Description": "Service", "PriceExcl": 100}],
)
```

## debtors

| Method | Description | Example |
|---|---|---|
| `list(limit=..., offset=...)` | List debtors. | ``client.debtors.list(limit=100)`` |
| `show(Identifier=...)` | Get a debtor. | ``client.debtors.show(Identifier="DB10000")`` |
| `create(...)` | Create a debtor. | ``client.debtors.create(DebtorCode="DB10000", CompanyName="Acme")`` |
| `edit(Identifier=..., ...)` | Update a debtor. | ``client.debtors.edit(Identifier="DB10000", EmailAddress="info@acme.tld")`` |
| — | Delete is not available (raises `ClientError`). | — |
| `extra_client_contact_add(Identifier=..., ...)` | Add an extra client contact. | ``client.debtors.extra_client_contact_add(Identifier="DB10000", Name="Jane")`` |
| `extra_client_contact_edit(Identifier=..., ContactIdentifier=..., ...)` | Edit an extra client contact. | ``client.debtors.extra_client_contact_edit(Identifier="DB10000", ContactIdentifier="C1", Name="Janet")`` |
| `extra_client_contact_delete(Identifier=..., ContactIdentifier=...)` | Delete an extra client contact. | ``client.debtors.extra_client_contact_delete(Identifier="DB10000", ContactIdentifier="C1")`` |
| `attachment_add(Identifier=..., FileName=..., FileData=...)` | Add attachment to a debtor. | ``client.debtors.attachment_add(Identifier="DB10000", FileName="doc.pdf", FileData="<base64>")`` |
| `attachment_delete(Identifier=..., AttachmentGuid=...)` | Remove a debtor attachment. | ``client.debtors.attachment_delete(Identifier="DB10000", AttachmentGuid="ATT-1")`` |
| `attachment_download(Identifier=..., AttachmentGuid=...)` | Download a debtor attachment. | ``client.debtors.attachment_download(Identifier="DB10000", AttachmentGuid="ATT-1")`` |

## creditors

| Method | Description | Example |
|---|---|---|
| `list(limit=..., offset=...)` | List creditors. | ``client.creditors.list(limit=100)`` |
| `show(Identifier=...)` | Get a creditor. | ``client.creditors.show(Identifier="CR10000")`` |
| `create(...)` | Create a creditor. | ``client.creditors.create(CreditorCode="CR10000", CompanyName="Vendor")`` |
| `edit(Identifier=..., ...)` | Update a creditor. | ``client.creditors.edit(Identifier="CR10000", EmailAddress="ap@vendor.tld")`` |
| `delete(Identifier=...)` | Delete a creditor. | ``client.creditors.delete(Identifier="CR10000")`` |
| `attachment_add(Identifier=..., FileName=..., FileData=...)` | Add attachment to a creditor. | ``client.creditors.attachment_add(Identifier="CR10000", FileName="x.pdf", FileData="<base64>")`` |
| `attachment_delete(Identifier=..., AttachmentGuid=...)` | Remove a creditor attachment. | ``client.creditors.attachment_delete(Identifier="CR10000", AttachmentGuid="ATT-1")`` |
| `attachment_download(Identifier=..., AttachmentGuid=...)` | Download a creditor attachment. | ``client.creditors.attachment_download(Identifier="CR10000", AttachmentGuid="ATT-1")`` |

## products

| Method | Description | Example |
|---|---|---|
| `list(limit=..., offset=...)` | List products. | ``client.products.list(limit=100)`` |
| `show(Identifier=...)` | Get a product. | ``client.products.show(Identifier="P0001")`` |
| `create(ProductName=..., ProductKeyPhrase=..., PriceExcl=...)` | Create a product. | ``client.products.create(ProductName="Hosting", ProductKeyPhrase="hosting", PriceExcl=5.0)`` |
| `edit(Identifier=..., ...)` | Update a product. | ``client.products.edit(Identifier="P0001", PriceExcl=7.5)`` |
| `delete(Identifier=...)` | Delete a product. | ``client.products.delete(Identifier="P0001")`` |

## groups

| Method | Description | Example |
|---|---|---|
| `list(limit=..., offset=...)` | List groups. | ``client.groups.list(limit=100)`` |
| `show(Identifier=...)` | Get a group. | ``client.groups.show(Identifier="GRP1")`` |
| `create(Type=..., GroupName=...)` | Create a group. | ``client.groups.create(Type="debtor", GroupName="VIP")`` |
| `edit(Identifier=..., ...)` | Update a group. | ``client.groups.edit(Identifier="GRP1", GroupName="Key Accounts")`` |
| `delete(Identifier=...)` | Delete a group. | ``client.groups.delete(Identifier="GRP1")`` |

## subscriptions

| Method | Description | Example |
|---|---|---|
| `list(limit=..., offset=...)` | List subscriptions. | ``client.subscriptions.list(limit=100)`` |
| `show(Identifier=...)` | Get a subscription. | ``client.subscriptions.show(Identifier="SUB1")`` |
| `create(...)` | Create a subscription. | ``client.subscriptions.create(DebtorCode="DB10000", ...)`` |
| `edit(Identifier=..., ...)` | Update a subscription. | ``client.subscriptions.edit(Identifier="SUB1", ...)`` |
| — | Delete is not available (raises `ClientError`). | — |
| `terminate(Identifier=...)` | Terminate a subscription. | ``client.subscriptions.terminate(Identifier="SUB1")`` |

## settings

| Method | Description | Example |
|---|---|---|
| `list(...)` | List available settings. | ``client.settings.list()`` |
| — | Show/create/edit/delete are not available (raise `ClientError`). | — |

## cost_categories

Note: The controller name differs; methods map to specific `costcategory_*` actions.

| Method | Description | Example |
|---|---|---|
| `list(limit=..., offset=...)` | List cost categories. | ``client.cost_categories.list(limit=100)`` |
| `show(Identifier=...)` | Get a cost category. | ``client.cost_categories.show(Identifier="CC1")`` |
| `create(Title=...)` | Create a cost category. | ``client.cost_categories.create(Title="Cloud costs")`` |
| `edit(Identifier=..., ...)` | Update a cost category. | ``client.cost_categories.edit(Identifier="CC1", Title="Infra")`` |
| `delete(Identifier=...)` | Delete a cost category. | ``client.cost_categories.delete(Identifier="CC1")`` |

## interactions

| Method | Description | Example |
|---|---|---|
| `list(limit=..., offset=...)` | List interactions. | ``client.interactions.list(limit=100, offset=0)`` |
| `show(Identifier=...)` | Get an interaction. | ``client.interactions.show(Identifier="I00001")`` |
| `create(...)` | Create an interaction. | ``client.interactions.create(DebtorCode="DB10000", Subject="Onboarding call")`` |
| `edit(Identifier=..., ...)` | Update an interaction. | ``client.interactions.edit(Identifier="I00001", Subject="Follow-up call")`` |
| `delete(Identifier=...)` | Delete an interaction. | ``client.interactions.delete(Identifier="I00001")`` |
| `attachment_add(Identifier=..., FileName=..., FileData=...)` | Add attachment to an interaction. | ``client.interactions.attachment_add(Identifier="I00001", FileName="notes.txt", FileData="<base64>")`` |
| `attachment_delete(Identifier=..., AttachmentGuid=...)` | Remove an interaction attachment. | ``client.interactions.attachment_delete(Identifier="I00001", AttachmentGuid="ATT-123")`` |
| `attachment_download(Identifier=..., AttachmentGuid=...)` | Download an interaction attachment. | ``client.interactions.attachment_download(Identifier="I00001", AttachmentGuid="ATT-123")`` |

## quotes

| Method | Description | Example |
|---|---|---|
| `list(limit=..., offset=...)` | List quotes. | ``client.quotes.list(limit=100, offset=0)`` |
| `show(Identifier=...)` | Get a quote. | ``client.quotes.show(Identifier="Q0001")`` |
| `create(...)` | Create a quote. | ``client.quotes.create(DebtorCode="DB10000", PriceQuoteLines=[{"Description":"Setup","PriceExcl":50}])`` |
| `edit(Identifier=..., ...)` | Update a quote. | ``client.quotes.edit(Identifier="Q0001", Reference="2025-001")`` |
| `delete(Identifier=...)` | Delete a quote. | ``client.quotes.delete(Identifier="Q0001")`` |
| `send_by_email(Identifier=...)` | Send quote by email. | ``client.quotes.send_by_email(Identifier="Q0001")`` |
| `download(Identifier=...)` | Download quote PDF. | ``client.quotes.download(Identifier="Q0001")`` |
| `schedule(Identifier=..., ...)` | Schedule sending. | ``client.quotes.schedule(Identifier="Q0001", Date="2025-08-15")`` |
| `cancel_schedule(Identifier=...)` | Cancel scheduled send. | ``client.quotes.cancel_schedule(Identifier="Q0001")`` |
| `accept(Identifier=...)` | Accept quote. | ``client.quotes.accept(Identifier="Q0001")`` |
| `decline(Identifier=...)` | Decline quote. | ``client.quotes.decline(Identifier="Q0001")`` |
| `archive(Identifier=...)` | Archive quote. | ``client.quotes.archive(Identifier="Q0001")`` |
| `sort_lines(Identifier=..., LineNumbers=[...])` | Reorder lines. | ``client.quotes.sort_lines(Identifier="Q0001", LineNumbers=[2,1])`` |
| `price_quote_line_add(Identifier=..., PriceQuoteLine={...})` | Add a price quote line. | ``client.quotes.price_quote_line_add(Identifier="Q0001", PriceQuoteLine={"Description":"Support","PriceExcl":25})`` |
| `price_quote_line_delete(Identifier=..., LineNumber=...)` | Delete a price quote line. | ``client.quotes.price_quote_line_delete(Identifier="Q0001", LineNumber=1)`` |
| `attachment_add(Identifier=..., FileName=..., FileData=...)` | Add attachment to a quote. | ``client.quotes.attachment_add(Identifier="Q0001", FileName="terms.pdf", FileData="<base64>")`` |
| `attachment_delete(Identifier=..., AttachmentGuid=...)` | Remove a quote attachment. | ``client.quotes.attachment_delete(Identifier="Q0001", AttachmentGuid="ATT-9")`` |
| `attachment_download(Identifier=..., AttachmentGuid=...)` | Download a quote attachment. | ``client.quotes.attachment_download(Identifier="Q0001", AttachmentGuid="ATT-9")`` |
 
## tasks

| Method | Description | Example |
|---|---|---|
| `list(limit=..., offset=...)` | List tasks. | ``client.tasks.list(limit=100)`` |
| `show(Identifier=...)` | Get a task. | ``client.tasks.show(Identifier="T1")`` |
| `create(...)` | Create a task. | ``client.tasks.create(DebtorCode="DB10000", Subject="Call back")`` |
| `edit(Identifier=..., ...)` | Update a task. | ``client.tasks.edit(Identifier="T1", Status="completed")`` |
| `delete(Identifier=...)` | Delete a task. | ``client.tasks.delete(Identifier="T1")`` |
| `change_status(Identifier=..., Status=...)` | Change task status. | ``client.tasks.change_status(Identifier="T1", Status="completed")`` |
| `attachment_add(Identifier=..., FileName=..., FileData=...)` | Add task attachment. | ``client.tasks.attachment_add(Identifier="T1", FileName="note.txt", FileData="<base64>")`` |
| `attachment_delete(Identifier=..., AttachmentGuid=...)` | Remove task attachment. | ``client.tasks.attachment_delete(Identifier="T1", AttachmentGuid="A1")`` |
| `attachment_download(Identifier=..., AttachmentGuid=...)` | Download task attachment. | ``client.tasks.attachment_download(Identifier="T1", AttachmentGuid="A1")`` |

## transactions

| Method | Description | Example |
|---|---|---|
| `list(limit=..., offset=...)` | List transactions. | ``client.transactions.list(limit=100)`` |
| `show(Identifier=...)` | Get a transaction. | ``client.transactions.show(Identifier="TR1")`` |
| `create(...)` | Create a transaction. | ``client.transactions.create(...)`` |
| `edit(Identifier=..., ...)` | Update a transaction. | ``client.transactions.edit(Identifier="TR1", ...)`` |
| `delete(Identifier=...)` | Delete a transaction. | ``client.transactions.delete(Identifier="TR1")`` |
| `match(Identifier=...)` | Match a transaction. | ``client.transactions.match(Identifier="TR1")`` |
| `ignore(Identifier=...)` | Ignore a transaction. | ``client.transactions.ignore(Identifier="TR1")`` |

## Enums appendix

These enums are provided for clarity around action names. In code, you usually call resource methods directly.

### Generic `Action`
- LIST, SHOW, ADD, EDIT, DELETE
- SEND_BY_EMAIL, DOWNLOAD, SCHEDULE, CANCEL_SCHEDULE, SORT_LINES
- ATTACHMENT_ADD, ATTACHMENT_DELETE, ATTACHMENT_DOWNLOAD

### `QuoteAction`
- SEND_BY_EMAIL, DOWNLOAD, SCHEDULE, CANCEL_SCHEDULE, ACCEPT, DECLINE, ARCHIVE, SORT_LINES
- PRICE_QUOTE_LINE_ADD, PRICE_QUOTE_LINE_DELETE

### `DebtorAction`
- EXTRA_CLIENT_CONTACT_ADD, EXTRA_CLIENT_CONTACT_EDIT, EXTRA_CLIENT_CONTACT_DELETE

### `TaskAction`
- CHANGE_STATUS

### `TransactionAction`
- MATCH, IGNORE