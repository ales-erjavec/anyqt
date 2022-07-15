from . import _api

# List names imported from Qt4's QtCore module
__Qt4_QtCore = [
    'QAbstractAnimation',
    'QAbstractEventDispatcher',
    'QAbstractFileEngine',
    'QAbstractFileEngineHandler',
    'QAbstractFileEngineIterator',
    'QAbstractItemModel',
    'QAbstractListModel',
    'QAbstractState',
    'QAbstractTableModel',
    'QAbstractTransition',
    'QAnimationGroup',
    'QBasicTimer',
    'QBitArray',
    'QBuffer',
    'QByteArray',
    'QByteArrayMatcher',
    'QChildEvent',
    'QCoreApplication',
    'QCryptographicHash',
    'QDataStream',
    'QDate',
    'QDateTime',
    'QDir',
    'QDirIterator',
    'QDynamicPropertyChangeEvent',
    'QEasingCurve',
    'QElapsedTimer',
    'QEvent',
    'QEventLoop',
    'QEventTransition',
    'QFSFileEngine',
    'QFile',
    'QFileInfo',
    'QFileSystemWatcher',
    'QFinalState',
    'QGenericArgument',
    'QGenericReturnArgument',
    'QHistoryState',
    'QIODevice',
    'QLibrary',
    'QLibraryInfo',
    'QLine',
    'QLineF',
    'QLocale',
    'QMargins',
    'QMetaClassInfo',
    'QMetaEnum',
    'QMetaMethod',
    'QMetaObject',
    'QMetaProperty',
    'QMetaType',
    'QMimeData',
    'QModelIndex',
    'QMutex',
    'QMutexLocker',
    'QObject',
    'QObjectCleanupHandler',
    'QParallelAnimationGroup',
    'QPauseAnimation',
    'QPersistentModelIndex',
    'QPluginLoader',
    'QPoint',
    'QPointF',
    'QProcess',
    'QProcessEnvironment',
    'QPropertyAnimation',
    'QPyNullVariant',
    'QReadLocker',
    'QReadWriteLock',
    'QRect',
    'QRectF',
    'QRegExp',
    'QResource',
    'QRunnable',
    'QSemaphore',
    'QSequentialAnimationGroup',
    'QSettings',
    'QSharedMemory',
    'QSignalMapper',
    'QSignalTransition',
    'QSize',
    'QSizeF',
    'QSocketNotifier',
    'QState',
    'QStateMachine',
    'QSysInfo',
    'QSystemLocale',
    'QSystemSemaphore',
    'QT_TRANSLATE_NOOP',
    'QT_TR_NOOP',
    'QT_TR_NOOP_UTF8',
    'QT_VERSION',
    'QT_VERSION_STR',
    'QTemporaryFile',
    'QTextBoundaryFinder',
    'QTextCodec',
    'QTextDecoder',
    'QTextEncoder',
    'QTextStream',
    'QTextStreamManipulator',
    'QThread',
    'QThreadPool',
    'QTime',
    'QTimeLine',
    'QTimer',
    'QTimerEvent',
    'QTranslator',
    'QUrl',
    'QUuid',
    'QVariant',
    'QVariantAnimation',
    'QWaitCondition',
    'QWriteLocker',
    'QXmlStreamAttribute',
    'QXmlStreamAttributes',
    'QXmlStreamEntityDeclaration',
    'QXmlStreamEntityResolver',
    'QXmlStreamNamespaceDeclaration',
    'QXmlStreamNotationDeclaration',
    'QXmlStreamReader',
    'QXmlStreamWriter',
    'Q_ARG',
    'Q_CLASSINFO',
    'Q_ENUMS',
    'Q_FLAGS',
    'Q_RETURN_ARG',
    'Qt',
    'QtCriticalMsg',
    'QtDebugMsg',
    'QtFatalMsg',
    'QtMsgType',
    'QtSystemMsg',
    'QtWarningMsg',
    'SIGNAL',
    'SLOT',
    'bin_',
    'bom',
    'center',
    'dec',
    'endl',
    'fixed',
    'flush',
    'forcepoint',
    'forcesign',
    'hex_',
    'left',
    'lowercasebase',
    'lowercasedigits',
    'noforcepoint',
    'noforcesign',
    'noshowbase',
    'oct_',
    'qAbs',
    'qAddPostRoutine',
    'qChecksum',
    'qCompress',
    'qCritical',
    'qDebug',
    'qErrnoWarning',
    'qFatal',
    'qFuzzyCompare',
    'qInf',
    'qInstallMsgHandler',
    'qIsFinite',
    'qIsInf',
    'qIsNaN',
    'qIsNull',
    'qQNaN',
    'qRegisterResourceData',
    'qRemovePostRoutine',
    'qRound',
    'qRound64',
    'qSNaN',
    'qSetFieldWidth',
    'qSetPadChar',
    'qSetRealNumberPrecision',
    'qSharedBuild',
    'qSwap',
    'qUncompress',
    'qUnregisterResourceData',
    'qVersion',
    'qWarning',
    'qrand',
    'qsrand',
    'reset',
    'right',
    'scientific',
    'showbase',
    'uppercasebase',
    'uppercasedigits',
    'ws'
]

