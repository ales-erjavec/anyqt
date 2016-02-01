from . import _api

__all__ = [
    'QGraphicsSvgItem',
    'QSvgGenerator',
    'QSvgRenderer',
    'QSvgWidget'
]

if _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtSvg import (
        QGraphicsSvgItem,
        QSvgGenerator,
        QSvgRenderer,
        QSvgWidget,
    )
elif _api.USED_API == _api.QT_API_PYQT4:
    from PyQt4.QtSvg import (
        QGraphicsSvgItem,
        QSvgGenerator,
        QSvgRenderer,
        QSvgWidget,
    )
elif _api.USED_API == _api.QT_API_PYSIDE:
    from PySide.QtSvg import (
        QGraphicsSvgItem,
        QSvgGenerator,
        QSvgRenderer,
        QSvgWidget,
    )
