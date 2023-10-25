# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 07:23:24 2023

@author: batta
"""
import pandas as pd
df=pd.read_csv('Cars.csv')
df.shape
df

df['MPG'].hist()
df['MPG'].skew()
from scipy import stats
statistics, p_value= stats.normaltest(df['MPG'])

# statistics, p_value

if p_value>=0.05:
    print('The MPG column is not normally distributed')
else:
    print('The MPG column is normally distributed')
    
    
    