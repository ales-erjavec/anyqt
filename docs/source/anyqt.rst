.. module:: AnyQt


:mod:`AnyQt`
============

.. autofunction:: availableapi

.. autofunction:: setpreferredapi

.. autofunction:: selectapi

.. autodata:: USED_API


:mod:`AnyQt.QtCore`
-------------------

Export a Qt5 compatible QtCore module.

* PyQt5: Full :mod:`PyQt5.QtCore` module is reexported
* PyQt4: Full :mod:`PyQt4.QtCore` module is reexported and in addition
  `QAbstractProxyModel`, `QIdentityProxyModel`, `QItemSelection`,
  `QItemSelectionModel`, `QItemSelectionRange`, `QSortFilterProxyModel`,
  `QStringListModel`, are imported from :mod:`PyQt4.QtGui`

.. note::
    The folowing are not available when using :mod:`PyQt5`:
        * 'QAbstractFileEngine'
        * 'QAbstractFileEngineHandler'
        * 'QAbstractFileEngineIterator'
        * 'QFSFileEngine'
        * 'QPyNullVariant'
        * 'QSystemLocale'
        * 'SIGNAL'
        * 'SLOT'
        * 'qInstallMsgHandler'
        * 'qSwap'

.. note::
    QUrl in Qt5 has a different interface (some functionality was split into
    QUrlParse). No attempt is made to taper over the differences.

Use `AnyQt.QtCore.QT_VERSION` to check if a feature is present.


:mod:`AnyQt.QtGui`
------------------

Export a Qt5 compatible QtGui module.

* PyQt5: Full :mod:`PyQt5.QtGui` module is reexported
* PyQt4: The following members are imported from :mod:`PyQt4.QtGui`:
    * 'QAbstractTextDocumentLayout'
    * 'QActionEvent'
    * 'QBitmap'
    * 'QBrush'
    * 'QClipboard'
    * 'QCloseEvent'
    * 'QColor'
    * 'QConicalGradient'
    * 'QContextMenuEvent'
    * 'QCursor'
    * 'QDesktopServices'
    * 'QDoubleValidator'
    * 'QDrag'
    * 'QDragEnterEvent'
    * 'QDragLeaveEvent'
    * 'QDragMoveEvent'
    * 'QDropEvent'
    * 'QFileOpenEvent'
    * 'QFocusEvent'
    * 'QFont'
    * 'QFontDatabase'
    * 'QFontInfo'
    * 'QFontMetrics'
    * 'QFontMetricsF'
    * 'QGlyphRun'
    * 'QGradient'
    * 'QHelpEvent'
    * 'QHideEvent'
    * 'QHoverEvent'
    * 'QIcon'
    * 'QIconDragEvent'
    * 'QIconEngine'
    * 'QImage'
    * 'QImageIOHandler'
    * 'QImageReader'
    * 'QImageWriter'
    * 'QInputEvent'
    * 'QInputMethodEvent'
    * 'QIntValidator'
    * 'QKeyEvent'
    * 'QKeySequence'
    * 'QLinearGradient'
    * 'QMatrix2x2'
    * 'QMatrix2x3'
    * 'QMatrix2x4'
    * 'QMatrix3x2'
    * 'QMatrix3x3'
    * 'QMatrix3x4'
    * 'QMatrix4x2'
    * 'QMatrix4x3'
    * 'QMatrix4x4'
    * 'QMouseEvent'
    * 'QMoveEvent'
    * 'QMovie'
    * 'QPaintDevice'
    * 'QPaintEngine'
    * 'QPaintEngineState'
    * 'QPaintEvent'
    * 'QPainter'
    * 'QPainterPath'
    * 'QPainterPathStroker'
    * 'QPalette'
    * 'QPen'
    * 'QPicture'
    * 'QPictureIO'
    * 'QPixmap'
    * 'QPixmapCache'
    * 'QPolygon'
    * 'QPolygonF'
    * 'QQuaternion'
    * 'QRadialGradient'
    * 'QRawFont'
    * 'QRegExpValidator'
    * 'QRegion'
    * 'QResizeEvent'
    * 'QSessionManager'
    * 'QShortcutEvent'
    * 'QShowEvent'
    * 'QStandardItem'
    * 'QStandardItemModel'
    * 'QStaticText'
    * 'QStatusTipEvent'
    * 'QSyntaxHighlighter'
    * 'QTabletEvent'
    * 'QTextBlock'
    * 'QTextBlockFormat'
    * 'QTextBlockGroup'
    * 'QTextBlockUserData'
    * 'QTextCharFormat'
    * 'QTextCursor'
    * 'QTextDocument'
    * 'QTextDocumentFragment'
    * 'QTextDocumentWriter'
    * 'QTextFormat'
    * 'QTextFragment'
    * 'QTextFrame'
    * 'QTextFrameFormat'
    * 'QTextImageFormat'
    * 'QTextInlineObject'
    * 'QTextItem'
    * 'QTextLayout'
    * 'QTextLength'
    * 'QTextLine'
    * 'QTextList'
    * 'QTextListFormat'
    * 'QTextObject'
    * 'QTextObjectInterface'
    * 'QTextOption'
    * 'QTextTable'
    * 'QTextTableCell'
    * 'QTextTableCellFormat'
    * 'QTextTableFormat'
    * 'QTouchEvent'
    * 'QTransform'
    * 'QValidator'
    * 'QVector2D'
    * 'QVector3D'
    * 'QVector4D'
    * 'QWhatsThisClickedEvent'
    * 'QWheelEvent'
    * 'QWindowStateChangeEvent'
    * 'qAlpha'
    * 'qBlue'
    * 'qFuzzyCompare'
    * 'qGray'
    * 'qGreen'
    * 'qIsGray'
    * 'qRed'
    * 'qRgb'
    * 'qRgba'

