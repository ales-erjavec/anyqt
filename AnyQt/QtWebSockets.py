from . import _api

if _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtWebSockets import *
elif _api.USED_API == _api.QT_API_PYSIDE2:
    from PySide2.QtWebSockets import *
else:
    raise ImportError("No module named 'QtWebSockets' in the selected "
                      "Qt api ({})".format(_api.USED_API))
