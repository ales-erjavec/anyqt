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
