import setuptools


setuptools.setup(
    name="boilerplate",
    version="0.1",
    description="Python boilerplate project",
    url="https://github.com/westphahl/boilerplate",
    author="Simon Westphahl",
    author_email="westphahl@gmail.com",
    license="MIT",
    classifiers=[  # See: https://pypi.python.org/pypi?%3Aaction=list_classifier
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    keywords="example boilerplate",
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "boilerplate_script = boilerplate.script:main"
        ]
    }
)
