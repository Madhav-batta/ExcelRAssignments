# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:03:32 2023

@author: batta
"""

import numpy as np
import pandas as pd

df = np.array([[34],[36],[36],[38],[38],[39],[39],[40],[40],[41],[41],[41],[41],[42],[42],[45],[49],[56]])
df = pd.DataFrame(df)
df.describe()
df.shape

x1=df.mean()
x2=df.median()
x3=df.std()
variance=pow(x3,2)
print('Mean, median, standard deviation, variance = ', x1,x2,x3,variance)

df.hist()
df.boxplot(vert=False)

