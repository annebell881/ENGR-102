# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 09:54:42 2020

@author: Anne
"""


# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 2 - 2
# Date:         08 28 2020
#

#This program is going to focus on liner polation of 
#three variables

#Initalizes the first set of varaiables
t1 = 5
x1 = 2
y1 = 5
z1 = 10

#Initalizes the second set of varaiables
t2 = 63
x2 = -5
y2 = 34
z2 = 5

#Initalizes the time for the linear polation
t0 = 50

#Sets the equation variable and finds there soultion
x0 = x1 + ((x2 - x1) / (t2 - t1) * (t0 - t1))
y0 = y1 + ((y2 - y1) / (t2 - t1) * (t0 - t1))
z0 = z1 + ((z2 - z1) / (t2 - t1) * (t0 - t1))

#Prints the soultion
print("time of interest =", t0, "seconds.")
print ("x0 =", x0, "m")
print ("y0 =", y0, "m")
print ("z0 =", z0, "m")
