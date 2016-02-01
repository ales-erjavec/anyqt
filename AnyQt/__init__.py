import os
import sys

from . import _api

if "QT_API" in os.environ:
    _api.comittoapi(os.environ["QT_API"])
else:
    __existing = None
    # Check sys.modules for existing imports
    if "PyQt5" in sys.modules:
        __existing = _api.QT_API_PYQT5
    elif "PyQt4" in sys.modules:
        __existing = _api.QT_API_PYQT4
    elif "PySide" in sys.modules:
        __existing = _api.QT_API_PYSIDE

    if __existing is not None:
        _api.comittoapi(__existing)
