# Changelog

All notable changes to this project will be documented in this file.

## [1.1.0] - 2025-08-10

**Added**

- Interactions API support:
	- New resource: `client.interactions` with `list`, `show`, `create`, `edit`, `delete`.
	- Attachment operations: `attachment_add`, `attachment_delete`, `attachment_download`.
	- New enum: `InteractionAction` (`attachmentadd`, `attachmentdelete`, `attachmentdownload`).

**Documentation**

- Endpoints page refactored to tables with descriptions and inline code examples.
- New Interactions section with CRUD and attachment examples.

**Tests**

- Added `tests/test_interactions.py` covering CRUD and attachment flows.
- Full suite passes locally.

**Internal**

- Exposed `interactions` on the `WeFact` client.
- Exported `InteractionAction` in `wefact.enums`.

## [1.0.0] - 2025-08-09

First release with the full API spec implemented.