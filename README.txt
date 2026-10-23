AnyQt
-----

PyQt/PySide compatibility layer.

Features:

* At the top level AnyQt exports a Qt6 compatible module namespace along with
  some minimal renames to better support portability between different
  versions
* Which Qt api/backend is chosen can be controlled by a QT_API env variable
* The api can be chosen/forced programmatically (as long as no
  PyQt6/PyQt5/PySide6/PySide2 was already imported)
* provides an optional compatibility import hook, that denys imports from
  conflicting Qt api, or intercepts and fakes a Qt4 api imports, to use a Qt5
  compatible API (some monkey patching is involved).

The documentation is hosted at https://anyqt.readthedocs.io/en/stable/

