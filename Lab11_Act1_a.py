# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:38:21 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 11 1a
# Date:         01 11 2020

import math

def remainingVol(height, length, width, radius):
    cubeVol = height * length * width
    holeVol = math.pi*height*(radius**2)
    return cubeVol - holeVol

#Test function
length = float(input("Please enter a length of the cube: "))
height = float(input("Please enter the height of the cube:"))
width = float(input("Please enter the width of the cube:"))
radius = float(input("Please enter the radius of the hole:"))
volume = remainingVol(height,length,width,radius)

print("The remaining Volume is ", volume)