import warnings

from .. import _api

__all__ = [
    'QAbstractButton',
    'QAbstractGraphicsShapeItem',
    'QAbstractItemDelegate',
    'QAbstractItemView',
    'QAbstractPrintDialog',
    'QAbstractProxyModel',
    'QAbstractScrollArea',
    'QAbstractSlider',
    'QAbstractSpinBox',
    'QAbstractTextDocumentLayout',
    'QAction',
    'QActionEvent',
    'QActionGroup',
    'QApplication',
    'QBitmap',
    'QBoxLayout',
    'QBrush',
    'QButtonGroup',
    'QCalendarWidget',
    'QCheckBox',
    'QClipboard',
    'QCloseEvent',
    'QColor',
    'QColorDialog',
    'QColumnView',
    'QComboBox',
    'QCommandLinkButton',
    'QCommonStyle',
    'QCompleter',
    'QConicalGradient',
    'QContextMenuEvent',
    'QCursor',
    'QDataWidgetMapper',
    'QDateEdit',
    'QDateTimeEdit',
    'QDesktopServices',
    'QDesktopWidget',
    'QDial',
    'QDialog',
    'QDialogButtonBox',
    'QDirModel',
    'QDockWidget',
    'QDoubleSpinBox',
    'QDoubleValidator',
    'QDrag',
    'QDragEnterEvent',
    'QDragLeaveEvent',
    'QDragMoveEvent',
    'QDropEvent',
    'QErrorMessage',
    'QFileDialog',
    'QFileIconProvider',
    'QFileOpenEvent',
    'QFileSystemModel',
    'QFocusEvent',
    'QFocusFrame',
    'QFont',
    'QFontComboBox',
    'QFontDatabase',
    'QFontDialog',
    'QFontInfo',
    'QFontMetrics',
    'QFontMetricsF',
    'QFormLayout',
    'QFrame',
    'QGesture',
    'QGestureEvent',
    'QGestureRecognizer',
    'QGlyphRun',
    'QGradient',
    'QGraphicsAnchor',
    'QGraphicsAnchorLayout',
    'QGraphicsBlurEffect',
    'QGraphicsColorizeEffect',
    'QGraphicsDropShadowEffect',
    'QGraphicsEffect',
    'QGraphicsEllipseItem',
    'QGraphicsGridLayout',
    'QGraphicsItem',
    'QGraphicsItemGroup',
    'QGraphicsLayout',
    'QGraphicsLayoutItem',
    'QGraphicsLineItem',
    'QGraphicsLinearLayout',
    'QGraphicsObject',
    'QGraphicsOpacityEffect',
    'QGraphicsPathItem',
    'QGraphicsPixmapItem',
    'QGraphicsPolygonItem',
    'QGraphicsProxyWidget',
    'QGraphicsRectItem',
    'QGraphicsRotation',
    'QGraphicsScale',
    'QGraphicsScene',
    'QGraphicsSceneContextMenuEvent',
    'QGraphicsSceneDragDropEvent',
    'QGraphicsSceneEvent',
    'QGraphicsSceneHelpEvent',
    'QGraphicsSceneHoverEvent',
    'QGraphicsSceneMouseEvent',
    'QGraphicsSceneMoveEvent',
    'QGraphicsSceneResizeEvent',
    'QGraphicsSceneWheelEvent',
    'QGraphicsSimpleTextItem',
    'QGraphicsTextItem',
    'QGraphicsTransform',
    'QGraphicsView',
    'QGraphicsWidget',
    'QGridLayout',
    'QGroupBox',
    'QHBoxLayout',
    'QHeaderView',
    'QHelpEvent',
    'QHideEvent',
    'QHoverEvent',
    'QIcon',
    'QIconDragEvent',
    'QIconEngine',
    'QIconEngineV2',
    'QIdentityProxyModel',
    'QImage',
    'QImageIOHandler',
    'QImageReader',
    'QImageWriter',
    # 'QInputContext',
    # 'QInputContextFactory',
    'QInputDialog',
    'QInputEvent',
    'QInputMethodEvent',
    'QIntValidator',
    'QItemDelegate',
    'QItemEditorCreatorBase',
    'QItemEditorFactory',
    'QItemSelection',
    'QItemSelectionModel',
    'QItemSelectionRange',
    'QKeyEvent',
    'QKeyEventTransition',
    'QKeySequence',
    'QLCDNumber',
    'QLabel',
    'QLayout',
    'QLayoutItem',
    'QLineEdit',
    'QLinearGradient',
    'QListView',
    'QListWidget',
    'QListWidgetItem',
    # 'QMacCocoaViewContainer',
    # 'QMacPasteboardMime',
    'QMainWindow',
    # 'QMatrix',
    'QMatrix2x2',
    'QMatrix2x3',
    'QMatrix2x4',
    'QMatrix3x2',
    'QMatrix3x3',
    'QMatrix3x4',
    'QMatrix4x2',
    'QMatrix4x3',
    'QMatrix4x4',
    'QMdiArea',
    'QMdiSubWindow',
    'QMenu',
    'QMenuBar',
    'QMessageBox',
    # 'QMimeSource',
    'QMouseEvent',
    'QMouseEventTransition',
    'QMoveEvent',
    'QMovie',
    'QPageSetupDialog',
    'QPaintDevice',
    'QPaintEngine',
    'QPaintEngineState',
    'QPaintEvent',
    'QPainter',
    'QPainterPath',
    'QPainterPathStroker',
    'QPalette',
    'QPanGesture',
    'QPen',
    'QPicture',
    'QPictureIO',
    'QPinchGesture',
    'QPixmap',
    'QPixmapCache',
    'QPlainTextDocumentLayout',
    'QPlainTextEdit',
    'QPolygon',
    'QPolygonF',
    'QPrintDialog',
    'QPrintEngine',
    'QPrintPreviewDialog',
    'QPrintPreviewWidget',
    'QPrinter',
    'QPrinterInfo',
    'QProgressBar',
    'QProgressDialog',
    # 'QProxyModel',
    'QPushButton',
    # 'QPyTextObject',
    'QQuaternion',
    'QRadialGradient',
    'QRadioButton',
    'QRawFont',
    'QRegExpValidator',
    'QRegion',
    'QResizeEvent',
    'QRubberBand',
    'QScrollArea',
    'QScrollBar',
    'QSessionManager',
    'QShortcut',
    'QShortcutEvent',
    'QShowEvent',
    'QSizeGrip',
    'QSizePolicy',
    'QSlider',
    'QSortFilterProxyModel',
    # 'QSound',
    'QSpacerItem',
    'QSpinBox',
    'QSplashScreen',
    'QSplitter',
    'QSplitterHandle',
    'QStackedLayout',
    'QStackedWidget',
    'QStandardItem',
    'QStandardItemModel',
    'QStaticText',
    'QStatusBar',
    'QStatusTipEvent',
    'QStringListModel',
    'QStyle',
    'QStyleFactory',
    'QStyleHintReturn',
    'QStyleHintReturnMask',
    'QStyleHintReturnVariant',
    'QStyleOption',
    'QStyleOptionButton',
    'QStyleOptionComboBox',
    'QStyleOptionComplex',
    'QStyleOptionDockWidget',
    'QStyleOptionDockWidgetV2',
    'QStyleOptionFocusRect',
    'QStyleOptionFrame',
    'QStyleOptionFrameV2',
    'QStyleOptionFrameV3',
    'QStyleOptionGraphicsItem',
    'QStyleOptionGroupBox',
    'QStyleOptionHeader',
    'QStyleOptionMenuItem',
    'QStyleOptionProgressBar',
    'QStyleOptionProgressBarV2',
    'QStyleOptionRubberBand',
    'QStyleOptionSizeGrip',
    'QStyleOptionSlider',
    'QStyleOptionSpinBox',
    'QStyleOptionTab',
    'QStyleOptionTabBarBase',
    'QStyleOptionTabBarBaseV2',
    'QStyleOptionTabV2',
    'QStyleOptionTabV3',
    'QStyleOptionTabWidgetFrame',
    'QStyleOptionTabWidgetFrameV2',
    'QStyleOptionTitleBar',
    'QStyleOptionToolBar',
    'QStyleOptionToolBox',
    'QStyleOptionToolBoxV2',
    'QStyleOptionToolButton',
    'QStyleOptionViewItem',
    'QStyleOptionViewItemV2',
    'QStyleOptionViewItemV3',
    'QStyleOptionViewItemV4',
    'QStylePainter',
    'QStyledItemDelegate',
    'QSwipeGesture',
    'QSyntaxHighlighter',
    'QSystemTrayIcon',
    'QTabBar',
    'QTabWidget',
    'QTableView',
    'QTableWidget',
    'QTableWidgetItem',
    'QTableWidgetSelectionRange',
    'QTabletEvent',
    'QTapAndHoldGesture',
    'QTapGesture',
    'QTextBlock',
    'QTextBlockFormat',
    'QTextBlockGroup',
    'QTextBlockUserData',
    'QTextBrowser',
    'QTextCharFormat',
    'QTextCursor',
    'QTextDocument',
    'QTextDocumentFragment',
    'QTextDocumentWriter',
    'QTextEdit',
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
    'QTimeEdit',
    'QToolBar',
    'QToolBox',
    'QToolButton',
    'QToolTip',
    'QTouchEvent',
    'QTransform',
    'QTreeView',
    'QTreeWidget',
    'QTreeWidgetItem',
    'QTreeWidgetItemIterator',
    'QUndoCommand',
    'QUndoGroup',
    'QUndoStack',
    'QUndoView',
    'QVBoxLayout',
    'QValidator',
    'QVector2D',
    'QVector3D',
    'QVector4D',
    'QWhatsThis',
    'QWhatsThisClickedEvent',
    'QWheelEvent',
    'QWidget',
    'QWidgetAction',
    'QWidgetItem',
    'QWindowStateChangeEvent',
    'QWizard',
    'QWizardPage',
    # 'QWorkspace',
    "QWIDGETSIZE_MAX",
    'qAlpha',
    'qApp',
    'qBlue',
    'qDrawBorderPixmap',
    'qDrawPlainRect',
    'qDrawShadeLine',
    'qDrawShadePanel',
    'qDrawShadeRect',
    'qDrawWinButton',
    'qDrawWinPanel',
    'qFuzzyCompare',
    'qGray',
    'qGreen',
    'qIsGray',
    'qRed',
    'qRgb',
    'qRgba',
    # 'qSwap',

    # 'qt_mac_secure_keyboard',
    # 'qt_mac_set_dock_menu',
    # 'qt_mac_set_menubar_icons',
    # 'qt_mac_set_menubar_merge',
    # 'qt_mac_set_native_menubar',
    # 'qt_mac_set_press_and_hold_context',
    # 'qt_set_sequence_auto_mnemonic'
]

