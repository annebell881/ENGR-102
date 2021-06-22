# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 08:08:09 2020

@author: Anne
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 3 - 1b
# Date:         09 04 2020
#

#This line of code tells the user what the program is doing
print("This code converts BTUs to Joules")

#This line of code takes input from the user
btu = float(input("Please input the amount of BTUs: "))

#This line of code does the conversion
joules = 1055.05585262 * btu

#This line of code prints the output
print(('%.2f' % btu), " BTUS is equal to", ('%.2f' %joules), "joules.")