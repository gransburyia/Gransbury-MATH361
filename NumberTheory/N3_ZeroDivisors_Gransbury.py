# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:38:29 2019

@author: grans
"""

n = 20

def findingTerms(n):
    for ii in range(1, n):
        for jj in range(1, n):
            if (ii * jj) % n == 0:
                if tuple_list.count([jj,ii]) == 0 and tuple_list.count([ii,jj]) == 0:
                    tuple_list.append([ii,jj]);
                if int_list.count(ii) == 0:
                    int_list.append(ii)
                if int_list.count(jj) == 0:
                    int_list.append(jj)    
                

            
tuple_list = []
int_list = []


for i in range(1, n+1):
    findingTerms(i)
    print("These are the numbers that are zero divisors of the number",i,int_list[:])
    int_list = []