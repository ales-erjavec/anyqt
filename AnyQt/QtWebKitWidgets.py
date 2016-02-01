from . import _api

__all__ = [
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
