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

if _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtNetwork import *
elif _api.USED_API == _api.QT_API_PYQT4:
    from PyQt4.QtNetwork import *
elif _api.USED_API == _api.QT_API_PYSIDE:
    from PySide.QtNetwork import *
