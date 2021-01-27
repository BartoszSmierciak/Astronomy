import numpy as np
import statistics
import time

def time_stat(func, size, ntrials):
  seconds = []
  for i in range(ntrials):
    data = np.random.rand(size)
    start = time.perf_counter()
    res = func(data)
    seconds.append(time.perf_counter() - start)
  mean = func(seconds)
  return mean

if __name__ == '__main__':
  print('{:.6f}s for statistics.mean'.format(time_stat(statistics.mean, 10**5, 10)))
  print('{:.6f}s for np.mean'.format(time_stat(np.mean, 10**5, 1000)))
