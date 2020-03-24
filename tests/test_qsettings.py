import unittest

from AnyQt.QtCore import QSettings, QStandardPaths


class TestQSettings(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        QStandardPaths.setTestModeEnabled(True)
        QSettings.setDefaultFormat(QSettings.IniFormat)

    def tearDown(self) -> None:
        QStandardPaths.setTestModeEnabled(False)
        QSettings.setDefaultFormat(QSettings.NativeFormat)
        super().tearDown()

    def test_qsettings(self):
        s = QSettings()
        s.setValue("one", 1)
        s.setValue("one-half", 0.5)
        s.setValue("empty", "")
        s.setValue("true", True)
        s.sync()
        del s
        s = QSettings()
        self.assertEqual(s.value("one", type=int), 1)
        self.assertEqual(s.value("one-half", type=float), 0.5)
        self.assertEqual(s.value("empty", type=str), "")
        self.assertEqual(s.value("true", type=bool), True)