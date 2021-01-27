def calculate_mean(data):
  return sum(data)/len(data)


if __name__ == '__main__':
  mean = calculate_mean([1,2.2,0.3,3.4,7.9])
  print(mean)
