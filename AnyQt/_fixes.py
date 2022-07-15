import os
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


def fix_pyqt6_qtgui_qaction_menu(namespace):
    if namespace.get("__name__") != "AnyQt.QtGui":
        return
    import ctypes
    from ._ctypes import load_qtlib
    qtgui = load_qtlib("QtGui")
    if os.name == "posix":  # assuming gcc compatible compiler
        _QAction_setMenuObject = qtgui['_ZN7QAction13setMenuObjectEP7QObject']
        _QAction_menuObject = qtgui['_ZNK7QAction10menuObjectEv']
    elif os.name == "nt":
        _QAction_setMenuObject = qtgui['?setMenuObject@QAction@@AEAAXPEAVQObject@@@Z']
        _QAction_menuObject = qtgui['?menuObject@QAction@@AEBAPEAVQObject@@XZ']
    else:
        return

    _QAction_menuObject.argtypes = [ctypes.c_void_p]
    _QAction_menuObject.restype = ctypes.c_void_p

    _QAction_setMenuObject.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

    from PyQt6.QtGui import QAction
    from PyQt6.sip import isdeleted, unwrapinstance, wrapinstance
    try:
        from PyQt6.QtWidgets import QMenu
    except ImportError:
        return  # No QtWidgets then no setMenu

    if hasattr(QAction, "setMenu"):
        return

    def QAction_setMenu(self, menu):
        if menu is not None and not isinstance(menu, QMenu):
            raise TypeError()
        if menu is not None and isdeleted(menu):
            raise RuntimeError()
        if isdeleted(self):
            raise RuntimeError()
        self.__QAction_menu = menu
        _QAction_setMenuObject(
            unwrapinstance(self),
            unwrapinstance(menu) if menu is not None else 0
        )

    def QAction_menu(self):
        if isdeleted(self):
            raise RuntimeError()
        ptr = _QAction_menuObject(unwrapinstance(self))
        if ptr is None:
            return None
        menu = wrapinstance(ptr, QMenu)
        return menu

    QAction.setMenu = QAction_setMenu
    QAction.menu = QAction_menu


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


def fix_pyqt5_missing_enum_members(namespace: Dict[str, Any]):
    import enum
    from AnyQt import sip

    def is_pyqt_enum_type(value):
        return (isinstance(value, type)
                and issubclass(value, int)
                and value is not int
                and "." in value.__qualname__
                and not issubclass(value, enum.Enum))

    for _, class_ in list(namespace.items()):
        if isinstance(class_, (sip.simplewrapper, sip.wrappertype)):
            enum_types = {}
            for name, value in list(class_.__dict__.items()):
                if is_pyqt_enum_type(value):
                    enum_types[value.__qualname__] = value
            types_ = tuple(enum_types.values())
            for name, value in list(class_.__dict__.items()):
                if type(value) in types_:
                    type_ = enum_types[type(value).__qualname__]
                    if hasattr(type_, name) and (
                            getattr(type_, name) != value and
                            type_.__qualname__ != "QKeySequence.StandardKey"
                    ):
                        warnings.warn(
                            f"{type_} {name} is already present and is not "
                            f"{value}", RuntimeWarning
                        )
                    elif not hasattr(type_, name):
                        setattr(type_, name, value)


