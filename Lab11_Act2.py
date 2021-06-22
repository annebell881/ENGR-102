# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 12:43:32 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 11 2
# Date:         01 11 2020

####Part A#########
#using the function x^2 + 1
#creates a function for x at that function
def func(x):
    y = x**2 + 1
    return y

######B#############
#checks the derivitive using f(x+a) - f(x-a) / 2a
def deriv(func,x):
    a = 1e-10
    b = (func(x + a) - func(x - a)) / (2 * a)
    return b
    
#####C################
#first step of newtons method
def newtonStep(func, x):
    xi = x - (func(x)/deriv(func, x))
    return xi 

#######D##########
#using newtons method
def newton(func, x):
    error = 1
    answers=[]
    count = 0
    errorOld = 1000000
    while abs(error) > 1e-6:
        count += 1
        answers.append(x)
        newRoot = newtonStep(func, x)
        error = newRoot - x
        x = newRoot
        if error > errorOld:
           print("The function is diverging")
           break
        #breaks loop if more than 50
        if count > 50:
            print("Loop is more than 50 itterations")
            break
        return answers
    
#

##"Main" function
x = float(input("Please enter a value for x: "))
print(func(x))
print(deriv(func, x))
