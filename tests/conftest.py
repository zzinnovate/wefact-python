# tests/conftest.py

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