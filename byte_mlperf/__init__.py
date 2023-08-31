import sys
from packaging.version import parse

from .version import __version__

python3_minimum_version = '3.6.0'

assert (sys.version_info < (3,6), \
    f'Please install python>={python3_minimum_version}.'

__all__ = ['__version__']
