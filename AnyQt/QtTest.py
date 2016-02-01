from . import _api

if _api == _api.QT_API_PYQT5:
    from PyQt5.QtTest import *
elif _api == _api.QT_API_PYQT4:
    from PyQt4.QtTest import *
elif _api == _api.QT_API_PYSIDE:
    from PySide.QtTest import *
