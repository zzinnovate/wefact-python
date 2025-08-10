# Errors and exceptions

The client raises specific exceptions based on HTTP response codes and transport conditions. All exceptions inherit from `WeFactAPIError`.

## Exception classes

- AuthenticationError → 401 Invalid API key
- NotFoundError → 404 Endpoint not found
- ValidationError → 4xx with body indicating validation/problem details
- ClientError → network issues and other client-side failures
- ServerError → 5xx responses

## Handling

```python
from wefact import WeFact
from wefact.exceptions import (
    AuthenticationError,
    NotFoundError,
    ValidationError,
    ClientError,
    ServerError,
)

client = WeFact(api_key="...")

try:
    client.invoices.list()
except AuthenticationError:
    print("Invalid API key")
except NotFoundError:
    print("Endpoint not found")
except ValidationError as e:
    print(f"Bad request: {e}")
except (ClientError, ServerError) as e:
    print(f"Transport/server error: {e}")
```