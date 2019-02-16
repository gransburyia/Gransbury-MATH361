# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 12:02:53 2019

@author: grans
"""

def fibNums(F1, F0, term, m):
    for ii in range(2,term):
        F2 = my_list[ii - 1] +  my_list[ii -2]
        my_list.append(F2)
        if(F2 % m == 0):
            fibMults.append(F2)
        
        

F0 = 0
F1 = 1

term = 10000
m = 81

my_list = []
fibMults = []

my_list.append(F1)
my_list.append(F0)

fibNums(F1,F0,term, m)

p = (len(fibMults) / term) * 100

print("The percentage of numbers divisible by",m,"is",p,"%")
    
    
