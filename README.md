#  Scaling Test

## Installation 

```
pip install . 
python run_benchmark.py
``

# Results for DAXPY (M2 Mac, ran on plane to test if threaded parallelism can be achieved / GIL was released)

```
Test Numpy
Threads: 1 | Median Time: 0.39301833299396094
Threads: 2 | Median Time: 0.131046750000678
Threads: 3 | Median Time: 0.11637654100195505
Threads: 4 | Median Time: 0.10126320800191024
Test Numpy (Presliced)
Threads: 1 | Median Time: 0.19371449999744073
Threads: 2 | Median Time: 0.13527887499367353
Threads: 3 | Median Time: 0.12237937500322005
Threads: 4 | Median Time: 0.10187695800414076
Testing Cython
Threads: 1 | Median Time: 0.08320249999815132
Threads: 2 | Median Time: 0.06291295800474472
Threads: 3 | Median Time: 0.04680183400341775
Threads: 4 | Median Time: 0.04009670799860032
Test Numba
Threads: 1 | Median Time: 0.31502479199843947
Threads: 2 | Median Time: 0.0647294160007732
Threads: 3 | Median Time: 0.05091737500333693
Threads: 4 | Median Time: 0.045245332999911625
Test Scipy
Threads: 1 | Median Time: 0.11216016700200271
Threads: 2 | Median Time: 0.11277187499945285
Threads: 3 | Median Time: 0.10452395900210831
Threads: 4 | Median Time: 0.10817854199558496
Test PyKokkos
Threads: 1 | Median Time: 0.034504124999998
Threads: 2 | Median Time: 0.03639695900000106
Threads: 3 | Median Time: 0.03581791700000281
Threads: 4 | Median Time: 0.03660024999999223

```

This is a very very memory bound kernel and does not get speedup

