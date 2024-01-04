from scipy.linalg.blas import daxpy as scipy_daxpy


def daxpy_handle(a, x, y, start, end):
    n = end - start
    scipy_daxpy(x=x, y=y, a=a, offx=start, offy=start, n=n)
