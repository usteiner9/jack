import codecs
import os
import sys

from distutils.core import setup
from pip.req import parse_requirements

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload -r pypi')
    sys.exit()

PACKAGE_VERSION = '0.1.0'
PACKAGE_DOWNLOAD_URL = (
    'https://github.com/dbader/jack/tarball/' + PACKAGE_VERSION
)

install_reqs = parse_requirements('requirements.txt')
reqs = [str(ir.req) for ir in install_reqs]

def read_file(filename):
    """
    Read a utf8 encoded text file and return its contents.
    """
    with codecs.open(filename, 'r', 'utf8') as f:
        return f.read()

setup(
    name='jack',
    packages=['jack'],
    version=PACKAGE_VERSION,
    description='A command line tool for time-based queries on log files.',
    long_description=read_file('README.md'),
    license=read_file('LICENSE'),
    author='Daniel Bader',
    author_email='mail@dbader.org',
    url='https://github.com/dbader/jack',
    download_url=PACKAGE_DOWNLOAD_URL,
    install_requires=reqs,
    entry_points={
        'console_scripts': [
            'jack = jack:_main',
        ],
    },
    keywords=[
        'jack', 'log', 'logs', 'logging', 'query',
        'search'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Natural Language :: English',
    ],
)
