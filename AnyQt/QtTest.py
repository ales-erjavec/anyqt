from . import _api

if _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtTest import *
elif _api.USED_API == _api.QT_API_PYQT4:
    from PyQt4.QtTest import *
elif _api.USED_API == _api.QT_API_PYSIDE:
    from PySide.QtTest import *


def _QTest_qWaitForWindowExposed(widget, timeout=1000):
    # A Qt5 compatible (probably) QTest.qWaitForWindowExposed(QWidget, int)
    # (mostly copied from qtestsystem.h in qt5/qtbase)
    from AnyQt.QtCore import \
        Qt, QCoreApplication, QEventLoop, QElapsedTimer, QEvent
    window = widget.window()
    timer = QElapsedTimer()
    timer.start()

    # Is widget.testAttribute(Qt.WA_Mapped) a suitable replacement for
    # QWindow.isExposed in Qt5??
    # Not exactly. In Qt5
    # window().testAttribute(Qt.WA_Mapped) == window().windowHandle.isExposed()
    # but both are False if a window is fully obscured by other windows,
    # in Qt4 there is no difference if a window is obscured.
    while not window.testAttribute(Qt.WA_Mapped):
        remaining = timeout - timer.elapsed()
        if remaining <= 0:
            break
        QCoreApplication.processEvents(QEventLoop.AllEvents, remaining)
        QCoreApplication.sendPostedEvents(None, QEvent.DeferredDelete)
        QTest.qSleep(10)

    return window.testAttribute(Qt.WA_Mapped)


def _QTest_qWaitForWindowActive(widget, timeout=1000):
    # A Qt5 compatible (probably) QTest.qWaitForWindowActive(QWidget, int)
    # (mostly copied from qtestsystem.h in qt5/qtbase)
    from AnyQt.QtCore import \
        Qt, QCoreApplication, QEventLoop, QElapsedTimer, QEvent
    window = widget.window()
    timer = QElapsedTimer()
    timer.start()

    while not window.isActiveWindow():
        remaining = timeout - timer.elapsed()
        if remaining <= 0:
            break
        QCoreApplication.processEvents(QEventLoop.AllEvents, remaining)
        QCoreApplication.sendPostedEvents(None, QEvent.DeferredDelete)
        QTest.qSleep(10)

    # See the explanation in qtestsystem.h
    if window.isActiveWindow():
        wait_no = 0
        while window.pos().isNull():
            if wait_no > timeout // 10:
                break
            wait_no += 1
            QTest.qWait(10)

    return window.isActiveWindow()

if _api.USED_API in {_api.QT_API_PYQT4, _api.QT_API_PYSIDE}:
    QTest.qWaitForWindowExposed = _QTest_qWaitForWindowExposed
    QTest.qWaitForWindowActive = _QTest_qWaitForWindowActive

    from AnyQt.QtCore import QObject, QByteArray as _QByteArray

    # not exposed in PyQt4 or PySide. Going by PyQt5 interface
    class QSignalSpy(QObject):
        """
        QSignalSpy(boundsignal)
        """
        def __init__(self, boundsig, **kwargs):
            super(QSignalSpy, self).__init__(**kwargs)
            from AnyQt.QtCore import QEventLoop, QTimer
            self.__boundsig = boundsig
            self.__boundsig.connect(lambda *args: self.__record(*args))
            self.__recorded = []  # type: List[List[Any]]
            self.__loop = QEventLoop()
            self.__timer = QTimer(self, singleShot=True)
            self.__timer.timeout.connect(self.__loop.quit)

        def __record(self, *args):
            self.__recorded.append(list(args))
            if self.__loop.isRunning():
                self.__loop.quit()

        def signal(self):
            return _QByteArray(self.__boundsig.signal[1:].encode("latin-1"))

        def isValid(self):
            return True

        def wait(self, timeout=5000):
            count = len(self)
            self.__timer.stop()
            self.__timer.setInterval(timeout)
            self.__timer.start()
            self.__loop.exec_()
            self.__timer.stop()
            return len(self) != count

        def __getitem__(self, index):
            return self.__recorded[index]

        def __setitem__(self, index, value):
            self.__recorded.__setitem__(index, value)

        def __delitem__(self, index):
            self.__recorded.__delitem__(index)

        def __len__(self):
            return len(self.__recorded)

    del QObject
