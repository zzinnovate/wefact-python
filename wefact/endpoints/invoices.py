# File: /wefact-python/wefact-python/src/wefact/endpoints/invoices.py

from wefact.endpoints.base import BaseEndpoint

class Invoices(BaseEndpoint):
    def list(self, **kwargs):
        """List all invoices."""
        return self.get('invoices', params=kwargs)

    def list_all(self):
        """List all invoices and retrieve detailed information for each."""
        response = self.list()
        if 'invoices' in response:
            return [self.show(invoice['Identifier']) for invoice in response['invoices']]
        return []

    def create(self, debtor_code, invoice_lines, **kwargs):
        """Create a new invoice."""
        data = {
            'DebtorCode': debtor_code,
            'InvoiceLines': invoice_lines,
            **kwargs
        }
        return self.post('invoices', json=data)

    def edit(self, identifier, invoice_lines, **kwargs):
        """Update an existing invoice."""
        data = {
            'Identifier': identifier,
            'InvoiceLines': invoice_lines,
            **kwargs
        }
        return self.put('invoices', json=data)

    def show(self, identifier):
        """Show details of a specific invoice."""
        return self.get(f'invoices/{identifier}')

    def delete(self, identifier):
        """Delete a specific invoice."""
        return self.delete(f'invoices/{identifier}')

    def credit(self, identifier):
        """Credit a specific invoice."""
        return self.post(f'invoices/{identifier}/credit')

    def mark_as_paid(self, identifier):
        """Mark a specific invoice as paid."""
        return self.post(f'invoices/{identifier}/mark-as-paid')

    def mark_as_unpaid(self, identifier):
        """Mark a specific invoice as unpaid."""
        return self.post(f'invoices/{identifier}/mark-as-unpaid')

    def send_by_email(self, identifier):
        """Send a specific invoice by email."""
        return self.post(f'invoices/{identifier}/send-by-email')

    def download(self, identifier):
        """Download a specific invoice."""
        return self.get(f'invoices/{identifier}/download')

    def block(self, identifier):
        """Block a specific invoice."""
        return self.post(f'invoices/{identifier}/block')

    def unblock(self, identifier):
        """Unblock a specific invoice."""
        return self.post(f'invoices/{identifier}/unblock')

    def schedule(self, identifier, scheduled_at):
        """Schedule a specific invoice."""
        data = {
            'Identifier': identifier,
            'ScheduledAt': scheduled_at
        }
        return self.post(f'invoices/{identifier}/schedule', json=data)

    def cancel_schedule(self, identifier):
        """Cancel the schedule for a specific invoice."""
        return self.post(f'invoices/{identifier}/cancel-schedule')

    def add_line(self, identifier, invoice_lines):
        """Add a line to a specific invoice."""
        data = {
            'Identifier': identifier,
            'InvoiceLines': invoice_lines
        }
        return self.post(f'invoices/{identifier}/add-line', json=data)

    def delete_line(self, identifier, line_identifier):
        """Delete a line from a specific invoice."""
        data = {
            'Identifier': identifier,
            'LineIdentifier': line_identifier
        }
        return self.post(f'invoices/{identifier}/delete-line', json=data)

    def add_attachment(self, reference_identifier, attachment_data):
        """Add an attachment to a specific invoice."""
        data = {
            'ReferenceIdentifier': reference_identifier,
            **attachment_data
        }
        return self.post(f'invoices/{reference_identifier}/attachments', json=data)

    def delete_attachment(self, identifier, reference_identifier, attachment_type):
        """Delete an attachment from a specific invoice."""
        return self.delete(f'invoices/{reference_identifier}/attachments/{identifier}?type={attachment_type}')

    def download_attachment(self, reference_identifier, filename, attachment_type):
        """Download an attachment from a specific invoice."""
        return self.get(f'invoices/{reference_identifier}/attachments/{filename}?type={attachment_type}')