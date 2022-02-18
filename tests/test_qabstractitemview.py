import  unittest
import warnings

from AnyQt.QtCore import QStringListModel
from AnyQt.QtWidgets import QApplication, QTableView, QStyledItemDelegate, \
    QStyleOptionViewItem


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

    def test_qabstratitemview_item_delegate_for_index(self):
        view = QTableView()
        model = QStringListModel()
        model.setStringList(["AA", "BB"])
        view.setModel(model)
        idx1 = model.index(0, 0)
        idx2 = model.index(1, 0)
        delegate = QStyledItemDelegate()
        view.setItemDelegate(delegate)
        with warnings.catch_warnings(record=True):
            self.assertIs(view.itemDelegate(idx1), delegate)
            self.assertIs(view.itemDelegate(idx2), delegate)

    def test_qabstractitemview_view_options(self):
        view = QTableView()
        with warnings.catch_warnings(record=True):
            opt1 = view.viewOptions()
        self.assertIs(opt1.widget, view)
        self.assertTrue(opt1.showDecorationSelected)
        opt2 = QStyleOptionViewItem()
        view.initViewItemOption(opt2)
        self.assertIs(opt2.widget, view)
        self.assertTrue(opt2.showDecorationSelected)

