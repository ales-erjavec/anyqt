from warnings import warn

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

if _api.USED_API == _api.QT_API_PYQT6:
    from PyQt6.QtWidgets import *
    from PyQt6.QtGui import QAction, QActionGroup
    from PyQt6.QtGui import QUndoCommand, QUndoStack, QUndoGroup
    from PyQt6.QtGui import QShortcut
    QStyle.State = QStyle.StateFlag
    QStyle.SubControls = QStyle.SubControl
elif _api.USED_API == _api.QT_API_PYQT5:
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

    # Some extra forward compatibility
    QHeaderView.setSectionResizeMode = lambda self, *args: self.setResizeMode(*args)
    QHeaderView.sectionResizeMode = lambda self: self.resizeMode()
    QHeaderView.sectionsClickable = lambda self: self.isClickable()
    QHeaderView.setSectionsClickable = \
        lambda self, clickable: self.setClickable(clickable)
    QHeaderView.sectionsMovable = lambda self: self.isMovable()
    QHeaderView.setSectionsMovable = \
        lambda self, movable: self.setMovable(movable)

    from PyQt4 import QtCore as __QtCore
    QWidget = _QtGui.QWidget
    __QPixmap = _QtGui.QPixmap

    def _QWidget_grab(self, rect=__QtCore.QRect(0, 0, -1, -1)):
        if not rect.isValid():
            return __QPixmap.grabWidget(self)
        else:
            return __QPixmap.grabWidget(self, rect)

    QWidget.grab = _QWidget_grab
    del _QtGui, __QtCore

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

    # Some extra forward compatibility
    QHeaderView.setSectionResizeMode = lambda self, *args: self.setResizeMode(*args)
    QHeaderView.sectionResizeMode = lambda self: self.resizeMode()
    QHeaderView.sectionsClickable = lambda self: self.isClickable()
    QHeaderView.setSectionsClickable = \
        lambda self, clickable: self.setClickable(clickable)
    QHeaderView.sectionsMovable = lambda self: self.isMovable()
    QHeaderView.setSectionsMovable = \
        lambda self, movable: self.setMovable(movable)

    from PySide import QtCore as __QtCore
    QWidget = _QtGui.QWidget
    __QPixmap = _QtGui.QPixmap

    def _QWidget_grab(self, rect=__QtCore.QRect(0, 0, -1, -1)):
        if not rect.isValid():
            return __QPixmap.grabWidget(self)
        else:
            return __QPixmap.grabWidget(self, rect)

    QWidget.grab = _QWidget_grab
    del _QtGui, __QtCore

elif _api.USED_API == _api.QT_API_PYSIDE2:
    from PySide2.QtWidgets import *

try:
    QWIDGETSIZE_MAX  # Missing in older PyQt5, PyQt4
except NameError:
    QWIDGETSIZE_MAX = (1 << 24) - 1


if not hasattr(QWidget, "screen"):
    def QWidget_screen(self):
        screens = QApplication.screens()
        desktop = __QApplication_desktop()  # avoid deprecation warning
        screen_num = desktop.screenNumber(self)
        if 0 <= screen_num < len(screens):
            return screens[screen_num]
        else:
            return QApplication.primaryScreen()
    QWidget.screen = QWidget_screen
    del QWidget_screen

if hasattr(QWidget, "getContentsMargins"):
    def QWidget_getContentsMargins(self):
        warn("QWidget.getContentsMargins is obsolete and is removed in Qt6",
             DeprecationWarning, stacklevel=2)
        return __QWidget_getContentsMargins(self)
    __QWidget_getContentsMargins = QWidget.getContentsMargins
    QWidget.getContentsMargins = QWidget_getContentsMargins

if hasattr(QLineEdit, "getTextMargins"):
    def __QLineEdit_getTextMargins(self):
        warn("QLineEdit.getTextMargins is deprecated and will be removed.",
             DeprecationWarning, stacklevel=2)
        m = self.textMargins()
        return m.left(), m.top(), m.right(), m.bottom()
    QLineEdit.getTextMargins = __QLineEdit_getTextMargins
    del __QLineEdit_getTextMargins

if not hasattr(QAbstractItemView, "viewOptions"):
    def __QAbstractItemView_viewOptions(self):
        opt = QStyleOptionViewItem()
        self.initViewItemOption(opt)
        return opt
    QAbstractItemView.viewOptions = __QAbstractItemView_viewOptions
    del __QAbstractItemView_viewOptions
elif not hasattr(QAbstractItemView, "initViewItemOption"):
    def __QAbstractItemView_initViewItemOption(self, option):
        opt = self.viewOptions()
        option.initFrom(self)
        option.state = opt.state
        option.font = opt.font
        option.decorationSize = opt.decorationSize
        option.decorationPosition = opt.decorationPosition
        option.decorationAlignment = opt.decorationAlignment
        option.displayAlignment = opt.displayAlignment
        option.textElideMode = opt.textElideMode
        option.rect = opt.rect
        option.showDecorationSelected = opt.showDecorationSelected
        option.features = opt.features
        option.locale = opt.locale
        option.widget = opt.widget
    QAbstractItemView.initViewItemOption = __QAbstractItemView_initViewItemOption
    del __QAbstractItemView_initViewItemOption