__removed__ = [
    'QMatrix',
    'QMimeSource',
    'QProxyModel',
    'QPyTextObject',
    'QWorkspace',
    'qSwap',
]

assert _api.USED_API == _api.QT_API_PYQT5

from PyQt5.QtCore import (
    QAbstractProxyModel,
    QIdentityProxyModel,
    QItemSelection,
    QItemSelectionModel,
    QItemSelectionRange,
    QSortFilterProxyModel,
    QStringListModel,
)

from PyQt5.QtGui import (
    QAbstractTextDocumentLayout,
    QActionEvent,
    QBitmap,
    QBrush,
    QClipboard,
    QCloseEvent,
    QColor,
    QConicalGradient,
    QContextMenuEvent,
    QCursor,
    QDesktopServices,
    QDoubleValidator,
    QDrag,
    QDragEnterEvent,
    QDragLeaveEvent,
    QDragMoveEvent,
    QDropEvent,
    QFileOpenEvent,
    QFocusEvent,
    QFont,
    QFontDatabase,
    QFontInfo,
    QFontMetrics,
    QFontMetricsF,
    QGlyphRun,
    QGradient,
    QHelpEvent,
    QHideEvent,
    QHoverEvent,
    QIcon,
    QIconDragEvent,
    QIconEngine,
    QImage,
    QImageIOHandler,
    QImageReader,
    QImageWriter,
    QInputEvent,
    QInputMethodEvent,
    QIntValidator,
    QKeyEvent,
    QKeySequence,
    QLinearGradient,
    QMatrix2x2,
    QMatrix2x3,
    QMatrix2x4,
    QMatrix3x2,
    QMatrix3x3,
    QMatrix3x4,
    QMatrix4x2,
    QMatrix4x3,
    QMatrix4x4,
    QMouseEvent,
    QMoveEvent,
    QMovie,
    QPaintDevice,
    QPaintEngine,
    QPaintEngineState,
    QPaintEvent,
    QPainter,
    QPainterPath,
    QPainterPathStroker,
    QPalette,
    QPen,
    QPicture,
    QPictureIO,
    QPixmap,
    QPixmapCache,
    QPolygon,
    QPolygonF,
    QQuaternion,
    QRadialGradient,
    QRawFont,
    QRegExpValidator,
    QRegion,
    QResizeEvent,
    QSessionManager,
    QShortcutEvent,
    QShowEvent,
    QStandardItem,
    QStandardItemModel,
    QStaticText,
    QStatusTipEvent,
    QSyntaxHighlighter,
    QTabletEvent,
    QTextBlock,
    QTextBlockFormat,
    QTextBlockGroup,
    QTextBlockUserData,
    QTextCharFormat,
    QTextCursor,
    QTextDocument,
    QTextDocumentFragment,
    QTextDocumentWriter,
    QTextFormat,
    QTextFragment,
    QTextFrame,
    QTextFrameFormat,
    QTextImageFormat,
    QTextInlineObject,
    QTextItem,
    QTextLayout,
    QTextLength,
    QTextLine,
    QTextList,
    QTextListFormat,
    QTextObject,
    QTextObjectInterface,
    QTextOption,
    QTextTable,
    QTextTableCell,
    QTextTableCellFormat,
    QTextTableFormat,
    QTouchEvent,
    QTransform,
    QValidator,
    QVector2D,
    QVector3D,
    QVector4D,
    QWhatsThisClickedEvent,
    QWheelEvent,
    QWindowStateChangeEvent,
    qAlpha,
    qBlue,
    qFuzzyCompare,
    qGray,
    qGreen,
    qIsGray,
    qRed,
    qRgb,
    qRgba
)

