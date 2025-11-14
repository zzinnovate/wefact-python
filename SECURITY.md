# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in this library, please report it by emailing **hello@zzinnovate.com**. Include a clear description of the issue and steps to reproduce if possible.

We will review and respond to security reports promptly.

## Best Practices for Users

When using the WeFact Python Wrapper, follow these security guidelines:

### Protect Your API Keys

- **Never commit API keys** to version control or include them in your source code
- **Use environment variables** to store your WeFact API key (the library supports `.env` files via `python-dotenv`)
- **Limit API key permissions** to only what your application needs in the WeFact dashboard

### Keep Dependencies Updated

This library has minimal dependencies (`requests`, `pydantic`, `python-dotenv`, and a few utilities). We will regularly update to the latest version to receive security patches:

### Example: Secure API Key Usage

```python
import os
from wefact import WeFact

# Good: Load from environment variable
api_key = os.getenv('WEFACT_API_KEY')
client = WeFact(api_key=api_key)

# Bad: Hard-coded API key (never do this!)
# client = WeFact(api_key='your-secret-key-here')
```

## Supported Versions

We recommend always using the latest version. Security updates will be released as patch versions.