import unittest

from AnyQt.QtGui import QFontDatabase
from AnyQt.QtWidgets import QApplication


class TestQFontDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        app = QApplication.instance()
        if app is None:
            app = QApplication([])
        cls.app = app

    @classmethod
    def tearDownClass(cls) -> None:
        # cls.app = None
        super().tearDownClass()

    def test_qfontdatabase_static(self):
        families = QFontDatabase.families()
        styles = QFontDatabase.styles(families[0])
        systems = QFontDatabase.writingSystems()
        systems = QFontDatabase.writingSystems(families[0])
