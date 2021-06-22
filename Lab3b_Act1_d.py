# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:30:08 2020

@author: Anne
"""
import math

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 3b - 1d
# Date:         09 04 2020
#

#line of code tells the user what the code does
print("This program calculates the stress given the normal stress, cohesion and angle of friction." )

#This code asks for user input
normal_stress = float(input("Please enter the normal stress ( lbf/in^2): "))
cohesion = float(input("Please enter the cohesion of the material (lbf/in^2): "))
degrees = float(input("Please enter the angle (Degrees): "))

#This line of code performs the calculations
radians = (degrees* math.pi) /180
shear_stress = normal_stress * math.tan(radians) + cohesion

#This line of code displays the output
print ("The shear stress is:", ('%.3f' %shear_stress) , "ibf/in^2.")