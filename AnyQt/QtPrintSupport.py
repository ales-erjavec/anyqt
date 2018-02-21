from . import _api

# Names imported from Qt'4 QtGui module
__Qt4_QtGui = [
    'QAbstractPrintDialog',
    'QPageSetupDialog',
    'QPrintDialog',
    'QPrintEngine',
    'QPrintPreviewDialog',
    'QPrintPreviewWidget',
    'QPrinter',
    'QPrinterInfo'
]

if _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtPrintSupport import *
elif _api.USED_API == _api.QT_API_PYQT4:
    from PyQt4.QtGui import (
        QAbstractPrintDialog,
        QPageSetupDialog,
        QPrintDialog,
        QPrintEngine,
        QPrintPreviewDialog,
        QPrintPreviewWidget,
        QPrinter,
        QPrinterInfo
    )
elif _api.USED_API == _api.QT_API_PYSIDE:
    from PySide.QtGui import (
        QAbstractPrintDialog,
        QPageSetupDialog,
        QPrintDialog,
        QPrintEngine,
        QPrintPreviewDialog,
        QPrintPreviewWidget,
        QPrinter,
        QPrinterInfo
    )
elif _api.USED_API == _api.QT_API_PYSIDE2:
    from PySide2.QtPrintSupport import *
