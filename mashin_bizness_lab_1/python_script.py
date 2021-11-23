import numpy as np
import pandas as pd
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.info())
print(df[['gender']])
print(df[['gender']].shape)
print(df[['gender']].isna().sum())
print(df['gender'][df['gender'].sort_values() == 'Female'])
print(df['gender'][df['gender'].sort_values() == 'Male'])
wuman = 3488 / 7043
man = 3555 / 7043
print(wuman, man)


