# tests/conftest.py

import pathlib
import pytest
from wefact import WeFact

@pytest.fixture(scope="session")
def api_client():
    client = WeFact(api_key="your_api_key_here")
    yield client

@pytest.fixture
def sample_creditor():
    return {
        "CompanyName": "Sample Company",
        "SurName": "Sample Surname"
    }

@pytest.fixture
def sample_invoice():
    return {
        "DebtorCode": "DB10000",
        "InvoiceLines": [
            {
                "Number": 1,
                "ProductCode": "P0001",
                "Description": "Sample Product",
                "PriceExcl": 100
            }
        ]
    }


def pytest_collection_modifyitems(session, config, items):
    """Fail collection if any project modules contain syntax errors.

    Compiles all .py files under the main package directories to catch
    indentation/syntax issues that might not be imported by specific tests.
    """
    project_root = pathlib.Path(__file__).parents[1]
    # Directories to check for syntax validity
    to_check = [
        project_root / "wefact",
    ]

    for base in to_check:
        if not base.exists():
            continue
        for py_file in base.rglob("*.py"):
            source = py_file.read_text(encoding="utf-8")
            try:
                compile(source, str(py_file), "exec")
            except SyntaxError as e:
                # Raise a collection error with a readable message
                raise pytest.UsageError(
                    f"Syntax error in {py_file}: {e.msg} at line {e.lineno}"
                )