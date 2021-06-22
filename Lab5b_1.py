# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 08:19:36 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 5b - 1
# Date:         09 18 2020
#

#prints what the program does
print ("This program estimates the value of e of the infinte series.") 

#gathers the input from the user
user_input = float(input("Please input a number between 0 and 4: "))
if (user_input <= -1 or user_input >= 5):
    print("Invaild statement, now exiting the program.")
else:
    tol = 1e-7
    n = 1 #start n at 1 because 0 equals 1
    sum_e = 1.0 #total sum has to start at one bc zero = 1
    term = 1 #value on current term
    while (abs(term)>tol):
        term *= user_input / n
        sum_e += term
        n += 1
    
print ("At x= ", ('%.2f' %user_input), "based on the function e^x is estimated to be ", ('%.4f' %sum_e))
        