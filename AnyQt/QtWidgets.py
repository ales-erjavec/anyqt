from . import _api

__all__ = [
    'QAbstractButton',
    'QAbstractGraphicsShapeItem',
    'QAbstractItemDelegate',
    'QAbstractItemView',
    'QAbstractScrollArea',
    'QAbstractSlider',
    'QAbstractSpinBox',
    'QAction',
    'QActionGroup',
    'QApplication',
    'QBoxLayout',
    'QButtonGroup',
    'QCalendarWidget',
    'QCheckBox',
    'QColorDialog',
    'QColumnView',
    'QComboBox',
    'QCommandLinkButton',
    'QCommonStyle',
    'QCompleter',
    'QDataWidgetMapper',
    'QDateEdit',
    'QDateTimeEdit',
    'QDesktopWidget',
    'QDial',
    'QDialog',
    'QDialogButtonBox',
    'QDirModel',
    'QDockWidget',
    'QDoubleSpinBox',
    'QErrorMessage',
    'QFileDialog',
    'QFileIconProvider',
    'QFileSystemModel',
    'QFocusFrame',
    'QFontComboBox',
    'QFontDialog',
    'QFormLayout',
    'QFrame',
    'QGesture',
    'QGestureEvent',
    'QGestureRecognizer',
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
    'QInputDialog',
    'QItemDelegate',
    'QItemEditorCreatorBase',
    'QItemEditorFactory',
    'QKeyEventTransition',
    'QKeySequenceEdit',
    'QLCDNumber',
    'QLabel',
    'QLayout',
    'QLayoutItem',
    'QLineEdit',
    'QListView',
    'QListWidget',
    'QListWidgetItem',
    'QMacCocoaViewContainer',
    'QMainWindow',
    'QMdiArea',
    'QMdiSubWindow',
    'QMenu',
    'QMenuBar',
    'QMessageBox',
    'QMouseEventTransition',
    'QOpenGLWidget',
    'QPanGesture',
    'QPinchGesture',
    'QPlainTextDocumentLayout',
    'QPlainTextEdit',
    'QProgressBar',
    'QProgressDialog',
    'QProxyStyle',
    'QPushButton',
    'QRadioButton',
    'QRubberBand',
    'QScrollArea',
    'QScrollBar',
    'QScroller',
    'QScrollerProperties',
    'QShortcut',
    'QSizeGrip',
    'QSizePolicy',
    'QSlider',
    'QSpacerItem',
    'QSpinBox',
    'QSplashScreen',
    'QSplitter',
    'QSplitterHandle',
    'QStackedLayout',
    'QStackedWidget',
    'QStatusBar',
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
    'QStyleOptionFocusRect',
    'QStyleOptionFrame',
    'QStyleOptionGraphicsItem',
    'QStyleOptionGroupBox',
    'QStyleOptionHeader',
    'QStyleOptionMenuItem',
    'QStyleOptionProgressBar',
    'QStyleOptionRubberBand',
    'QStyleOptionSizeGrip',
    'QStyleOptionSlider',
    'QStyleOptionSpinBox',
    'QStyleOptionTab',
    'QStyleOptionTabBarBase',
    'QStyleOptionTabWidgetFrame',
    'QStyleOptionTitleBar',
    'QStyleOptionToolBar',
    'QStyleOptionToolBox',
    'QStyleOptionToolButton',
    'QStyleOptionViewItem',
    'QStylePainter',
    'QStyledItemDelegate',
    'QSwipeGesture',
    'QSystemTrayIcon',
    'QTabBar',
    'QTabWidget',
    'QTableView',
    'QTableWidget',
    'QTableWidgetItem',
    'QTableWidgetSelectionRange',
    'QTapAndHoldGesture',
    'QTapGesture',
    'QTextBrowser',
    'QTextEdit',
    'QTimeEdit',
    'QToolBar',
    'QToolBox',
    'QToolButton',
    'QToolTip',
    'QTreeView',
    'QTreeWidget',
    'QTreeWidgetItem',
    'QTreeWidgetItemIterator',
    'QUndoCommand',
    'QUndoGroup',
    'QUndoStack',
    'QUndoView',
    'QVBoxLayout',
    'QWIDGETSIZE_MAX',
    'QWhatsThis',
    'QWidget',
    'QWidgetAction',
    'QWidgetItem',
    'QWizard',
    'QWizardPage',
    'qApp',
    'qDrawBorderPixmap',
    'qDrawPlainRect',
    'qDrawShadeLine',
    'qDrawShadePanel',
    'qDrawShadeRect',
    'qDrawWinButton',
    'qDrawWinPanel'
]

