# /wefact-python/wefact-python/tests/test_invoices.py

import pytest
from wefact import WeFact

@pytest.fixture
def client():
    return WeFact(api_key='your_api_key')

def test_list_invoices(client, mocker):
    mock_response = {'invoices': []}
    mocker.patch('wefact.request.requests.post', return_value=type('R', (), {
        'status_code': 200,
        'json': staticmethod(lambda: mock_response)
    })())
    response = client.invoices.list()
    assert isinstance(response, dict)
    assert 'invoices' in response

def test_create_invoice(client, mocker):
    mock_response = {'status': 'success', 'invoice': {'Identifier': 'INV10000'}}
    mocker.patch('wefact.request.requests.post', return_value=type('R', (), {
        'status_code': 200,
        'json': staticmethod(lambda: mock_response)
    })())
    response = client.invoices.create(
        DebtorCode='DB10000',
        InvoiceLines=[{'Number': 1, 'ProductCode': 'P0001', 'Description': 'Test Product', 'PriceExcl': 100}],
    )
    assert response['status'] == 'success'
    assert 'invoice' in response

def test_show_invoice(client, mocker):
    invoice_id = 'INV10000'
    mock_response = {'status': 'success', 'invoice': {'Identifier': invoice_id}}
    mocker.patch('wefact.request.requests.post', return_value=type('R', (), {
        'status_code': 200,
        'json': staticmethod(lambda: mock_response)
    })())
    response = client.invoices.show(Identifier=invoice_id)
    assert response['status'] == 'success'
    assert response['invoice']['Identifier'] == invoice_id

def test_update_invoice(client, mocker):
    invoice_id = 'INV10000'
    mock_response = {'status': 'success'}
    mocker.patch('wefact.request.requests.post', return_value=type('R', (), {
        'status_code': 200,
        'json': staticmethod(lambda: mock_response)
    })())
    response = client.invoices.edit(
        Identifier=invoice_id,
        InvoiceLines=[{'Number': 1, 'ProductCode': 'P0001', 'Description': 'Updated Product', 'PriceExcl': 150}],
    )
    assert response['status'] == 'success'

def test_delete_invoice(client, mocker):
    invoice_id = 'INV10000'
    mock_response = {'status': 'success'}
    mocker.patch('wefact.request.requests.post', return_value=type('R', (), {
        'status_code': 200,
        'json': staticmethod(lambda: mock_response)
    })())
    response = client.invoices.delete(Identifier=invoice_id)
    assert response['status'] == 'success'