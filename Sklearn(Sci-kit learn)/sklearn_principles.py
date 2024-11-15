import pandas as pd
from sklearn.preprocessing import LabelEncoder
import warnings


warnings.filterwarnings("ignore", category=UserWarning)



data_set = pd.read_excel("C:/Users/PC/Desktop/Programlama/ClassifficationProject/Datasets/VeriOnIsleme_2.xlsx")

X = data_set.iloc[:, :-1].values
y = data_set.iloc[:, 5].values

label_encoder_X = LabelEncoder()
X[:, 0] = label_encoder_X.fit_transform(X[:, 0])
print(X)