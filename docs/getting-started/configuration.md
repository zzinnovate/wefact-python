# Configuration

The client needs an API key. The API URL defaults to `https://api.mijnwefact.nl/v2/`, but can be overridden.

## Environment variables

Recommended for production:

```
WEFACT_API_KEY=your_api_key
```

Load and use:

```python
import os
from wefact import WeFact

client = WeFact(api_key=os.getenv("WEFACT_API_KEY"))
```

## Explicit configuration for testing or scripts

```python
from wefact import WeFact

client = WeFact(api_key="your_api_key")
```

## Override API URL (optional)

Only needed for testing or custom WeFact installations:

```python
from wefact import WeFact

client = WeFact(
    api_key="your_api_key",
    api_url="https://custom.wefact.url/v2/"
)
```