# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 15:03:05 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 7b act 2
# Date:         04-10-2020


##############Part A##############
#create a list
a = [3,4,9,4,7,7,5,2,8,5,3,1,9,2]
a.sort()
#if the number of nums is not even finding the median
if len(a) %2 != 0:
    index = len(a)//2
    median = a[index]
#If the median of the num is an even number
else:
    index1 = (len(a)//2)-1
    index2 = len(a)//2
    median = (a[index1] + a[index2])/2
#prints the median
print("The median is ", median)

###########Part B############
#copies a's list for b 
b = [3,4,9,4,7,7,5,2,8,5,3,1,9,2]
#creates an empty list
b_sort = [ ]
#creates a for loop
for i in range (len(b)):
    min_val = b[0]
    pos = 0
    #finds the min value and puts it in the empty list
    for j in range(1, len(b)):
        if b[j] < min_val:
            min_val = b[j]
            pos = j
    b_sort+=[min_val]
    b[pos:pos + 1] = []
