import unittest

class TestExports(unittest.TestCase):
    names = [
        "AnyQt.QtCore:Signal",
        "AnyQt.QtCore:Slot",
        "AnyQt.QtCore:Property",

        "AnyQt.QtGui:QUndoCommand",
        "AnyQt.QtGui:QUndoGroup",
        "AnyQt.QtGui:QUndoStack",
        "AnyQt.QtGui:QShortcut",
        "AnyQt.QtGui:QAction",
        "AnyQt.QtGui:QActionGroup",
        "AnyQt.QtGui:QFileSystemModel",
    ]
    def test_exports(self):
        for name in self.names:
            pkg, _, item = name.rpartition(":")
            module = __import__(pkg, fromlist=[item])
            getattr(module, item)