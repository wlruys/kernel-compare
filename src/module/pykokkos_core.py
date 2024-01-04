import pykokkos as pk
import numpy as np

pk.set_default_space(pk.OpenMP)


@pk.workunit
def daxpy_kernel(
    tid: int,
    a: float,
    x: pk.View1D[float],
    y: pk.View1D[float],
    start: int,
    end: int,
    stride: int = 1,
):
    for i in range(start + tid, end, stride):
        y[i] = a * x[i] + y[i]


def daxpy_handle(
    a: float,
    x: pk.View1D[float] | np.ndarray,
    y: pk.View1D[float] | np.ndarray,
    start: int,
    end: int,
):
    if isinstance(x, np.ndarray):
        x = pk.array(x)
    if isinstance(y, np.ndarray):
        y = pk.array(y)

    num_threads = 1
    pk.parallel_for(
        num_threads,
        daxpy_kernel,
        a=a,
        x=x,
        y=y,
        start=start,
        end=end,
        stride=num_threads,
    )
