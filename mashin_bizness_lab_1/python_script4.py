import numpy as np
import pandas as pd
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.info())
print(df['TotalCharges1'].shape)
print(df['TotalCharges1'].dtypes)
print(df['TotalCharges1'].replace(' ', 'np.nan'))
print(df['TotalCharges1'].sort_values() == 'nan')
print(df['TotalCharges1'].fillna(0))
print(df['TotalCharges1'].dtypes)
df = pd.to_numeric(df['TotalCharges1'], errors='coerce')
print(df['TotalCharges1'].dtypes)
print(df['TotalCharges1'].astype(np.float32))
print(df['TotalCharges1'].dtypes)
print(df['TotalCharges1'].mean())
print(df['TotalCharges1'].median())
print(df['TotalCharges1'].std())



