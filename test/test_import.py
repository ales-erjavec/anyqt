import subprocess
import sys

apis = {
    'pyqt4': 'PyQt4',
    'pyqt5': 'PyQt5',
    'pyside': 'PySide',
    'pyside2': 'PySide2',
    'pyqt6:': "PyQt6"
}

submodules_common = [
    'QtCore',
    'QtGui',
    'QtHelp',
    'QtMultimedia',
    'QtNetwork',
    'QtOpenGL',
    'QtPrintSupport',
    'QtSql',
    'QtSvg',
    'QtTest',
    'QtWidgets',
    'QtXml',

]
submodules_qt4 = [
    'QtXmlPatterns'
]
submodules_qt5 = [
    'QtMultimediaWidgets',
    'QtWebChannel',
    'QtWebEngineWidgets',
    'QtWebEngineCore',
    'QtWebSockets',
    'QtQml',
    'QtXmlPatterns',
]

submodules_qt6 = [
    "QtSvgWidgets",
]


def get_qt_version(modname):
    cmd = [sys.executable, '-c', 'import '+modname+';from AnyQt.QtCore import QT_VERSION_STR; print(QT_VERSION_STR)']
    return subprocess.check_output(cmd)


def try_import(modname):
    cmd = [sys.executable, '-c', 'import '+modname]
    ret = subprocess.call(cmd)
    return ret == 0


def try_import_anyqt(modname, submodule):
    cmd = [sys.executable, '-c', 'import '+modname+'; import AnyQt.'+submodule]
    ret = subprocess.call(cmd)
    return ret == 0


for api in apis:
    modname = apis[api]
    if try_import(modname):
        qt_version = get_qt_version(modname).decode()
        print('-- Found', modname, 'Qt=', qt_version)
        submodules = list(submodules_common)
        if qt_version[0] == '4':
            submodules.extend(submodules_qt4)
        if qt_version[0] == '5':
            submodules.extend(submodules_qt5)
        if qt_version[0] == '6':
            submodules.extend(submodules_qt6)
        for submodule in submodules:
            if try_import_anyqt(modname, submodule):
                print(submodule, 'Ok')
            else:
                print(submodule, 'FAIL')
    else:
        print(modname, '-- not found')
    

