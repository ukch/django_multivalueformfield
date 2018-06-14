#!/usr/bin/env python

from setuptools import setup

setup(
    name='django_multivalueformfield',
    description='Multiple-value field for Django forms',
    version='0.0.1',
    url='https://github.com/ukch/django_multivalueformfield',
    author='Joel Cross',
    author_email='joel@kazbak.co.uk',
    py_modules=['multivaluefield'],
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django :: 2.0',
    ],
    install_requires=[
        'Django>=2.0',
    ],
)
