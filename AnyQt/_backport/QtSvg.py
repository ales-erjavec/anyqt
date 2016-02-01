from .. import _api

assert _api.USED_API == _api.QT_API_PYQT5

from PyQt5.QtSvg import (
    QGraphicsSvgItem,
    QSvgGenerator,
    QSvgRenderer,
    QSvgWidget,
)