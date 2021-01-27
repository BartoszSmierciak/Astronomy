def hms2dec(h,m,s):
  return 15*(h + m/60 + s/3600)


if __name__ == '__main__':
  print(hms2dec(23, 12, 6))
