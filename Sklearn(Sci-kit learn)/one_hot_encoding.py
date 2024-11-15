import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from data_type_converter import DataTypeConverter
import warnings


warnings.filterwarnings("ignore", category=UserWarning)



data_set = pd.read_excel("C:/Users/PC/Desktop/Programlama/ClassifficationProject/Datasets/VeriOnIsleme_2.xlsx")

X = data_set.iloc[:, :-1].values
y = data_set.iloc[:, 5].values

label_encoder_X = LabelEncoder()
X[:, 0] = label_encoder_X.fit_transform(X[:, 0])

one_hot_encoder_X = OneHotEncoder(categories='auto', handle_unknown='ignore')
#X = one_hot_encoder_X.fit_transform(X).toarray()

transformer = ColumnTransformer(
     transformers=[
          (
               "OneHot",
               one_hot_encoder_X,
               [0]
          )
          ],remainder='passthrough'
)

X = transformer.fit_transform(X)

print(X)

