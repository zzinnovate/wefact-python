# This file initializes the WeFact package and can include package-level documentation.

from .version import __version__
from .wefact import WeFact

__all__ = [
    '__version__',
    'WeFact',
]