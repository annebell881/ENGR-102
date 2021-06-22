# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 23:31:03 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 6b act 3
# Date:         26-09-2020


print (" This program prints what layers of a pyrimid would have.")

#input on number of loops
n = int(input("Enter a value for N:"))

#print the header
print("-----------------------------------------")
print ("Number".ljust(12), "lHS".ljust(10), "RHS".rjust(10))
print ("of Layers".ljust(12))

#Nested loop to show the equality holds
for i in range (1, n+1):
    lHS = 0
    rHS = 0
    print("--------------------------")
    for j in range (1, i+1):
        lHS += j**2
        rHS += (2*j-1) *(i-(j-1))
        print(str(i).ljust(12), str(lHS).ljust(10), str(rHS).rjust(10))