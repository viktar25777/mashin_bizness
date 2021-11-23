import numpy as np
import pandas as pd
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.info())
print(df['StreamingTV'].shape)
print(df['StreamingTV'].isna().sum())
print(df['StreamingTV'].dtypes)
df = df['StreamingTV'].isin([1.0,'Yes'])
print(df['StreamingTV'].dtypes)
df = df['StreamingTV'].replace({True: 1, False: 0})
print(df['StreamingTV'].dtypes)
df.to_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')


