# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 20:21:40 2020

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

#This code calculates the Area of a tirangle and outputs the largest side

#imports math
import math
#This code gets the input of the sides of a triangle
a = float(input("Please enter the side A of the triangle: (in meters) "))
b = float(input("Please enter the side B of the triangle: (in meters) "))
c = float(input("Please enter the side C of the triangle: (in meters) "))

#Gives user error if input is not valid
if ((a < 0.0) and (b < 0.0) and (c < 0.0)):
    print(" Sides of a triangle can not be negitive, calculations can not be computed.")
elif ((a + b < c) or (a + c < b) or (c + b < a)):
    print ("Does not form a triangle, calculations can not be computed")
else:
    #If input is vaild computes the area of a triangle
    s = (a+b+c) / 2
    area = float(math.sqrt((s *(s-a)*(s-b)*(s-c))))
    #computes the larget side of the triangle
    largest_side = float(a)
    if b > largest_side:
        largest_side = float(b)
    if c > largest_side:
        largest_side = float(c)

    #prints the output of the program
    print ("Area of the given triangle is ", ('%.1f' %area) ," square meters.")
    print(('%.1f' %largest_side), " m is the largest size")
    
    