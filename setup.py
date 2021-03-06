from os import path
from codecs import open

import setuptools

from setuptools import find_packages, setup


here = path.abspath(path.dirname(__file__))


# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dumpenv',

    # Updated via travisd: https://travis-ci.org/guettli/dumpenv
    # See .travis.yml
    version='2018.10.0',

    description='dumpenv: Dump values of the current Python environment',
    long_description=long_description,

    url='https://github.com/guettli/dumpenv/',

    author='Thomas Guettler',
    author_email='info.dumpenv@thomas-guettler.de',

    license='Apache Software License 2.0',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Information Technology',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache Software License',


        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[],
    packages=setuptools.find_packages(),

    entry_points={
        'console_scripts': [
            'dumpenv=dumpenv:main',
        ],
    }
)
