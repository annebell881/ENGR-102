# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 18:33:52 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 4- act 1
# Date:         09/10/2020
#

########## Part A ##########
a = 1 / 7
print (a)
b = a * 7
print(b)

#The value of B is 1

c = 2 * a
d = 5 * a
e = c + d
print(e)
 
#Value of e is 0.9999999

import math
x = math.sqrt(1 / 3)
print(x)
y = x * x * 3
print(y)
z = x * 3 * x
print(z)

# y is 1 
#z is 0.9999999

########## Part B ##########
TOL = 1e-10
# check if b and e are equal within specified tolerance

if abs (e - b) < TOL:
    print("b and e are equal within tolerance of", TOL)
else:
    print("b and e are NOT equal within tolerance of", TOL)
    
# check if y and z are equal within specified tolerance

if abs (z - y) < TOL:
    print("y and z are equal within tolerance of", TOL)
else:
    print("y and z are NOT equal within tolerance of", TOL)

