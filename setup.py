# -*- coding: utf-8 -*-
# file: setup.py

# This code is part of QuasiGraph

from pathlib import Path
from setuptools import setup, find_packages

setup(
    name = "quasigraph",
    version = "0.1.0",
    packages = find_packages(),
    author = "Leandro Seixas",
    author_email = "leandro.seixas@mackenzie.br", 
    url="https://github.com/leseixas/QuasiGraph",
    description = "QuasiGraph",
    long_description='''
    QuasiGraph
    ''',
    install_requires = [
        'numpy >= 1.26.*',
        'pandas >= 2.11.*',
        'ase >= 3.22.*',
        'mendeleev >= 0.14.*',
        'acat >= 1.5.*'
    ], 
    license = 'MIT',
    classifiers = [
         "Development Status :: 1 - Planning",
         "Programming Language :: Python :: 3",
         "Topic :: Scientific/Engineering :: Chemistry",
         "Topic :: Scientific/Engineering :: Physics",
         "Operating System :: OS Independent"
    ],
    python_requires = '>= 3.10.*'
)
