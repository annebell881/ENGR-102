# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 10:44:07 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 1b - 1
# Date:         08 22 2020
#

import math 

#This line prints an interesting fact about me
print("An interesting fact about me is I have a dog that loves to jump through hoops.")

#This line uses Ohm's law to find the current through a conductor using a resistance of 20 ohms and 5 amperes
print ("The current though the conductor is:", 20*5 , "volts." )

#This line of code finds the kinetic energy of an object with a mass of 100 kg and velocity of 21 m/s
print ("The kinetic energy is:", (1/2) * 100 *(21**2), "Joules.")

#This line of code calulates Reynolds number for a fluid with velocity 100 m/s and kinematic viscosity 1.2 (m^2)/s, with characteristic linear dimension 2.5 m
print("Reynold's number for this fluid is:", (100*2.5) / 1.2, "dimesions.")

#This line of code calculates the radioactive decay of 3 g Radon-222 after 5 days, with a half life of 3.8 days.
print ("The amount of Radon-222 left after 5 days is:", 3 * (2**((-5)/3.5)) , "grams.")

#This line of code uses Mohr-coulomb criterion to calculate the sheer stress with a normal stress of 20 ibf/in^2
#applied to a material that has a cohesion of 2 ibf/in^2 and an internal friction of 35 degrees
print ("The shear stress is:", (20 * math.tan((35*math.pi) / 180)) + 2, "ibf/in^2.")