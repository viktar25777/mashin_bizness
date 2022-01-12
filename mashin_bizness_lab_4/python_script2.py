import numpy as np
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.info())
df = df['channel'].isin([1.0,'Phone'])
print(df['channel'].dtypes)
df = df['channel'].replace({True: 1, False: 0})
print(df['channel'].dtypes)
df.to_csv('data.csv')

