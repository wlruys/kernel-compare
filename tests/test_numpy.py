import threading
import time
import os

os.environ["MKL_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"

import numpy as np

from module import launcher, numpy_core


def test_scaling():
    N = 100_000_000
    for threads in range(1, 5):
        times = launcher(numpy_core.daxpy_handle, threads=threads, N=N, trials=5)
        print(f"Threads: {threads} | Median Time: {np.median(times)}", flush=True)


def test_scaling_2():
    N = 100_000_000
    for threads in range(1, 5):
        times = launcher(numpy_core.daxpy_handle_2, threads=threads, N=N, trials=5)
        print(f"Threads: {threads} | Median Time: {np.median(times)}", flush=True)
