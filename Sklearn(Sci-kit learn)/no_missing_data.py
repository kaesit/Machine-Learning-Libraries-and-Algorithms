import pandas as pd
import numpy as np
import warnings
from sklearn.impute import SimpleImputer


warnings.filterwarnings("ignore", category=UserWarning)



data_set = pd.read_excel("C:/Users/PC/Desktop/Programlama/ClassifficationProject/Datasets/VeriOnIsleme.xlsx")



X = data_set.iloc[:,:-1].values
y = data_set.iloc[:, 5].values

near_value = SimpleImputer(missing_values=np.nan, strategy='mean', 
                           fill_value=None, copy=True, add_indicator=False, 
                           keep_empty_features=False)

near_value = near_value.fit(X[:, 1:6])
X[:, 1:6] = near_value.transform(X[:, 1:6])

print("New Dataset with missing values not there anymore: \n", X)
print("Near Value Statictics: ", near_value.statistics_)