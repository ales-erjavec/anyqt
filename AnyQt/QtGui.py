from . import _api

# Names imported from Qt4's QtGui module
__Qt4_QtGui = [
    'QAbstractTextDocumentLayout',
    'QActionEvent',
    'QBitmap',
    'QBrush',
    'QClipboard',
    'QCloseEvent',
    'QColor',
    'QConicalGradient',
    'QContextMenuEvent',
    'QCursor',
    'QDesktopServices',
    'QDoubleValidator',
    'QDrag',
    'QDragEnterEvent',
    'QDragLeaveEvent',
    'QDragMoveEvent',
    'QDropEvent',
    'QFileOpenEvent',
    'QFocusEvent',
    'QFont',
    'QFontDatabase',
    'QFontInfo',
    'QFontMetrics',
    'QFontMetricsF',
    'QGlyphRun',
    'QGradient',
    'QHelpEvent',
    'QHideEvent',
    'QHoverEvent',
    'QIcon',
    'QIconDragEvent',
    'QIconEngine',
    'QImage',
    'QImageIOHandler',
    'QImageReader',
    'QImageWriter',
    'QInputEvent',
    'QInputMethodEvent',
    'QIntValidator',
    'QKeyEvent',
    'QKeySequence',
    'QLinearGradient',
    'QMatrix2x2',
    'QMatrix2x3',
    'QMatrix2x4',
    'QMatrix3x2',
    'QMatrix3x3',
    'QMatrix3x4',
    'QMatrix4x2',
    'QMatrix4x3',
    'QMatrix4x4',
    'QMouseEvent',
    'QMoveEvent',
    'QMovie',
    'QPaintDevice',
    'QPaintEngine',
    'QPaintEngineState',
    'QPaintEvent',
    'QPainter',
    'QPainterPath',
    'QPainterPathStroker',
    'QPalette',
    'QPen',
    'QPicture',
    'QPictureIO',
    'QPixmap',
    'QPixmapCache',
    'QPolygon',
    'QPolygonF',
    'QQuaternion',
    'QRadialGradient',
    'QRawFont',
    'QRegExpValidator',
    'QRegion',
    'QResizeEvent',
    'QSessionManager',
    'QShortcutEvent',
    'QShowEvent',
    'QStandardItem',
    'QStandardItemModel',
    'QStaticText',
    'QStatusTipEvent',
    'QSyntaxHighlighter',
    'QTabletEvent',
    'QTextBlock',
    'QTextBlockFormat',
    'QTextBlockGroup',
    'QTextBlockUserData',
    'QTextCharFormat',
    'QTextCursor',
    'QTextDocument',
    'QTextDocumentFragment',
    'QTextDocumentWriter',
    'QTextFormat',
    'QTextFragment',
    'QTextFrame',
    'QTextFrameFormat',
    'QTextImageFormat',
    'QTextInlineObject',
    'QTextItem',
    'QTextLayout',
    'QTextLength',
    'QTextLine',
    'QTextList',
    'QTextListFormat',
    'QTextObject',
    'QTextObjectInterface',
    'QTextOption',
    'QTextTable',
    'QTextTableCell',
    'QTextTableCellFormat',
    'QTextTableFormat',
    'QTouchEvent',
    'QTransform',
    'QValidator',
    'QVector2D',
    'QVector3D',
    'QVector4D',
    'QWhatsThisClickedEvent',
    'QWheelEvent',
    'QWindowStateChangeEvent',
    'qAlpha',
    'qBlue',
    'qFuzzyCompare',
    'qGray',
    'qGreen',
    'qIsGray',
    'qRed',
    'qRgb',
    'qRgba'
]

if _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtGui import *
elif _api.USED_API == _api.QT_API_PYQT4:
    import PyQt4.QtGui as _QtGui
    globals().update(
        {name: getattr(_QtGui, name)
         for name in __Qt4_QtGui if hasattr(_QtGui, name)}
    )
    del _QtGui
elif _api.USED_API == _api.QT_API_PYSIDE:
    from PySide import QtGui as _QtGui
    globals().update(
        {name: getattr(_QtGui, name)
         for name in __Qt4_QtGui if hasattr(_QtGui, name)}
    )
    del _QtGui
    # Known to be present in PyQt4 but not in PySide:
    #   QGlyphRun, QRawFont, QStaticText, QTextDocumentWriter

if _api.USED_API in [_api.QT_API_PYQT4, _api.QT_API_PYSIDE]:
    from AnyQt import QtCore as __QtCore

    def __QWheelEvent_angleDelta(self):
        """
        Qt5 compatible QWheelEvent.angleDelta

        Return the delta as an x or y axis aligned QPoint vector
        """
        if self.orientation() == __QtCore.Qt.Horizontal:
            return __QtCore.QPoint(self.delta(), 0)
        else:
            return __QtCore.QPoint(0, self.delta())

    def __QWheelEvent_pixelDelta(self):
        """
        Qt5 compatible QWheelEvent.pixelDelta

        Always return a null QPoint. This is acceptable and compatible with
        the API (i.e. the pixelDelta is only supported on platforms where
        high resolution is available).
        """
        return __QtCore.QPoint()

    QWheelEvent.angleDelta = __QWheelEvent_angleDelta
    QWheelEvent.pixelDelta = __QWheelEvent_pixelDelta

