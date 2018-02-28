from . import _api

if _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtOpenGL import *
elif _api.USED_API == _api.QT_API_PYQT4:
    from PyQt4.QtOpenGL import *
elif _api.USED_API == _api.QT_API_PYSIDE:
    from PySide.QtOpenGL import *
elif _api.USED_API == _api.QT_API_PYSIDE2:
    from PySide2.QtOpenGL import *

