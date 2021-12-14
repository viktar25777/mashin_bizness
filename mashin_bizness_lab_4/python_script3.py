import numpy as np
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.info())
df = df['zip_code'].isin([1.0,'Rural'])
print(df['zip_code'].dtypes)
df = df['zip_code'].replace({True: 1, False: 0})
print(df['zip_code'].dtypes)
df.to_csv('data.csv')

