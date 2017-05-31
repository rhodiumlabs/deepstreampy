import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='deepstreampy',
      version='0.1.1',
      author='Yavor Paunov',
      author_email='contact@yavorpaunov.com',
      description='A deepstream.io client.',
      license='MIT',
      url='https://www.github.com/YavorPaunov/deepstreampy',
      packages=setuptools.find_packages(),
      long_description=read('README.md'),
      test_suite='tests')
