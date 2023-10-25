# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 07:56:50 2023

@author: batta
"""
from scipy import stats

confi_1= 0.90
confi_2= 0.94
confi_3= 0.60

alpha_1 =1-confi_1
alpha_2=1-confi_2
alpha_3=1-confi_3

z_score_1=stats.norm.ppf(1-alpha_1/2)
z_score_2=stats.norm.ppf(1-alpha_2/2)
z_score_3=stats.norm.ppf(1-alpha_3/2)

print("Z-score for a 90% confidence interval:", z_score_1, "\n",
      "Z-score for a 94% confidence interval:", z_score_2, "\n",
      "Z-score for a 60% confidence interval:", z_score_3)
