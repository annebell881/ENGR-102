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
# Assignment:   Lab 3 - 1d
# Date:         09 04 2020
#

#this line of code tells the user what the program does
print("This program converts the number of seconds per revolution into hertz.")

#this line of code gathers the user input
sec_per_rev = float(input("Please input the value for seconds:"))

#this line of code calculates hertz
hertz = 1.0 / sec_per_rev

#this line of code prints the answer at 2 decimal places
print("The revoultion for", ('%.2f' % sec_per_rev), "seconds, is ", ('%.2f' % hertz ), "hertzs.")

