from warnings import warn
from .QtCore import QT_VERSION_INFO as __QT_VERSION_INFO
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

if _api.USED_API == _api.QT_API_PYQT6:
    from PyQt6.QtGui import *
    # Deprecated QEnterEvent accessors
    if not hasattr(QEnterEvent, "pos"):
        QEnterEvent.pos = lambda self: self.position().toPoint()
    if not hasattr(QEnterEvent, "globalPos"):
        QEnterEvent.globalPos = lambda self: self.globalPosition().toPoint()
    if not hasattr(QEnterEvent, "x"):
        QEnterEvent.x = lambda self: self.position().toPoint().x()
    if not hasattr(QEnterEvent, "y"):
        QEnterEvent.y = lambda self: self.position().toPoint().y()
    if not hasattr(QEnterEvent, "globalX"):
        QEnterEvent.globalX = lambda self: self.globalPosition().toPoint().x()
    if not hasattr(QEnterEvent, "globalY"):
        QEnterEvent.globalY = lambda self: self.globalPosition().toPoint().y()
    if not hasattr(QEnterEvent, "localPos"):
        QEnterEvent.localPos = lambda self: self.position()
    if not hasattr(QEnterEvent, "windowPos"):
        QEnterEvent.windowPos = lambda self: self.scenePosition()
    if not hasattr(QEnterEvent, "screenPos"):
        QEnterEvent.screenPos = lambda self: self.globalPosition()

    # Deprecated QMouseEvent accessors
    if not hasattr(QMouseEvent, "pos"):
        QMouseEvent.pos = lambda self: self.position().toPoint()
    if not hasattr(QMouseEvent, "globalPos"):
        QMouseEvent.globalPos = lambda self: self.globalPosition().toPoint()
    if not hasattr(QMouseEvent, "x"):
        QMouseEvent.x = lambda self: self.position().x()
    if not hasattr(QMouseEvent, "y"):
        QMouseEvent.y = lambda self: self.position().y()
    if not hasattr(QMouseEvent, "globalX"):
        QMouseEvent.globalX = lambda self: self.globalPosition().x()
    if not hasattr(QMouseEvent, "globalY"):
        QMouseEvent.globalY = lambda self: self.globalPosition().y()

    # Deprecated QDropEvent accessors
    if not hasattr(QDropEvent, "pos"):
        QDropEvent.pos = lambda self: self.position().toPoint()
    if not hasattr(QDropEvent, "posF"):
        QDropEvent.posF = lambda self: self.position()
    if not hasattr(QDropEvent, "mouseButtons"):
        QDropEvent.mouseButtons = lambda self: self.buttons()
    if not hasattr(QDropEvent, "keyboardModifiers"):
        QDropEvent.keyboardModifiers = lambda self: self.modifiers()

    # Deprecated QWheelEvent accessors
    if not hasattr(QWheelEvent, "pos"):
        QWheelEvent.pos = lambda self: self.position().toPoint()
    if not hasattr(QWheelEvent, "posF"):
        QWheelEvent.posF = lambda self: self.position()
    if not hasattr(QWheelEvent, "globalPos"):
        QWheelEvent.globalPos = lambda self: self.globalPosition().toPoint()
    if not hasattr(QWheelEvent, "globalPosF"):
        QWheelEvent.globalPosF = lambda self: self.globalPosition()
    if not hasattr(QWheelEvent, "x"):
        QWheelEvent.x = lambda self: self.position().x()
    if not hasattr(QWheelEvent, "y"):
        QWheelEvent.y = lambda self: self.position().y()
    if not hasattr(QWheelEvent, "globalX"):
        QWheelEvent.globalX = lambda self: self.globalPosition().x()
    if not hasattr(QWheelEvent, "globalY"):
        QWheelEvent.globalY = lambda self: self.globalPosition().y()
    if not hasattr(QWheelEvent, "mouseButtons"):
        QWheelEvent.mouseButtons = lambda self: self.buttons()
    if not hasattr(QWheelEvent, "keyboardModifiers"):
        QWheelEvent.keyboardModifiers = lambda self: self.modifiers()


