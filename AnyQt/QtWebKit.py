from . import _api

# Names imported from Qt4's QtWebKit module
__Qt4_QtWebKit = [
    'QWebDatabase',
    'QWebElement',
    'QWebElementCollection',
    'QWebHistory',
    'QWebHistoryInterface',
    'QWebHistoryItem',
    'QWebPluginFactory',
    'QWebSecurityOrigin',
    'QWebSettings',
    'qWebKitMajorVersion',
    'qWebKitMinorVersion',
    'qWebKitVersion'
]

if _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtWebKit import *
elif _api.USED_API == _api.QT_API_PYQT4:
    from PyQt4.QtWebKit import (
        QWebDatabase,
        QWebElement,
        QWebElementCollection,
        QWebHistory,
        QWebHistoryInterface,
        QWebHistoryItem,
        QWebPluginFactory,
        QWebSecurityOrigin,
        QWebSettings,
        qWebKitMajorVersion,
        qWebKitMinorVersion,
        qWebKitVersion
    )
elif _api.USED_API == _api.QT_API_PYSIDE:
    from PySide.QtWebKit import (
        QWebDatabase,
        QWebElement,
        QWebElementCollection,
        QWebHistory,
        QWebHistoryInterface,
        QWebHistoryItem,
        QWebPluginFactory,
        QWebSecurityOrigin,
        QWebSettings,
    )
    try:
        # missing in current PySide 1.2.2
        from PySide.QtWebKit import \
            qWebKitMajorVersion, qWebKitMinorVersion, qWebKitVersion
    except ImportError:
        pass
