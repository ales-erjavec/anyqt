.. module:: AnyQt


:mod:`AnyQt`
============

.. autofunction:: availableapi

.. autofunction:: setpreferredapi

.. autofunction:: selectapi

.. autodata:: USED_API


:mod:`AnyQt.QtCore`
-------------------

Export a Qt6 compatible QtCore module.

* :class:`QSignalMapper` imported from this module has `mappedInt`,
  `mappedString`, `mappedObject` and `mappedWidget` signals defined even
  when not present in Qt < 5.15. Use these instead of deprecated `mapped`
  overloads for forward compatibility with Qt6

  .. note:: A subclass of the real QSignalMapper is used.

* A forward compatible :func:`QLibraryInfo.path` is available (new in Qt6
  replaces :func:`QLibrartInfo.location`)


Use `AnyQt.QtCore.QT_VERSION` to check if a feature is present.

In adition :func:`cast`, :func:`isdeleted`, :func:`ispyowned`,
:func:`ispycreated`, :func:`delete`, :func:`unwrapinstance` and
:func:`wrapinstance` as defined by PyQt6.sip module.

:mod:`AnyQt.QtGui`
------------------

Export a Qt6 compatible QtGui module.

* A backported QGuiApplication.screenAt static method is added if not
  implemented by Qt5

* A QFontMetrics(F).horizontalAdvance method is made available if not present
  in Qt (<5.11)

* An missing QPdfWriter.setPageSize(QPageSize) overload for PyQt5 is added.

* All members of :class:`QFontDatabase` can be called as static methods the
  same way as in Qt 6.

* :class:`QAction` has ctypes based :func:`menu()` and  :func:`setMenu()`
  members if/when not present in PyQt6

* :class:`QFileSystemModel` is exported here when using PyQt5


:mod:`AnyQt.QtWidgets`
----------------------

Export a Qt6 compatible QtWidgets module

* A backward compatible :func:`QAbstractItemView.viewOptions` method is made
  available when using a Qt6 backend.

* A forward compatible :func:`QAbstractItemView.itemDelegateForIndex` method
  is made available (new in Qt 6.0). Use this instead of deprecated
  :func:`QAbstractItemView.itemDelegate(QModelIndex)` overload.

* A :func:`QWidget.screen` method is made available when not present in
  Qt5 (<5.14).

* :class:`QButtonGroup` imported from this module has `idClicked`, `idPressed`,
  `idReleased` and `idToggled` signals defined even when not present in
  Qt < 5.15. Use these instead of `clicked[int]`, `pressed[int]` and
  `toggled[int]` overloads for compatibility with Qt6 where they are
  removed.

  .. note:: A subclass of the real QGroupBox is used.

* :class:`QComboBox` imported from this module has `textActivated` and
  `textHighlighted` signals defined even when not present in Qt < 5.14.
  Use these instead of `activated[int]` and `highlighted[int]` overloads
  for compatibility with Qt6 where they are removed.

  .. note:: A subclass of the real QComboBox is used.

* :func:`QTextEdit.setTabStopDistance`, `QTextEdit.tabStopDistance`
  :func:`QPlainTextEdit.setTabStopDistance` :func:`QTextPlainEdit.setTabStopDistance`
  are made available if not present Qt5 (<5.10). Use these instead of the obsolete
  `setTabStopWidth` ...

:mod:`AnyQt.QtMultimedia`
-------------------------

:mod:`AnyQt.QtMultimediaWidgets`
--------------------------------

:mod:`AnyQt.QtNetwork`
----------------------

:mod:`AnyQt.QtPrintSupport`
---------------------------

:mod:`AnyQt.Qml`
----------------

:mod:`AnyQt.QtQuick`
--------------------

:mod:`AnyQt.QtSql`
------------------

:mod:`AnyQt.QtSvg`
------------------

:mod:`AnyQt.QtSvgWidgets`
-------------------------
A Qt6 compatible QtSvgWidgets module

:mod:`AnyQt.QtTest`
-------------------

:mod:`AnyQt.QtDBus`
-------------------

:mod:`AnyQt.QtDesigner`
-----------------------

:mod:`AnyQt.QtHelp`
-------------------

:mod:`AnyQt.QtOpenGL`
---------------------

:mod:`AnyQt.QtWebChannel`
-------------------------------

:mod:`AnyQt.QtWebEngineWidgets`
-------------------------------

:mod:`AnyQt.QtWebSockets`
-------------------------------

:mod:`AnyQt.QtXml`
------------------

:mod:`AnyQt.QtXmlPatterns`
--------------------------

:mod:`AnyQt.sip`
----------------

When using a PyQt5/6 then this is an alias for the corresponding sip module
