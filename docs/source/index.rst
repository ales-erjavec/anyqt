.. AnyQt documentation master file, created by
   sphinx-quickstart on Wed Apr  6 10:32:15 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to AnyQt's documentation!
=================================

AnyQt is a PyQt4/PyQt5 compatibility layer intended as a stepping stone to
full PyQt5 support while still providing support for PyQt4.

The idea is to use use a forward compatible module structure that mimics that
of Qt5, even when using Qt4

By default PyQt5 is used if available, but that can be changed by a QT_API env
variable (which can take either 'pyqt4' or 'pyqt5' values), or setting the
preferred api using the :func:`AnyQt.setpreferredapi`. However if any of the
Qt apis is already imported (listed in `sys.modules`) then it is used instead.

.. note::
   The final choice of api is delayed until the first AnyQt.Qt* module
   is imported


Contents:

.. toctree::
   :maxdepth: 2

   anyqt


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