# Extra PyQt4 defined names mapped from PyQt4 which are not present in
# PySide
__PyQt4_QtCore = [
    'PYQT_CONFIGURATION',
    'PYQT_VERSION',
    'PYQT_VERSION_STR',
    'pyqtBoundSignal',
    'pyqtPickleProtocol',
    'pyqtProperty',
    'pyqtRemoveInputHook',
    'pyqtRestoreInputHook',
    'pyqtSetPickleProtocol',
    'pyqtSignal',
    'pyqtSignature',
    'pyqtSlot',
    'pyqtWrapperType',
]

# List names imported from Qt4's QtGui module
__Qt4_QtGui = [
    'QAbstractProxyModel',
    'QIdentityProxyModel',
    'QItemSelection',
    'QItemSelectionModel',
    'QItemSelectionRange',
    'QSortFilterProxyModel',
    'QStringListModel',
]

#: Names in Qt4's QtCore module not in Qt5
__Qt4_QtCore_missing_in_Qt5 = [
    'QAbstractFileEngine',
    'QAbstractFileEngineHandler',
    'QAbstractFileEngineIterator',
    'QFSFileEngine',
    'QPyNullVariant',
    'QSystemLocale',
    'SIGNAL',
    'SLOT',
    'qInstallMsgHandler',
    'qSwap'
]

# extra names in PyQt4's QtCore not in Qt5
__PyQt4_QtCore_missing_in_Qt5 = [
    'pyqtSignature',
]

if _api.USED_API == _api.QT_API_PYQT6:
    from PyQt6.QtCore import *
    Signal = pyqtSignal
    Slot = pyqtSlot
    Property = pyqtProperty
    BoundSignal = pyqtBoundSignal
    Qt.Alignment = Qt.AlignmentFlag
    Qt.ApplicationStates = Qt.ApplicationState
    Qt.DockWidgetAreas = Qt.DockWidgetArea
    Qt.Edges = Qt.Edge
    Qt.FindChildOptions = Qt.FindChildOption
    Qt.GestureFlags = Qt.GestureFlag
    Qt.ImageConversionFlags = Qt.ImageConversionFlag
    Qt.ItemFlags = Qt.ItemFlag
    Qt.KeyboardModifiers = Qt.KeyboardModifier
    Qt.MatchFlags = Qt.MatchFlag
    Qt.MouseButtons = Qt.MouseButton
    Qt.MouseEventFlags = Qt.MouseEventFlag
    Qt.Orientations = Qt.Orientation
    Qt.ScreenOrientations = Qt.ScreenOrientation
    # Qt.SplitBehavior = Qt.SplitBehaviorFlags
    Qt.TextInteractionFlags = Qt.TextInteractionFlag
    Qt.ToolBarAreas = Qt.ToolBarArea
    Qt.TouchPointStates = Qt.TouchPointState
    Qt.WindowFlags = Qt.WindowType
    Qt.WindowStates = Qt.WindowState
    QItemSelectionModel.SelectionFlags = QItemSelectionModel.SelectionFlag
