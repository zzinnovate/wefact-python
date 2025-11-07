# Add Attachment Example for WeFact API Wrapper

# This script demonstrates how to add an attachment to an invoice using the WeFact API wrapper.

from wefact import WeFact, convert_to_base64

# Initialize the WeFact client with your API key
api_key = 'your-api-key'
we_fact_client = WeFact(api_key)

# Define the parameters for the attachment
invoice_id = 'your-invoice-id'  # Replace with your actual invoice ID
filename = 'example_attachment.pdf'  # Path to the file to be uploaded

# Convert the file to base64
base64_content = convert_to_base64(filename)

# Add the attachment to the invoice
try:
    response = we_fact_client.invoices.attachment_add(
        ReferenceIdentifier=invoice_id,
        Filename=filename,
        Base64=base64_content
    )
    print("Attachment added successfully:", response)
except Exception as e:
    print("An error occurred while adding the attachment:", str(e))