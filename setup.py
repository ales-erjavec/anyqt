#! /usr/bin/env python
# encoding: utf-8
import io

from setuptools import setup, find_packages

NAME = "AnyQt"
VERSION = "0.2.1"
AUTHOR = "Aleš Erjavec"
AUTHOR_EMAIL = "ales.erjavec@fri.uni-lj.si"
URL = "https://github.com/ales-erjavec/anyqt"
PACKAGES = find_packages(".", include="AnyQt*")

DESCRIPTION = "PyQt5/PyQt6 compatibility layer."

with io.open("README.txt", encoding="utf-8") as f:
    README = f.read()

LICENSE = "GPLv3"

CLASSIFIERS = [
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
]

KEYWORDS = [
    "GUI", "PyQt4", "PyQt5", "PySide", "PySide2", "compatibility"
]

PROJECT_URLS = {
    "Bug Reports": "https://github.com/ales-erjavec/anyqt/issues",
    "Source": URL,
    "Documentation": "https://anyqt.readthedocs.io/en/stable/"
}

if __name__ == "__main__":
    setup(
        name=NAME,
        version=VERSION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        url=URL,
        description=DESCRIPTION,
        long_description=README,
        long_description_content_type="text/plain",
        license=LICENSE,
        keywords=KEYWORDS,
        classifiers=CLASSIFIERS,
        packages=PACKAGES,
        project_urls=PROJECT_URLS,
        python_requires=">=3.6",
    )
