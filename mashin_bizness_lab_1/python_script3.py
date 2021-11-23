import numpy as np
import pandas as pd
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.info())
print(df['PhoneService'].shpe)
print(df['PhoneService'].isna().sum())
print(df['PhoneService'].dtypes)
df = df['PhoneService'].isin([1.0,'Yes'])
print(df['PhoneService'].dtypes)
df = df['PhoneService'].replace({True: 1, False: 0})
print(df['PhoneService'].dtypes)
df.to_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

