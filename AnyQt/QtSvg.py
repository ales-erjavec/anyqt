from . import _api

if _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtSvg import *
elif _api.USED_API == _api.QT_API_PYQT4:
    from PyQt4.QtSvg import *
elif _api.USED_API == _api.QT_API_PYSIDE:
    from PySide.QtSvg import *
