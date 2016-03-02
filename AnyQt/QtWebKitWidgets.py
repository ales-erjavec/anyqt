from . import _api

# Names imported from Qt4's QtWebKit module
__Qt4_QtWebKit = [
    'QGraphicsWebView',
    'QWebFrame',
    'QWebHitTestResult',
    'QWebInspector',
    'QWebPage',
    'QWebView',
]

if _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtWebKitWidgets import *
elif _api.USED_API == _api.QT_API_PYQT4:
    from PyQt4.QtWebKit import (
        QGraphicsWebView,
        QWebFrame,
        QWebHitTestResult,
        QWebInspector,
        QWebPage,
        QWebView,
    )
elif _api.USED_API == _api.QT_API_PYSIDE:
    from PySide.QtWebKit import (
        QGraphicsWebView,
        QWebFrame,
        QWebHitTestResult,
        QWebInspector,
        QWebPage,
        QWebView,
    )
