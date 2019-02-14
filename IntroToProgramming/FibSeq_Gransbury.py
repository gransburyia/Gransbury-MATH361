# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 10:20:58 2019

@author: grans
"""
def nextNum(F1, F0):
    for ii in range(2,term):
        F2 = my_list[ii - 1] +  my_list[ii -2]
        #Stores the value in the list
        my_list.append(F2)
        
def casNum(F0):
    for ii in range(1,term - 1):
        cas = (my_list[ii]) ** 2 - (my_list[ii - 1] * my_list[ii + 1])
        exponential = (-1) ** (ii - 1)
        if (cas == exponential):
            list_Cas.append(True)
        else:
            list_Cas.append(False)
            
        
F0 = 0
F1 = 1

term = 1000

my_list = []
list_Cas = []

my_list.append(F0)
my_list.append(F1)

list_Cas.append(False)

nextNum(F1,F0)

casNum(F0)

print(my_list)
print(list_Cas)




        
