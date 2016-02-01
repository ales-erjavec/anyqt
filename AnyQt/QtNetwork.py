from . import _api

__all__ = [
    'QAbstractNetworkCache',
    'QAbstractSocket',
    'QAuthenticator',
    'QDnsDomainNameRecord',
    'QDnsHostAddressRecord',
    'QDnsLookup',
    'QDnsMailExchangeRecord',
    'QDnsServiceRecord',
    'QDnsTextRecord',
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
    'QSslCertificateExtension',
    'QSslCipher',
    'QSslConfiguration',
    'QSslEllipticCurve',
    'QSslError',
    'QSslKey',
    'QSslPreSharedKeyAuthenticator',
    'QSslSocket',
    'QTcpServer',
    'QTcpSocket',
    'QUdpSocket',
]

if _api.USED_API == _api.QT_API_PYQT5:
    import PyQt5.QtNetwork as _QtNetwork
    locals().update(
        {name: getattr(_QtNetwork, name) for name in __all__}
    )
    del _QtNetwork
elif _api.USED_API == _api.QT_API_PYQT4:
    import PyQt4.QtNetwork as _QtNetwork
    __missing__ = [
        'QDnsDomainNameRecord',
        'QDnsHostAddressRecord',
        'QDnsLookup',
        'QDnsMailExchangeRecord',
        'QDnsServiceRecord',
        'QDnsTextRecord',
        'QSslCertificateExtension',
        'QSslEllipticCurve',
        'QSslPreSharedKeyAuthenticator'
    ]
    locals().update(
        {name: getattr(_QtNetwork, name) for name in __all__
         if hasattr(_QtNetwork, name)}
    )
elif _api.USED_API == _api.QT_API_PYSIDE:
    import PySide.QtNetwork as _QtNetwork
    __missing__ = [name for name in __all__ if not hasattr(_QtNetwork, name)]
    locals().update(
        {name: getattr(_QtNetwork, name) for name in __all__
         if hasattr(_QtNetwork, name)}
    )
