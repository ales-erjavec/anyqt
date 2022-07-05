import unittest
import gc

from AnyQt.QtGui import QStandardItem, QStandardItemModel

class TestQStandardItem(unittest.TestCase):
    def test(self):
        model = QStandardItemModel()
        item_parent = QStandardItem("parent")
        item_child = QStandardItem("child")
        model.insertRow(0, item_parent)
        item_parent.insertRow(0, item_child)
        self.assertEqual(model.index(0, 0).data(), "parent")
        self.assertEqual(model.index(0, 0, model.index(0, 0)).data(), "child")
        del item_child
        del item_parent
        gc.collect()
        self.assertEqual(model.index(0, 0).data(), "parent")
        self.assertEqual(model.index(0, 0, model.index(0, 0)).data(), "child")
