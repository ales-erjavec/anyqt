import sys
import warnings
import importlib.util
from importlib.abc import MetaPathFinder, Loader

from ._api import (
    USED_API, QT_API_PYQT4, QT_API_PYQT5, QT_API_PYSIDE
)


class _FinderLoader(MetaPathFinder, Loader):
    pass


class ImportHookBackport(_FinderLoader):
    """
    A python import hook (PEP-302) substituting Qt4 module imports, replacing
    them with a back compatible shim.
    """
    def __init__(self, whichapi):
        self.whichapi = whichapi

    def find_spec(self, fullname, path=None, target=None):
        if USED_API != QT_API_PYQT5:
            return

        toplevel = fullname.split(".", 1)[0]
        if toplevel == "PyQt4" and self.whichapi == QT_API_PYQT4:
            return importlib.util.spec_from_loader(fullname, self)
        elif toplevel == "PySide" and self.whichapi == QT_API_PYSIDE:
            return importlib.util.spec_from_loader(fullname, self)
        else:
            return

    def create_module(self, spec):
        pkgpath = spec.name.split(".")
        toplevel = pkgpath[0]
        subpkg = pkgpath[1] if len(pkgpath) > 1 else None

        assert toplevel.lower() == self.whichapi
        backportpkg = "AnyQt._backport"
        if subpkg is not None:
            backportpkg += "." + subpkg
        module = __import__(backportpkg, fromlist=["_"])
        warnings.warn(
            "Loaded module {} as a substitute for {}"
                .format(module.__name__, spec.name),
            RuntimeWarning, stacklevel=2,
        )
        return module

    def exec_module(self, module):
        return module


class ImportHookDeny(_FinderLoader):
    """
    A python import hook (PEP-302) preventing imports of a Qt api.

    Parameters
    ----------
    whichapi : str
        The Qt api whose import should be prevented.
    """
    def __init__(self, whichapi):
        self.whichapi = whichapi

    def find_spec(self, fullname, path=None, target=None):
        toplevel = fullname.split(".")[0]
        if self.whichapi == QT_API_PYQT5 and toplevel == "PyQt5" or \
                self.whichapi == QT_API_PYQT4 and toplevel == "PyQt4" or \
                self.whichapi == QT_API_PYSIDE and toplevel == "PySide":
            return importlib.util.spec_from_loader(fullname, self)
        else:
            return None

    def create_module(self, spec):
        raise ImportError("Import of {} is denied.".format(spec.name))

    def exec_module(self, module) -> None:
        raise ImportError


def install_backport_hook(api):
    """
    Install a backport import hook for Qt4 api

    Parameters
    ----------
    api : str
        The Qt4 api whose structure should be intercepted
        ('pyqt4' or 'pyside').

    Example
    -------
    >>> install_backport_hook("pyqt4")
    >>> import PyQt4
    Loaded module AnyQt._backport as a substitute for PyQt4

    """
    if api == USED_API:
        raise ValueError

    sys.meta_path.insert(0, ImportHookBackport(api))


def install_deny_hook(api):
    """
    Install a deny import hook for Qt api.

    Parameters
    ----------
    api : str
        The Qt api whose import should be prevented

    Example
    -------
    >>> install_deny_import("pyqt4")
    >>> import PyQt4
    Traceback (most recent call last):...
    ImportError: Import of PyQt4 is denied.

    """
    if api == USED_API:
        raise ValueError

    sys.meta_path.insert(0, ImportHookDeny(api))
