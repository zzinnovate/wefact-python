# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0b1] - 2025-08-15

**Changed**

- Dropped support for Python 3.8, 3.9, 3.10. Minimum is now 3.11+ (project not yet published to PyPI, so this is a pre-release adjustment for longevity and access to newer typing features).
- Build backend requirement bumped to `poetry-core>=2.0.0,<3.0.0` in line with the new Python baseline.

**Note**

- If you need legacy Python versions prior to 3.11, pin to `wefact-python==1.2.0` (unpublished tag) or earlier commit.

## [1.0.0a4] - 2025-08-10

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

## [1.0.0a3] - 2025-08-10

**Changed**

- Moved cost category-specific action constants out of the generic `Action` enum.
	- New enum: `CostCategoryAction` in `wefact.enums.cost_category_actions` (also exported via `wefact.enums`).
	- Replace usages of `Action.COSTCATEGORY_*` with `CostCategoryAction.*`.

## [1.0.0a2] - 2025-08-10

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
 

## [1.0.0a1] - 2025-08-09

First release with the full API spec implemented.