QIconEngineV2 = QIconEngine

from PyQt5.QtWidgets import (
    QAbstractButton,
    QAbstractGraphicsShapeItem,
    QAbstractItemDelegate,
    QAbstractItemView,
    QAbstractScrollArea,
    QAbstractSlider,
    QAbstractSpinBox,
    QAction,
    QActionGroup,
    QApplication,
    QBoxLayout,
    QButtonGroup,
    QCalendarWidget,
    QCheckBox,
    QColorDialog,
    QColumnView,
    QComboBox,
    QCommandLinkButton,
    QCommonStyle,
    QCompleter,
    QDataWidgetMapper,
    QDateEdit,
    QDateTimeEdit,
    QDesktopWidget,
    QDial,
    QDialog,
    QDialogButtonBox,
    QDirModel,
    QDockWidget,
    QDoubleSpinBox,
    QErrorMessage,
    QFileDialog,
    QFileIconProvider,
    QFileSystemModel,
    QFocusFrame,
    QFontComboBox,
    QFontDialog,
    QFormLayout,
    QFrame,
    QGesture,
    QGestureEvent,
    QGestureRecognizer,
    QGraphicsAnchor,
    QGraphicsAnchorLayout,
    QGraphicsBlurEffect,
    QGraphicsColorizeEffect,
    QGraphicsDropShadowEffect,
    QGraphicsEffect,
    QGraphicsEllipseItem,
    QGraphicsGridLayout,
    QGraphicsItem,
    QGraphicsItemGroup,
    QGraphicsLayout,
    QGraphicsLayoutItem,
    QGraphicsLineItem,
    QGraphicsLinearLayout,
    QGraphicsObject,
    QGraphicsOpacityEffect,
    QGraphicsPathItem,
    QGraphicsPixmapItem,
    QGraphicsPolygonItem,
    QGraphicsProxyWidget,
    QGraphicsRectItem,
    QGraphicsRotation,
    QGraphicsScale,
    QGraphicsScene,
    QGraphicsSceneContextMenuEvent,
    QGraphicsSceneDragDropEvent,
    QGraphicsSceneEvent,
    QGraphicsSceneHelpEvent,
    QGraphicsSceneHoverEvent,
    QGraphicsSceneMouseEvent,
    QGraphicsSceneMoveEvent,
    QGraphicsSceneResizeEvent,
    QGraphicsSceneWheelEvent,
    QGraphicsSimpleTextItem,
    QGraphicsTextItem,
    QGraphicsTransform,
    QGraphicsView,
    QGraphicsWidget,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QHeaderView,
    QInputDialog,
    QItemDelegate,
    QItemEditorCreatorBase,
    QItemEditorFactory,
    QKeyEventTransition,
    # QKeySequenceEdit,
    QLCDNumber,
    QLabel,
    QLayout,
    QLayoutItem,
    QLineEdit,
    QListView,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMdiArea,
    QMdiSubWindow,
    QMenu,
    QMenuBar,
    QMessageBox,
    QMouseEventTransition,
    # QOpenGLWidget,
    QPanGesture,
    QPinchGesture,
    QPlainTextDocumentLayout,
    QPlainTextEdit,
    QProgressBar,
    QProgressDialog,
    # QProxyStyle,
    QPushButton,
    QRadioButton,
    QRubberBand,
    QScrollArea,
    QScrollBar,
    # QScroller,
    # QScrollerProperties,
    QShortcut,
    QSizeGrip,
    QSizePolicy,
    QSlider,
    QSpacerItem,
    QSpinBox,
    QSplashScreen,
    QSplitter,
    QSplitterHandle,
    QStackedLayout,
    QStackedWidget,
    QStatusBar,
    QStyle,
    QStyleFactory,
    QStyleHintReturn,
    QStyleHintReturnMask,
    QStyleHintReturnVariant,
    QStyleOption,
    QStyleOptionButton,
    QStyleOptionComboBox,
    QStyleOptionComplex,
    QStyleOptionDockWidget,
    QStyleOptionFocusRect,
    QStyleOptionFrame,
    QStyleOptionGraphicsItem,
    QStyleOptionGroupBox,
    QStyleOptionHeader,
    QStyleOptionMenuItem,
    QStyleOptionProgressBar,
    QStyleOptionRubberBand,
    QStyleOptionSizeGrip,
    QStyleOptionSlider,
    QStyleOptionSpinBox,
    QStyleOptionTab,
    QStyleOptionTabBarBase,
    QStyleOptionTabWidgetFrame,
    QStyleOptionTitleBar,
    QStyleOptionToolBar,
    QStyleOptionToolBox,
    QStyleOptionToolButton,
    QStyleOptionViewItem,
    QStylePainter,
    QStyledItemDelegate,
    QSwipeGesture,
    QSystemTrayIcon,
    QTabBar,
    QTabWidget,
    QTableView,
    QTableWidget,
    QTableWidgetItem,
    QTableWidgetSelectionRange,
    QTapAndHoldGesture,
    QTapGesture,
    QTextBrowser,
    QTextEdit,
    QTimeEdit,
    QToolBar,
    QToolBox,
    QToolButton,
    QToolTip,
    QTreeView,
    QTreeWidget,
    QTreeWidgetItem,
    QTreeWidgetItemIterator,
    QUndoCommand,
    QUndoGroup,
    QUndoStack,
    QUndoView,
    QVBoxLayout,
    QWhatsThis,
    QWidget,
    QWidgetAction,
    QWidgetItem,
    QWizard,
    QWizardPage,
    qApp,
    qDrawBorderPixmap,
    qDrawPlainRect,
    qDrawShadeLine,
    qDrawShadePanel,
    qDrawShadeRect,
    qDrawWinButton,
    qDrawWinPanel
)

