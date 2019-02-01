# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 21:20:02 2019

@author: grans
"""


print("Please enter three numbers\n")

x = float(input("Enter a number: "))
y = float(input("Enter another number: "))
z = float(input("Enter a final number: "))

component1 = x + y

component2 = ((y * z) + (3 * x))

component3 = component1 ** 2

component4 = ((2 *  (component2) - (.5 * x)) / float(component1))

component5 = 7 % 3

operations = [component1,component2,component3,component4,component5]

component3 += 3

component5 *= (3/4)

totalSum = 0;

for ii in operations:
    totalSum += ii;
    
print("The sum is: ", totalSum)    
    
    
    
    
    
    