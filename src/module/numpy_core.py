import numpy as np


def daxpy_handle(a, x, y, start, end):
    y[start:end] = a * x[start:end] + y[start:end]


def daxpy_handle_2(a, x, y, start, end):
    y_slice = y[start:end]
    x_slice = x[start:end]
    y_slice[:] = a * x_slice + y_slice
