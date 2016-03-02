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

if _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtCore import *
    Signal = pyqtSignal
    Slot = pyqtSlot
    Property = pyqtProperty

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
