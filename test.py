'''
Created on 25/02/2015

@author: andre
'''
from example.example_cython import hypot as hypot_c
from example.example_python import hypot as hypot_p
from numpy.testing import assert_allclose
import numpy as np

x = np.random.random(1000)
y = np.random.random(1000)

h_p = hypot_p(x, y)
h_c = hypot_c(x, y)

# Function from the numpy library, written in Fortran.
h = np.hypot(x, y)

# Check if we did it right.
assert_allclose(h, h_p)
assert_allclose(h, h_c)

print 'The functions work well.'

'''
Test with 3 GHz macbook:

In [11]: timeit np.hypot(x,y)
100000 loops, best of 3: 11.1 us per loop

In [12]: timeit hypot_c(x,y)
100000 loops, best of 3: 13.2 us per loop

In [13]: timeit hypot_p(x,y)
100 loops, best of 3: 5.63 ms per loop
'''