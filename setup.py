from __future__ import print_function

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import goldsberry

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
      encoding = kwargs.get('encoding', 'utf-8')
      sep = kwargs.get('sep','\n')
      buf = []
      for filename in filenames:
            with io.open(filename, encoding=encoding) as f:
                  buf.append(f.read())
            return sep.join(buf)

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.rst') as changelog_file:
    changelog = changelog_file.read().replace('.. :changelog:', '')

class PyTest(TestCommand):
      def finalize_options(self):
            TestCommand.Finalize_options(self)
            self.test_args = []
            self.test_suite = True

      def run_test(self):
            import pytest
            errcode = pytest.main(self.test_args)
            sys.exit(errcode)

setup(
      name='py-goldsberry',
      version=goldsberry.__version__,
      url='http://github.com/bradleyfay/py-goldsberry',
      license='MIT',
      author='Bradley Fay',
      author_email='bradley.fay@gmail.com',
      tests_require=['pytest'],
      install_requires=['requests>=2.7'],
      description='API interface for stats.nba.com',
      long_description=readme + '\n\n' + changelog,
      packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
      include_package_data=True,
      platforms='any',
      keywords='sports NBA basketball',
      zip_safe=False,
      classifiers=[
      'Development Status :: 3 - Alpha',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 2.6',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.2',
      'Programming Language :: Python :: 3.3',
      'Programming Language :: Python :: 3.4'
      ]
      )

#!/usr/bin/env python
# -*- coding: utf-8 -*-
