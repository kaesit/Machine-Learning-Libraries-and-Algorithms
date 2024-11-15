import numpy as np
from scipy import stats
from sklearn import datasets

iris = datasets.load_iris()

iris = datasets.load_iris()

canak_yaprak_uzunlugu = iris.data[:, 0]

en_kucuk = np.min(canak_yaprak_uzunlugu)

en_buyuk = np.max(canak_yaprak_uzunlugu)

X = (np.arange(150, dtype=float))

for i in range(150):
     X[i] = ((canak_yaprak_uzunlugu[i] - en_kucuk) / (en_buyuk - en_kucuk))
     print(X[i])