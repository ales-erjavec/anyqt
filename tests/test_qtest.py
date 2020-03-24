import unittest
from itertools import count

from AnyQt.QtCore import QObject, isdeleted
from AnyQt.QtWidgets import QApplication
from AnyQt.QtTest import QTest


class TestQtTest(unittest.TestCase):
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

    def test_qwait(self):
        obj = QObject()
        obj.deleteLater()
        QTest.qWait(0)
        self.assertTrue(isdeleted(obj))

    def test_qwaitfor(self):
        counter = count()
        current = 0

        def pred():
            nonlocal current
            current = next(counter)
            return current > 4
        self.assertTrue(QTest.qWaitFor(pred, 100000))
        self.assertTrue(current == 5)
        self.assertFalse(QTest.qWaitFor(lambda: False, 10))
