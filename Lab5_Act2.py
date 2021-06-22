# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 08:19:37 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 5 - Act 2
# Date:         09 18 2020
#

############part a#############
#read in input for coefficents
A = float(input("Please input the coefficent A: "))
B = float(input("Please input the coefficent B: "))
C = float(input("Please input the coefficent C: "))
D = float(input("Please input the coefficent D: "))

#read in a value for x
x = float(input("Enter a value for x: "))

#evaluate and print the polynomial
fx = ( A * (x**3)) + ( B * (x**2)) + (C * x) + D
print("f'(", ('%.2f' %x), ") is ", ('%.2f' %fx))


#########part b#############
#Evaluate and print the polynomial deriv
f_ax = (3 * A * (x**2)) + (2 * B * x) + C
print("f'(", ('%.2f' %x), ") analytically is ", ('%.6f' %f_ax))

##########part c##############
#derivative one
#set a and tol
a = .1
tol = 10**(-6)

#calc first itteration
fxpa = ( A * ((x+a)**3)) + ( B * ((x+a)**2)) + (C * (x+a)) + D
deriv = (fxpa - fx) /a
diff = 1

while (diff > tol):
    a /= 2
    temp = deriv
    fxpa = ( A * ((x+a)**3)) + ( B * ((x+a)**2)) + (C * (x+a)) + D
    deriv = (fxpa - fx) /a
    diff = abs(temp - deriv)
    
#print
print("f'(", ('%.2f' %x), ") numerically is ", ('%.6f' %deriv))


#deriv 2
a = .1
tol = 10**(-6)

#calc first itteration
fxma = ( A * ((x-a)**3)) + ( B * ((x-a)**2)) + (C * (x-a)) + D
deriv = (fx - fxma) /a
diff = 1

while (diff > tol):
    a /= 2
    temp = deriv
    fxpa = ( A * ((x-a)**3)) + ( B * ((x-a)**2)) + (C * (x-a)) + D
    deriv = (fx - fxma) /a
    diff = abs(temp - deriv)
    
#print
print("f'(", ('%.2f' %x), ") numerically is ", ('%.6f' %deriv))

#deriv 3
a = .1
tol = 10**(-6)

#calc first itteration
fxma = ( A * ((x-a)**3)) + ( B * ((x-a)**2)) + (C * (x-a)) + D
fxpa = ( A * ((x+a)**3)) + ( B * ((x+a)**2)) + (C * (x+a)) + D
deriv = (fxpa - fxma) / (2*a)
diff = 1

while (diff > tol):
    a /= 2
    temp = deriv
    fxpa = ( A * ((x-a)**3)) + ( B * ((x-a)**2)) + (C * (x-a)) + D
    fxma = ( A * ((x-a)**3)) + ( B * ((x-a)**2)) + (C * (x-a)) + D
    deriv = (fxpa - fxma) /(2*a)
    diff = temp - deriv
    
#print
print("f'(", ('%.2f' %x), ") numerically is ", ('%.6f' %deriv))

#no