QStyleOptionViewItemV4 = QStyleOptionViewItem
QStyleOptionViewItemV3 = QStyleOptionViewItem
QStyleOptionViewItemV2 = QStyleOptionViewItem
QStyleOptionToolBoxV2 = QStyleOptionToolBox
QStyleOptionDockWidgetV2 = QStyleOptionDockWidget
QStyleOptionFrameV3 = QStyleOptionFrame
QStyleOptionFrameV2 = QStyleOptionFrame
QStyleOptionProgressBarV2 = QStyleOptionProgressBar
QStyleOptionTabWidgetFrameV2 = QStyleOptionTabWidgetFrame
QStyleOptionTabBarBaseV2 = QStyleOptionTabBarBase
QStyleOptionTabV2 = QStyleOptionTab
QStyleOptionTabV3 = QStyleOptionTab

from PyQt5.QtPrintSupport import (
    QAbstractPrintDialog,
    QPageSetupDialog,
    QPrintDialog,
    QPrintEngine,
    QPrintPreviewDialog,
    QPrintPreviewWidget,
    QPrinter,
    QPrinterInfo
)

try:
    # missing in some older PyQt5 releases (which?)
    from PyQt5.QtWidgets import QWIDGETSIZE_MAX
except ImportError:
    QWIDGETSIZE_MAX = (1 << 24) - 1

