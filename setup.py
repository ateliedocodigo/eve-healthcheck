#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import abspath, dirname, join

import setuptools

__version__ = "0.3.0"
__project_name__ = "eve-healthcheck"
__repo__ = "https://github.com/ateliedocodigo/eve-healthcheck"


def read(fname):
    with open(join(abspath(dirname(__file__)), fname)) as thefile:
        return thefile.read()
    # return open(os.path.join(os.path.dirname(__file__), fname)).read()


setuptools.setup(
    name=__project_name__,
    version=__version__,
    description="Python {} project".format(__project_name__),
    long_description=read("README.rst"),
    author="Luis Fernando Gomes",
    author_email="luiscoms@ateliedocodigo.com.br",
    url=__repo__,
    download_url="{}/tarball/{}".format(__repo__, __version__),
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    keywords="healthcheck eve_healthcheck",
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    install_requires=read("requirements.txt"),
)
