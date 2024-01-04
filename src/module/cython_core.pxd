cdef extern from "impl.hpp" nogil:
    cdef void daxpy(const double a, double* x, double* y, int start, int end) noexcept
