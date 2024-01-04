import cython

@cython.boundscheck(False)
@cython.nonecheck(False)
cpdef daxpy_handle(double a, double[:] x, double[:] y, int start, int end) noexcept:
    with nogil:
        daxpy(<double>a, <double*>&x[0], <double*>&y[0], <int>start, <int>end)