try:
    from PyQt5.QtMultimedia import QSound
    __all__.append("QSound")
except ImportError:
    pass


try:
    from PyQt5.QtWidgets import QMacCocoaViewContainer
    from PyQt5.QtMacExtras import QMacPasteboardMime, qRegisterDraggedTypes
    __all__.extend(
        ['QMacPasteboardMime',
         'QMacCocoaViewContainer',
         'qRegisterDraggedTypes']
    )
except ImportError:
    pass

try:
    from PyQt5.QtX11Extras import QX11Info
    QX11Info.isCompositingManagerRunning = staticmethod(lambda: True)
    __all__.append('QX11Info')
except ImportError:
    pass

from PyQt5.QtCore import (
    QStandardPaths as _QStandardPaths, QObject as _QObject
)

from ._utils import obsolete_rename as _obsolete_rename


# recreate Qt4 QDesktopServices
class QDesktopServices(QDesktopServices):
    StandardLocation = _QStandardPaths.StandardLocation
    DocumentsLocation = _QStandardPaths.DocumentsLocation
    FontsLocation = _QStandardPaths.FontsLocation
    ApplicationsLocation = _QStandardPaths.ApplicationsLocation
    MusicLocation = _QStandardPaths.MusicLocation
    MoviesLocation = _QStandardPaths.MoviesLocation
    PicturesLocation = _QStandardPaths.PicturesLocation
    TempLocation = _QStandardPaths.TempLocation
    HomeLocation = _QStandardPaths.HomeLocation
    DataLocation = _QStandardPaths.DataLocation
    CacheLocation = _QStandardPaths.CacheLocation

    @staticmethod
    def storageLocation(location):
        return _QStandardPaths.writableLocation(location)

    @staticmethod
    def displayName(location):
        return _QStandardPaths.displayName(location)


