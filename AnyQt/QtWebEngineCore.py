from . import _api

if _api.USED_API == _api.QT_API_PYQT6:
    from PyQt6.QtWebEngineCore import *
elif _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtWebEngineCore import *
    try:
        from PyQt5.QtWebEngineWidgets import (
            QWebEngineHistory,
            QWebEngineProfile,
            QWebEngineScript,
            QWebEngineScriptCollection,
            QWebEngineClientCertificateSelection,
            QWebEngineSettings,
            QWebEngineFullScreenRequest,
        )
    except ImportError:
        pass
elif _api.USED_API == _api.QT_API_PYSIDE2:
    from PySide2.QtWebEngineCore import *
    try:
        from PySide2.QtWebEngineWidgets import (
            QWebEngineHistory,
            QWebEngineProfile,
            QWebEngineScript,
            QWebEngineScriptCollection,
            # QWebEngineClientCertificateSelection,
            QWebEngineSettings,
            QWebEngineFullScreenRequest,
        )
    except ImportError:
        pass
elif _api.USED_API == _api.QT_API_PYSIDE6:
    from PySide6.QtWebEngineCore import *
else:
    raise ImportError("No module named 'QtWebEngineCore' in the selected "
                      "Qt api ({})".format(_api.USED_API))

_api.apply_global_fixes(globals())
