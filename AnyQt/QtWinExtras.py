from . import _api

if _api == _api.QT_API_PYQT5:
    from PyQt5.QtWinExtras import *
else:
    raise ImportError