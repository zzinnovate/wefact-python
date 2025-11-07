# Using WeFact Utility Functions Example

"""
This example demonstrates how to use the utility functions provided by the WeFact package
for common tasks like handling file attachments and formatting dates.
"""

from datetime import datetime, timedelta
from wefact import (
    WeFact,
    convert_to_base64,
    decode_base64_to_file,
    format_date_for_api,
    format_datetime_for_api
)

# Initialize the WeFact client
api_key = 'your-api-key'
client = WeFact(api_key)

# Example 1: Adding an attachment to an invoice using convert_to_base64
print("=== Example 1: Adding an Attachment ===")
invoice_id = 123  # Replace with actual invoice ID
file_path = "document.pdf"  # Replace with actual file path

# Convert file to base64 (handles file reading and encoding)
base64_content = convert_to_base64(file_path)

response = client.invoices.attachment_add(
    ReferenceIdentifier=invoice_id,
    Filename="document.pdf",
    Base64=base64_content
)
print(f"Attachment added: {response['status']}")

# Example 2: Downloading an invoice PDF and saving it
print("\n=== Example 2: Downloading an Invoice ===")
download_response = client.invoices.download(Identifier=invoice_id)

# The response contains Base64 encoded PDF
if 'Base64' in download_response:
    # Decode and save to file
    decode_base64_to_file(download_response['Base64'], "downloaded_invoice.pdf")
    print("Invoice saved to downloaded_invoice.pdf")

# Example 3: Marking an invoice as paid with formatted date
print("\n=== Example 3: Mark Invoice as Paid ===")
# Use today's date
pay_date = format_date_for_api(datetime.now())

response = client.invoices.mark_as_paid(
    Identifier=invoice_id,
    PayDate=pay_date
)
print(f"Invoice marked as paid on {pay_date}")

# Example 4: Scheduling an invoice to be sent tomorrow
print("\n=== Example 4: Schedule Invoice ===")
# Schedule for tomorrow at 10:00 AM
tomorrow = datetime.now() + timedelta(days=1)
tomorrow_10am = tomorrow.replace(hour=10, minute=0, second=0)
scheduled_time = format_datetime_for_api(tomorrow_10am)

response = client.invoices.schedule(
    Identifier=invoice_id,
    ScheduledAt=scheduled_time
)
print(f"Invoice scheduled for {scheduled_time}")

# Example 5: Pausing payment process with end date
print("\n=== Example 5: Pause Payment Process ===")
# Pause until 30 days from now
pause_until = datetime.now() + timedelta(days=30)
pause_end_date = format_date_for_api(pause_until)

response = client.invoices.payment_process_pause(
    Identifier=invoice_id,
    EndDate=pause_end_date
)
print(f"Payment process paused until {pause_end_date}")

print("\n=== All Examples Completed ===")
