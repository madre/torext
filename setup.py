#!/usr/bin/python
# -*- coding: utf-8 -*-

__version__ = '0.1'

from setuptools import setup

setup(
    name='torext',
    version=__version__,
    author='Nodemix',
    author_email='novoreorx@gmail.com',
    url='http://nodemix.com',
    description='torext is an instrumental package which aim at easy implementation of tornado based project',
    packages=[
        'torext',
        'torext.handler',
        'torext.utils',
        'torext.scripts',
        'torext.third'
    ],
    package_data = {
        'torext': ['fixtures/base_options.yaml', 
                   'fixtures/custom_options_template.yaml']
    },
    scripts=['bin/torext_syntax'],

    install_requires=[
        'tornado==2.2.1',
        'yaml',
        'pymongo>=2.1',
        'redis>=2.4',
        'pika>=0.9.5',
        'requests>=0.9',
        'pyflakes>=0.5.0'
    ]
)
