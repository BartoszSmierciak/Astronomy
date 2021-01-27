import numpy as np
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

if __name__ == '__main__':
  print(angular_dist(21.07, 0.1, 21.15, 8.2))
  print(angular_dist(10.3, -3, 24.3, -29))
