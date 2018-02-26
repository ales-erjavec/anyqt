from . import _api

if _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtQuick import *
elif _api.USED_API == _api.QT_API_PYSIDE2:
    from PySide2.QtQuick import *
else:
    raise ImportError("No module named 'QtQuick' in the selected "
                      "Qt api ({})".format(_api.USED_API))
