"""
NOTE: Importing this module will select and commit to a Qt API.
"""

import os
import sys
import warnings

import AnyQt

if sys.version_info < (3,):
    _intern = intern
else:
    _intern = sys.intern

USED_API = None

QT_API_PYQT5 = "pyqt5"
QT_API_PYQT4 = "pyqt4"
QT_API_PYSIDE = "pyside"
QT_API_PYSIDE2 = "pyside2"

def comittoapi(api):
    """
    Commit to the use of specified Qt api.

    Raise an error if another Qt api is already loaded in sys.modules

    """
    global USED_API
    assert USED_API is None, "committoapi called again!"
    check = ["PyQt4", "PyQt5", "PySide", "PySide2"]
    assert api in [QT_API_PYQT5, QT_API_PYQT4, QT_API_PYSIDE, QT_API_PYSIDE2]
    for name in check:
        if name.lower() != api and name in sys.modules:
            raise RuntimeError(
                "{} was already imported. Cannot commit to {}!"
                .format(name, api)
            )
    else:
        api = _intern(api)
        USED_API = api
        AnyQt.__SELECTED_API = api
        AnyQt.USED_API = api

if AnyQt.__SELECTED_API is not None:
    comittoapi(AnyQt.__SELECTED_API)
elif "QT_API" in os.environ:
    api = os.environ["QT_API"].lower()
    if api == "pyqt":
        # Qt.py allows both pyqt4 and pyqt to specify PyQt4.
        # When run from anaconda-navigator, pyqt is used.
        api = "pyqt4"
    if api in [QT_API_PYQT4, QT_API_PYQT5, QT_API_PYSIDE, QT_API_PYSIDE2]:
        comittoapi(api)
    else:
        warnings.warn(
            "'QT_API' environment variable names an unknown Qt API ('{}')."
            .format(os.environ["QT_API"]),
            RuntimeWarning, stacklevel=3)
        # pass through

if USED_API is None:
    # Check sys.modules for existing imports
    __existing = None
    if "PyQt5" in sys.modules:
        __existing = QT_API_PYQT5
    elif "PyQt4" in sys.modules:
        __existing = QT_API_PYQT4
    elif "PySide2" in sys.modules:
        __existing = QT_API_PYSIDE2
    elif "PySide" in sys.modules:
        __existing = QT_API_PYSIDE

    if __existing is not None:
        comittoapi(__existing)
    else:
        available = AnyQt.availableapi()
        __available = None

        if AnyQt.__PREFERRED_API is not None and \
                AnyQt.__PREFERRED_API.lower() in [name.lower() for name in available]:
            __available = AnyQt.__PREFERRED_API.lower()
        elif "PyQt5" in available:
            __available = QT_API_PYQT5
        elif "PyQt4" in available:
            __available = QT_API_PYQT4
        elif "PySide" in available:
            __available = QT_API_PYSIDE
        elif "PySide2" in available:
            __available = QT_API_PYSIDE2

        if __available is not None:
            comittoapi(__available)
        del __available

    del __existing

if USED_API is None:
    raise ImportError("PyQt4, PyQt5, PySide or PySide2 are not available for import")


if "ANYQT_HOOK_DENY" in os.environ:
    from AnyQt.importhooks import install_deny_hook
    for __denyapi in os.environ["ANYQT_HOOK_DENY"].split(","):
        if __denyapi.lower() != USED_API:
            install_deny_hook(__denyapi.lower())
    del install_deny_hook

if "ANYQT_HOOK_BACKPORT" in os.environ:
    from AnyQt.importhooks import install_backport_hook
    for __backportapi in os.environ["ANYQT_HOOK_BACKPORT"].split(","):
        if __backportapi.lower() != USED_API:
            install_backport_hook(__backportapi.lower())
    del install_backport_hook
