from tests.test_numpy import test_scaling

print("Test Numpy")
test_scaling()

from tests.test_numpy import test_scaling_2 as test_scaling

print("Test Numpy (Presliced)")
test_scaling()

from tests.test_cython import test_scaling

print("Testing Cython")
test_scaling()

from tests.test_numba import test_scaling

print("Test Numba")
test_scaling()

from tests.test_scipy import test_scaling

print("Test Scipy")
test_scaling()
