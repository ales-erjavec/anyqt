from . import _api

# Names imported from Qt4's QtGui module
__Qt4_QtGui = [
    'QMacPasteboardMime'
]

if _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtMacExtras import *
elif _api.USED_API == _api.QT_API_PYQT4:
    from PyQt4.QtGui import QMacPasteboardMime
elif _api.USED_API == _api.QT_API_PYSIDE:
    from PySide.QtGui import QMacPasteboardMime
