import numpy as np
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.info())
df = df['conversion'].replace('comversion', 'target')
df = df['offer'].replace('offer', 'treatment')
df = df['treatment'].isin([1.0,'Buy One Get One'])
df = df['treatment'].replace({True: 1, False: 0})
df.to_csv('data.csv')