# recreate PyQt4's QPyTextObject
class QPyTextObject(_QObject, QTextObjectInterface):
    pass

_QFileDialog = QFileDialog
# Recreate PyQt4 QFileDialog get{Open,Save}FileName..
class QFileDialog(_QFileDialog):
    @staticmethod
    def getOpenFileName(*args, **kwargs):
        fn, _ = _QFileDialog.getOpenFileName(*args, **kwargs)
        return fn

    @staticmethod
    def getOpenFileNameAndFilter(*args, **kwargs):
        return _QFileDialog.getOpenFileName(*args, **kwargs)

    @staticmethod
    def getOpenFileNames(*args, **kwargs):
        fn, _ = _QFileDialog.getOpenFileNames(*args, **kwargs)
        return fn

    @staticmethod
    def getOpenFileNamesAndFilter(*args, **kwargs):
        return _QFileDialog.getOpenFileNames(*args, **kwargs)

    @staticmethod
    def getSaveFileName(*args, **kwargs):
        fn, _ = _QFileDialog.getSaveFileName(*args, **kwargs)
        return fn

    @staticmethod
    def getSaveFileNameAndFilter(*args, **kwargs):
        return _QFileDialog.getSaveFileName(*args, **kwargs)


# Obsolete members of QHeaderView
QHeaderView.isClickable = lambda self: self.sectionsClickable()
QHeaderView.setClickable = lambda self, clickable: \
    self.setSectionsClickable(clickable)

