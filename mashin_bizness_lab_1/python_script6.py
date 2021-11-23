import numpy as np
import pandas as pd
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.info())
print(df['StreamingMovies'].shape)
print(df['StreamingMovies'].isna().sum())
print(df['StreamingMovies'].dtypes)
df = df['StreamingMovies'].isin([1.0,'Yes'])
print(df['StreamingMovies'].dtypes)
df = df['StreamingMovies'].replace({True: 1, False: 0})
print(df['StreamingMovies'].dtypes)
df.to_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

