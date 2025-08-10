# File: /wefact-python/wefact-python/src/wefact/endpoints/credit_invoices.py

from .base import BaseEndpoint

class CreditInvoicesEndpoint(BaseEndpoint):
    def list(self):
        """List all credit invoices."""
        return self.get('credit_invoices')

    def create(self, invoice_data):
        """Create a new credit invoice.

        Required parameters: InvoiceCode, CreditorCode, InvoiceLines.
        """
        return self.post('credit_invoices', json=invoice_data)

    def edit(self, invoice_id, invoice_data):
        """Update an existing credit invoice.

        Required parameter: Identifier or CreditInvoiceCode.
        """
        return self.put(f'credit_invoices/{invoice_id}', json=invoice_data)

    def show(self, invoice_id):
        """Show details of a specific credit invoice.

        Required parameter: Identifier or CreditInvoiceCode.
        """
        return self.get(f'credit_invoices/{invoice_id}')

    def delete(self, invoice_id):
        """Delete a credit invoice.

        Required parameter: Identifier or CreditInvoiceCode.
        """
        return self.delete(f'credit_invoices/{invoice_id}')