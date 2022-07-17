from setuptools import setup
from setuptools import find_packages

setup(
    name='mypackage',
    version='0.0.1',
    install_requires=[
        'importlib-metadata; python_version == "3.8"',
    ],
    packages=find_packages(
        where='.',
        include=['mypackage*'],  # ["*"] by default
        exclude=['mypackage.tests'],  # empty by default
    ),
    entry_points={
        'console_scripts': [
            'cli-name = mypackage.mymodule:some_func',
        ]
    }
)
