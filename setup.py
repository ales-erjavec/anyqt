#! /usr/bin/env python
# encoding: utf-8
import io

from setuptools import setup, find_packages

NAME = "AnyQt"
VERSION = "0.0.8"
AUTHOR = "Aleš Erjavec"
AUTHOR_EMAIL = "ales.erjavec@fri.uni-lj.si"
URL = "https://github.com/ales-erjavec/anyqt"
PACKAGES = find_packages(".")

DESCRIPTION = "PyQt4/PyQt5 compatibility layer."

with io.open("README.txt", encoding="utf-8") as f:
    README = f.read()

LICENSE = "GPLv3"

CLASSIFIERS = [
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
]

KEYWORDS = [
    "GUI", "PyQt4", "PyQt5", "compatibility"
]

if __name__ == "__main__":
    setup(
        name=NAME,
        version=VERSION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        url=URL,
        description=DESCRIPTION,
        long_description=README,
        license=LICENSE,
        keywords=KEYWORDS,
        classifiers=CLASSIFIERS,
        packages=PACKAGES,
        zip_safe=False,
    )
