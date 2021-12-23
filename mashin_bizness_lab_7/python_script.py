import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import scipy
import sklearn
import lightgbm
from sklearn.model_selection import (StratifiedShuffleSplit, GridSearchCV, train_test_split, cross_validate, cross_val_score)
from lightgbm import LGBMClassifier
from sklift.models import SoloModel
from sklift.viz import plot_qini_curve
from sklift.metrics import make_uplift_scorer
df = pd.read_csv('data1.csv')
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.info())
df1 = df
df1_macro = 0.50
df1 = cross_val_score(X = df['treatment'], y = df['target'], LGBMClassifier(random_state=42, n_jobs=-1), scoring='df1_macro', cv=3)
print(f'df1_macro {df1_macro.mean():.2f}')
