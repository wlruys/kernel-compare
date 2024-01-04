from numba import jit


@jit(nopython=True, nogil=True, parallel=False)
def daxpy_handle(a, x, y, start, end):
    for i in range(start, end):
        y[i] = a * x[i] + y[i]
