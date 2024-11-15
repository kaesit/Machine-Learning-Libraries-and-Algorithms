import numpy as np
from scipy import stats
from sklearn import datasets

iris = datasets.load_iris()

canak_yaprak_uzunlugu = iris.data[:, 0]

ortalama = np.mean(canak_yaprak_uzunlugu)

standart_sapma = np.std(canak_yaprak_uzunlugu)

X = (np.arange(150, dtype=float))

for i in range(150):
     X[i] = ((canak_yaprak_uzunlugu[i] - ortalama) / standart_sapma)
     print(X[i])