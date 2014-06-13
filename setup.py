#!/usr/bin/env python

from distutils.core import setup

setup(name='pyglow',
    version='1.0',
    description='Python wrapper for piglow',
    author='Boeeerb',
    py_modules=['pyglow'],
    scripts=['scripts/enable_i2c.py']
)
