import numpy as np
#import tensorflow as tf


def factorial(n):
     if n == 1:
          return 1
     elif n == 0:
          return 1
     elif n > 1:
          return n * factorial(n - 1)

print(factorial(7))

list = [[12, 41, 15, 16], [1, 4, 7, 6], [2, 4, 5, 3]]

print(np.sort(list))

dizi1 = np.array([1, 2, 11, 12])
dizi2 = np.array([7, 9, 3, 5])
print("Toplanmış dizi: ", dizi1 + dizi2)

print(np.matrix(list).shape)

dizi = np.arange(12)
dizi.shape = (3, 4)
print(dizi, "\n")
print(dizi[(0, 2), 1:4])