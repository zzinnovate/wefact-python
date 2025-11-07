"""Interaction resource for WeFact API."""

from .base import BaseResource
from ..enums import Action
from ..enums.interaction_actions import InteractionAction


class InteractionResource(BaseResource):
    """
    Interaction resource for managing communications and interactions.
    
    Supports CRUD operations and attachments.
    """
    
    controller_name = "interaction"

    # Attachments
    def attachment_add(self, **params):
        """
        Add an attachment to an interaction.
        
        Args:
            ReferenceIdentifier: Required
            Filename: Required
            Base64: Required (base64 encoded file)
            
        Returns:
            Success confirmation
        """
        return self._send_request(
            self.controller_name, InteractionAction.ATTACHMENT_ADD.value, params
        )

    def attachment_delete(self, **params):
        """
        Delete an attachment from an interaction.
        
        Args:
            ReferenceIdentifier: Required
            Identifier or Filename: Required
            
        Returns:
            Success confirmation
        """
        return self._send_request(
            self.controller_name, InteractionAction.ATTACHMENT_DELETE.value, params
        )

    def attachment_download(self, **params):
        """
        Download an interaction attachment.
        
        Args:
            ReferenceIdentifier: Required
            Filename: Required
            
        Returns:
            Response with Base64 encoded file
        """
        return self._send_request(
            self.controller_name, InteractionAction.ATTACHMENT_DOWNLOAD.value, params
        )
