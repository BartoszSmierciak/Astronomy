import numpy as np
from astropy.io import fits

def mean_fits(files):
  fitslist = []
  for file in files:
    hdulist = fits.open(file)
    fitslist.append(hdulist[0].data)
    
  mean = sum(fitslist)/len(fitslist)
  return mean
    


if __name__ == '__main__':
  data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
  print(data[100, 100])

  # plot:
  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()
