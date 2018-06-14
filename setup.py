#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django_multivalueformfield",
    version="0.0.1",
    author="Joel Cross",
    author_email="joel@kazbak.co.uk",
    description="Multiple-value field for Django forms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ukch/django_multivalueformfield",
    py_modules=["multivaluefield"],
    license="MIT",
    classifiers=(
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Framework :: Django :: 2.0",
    ),
    install_requires=(
        "Django>=2.0",
    ),
)
