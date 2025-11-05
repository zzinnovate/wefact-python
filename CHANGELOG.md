# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased] - 2025-11-05

**Added**

- **CreditInvoice API**: Complete support for purchase invoices (Inkoopfacturen)
  - New resource: `client.credit_invoices` with CRUD operations (`list`, `show`, `create`, `edit`, `delete`)
  - Payment operations: `part_payment`, `mark_as_paid`
  - Line management: `credit_invoice_line_add`, `credit_invoice_line_delete`
  - Attachments: `attachment_add`, `attachment_delete`, `attachment_download`
  - New enum: `CreditInvoiceAction` in `wefact.enums.credit_invoice_actions`
  - Tests: Added `tests/test_credit_invoices.py` with full coverage

**Changed**

- **Major Refactoring**: Modularized resources architecture
  - Split monolithic `wefact/resources.py` into individual files per resource
  - New structure: `wefact/resources/` directory with dedicated modules:
    - `base.py` - BaseResource with common CRUD operations
    - `invoice.py` - InvoiceResource (25 endpoints)
    - `credit_invoice.py` - CreditInvoiceResource (12 endpoints)
    - `debtor.py` - DebtorResource (10 endpoints)
    - `creditor.py` - CreditorResource (8 endpoints)
    - `product.py` - ProductResource (5 endpoints)
    - `quote.py` - QuoteResource (18 endpoints)
    - `subscription.py` - SubscriptionResource (5 endpoints)
    - `transaction.py` - TransactionResource (6 endpoints)
    - `task.py` - TaskResource (8 endpoints)
    - `interaction.py` - InteractionResource (7 endpoints)
    - `group.py` - GroupResource (5 endpoints)
    - `settings.py` - SettingsResource (1 endpoint)
    - `cost_category.py` - CostCategoryResource (5 endpoints)

- **Removed deprecated code**:
  - Deleted entire `wefact/endpoints/` directory (deprecated REST-style implementation)
  - Active implementation now uses controller/action pattern in `wefact/resources/`

**Documentation**

- Added `docs/implementation-complete.md` - comprehensive overview of all 13 resources and 115 API endpoints
- Added `docs/testing/invoice-endpoints.md` - complete invoice endpoint testing guide with state machine diagram
- Added `docs/api/parameters.md` - API parameters reference
- Updated `mkdocs.yml` navigation with new Testing and Implementation sections
- All resources now have detailed docstrings with parameter descriptions and return values

**Internal Improvements**

- Improved code documentation with method docstrings
- Better separation of concerns between different API resources
- Cleaner import structure in `wefact/resources/__init__.py`

**Coverage**

- **100% API Coverage**: All WeFact API v2 endpoints now implemented
- 13 resources covering all entity types
- 115 total API endpoints
- Complete CRUD support where applicable
- Full attachment support across all relevant resources

## [0.1.0b1] - 2025-08-15

**Changed**

- Dropped support for Python 3.8, 3.9, 3.10. Minimum is now 3.11+ (project not yet published to PyPI, so this is a pre-release adjustment for longevity and access to newer typing features).
- Build backend requirement bumped to `poetry-core>=2.0.0,<3.0.0` in line with the new Python baseline.

**Note**

- If you need legacy Python versions prior to 3.11, pin to `wefact-python==1.2.0` (unpublished tag) or earlier commit.

## [0.1.0a4] - 2025-08-10

**Added**

- Quotes API: full workflow on `client.quotes` (send_by_email, download, schedule, cancel_schedule, accept, decline, archive, sort_lines, price_quote_line_add/delete) plus attachments using generic `Action.ATTACHMENT_*`.
- Tasks API: `client.tasks` with CRUD, `change_status`, and attachments.
- Transactions API: `client.transactions` with CRUD, `match`, and `ignore`.
- Debtors: extra client contact operations (`extra_client_contact_add/edit/delete`) and attachments.
- Creditors: attachments operations.

**Enums**

- New: `DebtorAction`, `TaskAction`, `TransactionAction` (exported via `wefact.enums`).
- `Action` enum extended with generic attachment actions: `ATTACHMENT_ADD`, `ATTACHMENT_DELETE`, `ATTACHMENT_DOWNLOAD`.

**Docs**

- Endpoints docs: added Tasks and Transactions sections; documented Debtor extra contacts and attachments; Creditor attachments; added Enums appendix.

**Tests**

- Added unit tests for tasks, transactions, debtor extra contacts and attachments, and creditor attachments.
- Added a pytest collection-time syntax check to compile all modules and fail early on syntax errors.

## [0.1.0a3] - 2025-08-10

**Changed**

- Moved cost category-specific action constants out of the generic `Action` enum.
	- New enum: `CostCategoryAction` in `wefact.enums.cost_category_actions` (also exported via `wefact.enums`).
	- Replace usages of `Action.COSTCATEGORY_*` with `CostCategoryAction.*`.

## [0.1.0a2] - 2025-08-10

**Added**

- Interactions API support:
	- New resource: `client.interactions` with `list`, `show`, `create`, `edit`, `delete`.
	- Attachment operations: `attachment_add`, `attachment_delete`, `attachment_download`.
	- Attachment actions are now generic in `Action`; any previous Interaction-specific enum is obsolete and no longer exported.

**Documentation**

- Endpoints page refactored to tables with descriptions and inline code examples.
- New Interactions section with CRUD and attachment examples.

**Tests**

- Added `tests/test_interactions.py` covering CRUD and attachment flows.
- Full suite passes locally.

**Internal**

- Exposed `interactions` on the `WeFact` client.
 

## [0.1.0a1] - 2025-08-09

First release with the full API spec implemented.