from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

iris = datasets.load_iris()

model = LogisticRegression()

rfe = RFE(estimator=model, n_features_to_select=3)
rfe = rfe.fit(iris.data, iris.target)

print(rfe.support_)
