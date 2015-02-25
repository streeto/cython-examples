'''
Created on Nov 18, 2012

@author: andre
'''

import numpy

from distutils.core import setup
from Cython.Build import cythonize

setup(name='examples',
      version='0.1',
      description='Examples of cython usage.',
      author='Andre Luiz de Amorim',
      author_email='streetomon@gmail.com',
      license='MIT',
      packages=['example'],
      ext_modules=cythonize(['example/*.pyx']),
      include_dirs=[numpy.get_include()],
      provides=['example'],
      requires=['numpy', 'cython'],
      keywords=['Scientific/Engineering'],
      classifiers=[
                   "Development Status :: 4 - Beta",
                   "Programming Language :: Python",
                   "License :: OSI Approved :: MIT License",
                  ],
     )