* When using a Qt4 API, the :class:`QWheelEvent` gains a Qt5 compatible
  :func:`angleDelta` method.


:mod:`AnyQt.QtWidgets`
----------------------

Export a Qt5 compatible QtWidgets module

* PyQt5: Full :mod:`PyQt5.QtWidgets` module is reexported
* PyQt4: The following members from PyQt4.QtGui are exported:
    * 'QAbstractButton'
    * 'QAbstractGraphicsShapeItem'
    * 'QAbstractItemDelegate'
    * 'QAbstractItemView'
    * 'QAbstractScrollArea'
    * 'QAbstractSlider'
    * 'QAbstractSpinBox'
    * 'QAction'
    * 'QActionGroup'
    * 'QApplication'
    * 'QBoxLayout'
    * 'QButtonGroup'
    * 'QCalendarWidget'
    * 'QCheckBox'
    * 'QColorDialog'
    * 'QColumnView'
    * 'QComboBox'
    * 'QCommandLinkButton'
    * 'QCommonStyle'
    * 'QCompleter'
    * 'QDataWidgetMapper'
    * 'QDateEdit'
    * 'QDateTimeEdit'
    * 'QDesktopWidget'
    * 'QDial'
    * 'QDialog'
    * 'QDialogButtonBox'
    * 'QDirModel'
    * 'QDockWidget'
    * 'QDoubleSpinBox'
    * 'QErrorMessage'
    * 'QFileDialog'
    * 'QFileIconProvider'
    * 'QFileSystemModel'
    * 'QFocusFrame'
    * 'QFontComboBox'
    * 'QFontDialog'
    * 'QFormLayout'
    * 'QFrame'
    * 'QGesture'
    * 'QGestureEvent'
    * 'QGestureRecognizer'
    * 'QGraphicsAnchor'
    * 'QGraphicsAnchorLayout'
    * 'QGraphicsBlurEffect'
    * 'QGraphicsColorizeEffect'
    * 'QGraphicsDropShadowEffect'
    * 'QGraphicsEffect'
    * 'QGraphicsEllipseItem'
    * 'QGraphicsGridLayout'
    * 'QGraphicsItem'
    * 'QGraphicsItemGroup'
    * 'QGraphicsLayout'
    * 'QGraphicsLayoutItem'
    * 'QGraphicsLineItem'
    * 'QGraphicsLinearLayout'
    * 'QGraphicsObject'
    * 'QGraphicsOpacityEffect'
    * 'QGraphicsPathItem'
    * 'QGraphicsPixmapItem'
    * 'QGraphicsPolygonItem'
    * 'QGraphicsProxyWidget'
    * 'QGraphicsRectItem'
    * 'QGraphicsRotation'
    * 'QGraphicsScale'
    * 'QGraphicsScene'
    * 'QGraphicsSceneContextMenuEvent'
    * 'QGraphicsSceneDragDropEvent'
    * 'QGraphicsSceneEvent'
    * 'QGraphicsSceneHelpEvent'
    * 'QGraphicsSceneHoverEvent'
    * 'QGraphicsSceneMouseEvent'
    * 'QGraphicsSceneMoveEvent'
    * 'QGraphicsSceneResizeEvent'
    * 'QGraphicsSceneWheelEvent'
    * 'QGraphicsSimpleTextItem'
    * 'QGraphicsTextItem'
    * 'QGraphicsTransform'
    * 'QGraphicsView'
    * 'QGraphicsWidget'
    * 'QGridLayout'
    * 'QGroupBox'
    * 'QHBoxLayout'
    * 'QHeaderView'
    * 'QInputDialog'
    * 'QItemDelegate'
    * 'QItemEditorCreatorBase'
    * 'QItemEditorFactory'
    * 'QKeyEventTransition'
    * 'QLCDNumber'
    * 'QLabel'
    * 'QLayout'
    * 'QLayoutItem'
    * 'QLineEdit'
    * 'QListView'
    * 'QListWidget'
    * 'QListWidgetItem'
    * 'QMacCocoaViewContainer'
    * 'QMainWindow'
    * 'QMdiArea'
    * 'QMdiSubWindow'
    * 'QMenu'
    * 'QMenuBar'
    * 'QMessageBox'
    * 'QMouseEventTransition'
    * 'QPanGesture'
    * 'QPinchGesture'
    * 'QPlainTextDocumentLayout'
    * 'QPlainTextEdit'
    * 'QProgressBar'
    * 'QProgressDialog'
    * 'QPushButton'
    * 'QRadioButton'
    * 'QRubberBand'
    * 'QScrollArea'
    * 'QScrollBar'
    * 'QShortcut'
    * 'QSizeGrip'
    * 'QSizePolicy'
    * 'QSlider'
    * 'QSpacerItem'
    * 'QSpinBox'
    * 'QSplashScreen'
    * 'QSplitter'
    * 'QSplitterHandle'
    * 'QStackedLayout'
    * 'QStackedWidget'
    * 'QStatusBar'
    * 'QStyle'
    * 'QStyleFactory'
    * 'QStyleHintReturn'
    * 'QStyleHintReturnMask'
    * 'QStyleHintReturnVariant'
    * 'QStyleOption'
    * 'QStyleOptionButton'
    * 'QStyleOptionComboBox'
    * 'QStyleOptionComplex'
    * 'QStyleOptionDockWidget'
    * 'QStyleOptionFocusRect'
    * 'QStyleOptionFrame'
    * 'QStyleOptionGraphicsItem'
    * 'QStyleOptionGroupBox'
    * 'QStyleOptionHeader'
    * 'QStyleOptionMenuItem'
    * 'QStyleOptionProgressBar'
    * 'QStyleOptionRubberBand'
    * 'QStyleOptionSizeGrip'
    * 'QStyleOptionSlider'
    * 'QStyleOptionSpinBox'
    * 'QStyleOptionTab'
    * 'QStyleOptionTabBarBase'
    * 'QStyleOptionTabWidgetFrame'
    * 'QStyleOptionTitleBar'
    * 'QStyleOptionToolBar'
    * 'QStyleOptionToolBox'
    * 'QStyleOptionToolButton'
    * 'QStyleOptionViewItem'
    * 'QStylePainter'
    * 'QStyledItemDelegate'
    * 'QSwipeGesture'
    * 'QSystemTrayIcon'
    * 'QTabBar'
    * 'QTabWidget'
    * 'QTableView'
    * 'QTableWidget'
    * 'QTableWidgetItem'
    * 'QTableWidgetSelectionRange'
    * 'QTapAndHoldGesture'
    * 'QTapGesture'
    * 'QTextBrowser'
    * 'QTextEdit'
    * 'QTimeEdit'
    * 'QToolBar'
    * 'QToolBox'
    * 'QToolButton'
    * 'QToolTip'
    * 'QTreeView'
    * 'QTreeWidget'
    * 'QTreeWidgetItem'
    * 'QTreeWidgetItemIterator'
    * 'QUndoCommand'
    * 'QUndoGroup'
    * 'QUndoStack'
    * 'QUndoView'
    * 'QVBoxLayout'
    * 'QWIDGETSIZE_MAX'
    * 'QWhatsThis'
    * 'QWidget'
    * 'QWidgetAction'
    * 'QWidgetItem'
    * 'QWizard'
    * 'QWizardPage'
    * 'qApp'
    * 'qDrawBorderPixmap'
    * 'qDrawPlainRect'
    * 'qDrawShadeLine'
    * 'qDrawShadePanel'
    * 'qDrawShadeRect'
    * 'qDrawWinButton'
    * 'qDrawWinPanel'


