import os
from itertools import chain
from typing import Iterable
import glob
import sys
import ctypes

from AnyQt.QtCore import QLibraryInfo, QT_VERSION


def find_library(name, path) -> Iterable[str]:
    if sys.platform == "darwin":
        test = [
            name,
            name + ".so",
            name + ".dylib"
            "{name}.framework/{name}".format(name=name),
            "{name}.framework/Versions/Current/{name}".format(name=name),
            "{name}.framework/Versions/*/{name}".format(name=name),
            "lib{name}.dylib".format(name=name),
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
