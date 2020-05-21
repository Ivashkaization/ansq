import sys
from setuptools import setup, find_packages
from ansq import __version__

PY_VER = sys.version_info
install_requires = [
    'aiohttp==3.6.2',
]

classifiers = [
    'License :: OSI Approved :: MIT License',
    'Development Status :: 4 - Beta',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries',
]

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='ansq',
    version=__version__.__version__,
    description='Enhanced, written with native Asynchronous I/O NSQ package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=classifiers,
    author='Alexander "GinTR1k" Karateev',
    author_email='administrator@gintr1k.space',
    url='https://github.com/GinTR1k/ansq',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=install_requires,
    include_package_data=True,
)
