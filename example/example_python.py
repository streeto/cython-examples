'''
Created on 25/02/2015

@author: andre
'''

from __future__ import division
import numpy as np

__all__ = ['hypot']

def hypot(x, y):
    
    h = np.empty_like(x)

    for i in xrange(len(x)):
        xi = x[i]
        yi = y[i]
        h[i] = np.sqrt(xi * xi + yi * yi)

    return h
