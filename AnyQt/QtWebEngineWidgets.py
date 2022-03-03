from . import _api

if _api.USED_API == _api.QT_API_PYQT6:
    from PyQt6.QtWebEngineWidgets import *
    from PyQt6.QtWebEngineCore import (
        QWebEngineHistory,
        QWebEngineProfile,
        QWebEngineScript,
        QWebEngineScriptCollection,
        QWebEngineClientCertificateSelection,
        QWebEngineSettings,
        QWebEngineFullScreenRequest,
    )
elif _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtWebEngineWidgets import *
elif _api.USED_API == _api.QT_API_PYSIDE2:
    from PySide2.QtWebEngineWidgets import *
else:
    raise ImportError("No module named 'QtWebEngineWidgets' in the selected "
                      "Qt api ({})".format(_api.USED_API))

_api.apply_global_fixes(globals())
