import numpy as np
import pandas as pd
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.info())
print(df['Churn'].shape)
print(df['Churn'].isna().sum())
print(df['Churn'].dtypes)
df = df['Churn'].isin([1.0,'Yes'])
print(df['Churn'].dtypes)
df = df['Churn'].replace({True: 1, False: 0})
print(df['Churn'].dtypes)
df.to_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

