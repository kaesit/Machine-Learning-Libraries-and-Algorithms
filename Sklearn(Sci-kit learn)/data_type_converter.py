from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

class DataTypeConverter(BaseEstimator, TransformerMixin):
    def __init__(self, dtype):
        self.dtype = dtype

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.astype(self.dtype)