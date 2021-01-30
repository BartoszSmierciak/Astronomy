import numpy as np
def hms2dec(h,m,s):
  return 15*(h + m/60 + s/3600)

def dms2dec(d,m,s):
  if d < 0 :
    return -(-d + m/60 + s/3600)
  else:
    return (d + m/60 + s/3600)

  
def import_bss():
  cat = np.loadtxt('bss.dat', usecols=range(1, 7))
  i = 0
  bss = []
  for row in cat:
    i += 1
    bss.append((i, hms2dec(row[0],row[1],row[2]), dms2dec(row[3],row[4], row[5]))) 
  return bss
  
def import_super():
  cat = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
  sup = []
  i = 0
  for row in cat:
    i +=1
    sup.append((i, row[0],row[1]))
  return sup

def angular_dist(ra1, dec1, ra2, dec2):
  # Convert to radians
  r1 = np.radians(ra1)
  d1 = np.radians(dec1)
  r2 = np.radians(ra2)
  d2 = np.radians(dec2)

  a = np.sin(np.abs(d1 - d2)/2)**2
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2

  angle = 2*np.arcsin(np.sqrt(a + b))
    
  # Convert back to degrees
  return np.degrees(angle)

def find_closest(cat, ra, dec):
  min_dist = np.inf
  min_id = None
  for id1, ra1, dec1 in cat:
    dist = angular_dist(ra1, dec1, ra, dec)
    if dist < min_dist:
      min_id = id1
      min_dist = dist
    
  return min_id, min_dist


def crossmatch(cat1, cat2, max_radius):
  matches = []
  no_matches = []
  for id1, ra1, dec1 in cat1:
    id2, dist = find_closest(cat2, ra1, dec1)
    if dist > max_radius:
      no_matches.append(id1)
    else:
      matches.append((id1, id2, dist))
  return matches, no_matches


if __name__ == '__main__':
  bss_cat = import_bss()
  super_cat = import_super()


  max_dist = 40/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))

  max_dist = 5/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))
