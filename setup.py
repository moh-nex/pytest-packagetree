#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


setup(
    name='pytest-packagetree',
    version='0.0.1',
    author='Joshua Fehler',
    author_email='jsfehler@gmail.com',
    maintainer='Joshua Fehler',
    maintainer_email='jsfehler@gmail.com',
    license='MIT',
    url='https://github.com/jsfehler/pytest-packagetree',
    description='Pytest plugin or package-tree',
    py_modules=['pytest_packagetree', 'hooks'],
    install_requires=['pytest>=3.5.0', 'package-tree'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'splinter_stere = pytest_packagetree',
        ],
    },
)
