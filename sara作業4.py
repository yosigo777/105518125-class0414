# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 12:18:34 2022

@author: USER
"""

a = 2  #
b = 1  #
sum1 = 0
for i in range(20):
    sum1 += a / b
    b, a = a, a + b
print(round(sum1, 2))