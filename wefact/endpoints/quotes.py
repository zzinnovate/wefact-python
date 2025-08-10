# Thin endpoint wrapper for Quotes (price quotes)
# Prefer using `WeFact().quotes` resource for full capabilities.

from wefact.endpoints.base import BaseEndpoint

class Quotes(BaseEndpoint):
    def list(self, **kwargs):
        return self.client._send_request("pricequote", "list", kwargs)

    def show(self, **kwargs):
        return self.client._send_request("pricequote", "show", kwargs)

    def create(self, **kwargs):
        return self.client._send_request("pricequote", "add", kwargs)

    def edit(self, **kwargs):
        return self.client._send_request("pricequote", "edit", kwargs)

    def delete(self, **kwargs):
        return self.client._send_request("pricequote", "delete", kwargs)

    def send_by_email(self, **kwargs):
        return self.client._send_request("pricequote", "sendbyemail", kwargs)

    def download(self, **kwargs):
        return self.client._send_request("pricequote", "download", kwargs)

    def schedule(self, **kwargs):
        return self.client._send_request("pricequote", "schedule", kwargs)

    def cancel_schedule(self, **kwargs):
        return self.client._send_request("pricequote", "cancelschedule", kwargs)

    def accept(self, **kwargs):
        return self.client._send_request("pricequote", "accept", kwargs)

    def decline(self, **kwargs):
        return self.client._send_request("pricequote", "decline", kwargs)

    def archive(self, **kwargs):
        return self.client._send_request("pricequote", "archive", kwargs)

    def sort_lines(self, **kwargs):
        return self.client._send_request("pricequote", "sortlines", kwargs)

    def price_quote_line_add(self, **kwargs):
        return self.client._send_request("pricequote", "pricequotelineadd", kwargs)

    def price_quote_line_delete(self, **kwargs):
        return self.client._send_request("pricequote", "pricequotelinedelete", kwargs)

    def attachment_add(self, **kwargs):
        kwargs["Type"] = "pricequote"
        return self.client._send_request("pricequote", "attachmentadd", kwargs)

    def attachment_delete(self, **kwargs):
        kwargs["Type"] = "pricequote"
        return self.client._send_request("pricequote", "attachmentdelete", kwargs)

    def attachment_download(self, **kwargs):
        kwargs["Type"] = "pricequote"
        return self.client._send_request("pricequote", "attachmentdownload", kwargs)
