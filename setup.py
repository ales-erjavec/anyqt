#! /usr/bin/env python
# encoding: utf-8
from setuptools import setup, find_packages

NAME = "AnyQt"
VERSION = "0.0.1.dev0"
AUTHOR = "Aleš Erjavec"
AUTHOR_EMAIL = "ales.erjavec@fri.uni-lj.si"
PACKAGES = find_packages(".")

SETUP_REQUIRES = [
    "setuptools"
]

if __name__ == "__main__":
    setup(
        name=NAME,
        version=VERSION,
        author_email=AUTHOR_EMAIL,
        packages=PACKAGES,
        setup_requires=SETUP_REQUIRES,
    )