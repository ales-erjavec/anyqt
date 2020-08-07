import unittest

from AnyQt.QtGui import QAction
from AnyQt.QtWidgets import QWidget, QApplication


class TestQActionEvent_action(unittest.TestCase):
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

    def test_action(self):
        a = QAction()
        b = QAction()

        class Widget(QWidget):
            def test(self, event):
                pass

            def actionEvent(self, event):
                super().actionEvent(event)
                self.test(event)

        widget = Widget()

        def test(ev):
            assert ev.action() is b
        widget.test = test
        widget.addAction(b)

        def test(ev):
            assert ev.action() is a
            assert ev.before() is b
        widget.test = test
        widget.insertAction(b, a)
        del widget.test
