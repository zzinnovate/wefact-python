"""Transaction resource for WeFact API."""

from .base import BaseResource
from ..enums.transaction_actions import TransactionAction


class TransactionResource(BaseResource):
    """
    Transaction resource for managing bank transactions.
    
    Supports CRUD operations, matching to invoices, and ignoring transactions.
    """
    
    controller_name = "transaction"

    def match(self, **params):
        """
        Match a transaction to one or more invoices.
        
        Args:
            Identifier: Required
            InvoiceIdentifiers: Required (array of invoice IDs)
            
        Returns:
            Matched transaction details
        """
        return self._send_request(
            self.controller_name, TransactionAction.MATCH.value, params
        )

    def ignore(self, **params):
        """
        Mark a transaction as ignored.
        
        Args:
            Identifier: Required
            
        Returns:
            Ignored transaction details
        """
        return self._send_request(
            self.controller_name, TransactionAction.IGNORE.value, params
        )
