from numpy import random
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

sns.displot([0, 1, 2, 3, 4, 5])

plt.show()

sns.displot(random.normal(size=1000), kind="kde")

plt.savefig("plot.png")

x = random.normal(loc=1, scale=2, size=6)

print(x)

def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

arr = np.trunc([-3.1666, 3.6667])

print(arr)

arr = np.fix([-3.1666, 3.6667])

print(arr)

arr = np.around(3.1666, 2)

print(arr)

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# print(arr.shape)

# arr = np.array([1, 2, 3, 4], ndmin=5)

# print(arr)
# print('shape of array :', arr.shape)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# newarr = arr.reshape(2, 3, 2)

# print(newarr)

# arr = np.array([[1, 2, 3], [4, 5, 6]])

# newarr = arr.reshape(-1)

# print(newarr)

# arr = np.array([1, 2, 3, 4, 5, 6])

# newarr = np.array_split(arr, 3)

# print(newarr[0])
# print(newarr[1])
# print(newarr[2])

# arr = np.array([1, 2, 3, 4, 5])

# random.shuffle(arr)

# print(arr)

# print(random.permutation(arr))


