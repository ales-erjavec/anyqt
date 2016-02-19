import warnings


def fix_pyqt5_QGraphicsItem_itemChange():
    """
    Attempt to remedy:
    https://www.riverbankcomputing.com/pipermail/pyqt/2016-February/037015.html
    """
    from PyQt5.QtWidgets import QGraphicsObject, QGraphicsItem

    class Obj(QGraphicsObject):
        def itemChange(self, change, value):
            return QGraphicsObject.itemChange(self, change, value)

    obj = Obj()
    parent = Obj()
    obj.setParentItem(parent)

    if obj.parentItem() is None:
        # There was probably already some signal defined using QObject's
        # subclass from QtWidgets.
        # We will monkey patch the QGraphicsItem.itemChange and explicitly
        # sip.cast all input and output QGraphicsItem instances
        import sip
        QGraphicsItem_itemChange_old = QGraphicsItem.itemChange

        # All the QGraphicsItem.ItemChange flags which accept/return
        # a QGraphicsItem
        changeset = {
            QGraphicsItem.ItemParentChange,
            QGraphicsItem.ItemParentHasChanged,
            QGraphicsItem.ItemChildAddedChange,
            QGraphicsItem.ItemChildRemovedChange,
        }

        def QGraphicsItem_itemChange(self, change, value):
            if change in changeset:
                if isinstance(value, QGraphicsItem):
                    value = sip.cast(value, QGraphicsItem)
                rval = QGraphicsItem_itemChange_old(self, change, value)
                if isinstance(rval, QGraphicsItem):
                    rval = sip.cast(rval, QGraphicsItem)
                return rval
            else:
                return QGraphicsItem_itemChange_old(self, change, value)

        QGraphicsItem.itemChange = QGraphicsItem_itemChange
        warnings.warn("Monkey patching QGraphicsItem.itemChange",
                      RuntimeWarning)