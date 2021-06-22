# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 21:22:21 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 4b Prog 2
# Date:         09/12/2020
#

#This program prints out the quadratic equation given user coeffecients
#Gathers user input for the coefficients 
a = int(input("Please enter the coefficient A: "))
b = int(input("Please enter the coefficient B: "))
c = int(input("Please enter the coefficient C: "))

#This is going to code the quadratic equation given the coefficients

equ = " "

#conditions for A
if a == 0:
    equ+=" "
elif a == 1:
    equ += "x^2"
elif a == -1:
    equ +="- x^2"
elif a > 0:
    equ += str(a) + " x^2"
else:
    equ += " - " +str(-a) +" x"
    
#conditions for B
if b == 0:
    equ+=" "
elif b == 1:
    if a == 0:
        equ += " x"
    else:
        equ += " + x"
elif b == -1:
    equ +=" - x"
elif b > 0:
    if a == 0:
        equ += str(b) + " x"
    else:
        equ += " +" + str(b) + " x"
else:
    equ += " - " +str(-b) +" x"
    
    
#Conditions for C
if c == 0:
    equ+=" "
elif c >= 1:
    if a == 0 and b == 0:
        equ += str(c)
    else:
        equ += " + " + str(c)
elif c <= -1:
    equ += " - " + str(-c) 


#Prints the equation
print(equ)