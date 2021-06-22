# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 12:35:34 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 3b - Challenge
# Date:         09 04 2020
#

#This program rounds 2/7 to the decimal the user specifies

percision_value = int(input("Please enter the number of digits of precision for 2/7: "))
value = 2/7
print ("The value of 2/7 to", percision_value, " digits is: ", ('%.percision_valuef' %value))
