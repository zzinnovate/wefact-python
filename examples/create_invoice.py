# Create Invoice Example for WeFact API Wrapper

# This script demonstrates how to create an invoice using the WeFact API wrapper.

from wefact import WeFact

def create_invoice(api_key, debtor_code, invoice_lines):
    # Initialize the WeFact client with the provided API key
    client = WeFact(api_key)

    # Prepare the invoice data
    invoice_data = {
        'DebtorCode': debtor_code,
        'InvoiceLines': invoice_lines
    }

    # Create the invoice using the WeFact API
    response = client.invoices.create(**invoice_data)

    # Check the response status
    if response['status'] == 'success':
        print("Invoice created successfully!")
        print("Invoice details:", response['invoice'])
    else:
        print("Error creating invoice:", response['errors'])

if __name__ == "__main__":
    # Example usage
    API_KEY = 'your-api-key-here'
    DEBTOR_CODE = 'DB10000'
    INVOICE_LINES = [
        {
            'Number': 1,
            'ProductCode': 'P0001',
            'Description': 'Your product description',
            'PriceExcl': 100
        }
    ]

    create_invoice(API_KEY, DEBTOR_CODE, INVOICE_LINES)