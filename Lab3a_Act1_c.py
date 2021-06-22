# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 08:08:14 2020

@author: Anne
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 3 - 1c
# Date:         09 04 2020
#


#This line of code tells the user what the program is doing
print ("This code coverts Pascals to millimeters of mercury.")

#This line of code takes input from the user
pascal = float(input("Please enter the number of Pascals: "))

#This line of code does the conversion
mm_of_mercury = pascal * 0.0075006156130264

#This line of code prints the output
print(('%.2f' %pascal), " pascals is equal to ", ('%.2f' %mm_of_mercury), "mm of mercury")