import numpy as np
import pandas as pd
import scipy
import sklearn
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
df = pd.read_csv('1.csv')
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.info())
column_gender = make_column_transformer(
    (OneHotEncoder(), ['gender']),
    (CountVectorizer(), '"Female", "Male"'),
    remainder='drop')

print(column_gender)

