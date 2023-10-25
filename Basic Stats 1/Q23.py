# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 09:25:52 2023

@author: batta
"""

from scipy import stats

confidence_level_95 = 0.95
degrees_of_freedom = 24
t_score_95 = stats.t.ppf((1 + confidence_level_95) / 2, degrees_of_freedom)

print("t-score for a 95% confidence interval:", t_score_95, "\n")

confidence_level_96 = 0.96
t_score_96 = stats.t.ppf((1 + confidence_level_96) / 2, degrees_of_freedom)

print("t-score for a 96% confidence interval:", t_score_96, "\n")

confidence_level_99 = 0.99
t_score_99 = stats.t.ppf((1 + confidence_level_99) / 2, degrees_of_freedom)

print("t-score for a 99% confidence interval:", t_score_99, "\n")
