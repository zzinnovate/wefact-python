# WeFact API Testing CLI

An interactive command-line tool for testing the WeFact API endpoints. Built with Rich for a beautiful terminal experience.

## Features

✨ **Interactive TUI** - Navigate with keyboard shortcuts
🧪 **Comprehensive Testing** - Test all 12 WeFact API endpoints
📊 **Rich Visualizations** - Beautiful tables, progress bars, and panels
🎲 **Dummy Data Generation** - Create realistic test data automatically
⚙️ **Smart Configuration** - Automatic .env management
📈 **Performance Metrics** - Track response times and success rates

## Installation

The CLI tool is included with the wefact-python package. Install dependencies:

```bash
poetry install
```

Or with pip:

```bash
pip install rich textual faker pydantic python-dotenv
```

## Quick Start

Run the CLI tool:

```bash
# Using poetry
poetry run wefact-test

# Or directly with Python
python -m wefact_cli

# Or if installed globally
wefact-test
```

## Usage

### First Time Setup

1. **API Key**: The tool will prompt for your WeFact API key on first run
   - Enter your API key when prompted
   - It will be saved to `.env` automatically

2. **Dummy Data**: You'll be asked if you want to create test data
   - Creates 5 test items per endpoint (debtors, products, invoices, etc.)
   - IDs are saved to `.env` for future reference
   - Can be cleared later via the menu

### Main Menu Options

```
1. Test All Endpoints    - Run comprehensive test suite
2. Test Specific Endpoint - Select and test individual endpoint  
3. Initialize Dummy Data  - Create test data for all endpoints
4. View Dummy Data       - Display created test data IDs
5. Clear Dummy Data      - Remove all test data from API
6. Settings              - View and update configuration
7. Exit                  - Exit the application
```

### Testing Endpoints

When testing a specific endpoint:

1. Select the endpoint from the list (invoices, debtors, products, etc.)
2. Choose an action:
   - **Test All** - Run all basic tests (list, show)
   - **Specific method** - Test individual operations

### Dummy Data

The tool generates realistic Dutch test data using Faker:

- **Debtors**: 5 Dutch companies with addresses
- **Products**: Common SaaS products (hosting, domains, etc.)
- **Creditors**: 5 vendor records
- **Groups**: Customer and product groups
- **Invoices**: 5 test invoices
- **Quotes**: 5 price quotes
- **Subscriptions**: 5 recurring subscriptions
- **Interactions**: Customer interaction logs
- **Tasks**: 5 sample tasks
- **Cost Categories**: Expense categories

All created items are tracked in your `.env` file.

## Configuration

Configuration is stored in `.env`:

```properties
# Required
WEFACT_API_KEY=your_api_key_here

# Optional
WEFACT_API_URL=https://api.mijnwefact.nl/v2/

# Dummy data tracking (auto-managed)
WEFACT_DUMMY_DATA_INITIALIZED=true
DUMMY_DEBTOR_IDS=DB10001,DB10002,DB10003,DB10004,DB10005
DUMMY_PRODUCT_IDS=P0001,P0002,P0003,P0004,P0005
# ... etc
```

## Architecture

```
wefact_cli/
├── __init__.py          # Package initialization
├── __main__.py          # Entry point
├── cli.py               # Main CLI application
├── config.py            # Configuration management
├── dummy_data.py        # Dummy data generator
├── test_runner.py       # Test execution engine
├── ui/                  # Rich UI components
│   ├── prompts.py       # Interactive prompts
│   ├── tables.py        # Table formatters
│   └── panels.py        # Panel components
├── utils/               # Utilities
│   ├── env_handler.py   # .env read/write
│   ├── validators.py    # Input validation
│   └── formatters.py    # Output formatting
└── endpoints/           # Endpoint testers
    └── base_tester.py   # Generic tester base class
```

## Testing Workflow

1. **Initialize** - Set up API key and dummy data
2. **Test** - Run tests on endpoints
3. **Review** - Check results with color-coded output
4. **Iterate** - Test specific endpoints or methods
5. **Clean** - Clear dummy data when done

## Example Session

```
╭─────────────────────────────────────────╮
│  WeFact API Testing Tool v1.0          │
│  Interactive API Endpoint Tester        │
╰─────────────────────────────────────────╯

✓ API Key found in .env
? Dummy data not initialized. Create test data? Yes

Initializing dummy data...
  ✓ Created 5 debtors
  ✓ Created 5 products  
  ✓ Created 5 creditors
  ...

╭─────────── Main Menu ───────────╮
│ 1. Test All Endpoints           │
│ 2. Test Specific Endpoint       │
│ 3. View Dummy Data              │
│ 4. Clear Dummy Data             │
│ 5. Settings                     │
│ 6. Exit                         │
╰─────────────────────────────────╯

Select option: 2

Select Endpoint:
  1. Invoices
  2. Debtors
  3. Products
  ...

Testing invoices...
╭─────────── Test Results ───────────╮
│ Method    Status    Duration      │
├─────────────────────────────────────┤
│ list      ✓ PASS    245ms         │
│ show      ✓ PASS    182ms         │
╰─────────────────────────────────────╯
```

## Tips

- Use **Test All** first to validate your API connection
- The tool uses **read-only tests** by default (list, show)
- Dummy data is **safe to create and delete**
- Check **Settings** to verify your configuration
- Press **Ctrl+C** to interrupt long operations

## Troubleshooting

### API Key Issues
- Verify key in WeFact account settings
- Check `.env` file format
- Ensure no extra spaces in API key

### Connection Errors
- Check internet connection
- Verify API URL is correct
- Check WeFact API status

### Dummy Data Errors
- Some endpoints may reject duplicate data
- Clear and reinitialize if needed
- Check WeFact account limits

## Development

To extend the CLI with custom testers:

1. Create a new file in `wefact_cli/endpoints/`
2. Inherit from `BaseEndpointTester`
3. Add endpoint-specific test methods
4. Register in `TestRunner._get_tester()`

## License

MIT - Same as wefact-python package
