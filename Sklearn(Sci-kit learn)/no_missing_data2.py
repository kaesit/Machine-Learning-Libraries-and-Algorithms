import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer


dizi = [[5, 6, np.nan, 54, 6.2, 8.4, 6, 23], 
        [43, np.nan, 8.3, 6.5, np.nan, 6.7, 5.9, 4.3]] #? Bu kullanım zorluk çıkarır

dizi = pd.DataFrame([[5, 6.5, np.nan], 
                     [54, 6.2, 8.4], 
                     [6, 23, 6.5], 
                     [43, np.nan, 8.3], 
                     [np.nan, 6.5, 6.7], 
                     [5.9, 4.3, 2.1]], dtype='category') 
#! Pandas kütüphanesinin bu iş için özelleştirilmiş DataFrame özelliğini kullanmak her zaman daha iyidir.

dizi2 = pd.DataFrame([["DataFrame", 5, 6.5, np.nan], 
                     ["DataFrame", 54, 6.2, 8.4], 
                     ["DataFrame", 6, 23, 6.5], 
                     ["DataFrame", 43, np.nan, 8.3], 
                     ["DataFrame", np.nan, 6.5, 6.7], 
                     ["DataFrame", 5.9, 4.3, 2.1]], dtype='object') 




near_value = SimpleImputer(missing_values=np.nan, strategy='mean', 
                           fill_value=None, copy=True, add_indicator=False, 
                           keep_empty_features=False)

near_value2 = SimpleImputer(missing_values=np.nan, strategy='most_frequent', 
                           fill_value=None, copy=True, add_indicator=False, 
                           keep_empty_features=False)


X = dizi2.iloc[:, :-1].values
y = dizi2.iloc[:, 3].values

near_value = near_value.fit(X[:, 1:6])
X[:, 1:6] = near_value.transform(X[:, 1:6])

print("Ortalama Değerler Eklenince: \n", X)
print("Ortalama Değerler Eklenince: \n", near_value.fit_transform(dizi))
print("En Çok Tekrar Eden Değerler Eklenince: \n", near_value2.fit_transform(dizi))
