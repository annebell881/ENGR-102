# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 08:08:15 2020

@author: Anne
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 3 - 1e
# Date:         09 04 2020
#


#This line of code tells the user what the program is doing
print("This line of code converts Meters per second to miles per hour")

#This line of code takes input from the user
meters_per_sec = float(input("Please enter the number of meters per second: "))

#This line of code does the conversion
miles_per_hour = 2.237 * meters_per_sec

#This line of code prints the output
print(('%.2f' % meters_per_sec), "Meters per second is equal to ", ('%.2f' %miles_per_hour), "Miles per hour.")