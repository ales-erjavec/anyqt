import sys

from . import _api


class ImportHookBackport(object):
    def __init__(self, whichapi):
        self.whichapi = whichapi

    def find_module(self, name, path=None):
        if _api.USED_API != _api.QT_API_PYQT5:
            return

        toplevel = name.split(".", 1)[0]
        if toplevel == "PyQt4" and self.whichapi == _api.QT_API_PYQT4:
            return self
        elif toplevel == "PySide" and self.whichapi == _api.QT_API_PYSIDE:
            return self
        else:
            return

    def load_module(self, fullname):
        if fullname in sys.modules:
            # don't reload
            return sys.modules[fullname]

        pkgpath = fullname.split(".")
        toplevel = pkgpath[0]
        subpkg = pkgpath[1] if len(pkgpath) > 1 else None

        assert toplevel.lower() == self.whichapi
        backportpkg = "AnyQt._backport"
        if subpkg is not None:
            backportpkg += "." + subpkg
        module = __import__(backportpkg, fromlist=["_"])
        print("loaded module {} as a substitute for {}"
              .format(module.__name__, fullname))
        sys.modules[fullname] = module
        return module


class ImportHookDeny(object):
    def __init__(self, whichapi):
        self.whichapi = whichapi

    def find_module(self, name, path=None):
        toplevel = name.split(".")[0]
        if self.whichapi == _api.QT_API_PYQT5 and toplevel == "PyQt5":
            return self
        elif self.whichapi == _api.QT_API_PYQT4 and toplevel == "PyQt4":
            return self
        elif self.whichapi == _api.QT_API_PYSIDE and toplevel == "PySide":
            return self
        else:
            return None

    def load_module(self, fullname):
        raise ImportError("NO {} FOR YOU!!".format(fullname.split(".")[0]))


def install_import_hook(api):
    if api == _api.USED_API:
        raise ValueError

    sys.meta_path.insert(0, ImportHookBackport(api))


def install_deny_import(api):
    if api == _api.USED_API:
        raise ValueError

    sys.meta_path.insert(0, ImportHookDeny(api))
