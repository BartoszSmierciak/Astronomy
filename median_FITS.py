from astropy.io import fits
from statistics import median
import numpy as np
import time

def median_fits(files):
  fitslist = []
  #time start
  start = time.perf_counter()
  for file in files:
    hdulist = fits.open(file)
    fitslist.append(hdulist[0].data)
  fitslist= np.asarray(fitslist)
  med = np.median(fitslist,axis=0)
  #time end
  timer = time.perf_counter() - start
  sizefits = fitslist.nbytes
  size = (sizefits)/1024
  return med, timer, size

if __name__ == '__main__':
  result = median_fits(['image0.fits', 'image1.fits'])
  print(result[0][100, 100], result[1], result[2])
  
  result = median_fits(['image{}.fits'.format(str(i)) for i in range(11)])
  print(result[0][100, 100], result[1], result[2])
