from . import _api

if _api.USED_API == _api.QT_API_PYQT6:
    from PyQt6.QtPositioning import *
elif _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtPositioning import *
elif _api.USED_API == _api.QT_API_PYQT4:
    from PyQt4.QtPositioning import *
elif _api.USED_API == _api.QT_API_PYSIDE:
    from PySide.QtPositioning import *
elif _api.USED_API == _api.QT_API_PYSIDE2:
    from PySide2.QtPositioning import *
elif _api.USED_API == _api.QT_API_PYSIDE6:
    from PySide6.QtPositioning import *

_api.apply_global_fixes(globals())
