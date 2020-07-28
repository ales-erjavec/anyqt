import sys
import AnyQt._api as _api

if _api.USED_API == _api.QT_API_PYQT5:
    try:
        from PyQt5 import sip as __sip
    except ImportError:
        import sip as __sip
elif _api.USED_API == _api.QT_API_PYQT4:
    import sip as __sip
else:
    raise ImportError("AnyQt.sip")

sys.modules["AnyQt.sip"] = __sip
