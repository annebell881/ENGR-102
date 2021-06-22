# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:25:27 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 3b - 1a
# Date:         09 04 2020
#

#line of code tells the user what the code does
print("This program calculates the voltage given resistance and current")

#This code asks for user input
resistor = float(input('Please enter the resistance (ohms): '))
current = float(input ("Please enter the current (amperes): "))

#This line of code performs the calculations
voltage = resistor * current

#This line of code displays the output
print ("The voltage is ", ('%.1f' % voltage), " V")