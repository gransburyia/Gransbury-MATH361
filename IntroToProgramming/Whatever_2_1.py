# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 12:04:37 2019

@author: grans
"""


totalSum = 0;
multiples = []
for ii in range(0,2001):
    if ((ii % 3 == 0) or (ii % 5 == 0)):
        totalSum += ii
        multiples.append(ii)
        
print('The total list is: ', multiples)        
print('The total sum is: ', totalSum)

        