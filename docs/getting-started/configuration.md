# Configuration

The client needs an API key and (optionally) a base URL. The default base URL is `https://api.mijnwefact.nl/v2/`.

## Environment variables

Recommended for production-like environments:

```
WEFACT_API_KEY=your_api_key
WEFACT_BASE_URL=https://api.mijnwefact.nl/v2/
```

Load and use:

```python
import os
from wefact import WeFact

client = WeFact(api_key=os.getenv("WEFACT_API_KEY"))
```

## Explicit configuration

```python
from wefact import WeFact

client = WeFact(
  api_key="your_api_key",
  api_url="https://api.mijnwefact.nl/v2/",  # optional override
)
```