# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 09:23:49 2023

@author: batta
"""

from scipy.stats import norm
ci_min,ci_max= norm.interval(0.94, 200, 30)
print('(',ci_min,',',ci_max,')')
ci_min,ci_max= norm.interval(0.98, 200, 30)
print('(',ci_min,',',ci_max,')')
ci_min,ci_max= norm.interval(0.96, 200, 30)
print('(',ci_min,',',ci_max,')')