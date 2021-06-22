# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:30:07 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 3b - 1c
# Date:         09 04 2020
#

#line of code tells the user what the code does
print("This program tells the an=mount of Radon-222 left given the time, inital amount and half life, 3.8 days ")

#This code asks for user input
half_life = 3.8
time = float(input("Please give the time to calculate the amount left (Days): "))
inital_mass = float(input("Please give the inital amount of Radon-222 (g): "))

#This line of code performs the calculations
new_mass = inital_mass *(2**(- time / half_life))

#This line of code displays the output
print("The Radon-222 left is ", ('%.3f' %new_mass), "grams.")
