# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import os

from setuptools import find_packages, setup

BASE_DIR = os.path.dirname(__file__)

with open(os.path.join(BASE_DIR, 'README.md')) as readme:
    README = readme.read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='bittrex-test',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='Just a test',
    long_description=README,
    url='http://dryice.name/',
    author='Dryice Liu',
    author_email='dryiceliu@gmail.com',
    classifiers=[
        'Environment :: CLI',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=['bittrex'],
)
