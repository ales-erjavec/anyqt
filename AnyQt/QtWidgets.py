from . import _api

# Names imported from Qt4's QtGui module
__Qt4_QtGui = [
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
    # 'QKeySequenceEdit',
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
    # 'QOpenGLWidget',
    'QPanGesture',
    'QPinchGesture',
    'QPlainTextDocumentLayout',
    'QPlainTextEdit',
    'QProgressBar',
    'QProgressDialog',
    # 'QProxyStyle',
    'QPushButton',
    'QRadioButton',
    'QRubberBand',
    'QScrollArea',
    'QScrollBar',
    # 'QScroller',
    # 'QScrollerProperties',
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
    globals().update(
        {name: getattr(_QtGui, name)
         for name in __Qt4_QtGui if hasattr(_QtGui, name)}
    )

    # Alias the QStyleOption version classes
    QStyleOptionViewItem = _QtGui.QStyleOptionViewItemV4
    QStyleOptionViewItem_ = _QtGui.QStyleOptionViewItem
    QStyleOptionToolBox = _QtGui.QStyleOptionToolBoxV2
    QStyleOptionToolBox_ = _QtGui.QStyleOptionToolBox
    QStyleOptionDockWidget = _QtGui.QStyleOptionDockWidgetV2
    QStyleOptionDockWidget_ = _QtGui.QStyleOptionDockWidget
    QStyleOptionFrame = _QtGui.QStyleOptionFrameV3
    QStyleOptionFrame_ = _QtGui.QStyleOptionFrame
    QStyleOptionProgressBar = _QtGui.QStyleOptionProgressBarV2
    QStyleOptionProgressBar_ = _QtGui.QStyleOptionProgressBar
    QStyleOptionTabWidgetFrame = _QtGui.QStyleOptionTabWidgetFrameV2
    QStyleOptionTabWidgetFrame_ = _QtGui.QStyleOptionTabWidgetFrame
    QStyleOptionTabBarBase = _QtGui.QStyleOptionTabBarBaseV2
    QStyleOptionTabBarBase_ = _QtGui.QStyleOptionTabBarBase
    QStyleOptionTab = _QtGui.QStyleOptionTabV3
    QStyleOptionTab_ = _QtGui.QStyleOptionTab

    # PyQt5's version of QFileDialog's static methods
    class QFileDialog(_QtGui.QFileDialog):
        getOpenFileName = _QtGui.QFileDialog.getOpenFileNameAndFilter
        getOpenFileNames = _QtGui.QFileDialog.getOpenFileNamesAndFilter
        getSaveFileName = _QtGui.QFileDialog.getSaveFileNameAndFilter

    del _QtGui

elif _api.USED_API == _api.QT_API_PYSIDE:
    from PySide import QtGui as _QtGui
    globals().update(
        {name: getattr(_QtGui, name)
         for name in __Qt4_QtGui if hasattr(_QtGui, name)}
    )

    # Alias the QStyleOption version classes
    QStyleOptionViewItem = _QtGui.QStyleOptionViewItemV4
    QStyleOptionViewItem_ = _QtGui.QStyleOptionViewItem
    QStyleOptionToolBox = _QtGui.QStyleOptionToolBoxV2
    QStyleOptionToolBox_ = _QtGui.QStyleOptionToolBox
    QStyleOptionDockWidget = _QtGui.QStyleOptionDockWidgetV2
    QStyleOptionDockWidget_ = _QtGui.QStyleOptionDockWidget
    QStyleOptionFrame = _QtGui.QStyleOptionFrameV3
    QStyleOptionFrame_ = _QtGui.QStyleOptionFrame
    QStyleOptionProgressBar = _QtGui.QStyleOptionProgressBarV2
    QStyleOptionProgressBar_ = _QtGui.QStyleOptionProgressBar
    if hasattr(_QtGui, "QStyleOptionTabWidgetFrameV2"):
        QStyleOptionTabWidgetFrame = _QtGui.QStyleOptionTabWidgetFrameV2
        QStyleOptionTabWidgetFrame_ = _QtGui.QStyleOptionTabWidgetFrame
    else:
        QStyleOptionTabWidgetFrame = _QtGui.QStyleOptionTabWidgetFrame
        QStyleOptionTabWidgetFrame_ = _QtGui.QStyleOptionTabWidgetFrame

    QStyleOptionTabBarBase = _QtGui.QStyleOptionTabBarBaseV2
    QStyleOptionTabBarBase_ = _QtGui.QStyleOptionTabBarBase
    QStyleOptionTab = _QtGui.QStyleOptionTabV3
    QStyleOptionTab_ = _QtGui.QStyleOptionTab

    del _QtGui


try:
    QWIDGETSIZE_MAX  # Missing in older PyQt5, PyQt4
except NameError:
    QWIDGETSIZE_MAX = (1 << 24) - 1
