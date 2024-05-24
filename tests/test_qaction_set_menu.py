import unittest

from weakref import ref

from AnyQt.QtWidgets import QMenu, QApplication
from AnyQt.QtGui import QAction


class TestQAction_setMenu(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        app = QApplication.instance()
        if app is None:
            app = QApplication([])
        cls.app = app

    @classmethod
    def tearDownClass(cls) -> None:
        cls.app = None
        super().tearDownClass()

    def test(self):
        ac = QAction()
        menu = QMenu()
        wref = ref(menu)
        ac.setMenu(menu)
        self.assertIs(ac.menu(), menu)
        ac.setMenu(None)
        self.assertIs(ac.menu(), None)
        menu.setParent(None)  # parent is None but without this PySide2 fails??
        del menu
        self.assertIsNone(wref())
