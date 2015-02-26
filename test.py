'''
Created on 25/02/2015

@author: andre
'''
from example.example_cython import hypot as hypot_c
from example.example_f2py import hypot as hypot_f
from example.example_python import hypot as hypot_p
from numpy.testing import assert_allclose
import numpy as np

x = np.random.random(1000)
y = np.random.random(1000)

h_p = hypot_p(x, y)
h_c = hypot_c(x, y)
h_f = np.zeros_like(x)
hypot_f(x, y, h_f)

# Function from the numpy library, written in Fortran.
h = np.hypot(x, y)

# Check if we did it right.
assert_allclose(h, h_p)
assert_allclose(h, h_c)
assert_allclose(h, h_f)

print 'The functions work well.'

'''
In [1]: run test.py
The functions work well.

In [2]: timeit np.hypot(x,y)
100000 loops, best of 3: 11.2 us per loop

In [3]: timeit hypot_f(x,y,h_f)
100000 loops, best of 3: 3.93 us per loop

In [4]: timeit hypot_c(x,y)
100000 loops, best of 3: 12.8 us per loop

In [5]: timeit hypot_p(x,y)
100 loops, best of 3: 5.63 ms per loop
'''
