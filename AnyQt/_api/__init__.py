import sys

if sys.version_info < (3, ):
    _intern = intern
else:
    _intern = sys.intern

USED_API = None

QT_API_PYQT5 = "pyqt5"
QT_API_PYQT4 = "pyqt4"
QT_API_PYSIDE = "pyside"


def comittoapi(api):
    global USED_API
    assert USED_API is None, "committoapi called again!"
    check = ["PyQt4", "PyQt5", "PySide"]
    assert api in [QT_API_PYQT5, QT_API_PYQT4, QT_API_PYSIDE]
    for name in check:
        if name.lower() != api and name in sys.modules:
            raise RuntimeError(
                "{} was allready imported. Cannot commit to {}!"
                .format(name, api)
            )
    else:
        USED_API = _intern(api)