if _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import PYQT_VERSION as _PYQT_VERSION

    if _PYQT_VERSION < 0x50502:  # ?
        from . import _fixes
        _fixes.fix_pyqt5_QGraphicsItem_itemChange()
        del _fixes

elif _api.USED_API == _api.QT_API_PYQT4:
    from PyQt4 import QtGui as _QtGui
    __missing__ = [
        'QKeySequenceEdit',
        'QOpenGLWidget',
        'QProxyStyle',
        'QScroller',
        'QScrollerProperties',
    ]

    globals().update(
        {name: getattr(_QtGui, name) for name in __all__
         if name not in __missing__}
    )
    # Alias the QStyleOption version classes
    QStyleOptionViewItem = _QtGui.QStyleOptionViewItemV4,
    QStyleOptionToolBox = _QtGui.QStyleOptionToolBoxV2,
    QStyleOptionDockWidget = _QtGui.QStyleOptionDockWidgetV2
    QStyleOptionFrame = _QtGui.QStyleOptionFrameV3
    QStyleOptionProgressBar = _QtGui.QStyleOptionProgressBarV2
    QStyleOptionTabWidgetFrame = _QtGui.QStyleOptionTabWidgetFrameV2
    QStyleOptionTabBarBase = _QtGui.QStyleOptionTabBarBaseV2
    QStyleOptionTab = _QtGui.QStyleOptionTabV2
    del _QtGui

elif _api.USED_API == _api.QT_API_PYSIDE:
    from PySide import QtGui as _QtGui
    __missing__ = [
        'QKeySequenceEdit',
        'QOpenGLWidget',
        'QProxyStyle',
        'QScroller',
        'QScrollerProperties',
    ]

    globals().update(
        {name: getattr(_QtGui, name) for name in __all__
         if name not in __missing__}
    )
    # Alias the QStyleOption version classes
    QStyleOptionViewItem = _QtGui.QStyleOptionViewItemV4,
    QStyleOptionToolBox = _QtGui.QStyleOptionToolBoxV2,
    QStyleOptionDockWidget = _QtGui.QStyleOptionDockWidgetV2
    QStyleOptionFrame = _QtGui.QStyleOptionFrameV3
    QStyleOptionProgressBar = _QtGui.QStyleOptionProgressBarV2
    QStyleOptionTabWidgetFrame = _QtGui.QStyleOptionTabWidgetFrameV2
    QStyleOptionTabBarBase = _QtGui.QStyleOptionTabBarBaseV2
    QStyleOptionTab = _QtGui.QStyleOptionTabV3
    del _QtGui

if _api.USED_API != _api.QT_API_PYQT5:
    from .QtGui import QColor as _QColor
    _QColorDialog = QColorDialog

    class QColorDialog(_QColorDialog):
        @staticmethod
        def customColor(index):
            return _QColor.fromRgb(_QColorDialog.customColor(index))

        @staticmethod
        def setCustomColor(index, color):
            _QColorDialog.setCustomColor(index, color.rgba())

        @staticmethod
        def setStandardColor(index, color):
            _QColorDialog.setStandardColor(index, color.rgba())
