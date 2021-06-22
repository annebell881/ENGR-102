# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:30:05 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 3b - 1b
# Date:         09 04 2020
#

#line of code tells the user what the code does
print("This program calculates knetic energy given mass and velocity")

#This code asks for user input
mass = float(input("Please enter mass (kg): "))
velocity = float (input("Please enter velocity (m/s): "))

#This line of code performs the calculations

kinetic_energy = (1/2) * mass * (velocity ** 2)

#This line of code displays the output
print ("The kinetic energy is ", ('%.1f' %kinetic_energy), "Jolues.")
