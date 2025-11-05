"""
Example: Download an invoice as PDF

This example shows how to download an invoice as a PDF file.
The PDF will be saved to a 'downloads' folder in the current directory.

API Response format:
{
    'controller': 'invoice',
    'action': 'download',
    'status': 'success',
    'date': '2024-01-21T12:00:00+02:00',
    'invoice': {
        'Filename': 'Factuur-F2024-0001.pdf',
        'Base64': 'JVBERi0xLj...',  # Base64 encoded PDF
        'MimeType': 'application/pdf'
    }
}
"""

from wefact import WeFact
import base64
from pathlib import Path

# Initialize WeFact client
client = WeFact(api_key="your_api_key_here")

# Create downloads directory if it doesn't exist
downloads_dir = Path("downloads")
downloads_dir.mkdir(exist_ok=True)

# Get an invoice (replace with actual invoice code or identifier)
invoice_code = "F2024-001"

try:
    # Download invoice as PDF using InvoiceCode
    # You can also use: Identifier=123 instead
    response = client.invoices.download(InvoiceCode=invoice_code)
    
    # Check if download was successful and contains the PDF
    if response and 'invoice' in response and 'Base64' in response['invoice']:
        # Decode the base64 content
        pdf_content = base64.b64decode(response['invoice']['Base64'])
        
        # Get the filename from API or use invoice code
        filename = response['invoice'].get('Filename', f'{invoice_code}.pdf')
        
        # Save to downloads directory
        filepath = downloads_dir / filename
        filepath.write_bytes(pdf_content)
        
        print(f"✓ Invoice downloaded successfully!")
        print(f"  Saved to: {filepath.absolute()}")
        print(f"  File size: {len(pdf_content):,} bytes")
        print(f"  MIME type: {response['invoice'].get('MimeType', 'unknown')}")
    else:
        print("✗ No PDF content in response")
        print(f"  Response keys: {list(response.keys())}")
        if 'invoice' in response:
            print(f"  Invoice keys: {list(response['invoice'].keys())}")
        
except Exception as e:
    print(f"✗ Error downloading invoice: {e}")
