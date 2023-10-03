# -*- coding: utf-8 -*-
"""Galton's_Height_Data_Linear_Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rgTXTUtPkJ1Ca5NwJFeeBMqfDDsyNEpY
"""

# @title Import library
import pandas as pd

import numpy as np


import matplotlib.pyplot as plt


import seaborn as sns

# @title Import Data

df = pd.read_csv(r'https://github.com/YBI-Foundation/Dataset/raw/main/Francis%20Galton%20Regression%20Data.txt', delimiter= '\t')


df.head()

df.info()

df.corr()

df.shape

# @title Default MIssing Values
df.isna().sum()

sns.pairplot(df)

y = df['Height']

X = df['Father']

slope = ((df['Father']-df['Father'].mean())*(df['Height']-df['Height'].mean())).sum()/((df['Father']-df['Father'].mean())**2).sum()

slope

intercept = y.mean()-slope*X.mean()

intercept

X = df[['Father']]
y = df['Height']
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X,y)
print(lr.intercept_)
print(lr.coef_)

sns.lmplot(x = 'Father', y = 'Height', data = df)

sns.regplot(x = 'Father', y = 'Height', data = df)

y_pred = lr.predict(X)

residual = y-y_pred

residual.shape, y.shape

plt.scatter( x = y_pred, y = residual);

df.describe()

df.groupby(['Gender']).mean()

69/64-1

df.groupby(['Gender']).corr()

X = np.array([2,4,6,8]).reshape(-1,1)
y = np.array([3,7,5,10])
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X,y)
print(lr.intercept_)
print(lr.coef_)

