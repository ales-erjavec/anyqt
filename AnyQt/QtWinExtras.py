from . import _api

if _api.USED_API == _api.QT_API_PYQT6:
    from PyQt6.QtWinExtras import *
elif _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtWinExtras import *
elif _api.USED_API == _api.QT_API_PYSIDE2:
    from PySide2.QtWinExtras import *
else:
    raise ImportError

_api.apply_global_fixes(globals())

