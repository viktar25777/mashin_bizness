import numpy as np
import pandas as pd
import scipy
import sklearn
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
df = pd.read_csv('1.csv')
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.info())
X, y = make_classification(random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
pipe = Pipeline([('scaler', StandardScaler()), ('svc', SVC())])
print(pipe.fit(X_train, y_train))
print(pipe.score(X_test, y_test))


