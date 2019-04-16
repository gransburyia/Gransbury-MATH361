# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 12:26:56 2019

@author: grans
"""
def evaluate(x):
    coef.reverse()
    x = 2
    index = 0
    newList = []
    for i in coef:
        newList.append(i * x ** index)
        index += 1
    newList.reverse()
    answer = newList[0]
    index = 0
    for i in range(1, len(newList) - 1):
        if(operators[index] == '+'):
            answer = answer + newList[i]
        else:
            answer = answer - newList[i]
    return answer

def derivative():
    index = len(coef) - 1
    derCoef = []
    der = ""
    for i in coef:
        derCoef.append((str(index * i)))
        index -= 1
    for i in range(0, len(derCoef[0:-1])):
        if(i == len(derCoef[0:-1]) -1):
            der += " " + str(derCoef[-2])
        elif (i == len(derCoef[0:-1]) - 2):
            der += (str(derCoef[-3] + "x " + operators[-1]))
        else:
            der += (str(derCoef[i]) + "x^" + str(len(derCoef[0:-1]) - (i + 1)) + " " + operators[i] + " ")
    return der
    
def gettingCoef(degree):
    coef = [] #list of coefficients 

    indexTerms = 0

    for i in range(0, degree + 1):
        tempString = terms[indexTerms]
        find = 'x^' + str(degree)
        if degree > 1:
            if(poly.find(find) == -1):
                degree -= 1;
                coef.append(0)
            else:
                xFind = tempString.find('x')
                if xFind == 0:
                    coef.append(1)
                    indexTerms += 1
                    degree -= 1;
                else:
                    coef.append(float(tempString[0:xFind]))
                    indexTerms += 1
                    degree -= 1;
        elif degree == 1 and tempString == terms[-2]:
            xFind = tempString.find('x')  
            if xFind == 0:
                coef.append(1)
                indexTerms += 1
                degree -= 1;
            else:
                coef.append(float(tempString[0:xFind]))
                indexTerms += 1
                degree -= 1;
        elif degree == 0 and tempString == terms[-1]:
            coef.append(float(tempString[0]))
            indexTerms += 1
            degree -= 1;
        else:
            degree -= 1;
            coef.append(0)
    return coef
"""
main
"""    
    
poly = '3x^3 + x^2 + x + 1'

listOfAll = poly.split()

terms = [] #splits the polynomial at all spaces 

operators = [] #list of operators

for i in range(0,len(listOfAll)): # separates the terms from the operators
    tempString = listOfAll[i]
    if(i % 2 == 0):
        terms.append(tempString)
    else:
        operators.append(tempString)
        
if(poly.find('x^') != -1):
    degree = int(poly[poly.find('x^') + 2])
else:
    degree = 1;

coef = [] #list of coefficients 

coef = gettingCoef(degree)

x = 2

#print(evaluate(x))

der = derivative()
        
print(der)
    