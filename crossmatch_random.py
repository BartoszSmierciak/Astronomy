import numpy as np
import time

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
  return angle

def find_closest(cat, ra, dec):
  min_dist = np.inf
  min_id = None
  id2 = 0
  for ra1, dec1 in cat:
    dist = angular_dist(ra1,dec1,ra,dec)
    if dist < min_dist:
      min_id = id2
      min_dist = dist
    id2 += 1
    
  return min_id, np.degrees(min_dist)


def crossmatch(cat1, cat2, max_radius):
  matches = []
  no_matches = []
  id1 = 0
  start = time.perf_counter()
  for ra1, dec1 in cat1:
    id2, dist = find_closest(cat2, ra1, dec1)
    if dist > max_radius:
      no_matches.append(id1)
    else:
      matches.append((id1, id2, dist))
    id1 += 1
  seconds = time.perf_counter() - start
  return (matches, no_matches, seconds)


if __name__ == '__main__':
  # The example in the question
  cat1 = np.array([[180, 30], [45, 10], [300, -45]])
  cat2 = np.array([[180, 32], [55, 10], [302, -44]])
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

  # A function to create a random catalogue of size n
  def create_cat(n):
    ras = np.random.uniform(0, 360, size=(n, 1))
    decs = np.random.uniform(-90, 90, size=(n, 1))
    return np.hstack((ras, decs))

  # Test your function on random inputs
  np.random.seed(0)
  cat1 = create_cat(10)
  cat2 = create_cat(20)
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)
