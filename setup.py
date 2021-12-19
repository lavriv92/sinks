import pathlib
from setuptools import setup, find_packages

BASE_DIR = pathlib.Path(__file__).parent
README = (BASE_DIR / 'README.md').read_text()


setup(
    name='sinks',
    version='0.1.0',
    description='Simple elegant library which provides simple stream sources and operators',
    author_email='lavriv92@gmail.com',
    author='Ivan Lavriv',
    install_requires=['requests'],
    package=find_packages(exclude=('examples','tests',)),
    long_description=README,
    long_description_content_type='text/markdown',
    include_package_data=True,
    licence='MIT',
)
