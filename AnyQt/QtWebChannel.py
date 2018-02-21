from . import _api

if _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtWebChannel import *
elif _api.USED_API == _api.QT_API_PYSIDE2:
    from PySide2.QtWebChannel import *
else:
    raise ImportError("No module named 'QtWebChannel' in the selected "
                      "Qt api ({})".format(_api.USED_API))
