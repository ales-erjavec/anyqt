#! /usr/bin/env python
# encoding: utf-8
import io

from setuptools import setup, find_packages

NAME = "AnyQt"
VERSION = "0.0.1.dev0"
AUTHOR = "Aleš Erjavec"
AUTHOR_EMAIL = "ales.erjavec@fri.uni-lj.si"
URL = "https://github.com/ales-erjavec/anyqt"
PACKAGES = find_packages(".")

DESCRIPTION = "PyQt4/PyQt5 compatibility layer."

with io.open("README.txt", encoding="utf-8") as f:
    README = f.read()

SETUP_REQUIRES = [
    "setuptools"
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
        packages=PACKAGES,
        setup_requires=SETUP_REQUIRES,
        zip_safe=False,
    )
