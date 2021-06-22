# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 08:49:39 2020

@author: Anne
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 3b - 2
# Date:         09 04 2020
#

import math

#Collects the input values from user
x0 = float(input("Enter the x position of the observer "))
y0 = float(input("Enter the y position of the observer "))
z0 = float(input("Enter the z position of the observer "))

x1 = float(input("Enter the x position of the point one "))
y1 = float(input("Enter the y position of the point one "))
z1 = float(input("Enter the z position of the point one "))

x2 = float(input("Enter the x position of the point two "))
y2 = float(input("Enter the y position of the point two "))
z2 = float(input("Enter the z position of the point two "))

print()

#this block of code constructs the two vectors

v1x = x1 - x0
v1y = y1 - x0
v1z = z1 - x0

v2x = x2 - x0
v2y = y2 - x0
v2z = z2 - x0

#find the magnitude of the two vectors

mag_one = math.sqrt((v1x * v1x) + (v1y * v1y) + (v1z * v1z)) 
mag_two = math.sqrt((v2x * v2x) + (v2y * v2y) + (v2z * v2z))

#This block of code normalizes the vectors 
v1xn = v1x / mag_one
v1yn = v1y / mag_one
v1zn = v1z / mag_one
v2xn = v2x / mag_two
v2yn = v2y / mag_two
v2zn = v2z / mag_two

#The is block of code creates the dot product
dot_product = (v1xn * v2xn) + (v1yn * v2yn) + (v1zn * v2zn)

#Calculates the angle between the two vctors and convert to degrees
angle = math.acos(dot_product) * (180 / math.pi)

#This prints the result of the code
print("Observer location is x = ", x0, "y = ", y0, "z = ", z0)
print ("Point 1 location is x = ", x1, "y = ", y1, "z = ", z1 )
print ("Point 2 location is x = ", x2, "y = ", y2, "z = ", z2 )

print ("The angle between the points is: ", ('%.3f' %angle), "degrees.")