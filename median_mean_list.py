def list_stats(data):
  mean = sum(data)/len(data)
  sort_data = data.sort()
  mid = len(data)//2
  if len(data) % 2 == 0:
    median = (data[mid -1] + data[mid])/2
  else:
    median = data[mid]
  return median, mean

if __name__ == '__main__':

  m = list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 2.7])
  print(m)

  m = list_stats([1.5])
  print(m)
