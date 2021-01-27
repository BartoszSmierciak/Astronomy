def dms2dec(d,m,s):
  if d < 0 :
    return -(-d + m/60 + s/3600)
  else:
    return (d + m/60 + s/3600)

if __name__ == '__main__':
  print(dms2dec(22, 57, 18))
  print(dms2dec(-66, 5, 5.1))
