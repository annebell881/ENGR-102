# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 08:19:38 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 5 - Act 1
# Date:         09 18 2020
#

#Tells the user what the program does
print("This program will find the cubic root of a polynomial.")
#Case: fa+, fmid+, update bounds (mid,b)
#Case: fa+, fmid-, update bounds (a,mid)
#Case: fa-, fmid-, update bounds (mid,b)
#Case: fa-, fmid+, update bounds (a,mid)

#This block of code focuses on taking in user input

coff_A = float(input("Please enter the coefficient of the cubic term: "))
coff_B = float(input("Please enter the coefficient of the quadratic term: "))
coff_C = float(input("Please enter the coefficient of the linear term: "))
coff_D = float(input("Please enter the coefficient of contant term: "))

#Takes input for the bounds
a = float (input ("Please enter the lower bound of the domain: "))
b = float (input ("Please enter the upper bound of the domain: "))

#evalulates polynominal at root bounds
fa = (coff_A* (a**3)) + (coff_B* (a**2)) + (coff_C * a) + coff_D
fb = (coff_A* (b**3)) + (coff_B* (b**2)) + (coff_C * b) + coff_D

#creates an itterations count/ tol
count = 0
tol = 10**(-6)

#creates a loop to find the roots within the tolerence of 10^-6
if (fa  < 0 or fb < 0 ):
    while (abs(b-a) > tol):
        count += 1
        mid = (a*b)/2
        fmid = (coff_A* (mid**3)) + (coff_B* (mid**2)) + (coff_C * mid) + coff_D
        if (fmid * fa <= 0):
            #update b to mid
            b = mid
            fb = fmid
        else:
            #update a to mid
            a = mid
            fa = fmid
    output = (b+a) / 2
    print("The root is at x= ", ('%.3f' %output))
    print("It took ", count, " iterations to find the root.")
    
    