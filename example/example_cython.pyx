'''
Created on Jun 13, 2013

@author: andre
'''
from __future__ import division
import numpy as np
cimport numpy as np
cimport cython

__all__ = ['hypot', 'hypot_naive']

cdef extern from 'math.h':
    double sqrt(double x)

@cython.boundscheck(False)
def hypot(np.ndarray[np.double_t, ndim=1, mode='c'] x not None,
          np.ndarray[np.double_t, ndim=1, mode='c'] y not None):

    cdef unsigned int i
    cdef unsigned int N = len(x)
    cdef double xi, yi
    cdef np.ndarray[np.double_t, ndim=1, mode='c'] h = np.empty(N, dtype=np.float64)
    
    for i from 0 <= i < N:
        xi = x[i]
        yi = y[i]
        h[i] = sqrt(xi * xi + yi * yi)

    return h


def hypot_naive(x, y):
    
    h = np.empty_like(x)

    for i in xrange(len(x)):
        xi = x[i]
        yi = y[i]
        h[i] = np.sqrt(xi * xi + yi * yi)

    return h
