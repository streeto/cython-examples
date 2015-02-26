'''
Created on 25/02/2015

@author: andre
'''
from example.example_cython import hypot_naive as hypot_c1
from example.example_cython import hypot as hypot_c2
from example.example_f2py import hypot as hypot_f
from example.example_python import hypot as hypot_p
from numpy.testing import assert_allclose
import numpy as np
import timeit

x = np.random.random(1000)
y = np.random.random(1000)

h_p = hypot_p(x, y)
h_c1 = hypot_c1(x, y)
h_c2 = hypot_c2(x, y)
h_f = np.zeros_like(x)
hypot_f(x, y, h_f)

# Function from the numpy library, written in Fortran.
h = np.hypot(x, y)

# Check if we did it right.
assert_allclose(h, h_p)
assert_allclose(h, h_c1)
assert_allclose(h, h_c2)
assert_allclose(h, h_f)

print 'The functions work well.'

times = 1000

t = timeit.Timer('hypot_c1(x, y)', 'from __main__ import hypot_c1, x, y')
time_c1 = t.timeit(times) / times

t = timeit.Timer('hypot_p(x, y)', 'from __main__ import hypot_p, x, y')
time_p = t.timeit(times) / times

times = 100000

t = timeit.Timer('hypot_c2(x, y)', 'from __main__ import hypot_c2, x, y')
time_c2 = t.timeit(times) / times

t = timeit.Timer('hypot_f(x, y, h_f)', 'from __main__ import hypot_f, x, y, h_f')
time_f = t.timeit(times) / times

t = timeit.Timer('hypot(x, y)', 'from __main__ import x, y; from numpy import hypot')
time_np = t.timeit(times) / times

print 'Cython (naive) speedup: %.1f' % (time_p / time_c1)
print 'Cython speedup: %.1f' % (time_p / time_c2)
print 'numpy speedup: %.1f' % (time_p / time_np)
print 'Fortran (f2py) speedup: %.1f' % (time_p / time_f)