def fix_pyside_QActionEvent_action(namespace):
    if namespace.get("__name__") != "AnyQt.QtGui":
        return
    import ctypes
    try:
        from PySide2 import shiboken2  # PySide2 < 5.12.0
    except ImportError:
        import shiboken2
    from AnyQt.QtGui import QActionEvent
    from AnyQt.QtWidgets import QAction

    class _QActionEvent(ctypes.Structure):
        _fields_ = [
            ("vtable", ctypes.c_void_p),
            # QEvent
            ("d", ctypes.c_void_p),       # private data ptr
            ("t", ctypes.c_ushort),       # type
            ("_flags", ctypes.c_ushort),  # various flags
            # QActionEvent
            ("act", ctypes.c_void_p),     # QAction *act
            ("bef", ctypes.c_void_p),     # QAction *bef
        ]

        def action(self):
            return from_address(self.act, QAction)

        def before(self):
            return from_address(self.bef, QAction)

        @classmethod
        def from_event(cls, event: QActionEvent):
            p, = shiboken2.getCppPointer(event)
            return cls.from_address(p)

    def from_address(address: int, type_):
        if address:
            return shiboken2.wrapInstance(address, type_)
        else:
            return None

    def action(self):
        ev = _QActionEvent.from_event(self)
        return ev.action()

    def before(self):
        ev = _QActionEvent.from_event(self)
        return ev.before()

    if not hasattr(QActionEvent, "action"):
        QActionEvent.action = action
    if not hasattr(QActionEvent, "before"):
        QActionEvent.before = before


def fix_pyside_exec(namespace):
    if namespace.get("__name__") == "AnyQt.QtWidgets":
        from PySide2.QtWidgets import QApplication, QDialog, QMenu
        if "exec" not in QApplication.__dict__:
            QApplication.exec = lambda self: QApplication.exec_()
        if not hasattr(QDialog, "exec"):
            QDialog.exec = lambda self: QDialog.exec_(self)
        if not hasattr(QMenu, "exec"):
            QMenu.exec = lambda self: QMenu.exec_(self)
    if namespace.get("__name__") == "AnyQt.QtGui":
        from PySide2.QtGui import QGuiApplication, QDrag
        if "exec" not in QGuiApplication.__dict__:
            QGuiApplication.exec = lambda self: QGuiApplication.exec_()
        if not hasattr(QDrag, "exec"):
            QDrag.exec = (
                lambda self, *args, **kwargs: QDrag.exec_(self, *args, **kwargs)
            )
    elif namespace.get("__name__") == "AnyQt.QtCore":
        from PySide2.QtCore import QCoreApplication, QEventLoop, QThread
        if not hasattr(QCoreApplication, "exec"):
            QCoreApplication.exec = lambda self: QCoreApplication.exec_()
        if not hasattr(QEventLoop, "exec"):
            QEventLoop.exec = (
                lambda self, *args, **kwargs:
                    QEventLoop.exec_(self, *args, **kwargs)
            )
        if not hasattr(QThread, "exec"):
            QThread.exec = lambda self: QThread.exec_(self)
    elif namespace.get("__name__") == "AnyQt.QtPrintSupport":
        from PySide2.QtPrintSupport import QPageSetupDialog, QPrintDialog
        if "exec" not in QPageSetupDialog.__dict__:
            QPageSetupDialog.exec = lambda self: QPageSetupDialog.exec_(self)
        if "exec" not in QPrintDialog.__dict__:
            QPrintDialog.exec = lambda self: QPrintDialog.exec_(self)


def fix_qstandarditem_insert_row(namespace):
    if namespace.get("__name__") == "AnyQt.QtGui":
        QStandardItem = namespace["QStandardItem"]
        __QStandardItem_insertRow = QStandardItem.insertRow

        def QStandardItem_insertRow(self, row, items):
            if isinstance(items, QStandardItem):
                # PYSIDE-237
                __QStandardItem_insertRow(self, row, [items])
            else:
                __QStandardItem_insertRow(self, row, items)
        QStandardItem.insertRow = QStandardItem_insertRow


GLOBAL_FIXES = {
    "pyqt6": [
        fix_pyqt6_unscoped_enum,
        fix_pyqt6_qtgui_qaction_menu,
    ],
    "pyqt5": [
        fix_pyqt5_missing_enum_members,
    ],
    "pyside2": [
        fix_pyside_QActionEvent_action,
        fix_pyside_exec,
        fix_qstandarditem_insert_row,
    ],
}


def global_fixes(namespace):
    from AnyQt import _api
    fixes = GLOBAL_FIXES.get(_api.USED_API, [])
    for fixer in fixes:
        fixer(namespace)
