from typing import Union
from functools import lru_cache

from AnyQt.QtCore import QObject, Property


@lru_cache(maxsize=200)
def _converter(type_: Union[type, str]):
    class Obj(QObject):
        _f = None
        def _set(self, val):
            self._f = val
        def _get(self):
            return self._f

        prop = Property(type_, _get, _set)

    def convert(value):
        inst = Obj()
        ok = inst.setProperty('prop', value)
        if ok:
            return inst.property('prop')
        else:
            return None
    return convert


def qvariant_cast(value, type_: Union[type, str]):
    converter = _converter(type_)
    return converter(value)
