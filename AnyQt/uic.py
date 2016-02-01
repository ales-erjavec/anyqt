from . import _api

if _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.uic import *
elif _api.USED_API == _api.QT_API_PYQT4:
    from PyQt4.uic import *
elif _api.USED_API == _api.QT_API_PYSIDE:
    # This will fail with an ImportError (as it should)
    from PySide.uic import *
