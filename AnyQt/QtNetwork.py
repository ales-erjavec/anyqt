from . import _api

# Names imported from Qt4' QtNetwork module
__Qt4_QtNetwork = [
    'QAbstractNetworkCache',
    'QAbstractSocket',
    'QAuthenticator',
    # 'QDnsDomainNameRecord',
    # 'QDnsHostAddressRecord',
    # 'QDnsLookup',
    # 'QDnsMailExchangeRecord',
    # 'QDnsServiceRecord',
    # 'QDnsTextRecord',
    'QHostAddress',
    'QHostInfo',
    'QHttpMultiPart',
    'QHttpPart',
    'QLocalServer',
    'QLocalSocket',
    'QNetworkAccessManager',
    'QNetworkAddressEntry',
    'QNetworkCacheMetaData',
    'QNetworkConfiguration',
    'QNetworkConfigurationManager',
    'QNetworkCookie',
    'QNetworkCookieJar',
    'QNetworkDiskCache',
    'QNetworkInterface',
    'QNetworkProxy',
    'QNetworkProxyFactory',
    'QNetworkProxyQuery',
    'QNetworkReply',
    'QNetworkRequest',
    'QNetworkSession',
    'QSsl',
    'QSslCertificate',
    # 'QSslCertificateExtension',
    'QSslCipher',
    'QSslConfiguration',
    # 'QSslEllipticCurve',
    'QSslError',
    'QSslKey',
    # 'QSslPreSharedKeyAuthenticator',
    'QSslSocket',
    'QTcpServer',
    'QTcpSocket',
    'QUdpSocket',
]
if _api.USED_API == _api.QT_API_PYQT6:
    from PyQt6.QtNetwork import *
elif _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtNetwork import *
elif _api.USED_API == _api.QT_API_PYQT4:
    from PyQt4.QtNetwork import *
elif _api.USED_API == _api.QT_API_PYSIDE:
    from PySide.QtNetwork import *
elif _api.USED_API == _api.QT_API_PYSIDE2:
    from PySide2.QtNetwork import *
elif _api.USED_API == _api.QT_API_PYSIDE6:
    from PySide6.QtNetwork import *
else:
    raise ImportError(f"No module named '{__name__}' in the selected "
                      f"Qt api ({_api.USED_API})")

_api.apply_global_fixes(globals())
