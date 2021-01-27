#http://www.stat.cmu.edu/~ryantibs/papers/median.pdf
import numpy as np
def median_bins(data, B):
  
  mean = np.mean(data)
  std = np.std(data)
  
  minval = mean - std
  maxval = mean + std
  width = (2 * std)/B
  bins = np.zeros(B)
  ignore_bin = 0
  bin_ = 0
  for val in data:
    if val < minval:
      ignore_bin += 1
    elif val < maxval:
      bin_ = int((val - minval)/width)    
      bins[bin_] += 1
  return mean, std, ignore_bin, bins

def median_approx(data, B):
  mean, std, ignore_bin, bins = median_bins(data, B)
  n_data = len(data)
  midpoint  = (n_data + 1)/2
  count = ignore_bin
  for i, bincount in enumerate(bins):
    count += bincount
    if count >= midpoint:
      break
  width = (2 * std)/B
  median = mean - std + width*(i + 0.5)
  return median

if __name__ == '__main__':

  print(median_bins([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 1, 3, 2, 2, 6], 3))


  print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
  print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))
