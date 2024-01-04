#include "impl.hpp"

void daxpy(const double a, double *__restrict__ x, double *__restrict__ y,
           int start, int end) {
  for (int i = start; i < end; i++) {
    y[i] = a * x[i] + y[i];
  }
}
