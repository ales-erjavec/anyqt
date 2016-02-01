from . import _api

__all__ = ["QX11Info"]

if _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtX11Extras import QX11Info
elif _api.USED_API == _api.QT_API_PYQT4:
    from PyQt4.QtGui import QX11Info
elif _api.USED_API == _api.QT_API_PYSIDE:
    from PySide.QtGui import QX11Info
