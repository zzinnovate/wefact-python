from __future__ import annotations

import requests
from typing import Any, Dict

from .exceptions import (
    ClientError,
    ServerError,
    AuthenticationError,
    NotFoundError,
    ValidationError,
    raise_for_response,
    raise_for_wefact_payload,
)

class RequestMixin:
    api_key: str
    api_url: str

    def _send_request(self, controller: str, action: str, params: Dict[str, Any]) -> Dict[str, Any]:
        payload = {
            'api_key': self.api_key,
            'controller': controller,
            'action': action,
            **params,
        }
        try:
            response = requests.post(self.api_url, data=payload)
        except requests.RequestException as e:
            # Network/transport error
            raise ClientError(str(e)) from e

        # Raise on HTTP-level errors
        if not (200 <= int(getattr(response, 'status_code', 0)) < 300):
            raise_for_response(response)

        # Parse JSON
        try:
            data = response.json()
        except ValueError as e:
            raise ValidationError('Invalid JSON response') from e

        # Align with WeFact: status=='error' indicates an application-level error
        raise_for_wefact_payload(response, data)
        return data
