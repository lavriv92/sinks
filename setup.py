from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='sinks',
    version='0.1.0',
    package=find_packages()
    long_description=open(join(dirname(__file__), 'README.md')).read(),
)
