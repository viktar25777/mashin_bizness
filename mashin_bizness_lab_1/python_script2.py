import numpy as np
import pandas as pd
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.info())
print(df['TotalCharges'].isna().sum())
print(df['TotalCharges'].replace('isna().sum()', 'mean()'))
print(df['TotalCharges'].shape)
print(df['TotalCharges'].mean())
print(df['TotalCharges'].median())
print(df['TotalCharges'].std())


