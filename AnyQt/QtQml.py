from . import _api

if _api.USED_API == _api.QT_API_PYQT6:
    from PyQt6.QtQml import *
elif _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtQml import *
elif _api.USED_API == _api.QT_API_PYSIDE2:
    from PySide2.QtQml import *
else:
    raise ImportError("No module named 'QtQml' in the selected "
                      "Qt api ({})".format(_api.USED_API))

_api.apply_global_fixes(globals())
