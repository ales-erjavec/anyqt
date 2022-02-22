import enum
import warnings
from typing import Type, Dict, Any


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


def fix_pyqt6_unscoped_enum(namespace: Dict[str, Any]):
    """
    Lift all PyQt6 enum members up to class level.
    i.e. Qt.ItemFlags.DisplayRole -> Qt.DisplayRole
    """
    from PyQt6 import sip

    def members(enum: Type[enum.Enum]):
        return ((name, enum[name]) for name in enum.__members__)

    def lift_enum_namespace(type_, enum: Type[enum.Enum]):
        for name, value in members(enum):
            setattr(type_, name, value)

    def is_unscoped_enum(value):
        return isinstance(value, type) and issubclass(value, enum.Enum)

    def can_lift(type_, enum: Type[enum.Enum]):
        namespace = type_.__dict__
        return not any(name in namespace and namespace[name] is not value
                       for name, value in members(enum))

    for _, class_ in list(namespace.items()):
        if isinstance(class_, (sip.simplewrapper, sip.wrappertype)):
            for name, value in list(class_.__dict__.items()):
                if is_unscoped_enum(value):
                    if can_lift(class_, value):
                        lift_enum_namespace(class_, value)


GLOBAL_FIXES = {
    "pyqt6": [fix_pyqt6_unscoped_enum],
}


def global_fixes(namespace):
    from AnyQt import _api
    fixes = GLOBAL_FIXES.get(_api.USED_API, [])
    for fixer in fixes:
        fixer(namespace)
