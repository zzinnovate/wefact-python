# CLI Testing Tool

An interactive command-line tool for testing WeFact API endpoints during development. Useful for validating implementations, generating test data, and exploring API behavior.

!!! warning "Use with Development Environment Only"
    This tool creates real data in your WeFact environment. **Only use this with a development environment from WeFact.** Contact WeFact helpdesk to activate a development environment for testing purposes.

## Installation

The CLI tool is included in the development dependencies:

```bash
pip install -r requirements-dev.txt
```

## Usage

Run the CLI tool directly from the project root:

```bash
python -m wefact_cli
```

If you've installed the package in editable mode, you can also use:

```bash
wefact-test
```

## Project Structure

The CLI is organized into modules for testing, UI, and utilities:

```
wefact_cli/
├── __init__.py
├── __main__.py          # Entry point
├── cli.py               # Main application
├── config.py            # Configuration management
├── dummy_data.py        # Test data generator
├── test_runner.py       # Test execution
├── endpoints/
│   ├── __init__.py
│   └── base_tester.py   # Base test class
├── ui/
│   ├── __init__.py
│   ├── prompts.py       # Interactive prompts
│   ├── tables.py        # Table formatters
│   └── panels.py        # Panel components
└── utils/
    ├── __init__.py
    ├── env_handler.py   # Environment variables
    ├── validators.py    # Input validation
    └── formatters.py    # Response formatting
```

## Features

### API Key Management

The tool automatically loads your API key from `.env`:

```ini
WEFACT_API_KEY=your_api_key_here
```

If no key is found, you'll be prompted to enter one on first run.

### Test Data Generation

Generate dummy data for testing endpoints. Creates 5 items per resource type and stores IDs in `.env` for reference in tests.

Supported resources:
- Debtors (customers)
- Products
- Creditors (suppliers)
- Groups
- Invoices (requires product data)

Some resources may require specific WeFact plan features (CRM, etc.).

### Endpoint Testing

Test individual endpoints or run comprehensive test suites. Results include:
- Pass/fail status
- Execution timing
- Response validation
- Error details

### Interactive Interface

Built with Rich for terminal UI:
- Progress indicators
- Formatted tables
- Color-coded results
- Confirmation prompts

## Configuration

Configuration is stored in `.env` at the project root:

```ini
# API Configuration
WEFACT_API_KEY=your_api_key

# Test Data Tracking
WEFACT_DUMMY_DATA_INITIALIZED=true
DUMMY_DEBTOR_IDS=2,3,4,5,6
DUMMY_PRODUCT_IDS=2,3,4,5,6
DUMMY_CREDITOR_IDS=1,2,3,4,5
DUMMY_GROUP_IDS=1,2,3,4,5
```

## Extending the CLI

### Creating Endpoint Testers

Add endpoint-specific testers in `wefact_cli/endpoints/`:

```python
# wefact_cli/endpoints/invoices.py
from .base_tester import BaseEndpointTester

class InvoiceTester(BaseEndpointTester):
    def __init__(self, client):
        super().__init__(
            resource=client.invoices,
            resource_name="Invoice"
        )
    
    def test_mark_as_paid(self, identifier: str):
        """Test marking an invoice as paid."""
        result = self.resource.mark_as_paid(
            InvoiceCode=identifier
        )
        return self.validate_response(result)
    
    def test_send_email(self, identifier: str):
        """Test sending invoice by email."""
        result = self.resource.send_by_email(
            InvoiceCode=identifier
        )
        return self.validate_response(result)
```

### Wiring Into the CLI

Import and register in `test_runner.py`:

```python
from .endpoints.invoices import InvoiceTester

testers = {
    'invoices': InvoiceTester,
    'debtors': DebtorTester,
    # ... other testers
}
```

## Limitations

Some features require specific WeFact account capabilities:

- **CRM Features** - Interactions and Tasks require CRM activation
- **Cost Categories** - May not be available on all plans
- **Subscriptions** - Require valid debtor and product codes

The CLI handles unavailable features gracefully with warning messages.

## Dependencies

The CLI uses these packages (included in `requirements-dev.txt`):

- `rich` - Terminal formatting
- `textual` - TUI framework
- `faker` - Test data generation
- `pydantic` - Data validation
- `python-dotenv` - Environment variables

## Troubleshooting

**Module not found errors**

Ensure the virtual environment is activated and dependencies are installed:

```bash
pip install -r requirements-dev.txt
```

**API authentication errors**

Verify your API key in `.env` is valid and has the necessary permissions.

**Feature not available errors**

Some endpoints require specific WeFact plan features. Check your account capabilities.
