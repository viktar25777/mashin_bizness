import numpy as np
import pandas as pd
import scipy
import sklearn
from sklearn.model_selection import train_test_split
df = pd.read_csv('1.csv')
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.info())
X = df.iloc[:, 1:7]
y = df.iloc[:, 0]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
print(X_train)
print(X_test)
print(y_train)
print(y_test)

