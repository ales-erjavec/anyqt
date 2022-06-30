import  unittest

from AnyQt.QtCore import QBuffer, QSizeF

from AnyQt.QtGui import QPdfWriter, QPageSize


class TestQPDFWriter(unittest.TestCase):
    def test(self):
        b = QBuffer()
        w = QPdfWriter(b)
        size = QPageSize(QSizeF(10, 10), QPageSize.Millimeter)
        _ = w.setPageSize(size)
        self.assertTrue(w.setPageSize(size))