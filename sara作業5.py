# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 13:32:46 2022

@author: USER
"""

n=4
for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    for k in range(2*i+1):
        print('*',end='')
    print(' ')

for i in range(n-1): 
    for j in range(i+1): 
      print(' ',end='')
    for k in range(2*(n-i)-3): 
      print('*',end='')
    print('')