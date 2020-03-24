import unittest

import AnyQt
from AnyQt.QtCore import Qt, QPointF, QRectF

from AnyQt.QtGui import QPainter, QPixmap, QImage, QGuiApplication, QColor
from AnyQt.QtWidgets import QApplication


class TestDrawPixmapFragments(unittest.TestCase):
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
        img = QImage(100, 100, QImage.Format_ARGB32)
        img.fill(Qt.green)
        p = QPainter(img)
        pix = QPixmap(10, 10)
        pix.fill(Qt.red)
        frgmts = [
            QPainter.PixmapFragment.create(
                QPointF(25, 25),
                QRectF(0, 0, 10, 10),
                5., 5.,
            ),
            QPainter.PixmapFragment.create(
                QPointF(75, 75),
                QRectF(0, 0, 10, 10),
                5., 5.,
            )

        ]
        p.drawPixmapFragments(frgmts, pix)
        p.end()
        self.assertEqual(QColor(img.pixel(10, 10)), QColor(Qt.red))
        self.assertEqual(QColor(img.pixel(80, 80)),  QColor(Qt.red))
        self.assertEqual(QColor(img.pixel(90, 10)), QColor(Qt.green))
        self.assertEqual(QColor(img.pixel(10, 90)), QColor(Qt.green))

    @unittest.skipIf(not AnyQt.USED_API.lower().startswith("pyside"), "PySide only")
    def test_pyside(self):
        img = QImage(100, 100, QImage.Format_ARGB32)
        img.fill(Qt.green)
        p = QPainter(img)
        pix = QPixmap(10, 10)
        pix.fill(Qt.red)
        frgmt = QPainter.PixmapFragment.create(
            QPointF(25, 25),
            QRectF(0, 0, 10, 10),
            5., 5.,
        )
        p.drawPixmapFragments(frgmt, 1, pix)
        p.end()
        self.assertEqual(QColor(img.pixel(10, 10)), QColor(Qt.red))