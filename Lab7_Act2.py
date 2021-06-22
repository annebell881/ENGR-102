# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 13:03:45 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 7 act 2
# Date:         04-10-2020

from GradeData_Lab7Act2 import gradeData
import math

#############Part A######################
#creates average
average = 0
#creates average using code
for i in gradeData:
    average += i
average /= len(gradeData)
#prints average
print("The average number for the given list is ", average)

#########Part B################
#Creates Standard Devation
std = 0
#loops though and starts the calc for std
for i in gradeData:
    std += (i-average)**2
#finishes calc for Std
std /= (len(gradeData) - 1)
std = math.sqrt(std)
#prints std
print("The Standard Devation for the given list is ", std)


###########Part C#####################
#find the max and min from the list
#creates max and min
max_list = gradeData[0]
min_list = gradeData[0]

#Creates a loop to compare
for i in gradeData:
    
    #find the min
    if gradeData[i] < min_list:
        min_list = gradeData[i]
    
    #find the max
    if gradeData[i] > max_list:
        max_list = gradeData[i]
        
print("The minimum value of the list is ", min_list, " the maxium value of the list is ", max_list)
