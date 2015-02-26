'''
Created on Nov 18, 2012

@author: andre
'''

import numpy

from Cython.Build import cythonize
from numpy.distutils.core import setup, Extension

exts_c = cythonize(['example/*.pyx'])
exts_f = [Extension(name='example.example_f2py',
                 sources=['example/example_f2py.f'])]
setup(name='examples',
      version='0.1',
      description='Examples of cython usage.',
      author='Andre Luiz de Amorim',
      author_email='streetomon@gmail.com',
      license='MIT',
      packages=['example'],
      ext_modules=exts_f + exts_c,
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