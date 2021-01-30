import numpy as np
#bss:
# 1  00 04 35.65 -47 36 19.1
# 2  00 10 35.92 -30 27 48.3

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
  
#super:
#RA,Dec
#1.0583407,-52.9162402
#2.6084425,-41.5005753

def import_super():
  cat = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
  sup = []
  i = 0
  for row in cat:
    i +=1
    sup.append((i, row[0],row[1]))
  return sup

if __name__ == '__main__':

  bss_cat = import_bss()
  super_cat = import_super()
  print(bss_cat)
  print(super_cat)
