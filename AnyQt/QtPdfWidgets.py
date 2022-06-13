from . import _api

if _api.USED_API == _api.QT_API_PYQT6:
    from PyQt6.QtPdfWidgets import *
elif _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtPdfWidgets import *
elif _api.USED_API == _api.QT_API_PYQT4:
    from PyQt4.QtPdfWidgets import *
elif _api.USED_API == _api.QT_API_PYSIDE:
    from PySide.QtPdfWidgets import *
elif _api.USED_API == _api.QT_API_PYSIDE2:
    from PySide2.QtPdfWidgets import *
elif _api.USED_API == _api.QT_API_PYSIDE6:
    from PySide6.QtPdfWidgets import *
else:
    raise ImportError(f"No module named '{__name__}' in the selected "
                      f"Qt api ({_api.USED_API})")

_api.apply_global_fixes(globals())