QHeaderView.isMovable = lambda self: self.sectionsMovable()
QHeaderView.setMovable = lambda self, movable: \
    self.setSectionsMovable(movable)

QHeaderView.resizeMode = lambda self, logicalIndex: \
    self.sectionResizeMode(logicalIndex)
QHeaderView.setResizeMode = lambda self, *args: \
    self.setSectionResizeMode(*args)


def _QApplication_setGraphicsSystem(system):
    warnings.warn("QApplication.setGraphicsSystem() is not available in Qt5",)
QApplication.setGraphicsSystem = _QApplication_setGraphicsSystem


def _QLayout_setMargins(self, margin):
    warnings.warn(
        "QLayout.setMargin is obsolete and removed in PyQt5. "
        "Use setContentsMargins instead.",
        DeprecationWarning, stacklevel=2)
    self.setContentsMargins(margin, margin, margin, margin)
QLayout.setMargin = _QLayout_setMargins

_QGraphicsItem_scale1 = QGraphicsItem.scale


def _QGraphicssItem_scale(self, *args):
    if args:
        warnings.warn(
            "QGraphicsItem.scale(sx, sy) is obsolete and removed in PyQt5. "
            "Use setTransform(QTransform.fromScale(sx, sy), True) instead.",
            DeprecationWarning,
            stacklevel=2
        )
        self.setTransform(QTransform.fromScale(*args), True)
    else:
        return _QGraphicsItem_scale1(self)
QGraphicsItem.scale = _QGraphicssItem_scale


def _QGraphicsItem_translate(self, dx, dy):
    warnings.warn(
        "QGraphicsItem.translate(sx, dy) is obsolete and removed in PyQt5. "
        "Use setTransform(QTransform().translate(dx, dy), True) instead.",
        DeprecationWarning,
        stacklevel=2
    )
    self.setTransform(QTransform().translate(dx, dy), True)
QGraphicsItem.translate = _QGraphicsItem_translate


def _QGraphicsItem_rotate(self, angle):
    warnings.warn(
        "QGraphicsItem.rotate(angle) is obsolete and removed in PyQt5. "
        "Use setRotation(rotation() + angle)",
        DeprecationWarning,
        stacklevel=2
    )
    self.setRotation(self.rotation() + angle)
QGraphicsItem.rotate = _QGraphicsItem_rotate

_QPainter_drawPixmapFragments1 = QPainter.drawPixmapFragments


