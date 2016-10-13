from . import _api

if _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtWebEngineWidgets import *
else:
    raise ImportError("No module named 'QtWebEngineWidgets' in the selected "
                      "Qt api ({})".format(_api.USED_API))