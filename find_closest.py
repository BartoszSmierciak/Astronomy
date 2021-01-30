import numpy as np
def import_bss():
  cat = np.loadtxt('bss.dat', usecols=range(1, 7))
  i = 0
  bss = []
  for row in cat:
    i += 1
    if row[3] < 0 :
      bss.append((i, 15*(row[0] + row[1]/60 + row[2]/3600), -(-row[3] + row[4]/60 + row[5]/3600)))
    else:
      bss.append((i, 15*(row[0] + row[1]/60 + row[2]/3600), (row[3] + row[4]/60 + row[5]/3600)))   
  return bss

def angular_dist(ra1, dec1, ra2, dec2):
  ra1_rad = np.radians(ra1)
  ra2_rad = np.radians(ra2)
  dec1_rad = np.radians(dec1)
  dec2_rad = np.radians(dec2)
  
  a = np.sin(np.abs(dec1_rad - dec2_rad)/2)**2
  b = np.cos(dec1_rad)*np.cos(dec2_rad)*np.sin(np.abs(ra1_rad - ra2_rad)/2)**2
  d = 2*np.arcsin(np.sqrt(a + b))
  d = np.degrees(d)
  return d

def find_closest(cat, ra_s, dec_s):
  dist = []
  for row in cat:
    dist.append(angular_dist(ra_s, dec_s, row[1], row[2]))
  minimum = np.amin(dist)
  where = np.where(dist == np.amin(dist))
  return (int(where[0])+1, minimum)


if __name__ == '__main__':
  cat = import_bss()
  
  print(find_closest(cat, 175.3, -32.5))

  print(find_closest(cat, 32.2, 40.7))