from AnyQt.QtCore import QModelIndex as __QModelIndex


def __QAbstractItemView_itemDelegate(self, *args):
    if args and isinstance(args[0], __QModelIndex):
        return self.itemDelegateForIndex(*args)
    return __QAbstractItemView_itemDelegate_orig(self, *args)


if not hasattr(QAbstractItemView, "itemDelegateForIndex"):
    def __QAbstractItemView_itemDelegateForIndex(self, index):
        return __QAbstractItemView_itemDelegate_orig(self, index)
    QAbstractItemView.itemDelegateForIndex = __QAbstractItemView_itemDelegateForIndex

__QAbstractItemView_itemDelegate_orig = QAbstractItemView.itemDelegate
QAbstractItemView.itemDelegate = __QAbstractItemView_itemDelegate


if hasattr(QApplication, "desktop"):
    def QApplication_desktop():
        warn("QApplication.desktop is obsolete and is removed in Qt6",
             DeprecationWarning, stacklevel=2)
        return __QApplication_desktop()
    __QApplication_desktop = QApplication.desktop
    QApplication.desktop = staticmethod(QApplication_desktop)
    del QApplication_desktop

if not hasattr(QPlainTextEdit, "setTabStopDistance"):
    def __QPlainTextEdit_setTabStopDistance(self, width: float):
        self.setTabStopWidth(int(width))
    def __QPlainTextEdit_tabStopDistance(self) -> float:
        return float(self.tabStopWidth())
    QPlainTextEdit.setTabStopDistance = __QPlainTextEdit_setTabStopDistance
    QPlainTextEdit.tabStopDistance = __QPlainTextEdit_tabStopDistance


if not hasattr(QTextEdit, "setTabStopDistance"):
    def __QTextEdit_setTabStopDistance(self, width: float):
        self.setTabStopWidth(int(width))
    def __QTextEdit_tabStopDistance(self) -> float:
        return float(self.tabStopWidth())
    QTextEdit.setTabStopDistance = __QTextEdit_setTabStopDistance
    QTextEdit.tabStopDistance = __QTextEdit_tabStopDistance


from AnyQt.QtCore import Signal, Slot

if not hasattr(QButtonGroup, "idClicked"):
    class QButtonGroup(QButtonGroup):
        idClicked = Signal(int)
        idPressed = Signal(int)
        idReleased = Signal(int)
        idToggled = Signal(int, bool)

        def __init__(self, *args, **kwargs):
            buttonClicked = kwargs.pop("buttonClicked", None)
            buttonPressed = kwargs.pop("buttonPressed", None)
            buttonReleased = kwargs.pop("buttonReleased", None)
            buttonToggled = kwargs.pop("buttonToggled", None)
            super().__init__(*args, **kwargs)
            self.buttonClicked.connect(self.__button_clicked)
            self.buttonPressed.connect(self.__button_pressed)
            self.buttonReleased.connect(self.__button_released)
            self.buttonToggled.connect(self.__button_toggled)
            if buttonClicked is not None:
                self.buttonClicked.connect(buttonClicked)
            if buttonPressed is not None:
                self.buttonPressed.connect(buttonPressed)
            if buttonReleased is not None:
                self.buttonReleased.connect(buttonReleased)
            if buttonToggled is not None:
                self.buttonToggled.connect(buttonToggled)

        @Slot(QAbstractButton)
        def __button_clicked(self, button):
            self.idClicked.emit(self.id(button))

        @Slot(QAbstractButton)
        def __button_pressed(self, button):
            self.idPressed.emit(self.id(button))

        @Slot(QAbstractButton)
        def __button_released(self, button):
            self.idReleased.emit(self.id(button))

        @Slot(QAbstractButton, bool)
        def __button_toggled(self, button, checked):
            self.idToggled.emit(self.id(button), checked)

if not hasattr(QComboBox, "textActivated"):
    class QComboBox(QComboBox):
        textActivated = Signal(str)
        textHighlighted = Signal(str)

        def __init__(self, *args, **kwargs):
            activated = kwargs.pop("activated", None)
            highlighted = kwargs.pop("highlighted", None)
            super().__init__(*args, **kwargs)
            self.activated[int].connect(self.__activated)
            self.highlighted[int].connect(self.__highlighted)
            if activated is not None:
                self.activated.connect(activated)
            if highlighted is not None:
                self.highlighted.connect(highlighted)

        @Slot(int)
        def __activated(self, index):
            self.textActivated.emit(self.itemText(index))

        @Slot(int)
        def __highlighted(self, index):
            self.textHighlighted.emit(self.itemText(index))

del Signal, Slot

_api.apply_global_fixes(globals())
