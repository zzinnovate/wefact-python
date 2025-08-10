# Resources and operations

The client exposes Python resources that map to WeFact controllers. Methods accept keyword arguments which are posted as form data. Responses are JSON objects; most detail responses are nested under the controller name (e.g., `{"invoice": {...}}`).

Notation: args shown are common/illustrative; consult WeFact’s API for full parameter matrices.

## invoices

- list(limit=..., offset=...)
- show(Identifier=...)
- create(DebtorCode=..., InvoiceLines=[...])
- edit(Identifier=..., ...)
- delete(Identifier=...)
- credit(...), part_payment(...)
- mark_as_paid(...), mark_as_unpaid(...)
- send_by_email(...), send_reminder_by_email(...), send_summation_by_email(...)
- download(...)
- block(...), unblock(...)
- schedule(...), cancel_schedule(...)
- payment_process_pause(...), payment_process_reactivate(...)
- sort_lines(...), invoice_line_add(...), invoice_line_delete(...)
- attachment_add(...), attachment_delete(...), attachment_download(...)

Example:

```python
client.invoices.create(
  DebtorCode="DB10000",
  InvoiceLines=[{"Number": 1, "ProductCode": "P0001", "Description": "Service", "PriceExcl": 100}],
)
```

## debtors

- list(...), show(...), create(...), edit(...)
- delete: not available (raises ClientError)

## creditors

- list(...), show(...), create(...), edit(...), delete(...)

## products

- list(...), show(...), create(ProductName=..., ProductKeyPhrase=..., PriceExcl=...), edit(...), delete(...)

## groups

- list(...), show(...), create(Type=..., GroupName=...), edit(...), delete(...)

## subscriptions

- list(...), show(...), create(...), edit(...)
- delete: not available (raises ClientError)
- terminate(Identifier=...)

## settings

- list(...)
- show/create/edit/delete: not available (raise ClientError)

## cost_categories

Note: controller differs; methods map to specific costcategory actions.

- list(...), show(...), create(...), edit(...), delete(...)

Example:

```python
client.cost_categories.create(Title="Cloud costs")
```