elif _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtCore import *
    try:
        # QSignalMapper.mapped[QWidget] does not work unless QtWidgets is
        # imported before QSignalMapper is touched (even hasattr(QSM, "aa"))
        # will cause QSignalMapper.mapped[QWidget] to fail with KeyError.
        import PyQt5.QtWidgets
    except ImportError:
        pass
    Signal = pyqtSignal
    Slot = pyqtSlot
    Property = pyqtProperty
    BoundSignal = pyqtBoundSignal

elif _api.USED_API == _api.QT_API_PYQT4:
    from PyQt4 import QtCore as _QtCore, QtGui as _QtGui
    globals().update(
        {name: getattr(_QtCore, name)
         for name in __Qt4_QtCore + __PyQt4_QtCore if hasattr(_QtCore, name)}
    )
    globals().update(
        {name: getattr(_QtGui, name)
         for name in __Qt4_QtGui if hasattr(_QtCore, name)}
    )
    Signal = _QtCore.pyqtSignal
    Slot = _QtCore.pyqtSlot
    Property = _QtCore.pyqtProperty

    QAbstractProxyModel = _QtGui.QAbstractProxyModel
    QIdentityProxyModel = _QtGui.QIdentityProxyModel
    QItemSelection = _QtGui.QItemSelection
    QItemSelectionModel = _QtGui.QItemSelectionModel
    QItemSelectionRange = _QtGui.QItemSelectionRange
    QSortFilterProxyModel = _QtGui.QSortFilterProxyModel
    QStringListModel = _QtGui.QStringListModel
    del _QtCore, _QtGui

elif _api.USED_API == _api.QT_API_PYSIDE:
    from PySide import QtCore as _QtCore, QtGui as _QtGui
    globals().update(
        {name: getattr(_QtCore, name)
         for name in __Qt4_QtCore if hasattr(_QtCore, name)}
    )
    Signal = _QtCore.Signal
    Slot = _QtCore.Slot
    Property = _QtCore.Property

    QAbstractProxyModel = _QtGui.QAbstractProxyModel
    if hasattr(_QtGui, "QIdentityProxyModel"):
        QIdentityProxyModel = _QtGui.QIdentityProxyModel
    QItemSelection = _QtGui.QItemSelection
    QItemSelectionModel = _QtGui.QItemSelectionModel
    QItemSelectionRange = _QtGui.QItemSelectionRange
    QSortFilterProxyModel = _QtGui.QSortFilterProxyModel
    QStringListModel = _QtGui.QStringListModel

    _major, _minor, _micro = tuple(map(int, _QtCore.qVersion().split(".")[:3]))
    QT_VERSION = (_major << 16) + (_minor << 8) + _micro
    QT_VERSION_STR = "{}.{}.{}".format(_major, _minor, _micro)

    del _QtCore, _QtGui, _major, _minor, _micro
    # Known to be in PyQt4 but missing in PySide:
    #     Q_ARG, Q_CLASSINFO, Q_ENUMS, Q_FLAGS, Q_RETURN_ARG, ...
elif _api.USED_API == _api.QT_API_PYSIDE2:
    from PySide2.QtCore import *

    _major, _minor, _micro = tuple(map(int, qVersion().split(".")[:3]))
    QT_VERSION = (_major << 16) + (_minor << 8) + _micro
    QT_VERSION_STR = "{}.{}.{}".format(_major, _minor, _micro)
    BoundSignal = Signal

