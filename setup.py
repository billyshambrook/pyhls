"""Project setup."""
from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys

import pyhls


class PyTest(TestCommand):

    """Extend test command to use py.test."""

    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        """Override options."""
        self.pytest_args = []

    def finalize_options(self):
        """Override options."""
        pass

    def run(self):
        """
        Override what is ran.

        Import here, cause outside the eggs aren't loaded
        """
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='pyhls',
    version=pyhls.__version__,
    url='http://github.com/billyshambrook/pyhls/',
    license='GNU V3',
    author='Billy Shambrook',
    tests_require=['pytest'],
    install_requires=[],
    cmdclass={'test': PyTest},
    author_email='billy.shambrook@gmail.com',
    description='A HTTP Live Streaming (HLS) python library.',
    packages=['pyhls'],
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Conversion',
        'Topic :: Multimedia :: Video',
        'Topic :: Multimedia :: Video :: Conversion'
    ],
    extras_require={
        'testing': ['pytest'],
    }
)
