import numpy as np
import pandas as pd
import scipy
import sklearn
from sklearn import linear_model
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.model_selection import cross_val_score
df = pd.read_csv('train_case2.csv', sep=';')
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.info())
target = df['gender']
X = df.gender[:35000]
y = target[:35000]
lasso = linear_model.Lasso()
print(cross_val_score(lasso, X, y, cv=7))
