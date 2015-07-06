# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

setup(name='py-goldsberry',
      version='0.1',
      description='A Python Package for easily acquiring NBA Data for analysis',
      long_description='This is a big work-in-progress, but should be useful in the future.',
      url='http://github.com/bradleyfay/py-goldsberry',
      author='Bradley Fay',
      author_email='bradley.fay@gmail.com',
      license='MIT',
      keywords='funniest joke comedy flying circus',
      packages=['goldsberry'],
      install_requires=['requests>=2.2.1'],
      include_package_data=True,
      zip_safe=False)
