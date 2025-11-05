"""Debtor (client/customer) resource for WeFact API."""

from .base import BaseResource
from ..enums import Action
from ..enums.debtor_actions import DebtorAction
from ..exceptions import ClientError


class DebtorResource(BaseResource):
    """
    Debtor resource for managing clients/customers.
    
    Supports CRUD operations, extra contacts, and attachments.
    Note: Delete is not available for debtors.
    """
    
    controller_name = "debtor"

    def delete(self, **params):
        """Delete is not available for debtors."""
        raise ClientError("delete is not available for this resource.")

    # Extra client contact management
    
    def extra_client_contact_add(self, **params):
        """
        Add an extra contact person to a debtor.
        
        Args:
            Identifier or DebtorCode: Required
            EmailAddress: Required
            FirstName: Optional
            LastName: Optional
            Gender: Optional ('m' or 'f')
            TelephoneNumber: Optional
            
        Returns:
            Debtor with new contact added
        """
        return self._send_request(
            self.controller_name, DebtorAction.EXTRA_CLIENT_CONTACT_ADD.value, params
        )

    def extra_client_contact_edit(self, **params):
        """
        Edit an extra contact person.
        
        Args:
            Identifier or DebtorCode: Required
            ContactIdentifier: Required
            EmailAddress: Optional
            FirstName: Optional
            LastName: Optional
            Gender: Optional
            TelephoneNumber: Optional
            
        Returns:
            Debtor with updated contact
        """
        return self._send_request(
            self.controller_name, DebtorAction.EXTRA_CLIENT_CONTACT_EDIT.value, params
        )

    def extra_client_contact_delete(self, **params):
        """
        Delete an extra contact person.
        
        Args:
            Identifier or DebtorCode: Required
            ContactIdentifier: Required
            
        Returns:
            Debtor with contact removed
        """
        return self._send_request(
            self.controller_name, DebtorAction.EXTRA_CLIENT_CONTACT_DELETE.value, params
        )

    # Attachments
    
    def attachment_add(self, **params):
        """
        Add an attachment to a debtor.
        
        Args:
            ReferenceIdentifier or DebtorCode: Required
            Filename: Required
            Base64: Required (base64 encoded file)
            
        Returns:
            Success confirmation
        """
        params["Type"] = self.controller_name
        return self._send_request(
            self.controller_name, Action.ATTACHMENT_ADD.value, params
        )

    def attachment_delete(self, **params):
        """
        Delete an attachment from a debtor.
        
        Args:
            ReferenceIdentifier or DebtorCode: Required
            Identifier or Filename: Required
            
        Returns:
            Success confirmation
        """
        params["Type"] = self.controller_name
        return self._send_request(
            self.controller_name, Action.ATTACHMENT_DELETE.value, params
        )

    def attachment_download(self, **params):
        """
        Download a debtor attachment.
        
        Args:
            ReferenceIdentifier or DebtorCode: Required
            Filename: Required
            
        Returns:
            Response with Base64 encoded file
        """
        params["Type"] = self.controller_name
        return self._send_request(
            self.controller_name, Action.ATTACHMENT_DOWNLOAD.value, params
        )