elif _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import QUndoCommand, QUndoStack, QUndoGroup
    from PyQt5.QtWidgets import QShortcut, QAction, QActionGroup
    from PyQt5.QtCore import PYQT_VERSION as _PYQT_VERSION

    if _PYQT_VERSION < 0x50c00:  # 5.12.0

        class WheelEvent(QWheelEvent):
            from PyQt5.QtCore import (QPointF as _QPointF,
                                      QPoint as _QPoint,
                                      Qt as _Qt)

            _constructor_signature = \
                ((_QPointF, _QPoint),
                 (_QPointF, _QPoint),
                 (_QPoint,),
                 (_QPoint,),
                 (_Qt.MouseButtons, _Qt.MouseButton),
                 (_Qt.KeyboardModifiers, _Qt.KeyboardModifier),
                 (_Qt.ScrollPhase,),
                 (bool,),
                 (_Qt.MouseEventSource,))

            def __init__(self, *args):
                sig = WheelEvent._constructor_signature
                if len(args) == len(sig) and \
                        all(any(isinstance(a, t) for t in ts)
                            for a, ts in zip(args, sig)):
                    angleDelta = args[3]
                    if abs(angleDelta.x()) > abs(angleDelta.y()):
                        orientation = 0x1  # horizontal
                        delta = angleDelta.x()
                    else:
                        orientation = 0x2  # vertical
                        delta = angleDelta.y()
                    args = args[:4] + \
                           (delta, orientation) + \
                           args[4:7] + (args[8], args[7])
                super().__init__(*args)

        QWheelEvent = WheelEvent

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
elif _api.USED_API == _api.QT_API_PYSIDE2:
    from PySide2.QtGui import *

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


if _api.USED_API == _api.QT_API_PYQT5:
    # PyQt5 does not support setPageSize(QPageSize) overload
    def QPdfWriter_setPageSize(self, size):
        if isinstance(size, QPageSize):
            self.setPageSizeMM(size.size(QPageSize.Millimeter))
            return self.pageLayout().pageSize().isEquivalentTo(size)
        else:
            __QPdfWriter_setPageSize(self, size)
    __QPdfWriter_setPageSize = QPdfWriter.setPageSize
    QPdfWriter.setPageSize = QPdfWriter_setPageSize
    del QPdfWriter_setPageSize

if not hasattr(QGuiApplication, 'screenAt'):
    def QGuiApplication_screenAt(pos):
        visited = set()
        for screen in QGuiApplication.screens():
            if screen in visited:
                continue
            # The virtual siblings include the screen itself, so iterate directly
            for sibling in screen.virtualSiblings():
                if sibling.geometry().contains(pos):
                    return sibling
                visited.add(sibling)
        return None
    QGuiApplication.screenAt = staticmethod(QGuiApplication_screenAt)
    del QGuiApplication_screenAt


# Alias QFontMetrics(F).horizontalAdvance to QFontMetrics(F).width
# when it does not exists
if not hasattr(QFontMetrics, "horizontalAdvance"):
    def QFontMetrics_horizontalAdvance(self, *args, **kwargs):
        return __QFontMetrics_width(self, *args, **kwargs)
    __QFontMetrics_width = QFontMetrics.width
    QFontMetrics.horizontalAdvance = QFontMetrics_horizontalAdvance
    del QFontMetrics_horizontalAdvance
if not hasattr(QFontMetricsF, "horizontalAdvance"):
    def QFontMetricsF_horizontalAdvance(self, *args, **kwargs):
        return __QFontMetricsF_width(self, *args, **kwargs)
    __QFontMetricsF_width = QFontMetricsF.width
    QFontMetricsF.horizontalAdvance = QFontMetricsF_horizontalAdvance
    del QFontMetricsF_horizontalAdvance


# Warn on deprecated QFontMetrics.width
def QFontMetrics_width(self, *args, **kwargs):
    warn("QFontMetrics(F).width is obsolete. "
         "Replace with QFontMetrics(F).horizontalAdvance",
         DeprecationWarning, stacklevel=2)
    return self.horizontalAdvance(*args, **kwargs)


QFontMetricsF.width = QFontMetrics_width
QFontMetrics.width = QFontMetrics_width
del QFontMetrics_width

if __QT_VERSION_INFO < (6, 0):
    class QFontDatabase(QFontDatabase):
        def staticwrapper(f):
            from functools import wraps
            @wraps(f)
            def wrapped(*args, **kwargs):
                return f(QFontDatabase(), *args, **kwargs)
            return staticmethod(wrapped)
        bold = staticwrapper(QFontDatabase.bold)
        families = staticwrapper(QFontDatabase.families)
        font = staticwrapper(QFontDatabase.font)
        isBitmapScalable = staticwrapper(QFontDatabase.isBitmapScalable)
        isFixedPitch = staticwrapper(QFontDatabase.isFixedPitch)
        isPrivateFamily = staticwrapper(QFontDatabase.isPrivateFamily)
        isScalable = staticwrapper(QFontDatabase.isScalable)
        isSmoothlyScalable = staticwrapper(QFontDatabase.isSmoothlyScalable)
        italic = staticwrapper(QFontDatabase.italic)
        pointSizes = staticwrapper(QFontDatabase.pointSizes)
        smoothSizes = staticwrapper(QFontDatabase.smoothSizes)
        styleString = staticwrapper(QFontDatabase.styleString)
        styles = staticwrapper(QFontDatabase.styles)
        weight = staticwrapper(QFontDatabase.weight)
        writingSystems = staticwrapper(QFontDatabase.writingSystems)
        del staticwrapper


_api.apply_global_fixes(globals())
