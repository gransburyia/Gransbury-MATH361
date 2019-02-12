# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 12:29:28 2019

@author: grans
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math as m
import numpy as np
import matplotlib.pyplot as plt

stopNum = int(input("Enter a number that corresponds to the total number of terms in the partial sum sequence: \n"))

sumToI = 0.0;


sums= np.zeros([3,stopNum])

for jj in range(1,stopNum+1):
    sumToI += m.log(jj**4+jj+3)/ ((m.sqrt(jj)) + 3)
    sums[0][jj-1] = sumToI
   
sumToI = 0.0;    
for jj in range(1,stopNum+1):
    sumToI += (m.exp(jj/100))/ (jj**10)
    sums[1][jj-1] = sumToI
sumToI = 0.0
for jj in range(1,stopNum+1):
    sumToI += (jj**2 + m.factorial(jj)) / m.factorial(jj-1)
    sums[2][jj-1] = sumToI
          
print("The first summnation sums:")
print("The first 15 are:")
print(sums[0][:15])
print("The last 15 are:") 
print(sums[0][-15:])

listx=[]
for ii in range(1, stopNum + 1):
    listx.append(ii)

x =listx
y =sums[0][:]



plt.plot(x,y)
plt.show()

print("The second summnation sums:")
print("The first 15 are:")
print(sums[1][:15])
print("The last 15 are:") 
print(sums[1][-15:])

x =listx
y =sums[1][:]


plt.plot(x,y)
plt.show()

print("The third summnation sums:")
print("The first 15 are:")
print(sums[2][:15])
print("The last 15 are:") 
print(sums[2][-15:])

x =listx
y =sums[2][:]

plt.plot(x,y)
plt.show()