# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 08:08:08 2020

@author: Anne
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 3 - 1a
# Date:         09 04 2020
#

#this line of code prints what the program is doing
print("This code will convert Newtons to pounds")

#This line of code takes input from the user
newtons = float(input("Please input the number of newtons: "))

#This line of code calculates the conversion
pounds = newtons / 4.448

#This line of code prints the output
print(('%.2f' %newtons), " newtons is equal to ", ('%.2f' % pounds), " pounds.") 