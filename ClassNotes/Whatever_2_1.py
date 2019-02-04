# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 12:04:37 2019

@author: grans
"""
import matplotlib.pyplot as plt

n = 10
totalSum =0
x=[]
y=[]
for ii in range(1,n + 1):
        totalSum += (ii + 1) ** 2
        x.append(ii)
        y.append(totalSum)
        
plt.ylim(1,600 )
plt.xlim(1,10)       
        
plt.plot(x, y)
plt.show()
        