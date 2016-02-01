from . import _api

__all__ = [
    'QGL',
    'QGLContext',
    'QGLFormat',
    'QGLWidget'
]

if _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtOpenGL import (
        QGL,
        QGLContext,
        QGLFormat,
        QGLWidget,
    )

elif _api.USED_API == _api.QT_API_PYQT4:
    from PyQt4.QtOpenGL import (
        QGL,
        QGLContext,
        QGLFormat,
        QGLWidget,
    )

