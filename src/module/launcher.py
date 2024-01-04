import threading
import time
import os
from typing import Callable
import numpy as np


def launcher(
    func: Callable[[float, np.ndarray, np.ndarray, int, int], None],
    N=1000000,
    threads=4,
    trials=1,
):
    times = np.zeros(trials)
    for k in range(trials):
        np.random.seed(0)
        x = np.random.rand(N)
        y = np.random.rand(N)

        running_threads = []
        for i in range(threads):
            start_idx = int(i * N / threads)
            end_idx = int((i + 1) * N / threads)
            args = (2.0, x, y, start_idx, end_idx)
            t = threading.Thread(target=func, args=args)
            running_threads.append(t)

        start_t = time.perf_counter()
        for t in running_threads:
            t.start()

        for t in running_threads:
            t.join()
        end_t = time.perf_counter()
        duration = end_t - start_t
        times[k] = duration

        # print("Time taken: {}".format(duration), flush=True)
    return times
