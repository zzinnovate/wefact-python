"""Thin endpoint wrapper for Interactions, aligning with the client resources.

Prefer using `WeFact().interactions` resource for full capabilities.
"""

from wefact.endpoints.base import BaseEndpoint


class Interactions(BaseEndpoint):
    def list(self, **kwargs):
        """List interactions.

        Accepts any supported filter/pagination kwargs as defined by the API.
        """
        return self.client._send_request("interaction", "list", kwargs)

    def show(self, **kwargs):
        """Show details of a single interaction.

        Expected identifiers in kwargs (e.g., Identifier).
        """
        return self.client._send_request("interaction", "show", kwargs)

    def create(self, **kwargs):
        """Create a new interaction.

        Provide required interaction fields via kwargs.
        """
        return self.client._send_request("interaction", "add", kwargs)

    def edit(self, **kwargs):
        """Edit an existing interaction.

        Include the Identifier and fields to update via kwargs.
        """
        return self.client._send_request("interaction", "edit", kwargs)

    def delete(self, **kwargs):
        """Delete an interaction.

        Provide the Identifier in kwargs.
        """
        return self.client._send_request("interaction", "delete", kwargs)

    # Attachments
    def attachment_add(self, **kwargs):
        """Add an attachment to an interaction.

        Requires Identifier and attachment data (e.g., Filename, Content/Base64, etc.).
        """
        kwargs["Type"] = "interaction"
        return self.client._send_request("interaction", "attachmentadd", kwargs)

    def attachment_delete(self, **kwargs):
        """Delete an attachment from an interaction.

        Requires Identifier and attachment reference (e.g., AttachmentIdentifier or Filename).
        """
        kwargs["Type"] = "interaction"
        return self.client._send_request("interaction", "attachmentdelete", kwargs)

    def attachment_download(self, **kwargs):
        """Download an interaction attachment.

        Requires Identifier and attachment reference (e.g., Filename). Returns file bytes.
        """
        kwargs["Type"] = "interaction"
        return self.client._send_request("interaction", "attachmentdownload", kwargs)
