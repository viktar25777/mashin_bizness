import numpy as np
import pandas as pd
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.info())
print(df[['InternetService']])
print(df[['InternetService']].shape)
print(len(df['InternetService'].unique()))

