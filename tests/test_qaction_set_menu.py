import unittest

from AnyQt.QtTest import QSignalSpy
from AnyQt.QtWidgets import QMenu, QApplication
from AnyQt.QtGui import QAction
from AnyQt.QtCore import delete


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
        ac.setMenu(menu)
        self.assertIs(ac.menu(), menu)
        ac.setMenu(None)
        self.assertIs(ac.menu(), None)
        spy = QSignalSpy(menu.destroyed)
        delete(menu)
        del menu
        self.assertEqual(len(spy), 1)

