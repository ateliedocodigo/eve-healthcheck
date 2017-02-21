#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools

__version__ = "0.0.0"
__project_name__ = "eve-healthcheck"
__repo__ = "https://github.com/ateliedocodigo/eve-healthcheck"

setuptools.setup(
    name=__project_name__,
    version=__version__,
    description="Python {} project".format(__project_name__),
    url=__repo__,
    download_url="{}/tarball/{}".format(__repo__, __version__),
    author="Luis Fernando Gomes",
    author_email="luiscoms@ateliedocodigo.com.br",
    license="MIT",
    classifiers=[  # See: https://pypi.python.org/pypi?%3Aaction=list_classifier
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    keywords="example eve_healthcheck",
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "eve_healthcheck_script = eve_healthcheck.script:main"
        ]
    }
)
