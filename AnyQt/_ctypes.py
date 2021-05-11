import os
from itertools import chain
from typing import Iterable

import glob
import sys
import sysconfig
import ctypes.util

from AnyQt.QtCore import QLibraryInfo, QT_VERSION


def shlib_ext():
    """
    Return possible platform shared library extension.
    """
    extensions = []
    if sys.platform == "win32":
        extensions += [".dll"]
    elif sys.platform == "darwin":
        extensions += ["", ".dylib"]
    else:
        extensions += [".so"]

    confv = sysconfig.get_config_vars()
    so_ext = confv.get("SO", None)
    if so_ext is not None and so_ext not in extensions:
        extensions += [so_ext]
    return extensions

#
# NOTE: posix dlsym resolves references over linked libs
# `LoadLibrary(QtGui.__file__)` is sufficient. Windows?
# No. Only referenced lib is searched (LoadLibrary and GetProcAddress).
# But LoadLibrary("Qt5Gui.dll") might just do the trick.
#


def find_library(name, path) -> Iterable[str]:
    if sys.platform == "darwin":
        test = [
            name,
            name + ".so",
            name + ".dylib"
            "{name}.framework/{name}".format(name=name),
            "{name}.framework/Versions/Current/{name}".format(name=name),
            "{name}.framework/Versions/*/{name}".format(name=name),
        ]

    elif sys.platform == "win32":
        test = [name, name + ".dll"]
    else:
        test = [
            name,
            name + ".so",
            "lib{name}.so".format(name=name),
            "lib{name}.so.*".format(name=name)
        ]

    for suffix in test:
        yield from glob.iglob(os.path.join(path, suffix))
        # try:
        #     return next(glob.iglob(os.path.join(path, suffix)))
        # except StopIteration:
        #     pass


def find_qtlib(name) -> Iterable[str]:
    qtlibpath = QLibraryInfo.path(QLibraryInfo.LibrariesPath)
    major_version = (QT_VERSION >> 16)
    paths = find_library(name, qtlibpath)
    if name.startswith("Qt"):
        # common case for Qt builds on windows
        name_extra = "Qt{}{}".format(major_version, name[2:])
        extra = find_library(name_extra, qtlibpath)
    else:
        extra = []
    return chain(paths, extra, (name, *((name_extra,) if extra else ())))


def load_qtlib(name):
    for path in find_qtlib(name):
        try:
            return ctypes.cdll.LoadLibrary(path)
        except OSError:
            pass
    return None
