import numpy as np
import pandas as pd
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.info())

print(df['TechSupport'].shape)
print(df['TechSupport'].isna().sum())
print(df['TechSupport'].dtypes)
df = df['TechSupport'].isin([1.0,'Yes'])
print(df['TechSupport'].dtypes)
df = df['TechSupport'].replace({True: 1, False: 0})
print(df['TechSupport'].dtypes)
df.to_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')


