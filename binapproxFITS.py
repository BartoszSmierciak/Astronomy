from helper import running_stats
 #TODO: change running_stats to mean, std functions
from astropy.io import fits
import numpy as np
def median_bins_fits(filenames, B):
  
  mean, std = running_stats(filenames)
  
  dim = mean.shape
  
  width = (2 * std)/B
  bins = np.zeros((dim[0],dim[1],B))
  ignore_bin = np.zeros(dim)

  for file in filenames:
    hdulist = fits.open(file)
    data = hdulist[0].data
    
    for i in range(dim[0]):
      for j in range(dim[1]):
        val = data[i,j]
        mean_ = mean[i,j]
        std_ = std[i,j]
        if val < mean_ - std_:
          ignore_bin[i, j] += 1
        elif val >= mean_ - std_ and val < mean_ + std_:
          bin_ = int((val - (mean_ - std_))/width[i, j])    
          bins[i, j, bin_] += 1
  return mean, std, ignore_bin, bins

def median_approx_fits(filenames, B):
  mean, std, ignore_bin, bins = median_bins_fits(filenames, B)
  dim = mean.shape
  n_data = len(filenames)
  midpoint  = (n_data + 1)/2
  width = (2 * std)/B
  median = np.zeros(dim)
  for i in range(dim[0]):
    for j in range(dim[1]):
      count = ignore_bin[i, j]
      for b, bincount in enumerate(bins[i,j]):
        count += bincount
        if count >= midpoint:
          break
      median[i, j] = mean[i, j] - std[i, j] + width[i,j]*(b + 0.5)
  
  return median


if __name__ == '__main__':
  mean, std, left_bin, bins = median_bins_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)
  median = median_approx_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)
  
