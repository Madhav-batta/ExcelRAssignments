# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 22:08:41 2023

@author: batta
"""

import pandas as pd
table = {"Allied Signal": 24.23,
    "Bankers Trust": 25.53,
    "General Mills": 25.41,
    "ITT Industries": 24.14,
    "J.P.Morgan & Co.": 29.62,
    "Lehman Brothers": 28.25,
    "Marriott": 25.81,
    "MCI": 24.39,
    "Merrill Lynch": 40.26,
    "Microsoft": 32.95,
    "Morgan Stanley": 91.36,
    "Sun Microsystems": 25.99,
    "Travelers": 39.42,
    "US Airways": 26.71,
    "Warner-Lambert": 35.00}
df=pd.DataFrame(table.items(), columns=['Name of company','Measure_X'])
df.shape
df.head()
df["Decimal"] = df["Measure_X"] / 100

import matplotlib.pyplot as plt
plt.boxplot(df['Decimal'],vert=False)


#Outlier
import numpy as np
Q1=np.percentile(df['Decimal'],25)
Q3=np.percentile(df['Decimal'],75)
IQR=Q3-Q1
UW=Q3+1.5*IQR
LW=Q3-1.5*IQR
df[df['Decimal']>UW]
df[df['Decimal']<LW]
df_new=df[(df['Decimal']>=LW)&(df['Decimal']<=UW)]
df_new

x1=df_new['Decimal'].mean()
x2=df_new['Decimal'].std()
x3=pow(x2,2)
print('Mean:', round(x1, 2))
print('Standard Deviation:', round(x2, 2))
print('Variance:', round(x3, 2))
