"""Version info for pyvista-examples.

On the ``main`` branch, use 'dev' to denote a development version.
For example:

version_info = 0, 27, 0, now.year, now.month, now.day, now.hour, now.minute, now.second

When generating pre-release wheels, use '0rcN', for example:

version_info = 0, 28, '0rc1'

Denotes the first release candidate.

"""
import datetime

now = datetime.datetime.now()

# major, minor, patch
version_info = 0, 1, 2

# Nice string for the version
__version__ = '.'.join(map(str, version_info))
