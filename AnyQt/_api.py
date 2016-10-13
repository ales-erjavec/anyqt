"""
NOTE: Importing this module will select and commit to a Qt API.
"""

import os
import sys

import AnyQt

if sys.version_info < (3,):
    _intern = intern
else:
    _intern = sys.intern

USED_API = None

QT_API_PYQT5 = "pyqt5"
QT_API_PYQT4 = "pyqt4"
QT_API_PYSIDE = "pyside"


def comittoapi(api):
    """
    Commit to the use of specified Qt api.

    Raise an error if another Qt api is already loaded in sys.modules

    """
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
        api = _intern(api)
        USED_API = api
        AnyQt.__SELECTED_API = api
        AnyQt.USED_API = api

if AnyQt.__SELECTED_API is not None:
    comittoapi(AnyQt.__SELECTED_API)
elif "QT_API" in os.environ:
    comittoapi(os.environ["QT_API"].lower())
else:
    # Check sys.modules for existing imports
    __existing = None
    if "PyQt5" in sys.modules:
        __existing = QT_API_PYQT5
    elif "PyQt4" in sys.modules:
        __existing = QT_API_PYQT4
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

        if __available is not None:
            comittoapi(__available)
        del __available

    del __existing

if USED_API is None:
    raise ImportError("PyQt4, PyQt5 or PySide are not available for import")


if "ANYQT_HOOK_DENY" in os.environ:
    from AnyQt.importhooks import install_deny_hook
    for __denyapi in os.environ["ANYQT_HOOK_DENY"].split(","):
        if __denyapi.lower() != USED_API:
            install_deny_hook(__denyapi.lower())
    del install_deny_hook

if "ANYQT_HOOK_BACKPORT" in os.environ:
    from AnyQt.importhooks import install_backport_hook
    for __bacportapi in os.environ["ANYQT_HOOK_BACKPORT"].split(","):
        if __bacportapi.lower() != USED_API:
            install_backport_hook(__bacportapi.lower())
    del install_backport_hook