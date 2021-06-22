# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 17:23:09 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 1B-2
# Date:         08 22 2020
#

import math

#This section of code explains the process and my guess for function 1
print("This shows the evaluation of (2*tan(x))/x evaluated at x = 1 to 10^-7.")
print("My guess is 1.")

#This line of code shows the function results for function 1
print((2 * math.tan(1)) / 1)
print((2 * math.tan(0.1)) / 0.1)
print((2 * math.tan(0.01)) / 0.01)
print((2 * math.tan(0.001)) / 0.001)
print((2 * math.tan(0.0001)) / 0.0001)
print((2 * math.tan(0.00001)) / 0.00001)
print((2 * math.tan(0.000001)) / 0.000001)
print((2 * math.tan(0.0000001)) / 0.0000001)

#This line of code creates a space between the fuctions being shown in this lab
print()
print()

#This section of code explains the process and my guess for function 2
print("This shows the evaluation of (1-cosx)/(2*x^2) evaluated at x= 1 to 10^-7")
print("My guess is 0")

#This line of code shows the function results for function 2
print ((1 - math.cos(1)) / (2 * (1 ** 2)))
print ((1 - math.cos(0.1)) / (2 * (0.1 ** 2)))
print ((1 - math.cos(0.01)) / (2 * (0.01 ** 2)))
print ((1 - math.cos(0.001)) / (2 * (0.001 ** 2)))
print ((1 - math.cos(0.0001)) / (2 * (0.0001 ** 2)))
print ((1 - math.cos(0.00001)) / (2 * (0.00001 ** 2)))
print ((1 - math.cos(0.000001)) / (2 * (0.000001 ** 2)))
print ((1 - math.cos(0.0000001)) / (2 * (0.0000001 ** 2)))

#This line of code creates a space between the fuctions being shown in this lab
print()
print()

#This section of code explains the process and my guess for function 3 
print("This shows the evaluation of (1 + (1/x))^x evaluated at x= 1 to 10^7")
print("My guess is 1")

#This line of code shows the function results for function 3
print((1+ (1/1))**1)
print((1+ (1/10))**10)
print((1+ (1/100))**100)
print((1+ (1/1000))**1000)
print((1+ (1/10000))**10000)
print((1+ (1/100000))**100000)
print((1+ (1/1000000))**1000000)
print((1+ (1/10000000))**10000000)

#This line of code creates a space between the fuctions being shown in this lab
print()
print()