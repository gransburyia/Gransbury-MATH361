# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:52:53 2019

@author: grans
"""

def divisors(n):
    divisors_List.append(1)
    for i in range(1,n):
        for j in range(1,n):
            if i * j == n:
                divisors_List.append(i)

n = 28
                
divisors_List = []

divisors(n) 

print("These are the divisors of",n,":",divisors_List[:])     