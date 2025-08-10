# File: /wefact-python/wefact-python/examples/list_invoices.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dotenv import load_dotenv
from wefact import WeFact

load_dotenv()
api_key = os.getenv('WEFACT_API_KEY')

if not api_key:
    print("Error: API_KEY not found in .env file.")
    exit(1)

client = WeFact(api_key)

def list_invoices():
    try:
        response = client.invoices.list()
        if 'invoices' in response:
            for invoice in response['invoices']:
                print(f"Invoice Code: {invoice.get('InvoiceCode')}, Amount: {invoice.get('Amount')}, Status: {invoice.get('Status')}")
        else:
            print("No invoices found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    list_invoices()