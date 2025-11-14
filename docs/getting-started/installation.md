# Installation

## Requirements

- Python 3.11+

## Install

*(This library is not yet published on PyPI)*

```bash
# Basic installation (library only)
pip install wefact-python

# With CLI testing tool
pip install wefact-python[cli]

# For development (includes CLI, testing, and docs)
pip install -e ".[all]"
```

## From source

```bash
git clone https://github.com/zzinnovate/wefact-python.git
cd wefact-python

# Install with all development dependencies
pip install -e ".[all]"

# Or install specific groups
pip install -e ".[cli]"      # CLI testing tool only
pip install -e ".[dev]"      # Testing tools only
pip install -e ".[docs]"     # Documentation tools only
```

## Verify

```python
import wefact
print(wefact.__version__)
```

If you see a version string, the package is installed correctly.