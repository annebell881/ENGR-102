# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 08:08:17 2020

@author: Anne
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 3 - 1f
# Date:         09 04 2020
#

#This line of code tells the user what the program does
print("This program converts the number of degrees Fahrnheit into degrees celsius")

#This line of code takes user input
fahrenheit = float(input("Enter degrees Farenheit here:"))

#This line of code calculates degrees in celsius 
celsius = 5/9 *(fahrenheit - 32)

#This line of code prints out the output
print(('%.2f' % fahrenheit), "degrees in farenheit is equal to ", ('%.2f' % celsius), " degrees celsius.")