# Missing in PyQt4 <= 4.11.3
if not hasattr(QEvent, "MacSizeChange"):
    QEvent.MacSizeChange = QEvent.Type(177)

if not hasattr(QEvent, "ContentsRectChange"):
    QEvent.ContentsRectChange = QEvent.Type(178)

if not hasattr(QEvent, "NonClientAreaMouseButtonDblClick"):
    QEvent.NonClientAreaMouseButtonDblClick = QEvent.Type(176)

if not hasattr(QEvent, "NonClientAreaMouseButtonPress"):
    QEvent.NonClientAreaMouseButtonPress = QEvent.Type(174)

if not hasattr(QEvent, "NonClientAreaMouseButtonRelease"):
    QEvent.NonClientAreaMouseButtonRelease = QEvent.Type(175)

if not hasattr(QEvent, "NonClientAreaMouseMove"):
    QEvent.NonClientAreaMouseMove = QEvent.Type(173)


if not hasattr(QSignalMapper, "mappedInt"):  # Qt < 5.15
    class QSignalMapper(QSignalMapper):
        mappedInt = Signal(int)
        mappedString = Signal(str)
        mappedObject = Signal("QObject*")
        mappedWidget = Signal("QWidget*")

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.mapped[int].connect(self.mappedInt)
            self.mapped[str].connect(self.mappedString)
            self.mapped["QObject*"].connect(self.mappedObject)
            try:
                self.mapped["QWidget*"].connect(self.mappedWidget)
            except (KeyError, TypeError):
                pass

if not hasattr(QLibraryInfo, "path"):
    QLibraryInfo.path = QLibraryInfo.location

if not hasattr(QLibraryInfo, "LibraryLocation"):
    QLibraryInfo.LibraryLocation = QLibraryInfo.LibraryPath

if not hasattr(QLibraryInfo, "location"):
    QLibraryInfo.location = QLibraryInfo.path


if _api.USED_API == _api.QT_API_PYSIDE2:
    class QSettings(QSettings):
        """
        A subclass of QSettings with a simulated `type` parameter in
        value method.

        """
        # QSettings.value does not have `type` type in PySide2
        def value(self, key, defaultValue=None, type=None):
            """
            Returns the value for setting key. If the setting doesn't exist,
            returns defaultValue.
            """
            if not self.contains(key):
                return defaultValue

            value = super().value(key)
            if type is not None:
                value = self.__qvariant_cast(value, type)
                if value is None:
                    value = defaultValue
            return value

        from AnyQt._compat import qvariant_cast as __qvariant_cast
        __qvariant_cast = staticmethod(__qvariant_cast)
    try:
        QStringListModel
    except NameError:
        from PySide2.QtGui import QStringListModel


pyqtSignal = Signal
pyqtSlot = Slot
pyqtProperty = Property

if _api.USED_API == _api.QT_API_PYSIDE2:
    try:
        from PySide2 import shiboken2 as __shiboken2
    except ImportError:
        import shiboken2 as __shiboken2

    def cast(obj, type_):
        addr = unwrapinstance(obj)
        return wrapinstance(addr, type_)

    def unwrapinstance(obj):
        addr, = __shiboken2.getCppPointer(obj)
        return addr

    wrapinstance = __shiboken2.wrapInstance

    def isdeleted(obj):
        return not __shiboken2.isValid(obj)

    ispyowned = __shiboken2.ownedByPython
    delete = __shiboken2.delete
    ispycreated = __shiboken2.createdByPython
elif _api.USED_API in (_api.QT_API_PYQT5, _api.QT_API_PYQT6):
    from AnyQt.sip import (
        cast, isdeleted, ispyowned, ispycreated, delete, unwrapinstance,
        wrapinstance
    )


#: Qt version as a (major, minor, micro) tuple
QT_VERSION_INFO = tuple(map(int, qVersion().split(".")[:3]))

_api.apply_global_fixes(globals())
