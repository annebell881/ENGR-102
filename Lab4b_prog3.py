# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 21:37:06 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 4b Prog 1
# Date:         09/10/2020
#

#imports math
import math

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
    
#This code is finding the roots for the equations 
#If a and b is equal to zero
if a== 0 and b ==0:
    if c == 0:
        print("infinte soltions")
    else:
        print("You entered an invaild combination of coefficients.")
#If a is equal to zero
elif a == 0:
    x = - c / b
    print("The root of the equation : " + equ +"  is x =" + str(x))
#all other conditions
else:
    delt = (b**2) -(4*a*c)
    if delt == 0:
        x = -b / (2*a)
    #if delt is negitive
    if delt < 0 :
        term1 = -b /(2*a)
        term2 = math.sqrt(-delt)/(2*a)
        print("The roots of the equation: " + equ +"  are x = "+str(term1)+"+"+str(term2)+"i and x = "+ str(term1)+"-"+str(term2)+"i")
    else:
        x1 = (-b + math.sqrt(delt)) / (2*a)
        x2 = (-b - math.sqrt(delt)) / (2*a)
        print("The roots of the equation: " + equ +"  are x = "+ str(x1) +" and x = "+ str(x2))