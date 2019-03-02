# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 08:53:55 2019

@author: grans
"""

import matplotlib.pyplot as plt


#function to change
a_n = lambda n: 
#1 + b**n converges: 1 + (7/9)**n
#1 + b**n diverges: 1 + (3/2)**n
#1 + (f(n)/g(n)) converges: 1 + (n/n**4)
#1 + (f(n)/g(n)) diverges: 1 + (n**4/n**2)

def calculateProducts(n):
    product = 1
    for ii in range(1, n + 1):
        product *= a_n(ii)
        products.append(product)
    
    
n = 100000

products = []

calculateProducts(n)

print("The first 15 values of the product are:", products[:15])
print("The last 15 values of the product are:", products[-15:])

