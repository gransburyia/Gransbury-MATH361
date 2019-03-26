# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 19:24:29 2019

@author: grans
"""

n = 20
def findingTerms(n):
    for p1 in range(1, n):
        for p2 in range(1, n):
            if (p1 * p2) % n == 1:
                if tuple_list.count([p2,p1]) == 0 and tuple_list.count([p1,p2]) == 0:
                    tuple_list.append([p1,p2]);
                if int_list.count(p1) == 0:
                    int_list.append(p1)
                if int_list.count(p2) == 0:
                    int_list.append(p2)    
                

            
tuple_list = []
int_list = []


for i in range(1, n+1):
    findingTerms(i)
    print("for Z mod",i,":",int_list[:])
    int_list = []