..
  Known unavailable in PyQt4
    * 'QKeySequenceEdit',
    * 'QOpenGLWidget',
    * 'QProxyStyle',
    * 'QScroller',
    * 'QScrollerProperties',


* :class:`QFileDialog`\'s get{Open,Save}Filename provide a consistent PyQt5
  compatible interface (i.e. they return `(filename: str, format: str)` tuple.

* :class:`QHeaderView` provides a consistent forward compatible methods:
     * :func:`QHeaderView.setSectionResizeMode`
     * :func:`QHeaderView.sectionResizeMode`
     * :func:`QHeaderView.sectionsClickable`
     * :func:`QHeaderView.setSectionsClickable`
     * :func:`QHeaderView.sectionsMovable`
     * :func:`QHeaderView.setSectionsMovable`

* The versioned :class:`QStyleOption` subclasses in :mod:`PyQt4.QtGui` are
  renamed to their unversioned conterpart (e.g. the
  :class:`QStyleOptionViewItemV4` is exported as
  :class:`QStyleOptionViewItem`

* A forward compatile :func:`QWidget.grab` method is made available when
  using a Qt4 backend

:mod:`AnyQt.QtPrintSupport`
---------------------------

Export a Qt5 compatible QtPrintSupport module.


:mod:`AnyQt.QtWebKit`
---------------------

Export a Qt5 compatible QtWebKit module.


:mod:`AnyQt.QtWebKitWidgets`
----------------------------

Export a Qt5 compatible QtWebKitWidgets module.


:mod:`AnyQt.QtNetwork`
----------------------

:mod:`AnyQt.QtDBus`
-------------------

:mod:`AnyQt.QtDesigner`
-----------------------

:mod:`AnyQt.QtHelp`
-------------------

:mod:`AnyQt.QtMacExtras`
------------------------

* PyQt5: Full :mod:`PyQt5.QtMacExtras` is reexported
* PyQt4: :class:`QMacPasteboardMime` is imported from :mod:`PyQt4.QtGui`

:mod:`AnyQt.QtMultimedia`
-------------------------

.. :mod:`AnyQt.QtMultimediaWidgets`
   --------------------------------

:mod:`AnyQt.QtOpenGL`
---------------------

:mod:`AnyQt.QtSql`
------------------

:mod:`AnyQt.QtSvg`
------------------

:mod:`AnyQt.QtTest`
-------------------

:mod:`AnyQt.QtWinExtras`
------------------------

:mod:`AnyQt.QtXml`
------------------

:mod:`AnyQt.QtXmlPatterns`
--------------------------