from . import _api

if _api.USED_API == _api.QT_API_PYQT6:
    from PyQt6.QtLocation import *
elif _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtLocation import *
elif _api.USED_API == _api.QT_API_PYQT4:
    from PyQt4.QtLocation import *
elif _api.USED_API == _api.QT_API_PYSIDE:
    from PySide.QtLocation import *
elif _api.USED_API == _api.QT_API_PYSIDE2:
    from PySide2.QtLocation import *
elif _api.USED_API == _api.QT_API_PYSIDE6:
    from PySide6.QtLocation import *

_api.apply_global_fixes(globals())
