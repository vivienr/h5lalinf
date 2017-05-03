#!/usr/bin/env python

try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

import argparse
import h5py

setup(
    name='h5lalinf',
    scripts=['h5lalinf'],
    description='Prints a glimpse of a LALInference HDF5 file.',
    version = '0.1',
    author='Vivien Raymond',
    author_email='vivien.raymond@ligo.org',
    url='https://github.com/vivienr/h5lalinf',
    install_requires=['argparse', 'h5py'],
)
