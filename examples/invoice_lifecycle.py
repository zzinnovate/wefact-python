#!/usr/bin/env python3
"""
Example: Invoice Lifecycle

This example demonstrates the complete invoice lifecycle using the WeFact API:
- Creating an invoice
- Sending it by email
- Marking it as paid
- Creating a credit invoice
- Downloading the PDF

"""

import os
from wefact import WeFact
from wefact.enums import InvoiceStatus

def main():
    # Load API key from environment
    api_key = os.getenv('WEFACT_API_KEY')
    if not api_key:
        print("❌ Please set WEFACT_API_KEY environment variable")
        return
    
    # Initialize client
    client = WeFact(api_key=api_key)
    
    print("=" * 60)
    print("Invoice Lifecycle Example")
    print("=" * 60)
    
    # Step 1: Create an invoice
    print("\n1. Creating invoice...")
    try:
        invoice_response = client.invoices.create(
            DebtorCode='DB10000',  # Replace with your test debtor
            InvoiceLines=[
                {
                    'Number': 1,
                    'ProductCode': 'P0001',  # Replace with your test product
                    'Description': 'Test Product',
                    'PriceExcl': 100.00
                }
            ]
        )
        
        if invoice_response['status'] == 'success':
            invoice = invoice_response['invoice']
            invoice_code = invoice['InvoiceCode']
            print(f"✓ Invoice created: {invoice_code}")
            print(f"  Status: {invoice.get('Status')} (Draft)")
        else:
            print("✗ Failed to create invoice")
            return
    except Exception as e:
        print(f"✗ Error: {e}")
        return
    
    # Step 2: Send invoice by email
    print("\n2. Sending invoice by email...")
    try:
        send_response = client.invoices.send_by_email(InvoiceCode=invoice_code)
        if send_response['status'] == 'success':
            print(f"✓ Invoice sent")
            print(f"  Status changed to: Sent")
        else:
            print("✗ Failed to send invoice")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Step 3: Mark invoice as paid
    print("\n3. Marking invoice as paid...")
    try:
        paid_response = client.invoices.mark_as_paid(InvoiceCode=invoice_code)
        if paid_response['status'] == 'success':
            print(f"✓ Invoice marked as paid")
            print(f"  Status changed to: Paid")
        else:
            print("✗ Failed to mark as paid")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Step 4: Download invoice PDF
    print("\n4. Downloading invoice PDF...")
    try:
        download_response = client.invoices.download(InvoiceCode=invoice_code)
        if download_response['status'] == 'success' and 'invoice' in download_response:
            filename = download_response['invoice'].get('Filename', f'{invoice_code}.pdf')
            print(f"✓ Invoice downloaded: {filename}")
            print(f"  (Base64 content available in response)")
        else:
            print("✗ Failed to download")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Step 5: Create credit invoice
    print("\n5. Creating credit invoice...")
    try:
        credit_response = client.invoices.credit(InvoiceCode=invoice_code)
        if credit_response['status'] == 'success':
            credit_invoice = credit_response['invoice']
            credit_code = credit_invoice['InvoiceCode']
            print(f"✓ Credit invoice created: {credit_code}")
        else:
            print("✗ Failed to create credit invoice")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Step 6: Show final invoice details
    print("\n6. Retrieving final invoice state...")
    try:
        final_response = client.invoices.show(InvoiceCode=invoice_code)
        if final_response['status'] == 'success':
            final_invoice = final_response['invoice']
            print(f"✓ Invoice: {invoice_code}")
            print(f"  Amount: €{final_invoice.get('AmountIncl', 0)}")
            print(f"  Status: {final_invoice.get('Status')}")
            print(f"  Credited: {'Yes' if final_invoice.get('Credited') else 'No'}")
        else:
            print("✗ Failed to retrieve invoice")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    print("\n" + "=" * 60)
    print("Invoice Lifecycle Complete")
    print("=" * 60)
    print(f"\nCreated invoice: {invoice_code}")
    print("Note: This created real data in your WeFact account.")


if __name__ == '__main__':
    main()