def _QPainter_drawPixmapFragments(self, a1, a2, *args, **kwargs):
    if isinstance(a2, QPixmap):
        _QPainter_drawPixmapFragments1(self, a1, a2, *args, **kwargs)
    else:
        warnings.warn(
            "QPainter.drawPixmapFragments(list-of-QRectF, list-of-QRectF, "
            "QPixmap, QPainter.PixmapFragmentHints hints=0) is obsolete and "
            "removed in Qt5. "
            "Use QPainter.drawPixmapFragments(list-of-QPainter.PixmapFragment,"
            "QPixmap, QPainter.PixmapFragmentHints hints=0) instead",
            DeprecationWarning,
            stacklevel=2
        )
        targetRects, sourceRects = a1, a2
        pixmap = args[0]
        args = args[1:]
        fragments = [
            QPainter.PixmapFragment.create(
                tr.center(), sr,
                tr.width() / sr.width(),
                tr.height() / sr.height(),
            )
            for (tr, sr) in zip(targetRects, sourceRects)
        ]
        _QPainter_drawPixmapFragments1(
            self, fragments, pixmap, *args, **kwargs)
QPainter.drawPixmapFragments = _QPainter_drawPixmapFragments

QPixmap.grabWidget = staticmethod(lambda w: w.grab())

QColor.light = _obsolete_rename("QColor.light", QColor.lighter)
QColor.dark = _obsolete_rename("QColor.dark", QColor.darker)
QColor.getRgba = _obsolete_rename("QColor.getRgba", QColor.getRgb)

QRegion.unite = _obsolete_rename("QRegion.unite", QRegion.united)
QRegion.subtract = _obsolete_rename("QRegion.subtract", QRegion.subtracted)
QRegion.intersect = _obsolete_rename("QRegion.intersect", QRegion.intersected)
QRegion.eor = _obsolete_rename("QRegion.eor", QRegion.xored)

from PyQt5.QtCore import PYQT_VERSION as _PYQT_VERSION

if _PYQT_VERSION < 0x50502:  # ?
    from AnyQt import _fixes
    _fixes.fix_pyqt5_QGraphicsItem_itemChange()
    del _fixes

from AnyQt.QtCore import Qt as __Qt


# PyQt5 does not expose the obsolete QWheelEvent.orientation and
# QWheelEvent.delta
# Qt5 sends single wheel events if only one of angleDelta.{x,y} is non zero,
# otherwise two events are dispatched. First with the correct combined
# angleDelta and delta=angleDelta.y(), orientation=Qt.Vertical and
# another with null angleDelta and delta=angleDelta.x(),
# orientation = Qt.Horizontal
# (see QWindowSystemInterface::handleWheelEvent for details).
# Here we only report the Qt.Vertical parts of the non axis aligned deltas

def __QWheelEvent_delta(self):
    # type: () -> int
    warnings.warn("QWheelEvent.delta is obsolete and removed in PyQt5. "
                  "use angleDelta instead.",
                  DeprecationWarning, stacklevel=2)
    delta = self.angleDelta()  # type: QPoint
    if delta.x() == 0 and delta.y() != 0:
        # vertical
        return delta.y()
    elif delta.x() != 0 and delta.y() == 0:
        # horizontal
        return delta.x()
    elif delta.x() != 0 and delta.y() != 0:
        # vertical; the first of the assumed Qt4 compatibility events.
        return delta.y()
    elif delta.x() == 0 and delta.y() == 0:
        # horizontal; the second of the assumed Qt4 compatibility events.
        # report a 0 delta
        return 0
    else:
        assert False
QWheelEvent.delta = __QWheelEvent_delta


def __QWheelEvent_orientation(self):
    # type: () -> Qt.Orientation
    warnings.warn("QWheelEvent.orientation is obsolete and removed in PyQt5. "
                  "Use angleDelta instead.",
                  DeprecationWarning, stacklevel=2)
    delta = self.angleDelta()  # type: QPoint
    if delta.x() == 0 and delta.y() != 0:
        return __Qt.Vertical
    elif delta.x() != 0 and delta.y() == 0:
        return __Qt.Horizontal
    elif delta.x() != 0 and delta.y() != 0:
        # vertical; the first assumed Qt4 compatibility events
        return __Qt.Vertical
    elif delta.x() == 0 and delta.y() == 0:
        # horizontal; The second assumed Qt4 compatibility events
        return __Qt.Horizontal
    else:
        assert False
QWheelEvent.orientation = __QWheelEvent_orientation
