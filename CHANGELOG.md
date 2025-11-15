# Changelog

All notable changes to this project will be documented in this file.

## [1.0.3] - 2025-11-15

### Changed

- Updated project homepage URL in package metadata to point to documentation site

## [1.0.2] - 2025-11-15

### Changed

- Minor documentation improvements in README

## [1.0.1] - 2025-11-15

### Changed

- Updated documentation to clarify what WeFact is (Dutch invoicing and accounting platform)
- Added PyPI availability notice to README and docs
- Improved project description for international users
- Added tip in usage docs explaining flexible identifier types (integer/string auto-conversion)

### Fixed

- Fixed deprecation warnings in `pyproject.toml` (license configuration)
- Auto-convert integer Identifier parameters to strings for better developer experience

## [1.0.0] - 2025-11-14

Initial release. Complete WeFact API v2 wrapper with zero dependencies beyond `requests`.

### Core Features

- 13 resources covering 115 API endpoints
- Type hints for IDE support
- Modular architecture
- Built-in utilities for common operations

### API Resources

- **Invoices** (25 endpoints) - Complete lifecycle management
- **Credit Invoices** (12 endpoints) - Purchase invoice handling
- **Debtors** (10 endpoints) - Customer management
- **Creditors** (8 endpoints) - Supplier management
- **Products** (5 endpoints) - Product catalog
- **Quotes** (18 endpoints) - Quotation workflow
- **Subscriptions** (5 endpoints) - Recurring billing
- **Transactions** (6 endpoints) - Bank transaction matching
- **Tasks** (8 endpoints) - Task management
- **Interactions** (7 endpoints) - Communication logging
- **Groups** (5 endpoints) - Contact organization
- **Cost Categories** (5 endpoints) - Expense categorization
- **Settings** (1 endpoint) - Account configuration

### Documentation

- API reference with code examples
- Invoice lifecycle guide
- CLI testing tool reference
- Configuration guide

### Testing & Quality

- 95% test coverage across 168 tests
- CI/CD pipeline for Python 3.11-3.14
- Interactive CLI tool for development
- Comprehensive error handling