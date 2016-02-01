from . import _api

if _api.QT_API_PYQT5:
    from PyQt5.QtMultimediaWidgets import *
else:
    raise ImportError("No module named 'QtMultimediaWidgets' in the selected"
                      "Qt api ({})".format(_api.USED_API))