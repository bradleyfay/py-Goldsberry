from setuptools import setup

setup(name='py-goldsberry',
      version='0.0',
      description='Easy collection of NBA Statistics',
      long_description='Really, the funniest around.',
      url='http://github.com/bradleyfay/py-goldsberry',
      author='Bradley Fay',
      author_email='bradley.fay@gmail.com',
      license='MIT',
      keywords='funniest joke comedy flying circus',
      packages=['goldsberry'],
      install_requires=[
          'requests',
      ],
      include_package_data=True,
      zip_safe=False)
