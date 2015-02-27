# cython-examples
Simple cython examples. Also contains f2py examples for comparison.

Run 'python setup.py build_ext --inplace' to compile the code, and 'python test.py' to run the test.

Sample test output on a 3 GHz mac:

```
macpro:cython-examples andre$ python test.py 
The functions work well.
Cython (naive) speedup: 1.5
Cython speedup: 202.4
numpy speedup: 252.0
Fortran (f2py) speedup: 651.0
```
