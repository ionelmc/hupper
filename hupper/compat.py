# flake8: noqa
import imp
import importlib
import platform
import sys

PY2 = sys.version_info[0] == 2
WIN = sys.platform == 'win32'

OS64 = platform.machine().endswith('64')
PY64 = sys.maxsize > 2**32

if PY2:
    long = long
else:
    long = int

try:
    import queue
except ImportError:
    import Queue as queue

try:
    from _thread import interrupt_main
except ImportError:
    from thread import interrupt_main


try:
    import importlib.util as imputil
except ImportError:
    imputil = None

if imputil:
    get_pyc_path = imputil.cache_from_source
    get_py_path = imputil.source_from_cache

elif PY2:
    get_pyc_path = lambda path: path + 'c'
    get_py_path = lambda path: path[:-1]

# fallback on python < 3.5
else:
    get_pyc_path = imp.cache_from_source
    get_py_path = imp.source_from_cache


def is_watchdog_supported():
    """ Return ``True`` if watchdog is available."""
    try:
        import watchdog
    except ImportError:
        return False
    return True


################################################
# cross-compatible metaclass implementation
# Copyright (c) 2010-2012 Benjamin Peterson
def with_metaclass(meta, base=object):
    """Create a base class with a metaclass."""
    return meta("%sBase" % meta.__name__, (base,), {})
