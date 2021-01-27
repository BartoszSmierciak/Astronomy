import numpy as np

def mean_datasets(files):
  alldata = []
  for file in files:
    data = np.loadtxt(file, delimiter = ',')
    alldata.append(np.asarray(data, float))
  mean = np.around(sum(alldata)/len(files),1)
  return mean
      
if __name__ == '__main__':
  print(mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))
  print(mean_datasets(['data4.csv', 'data5.csv', 'data6.csv']))
