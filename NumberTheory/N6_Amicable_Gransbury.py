# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:52:56 2019

@author: grans
"""

def divisorsFuc(n):
    
    divisors.append(1)
    for i in range(1,n):
        for j in range(1,n):
            if i * j == n:
                divisors.append(i)

n = 1500
                
divisors = []

amicable_tuples = []

for term1 in range(2,n+1):
    divisors = []
    divisorsFuc(term1)
    sum1 = sum(divisors)
    divisors = []
    divisorsFuc(sum1)
    sum2 = sum(divisors)
    if sum2 == term1:
        amicable_tuples.append([term1,sum1]);
    
print(amicable_tuples[:])       
        