# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 17:01:15 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 2b - 2
# Date:         08 24 2020
#

import math 

#This line uses Ohm's law to find the current through a conductor using a 
#resistance of 20 ohms and 5 amperes

#This code section creates useful varriables
resistor = 20
current = 5
#this area of code creates the equation and prints the solution
voltage = resistor * current
print ("The current though the conductor is:", voltage , "volts." )


#This line of code finds the kinetic energy of an object with a mass of 100 kg 
#and velocity of 21 m/s

#This code section creates useful varriables
mass = 100
velocity = 21
#this area of code creates the equation and prints the solution
kinetic_energy = (1/2) * mass * (velocity ** 2)
print ("The kinetic energy is:", kinetic_energy, "Joules.")


#This line of code calulates Reynolds number for a fluid with velocity 100 m/s 
#and kinematic viscosity 1.2 (m^2)/s, with characteristic linear dimension 2.5 m

#This code section creates useful varriables
velocity_re = 100
kinemtic_velocity = 1.2
linear_dim = 2.5
#this area of code creates the equation and prints the solution
reynold_num = (velocity_re * linear_dim) / kinemtic_velocity
print("Reynold's number for this fluid is:", reynold_num, "unitless.")

#This line of code calculates the radioactive decay of 3 g Radon-222 after 5 
#days, with a half life of 3.8 days.

#This code section creates useful varriables
inital_mass = 3
time = 5
half_life = 3.8
#this area of code creates the equation and prints the solution
new_mass = inital_mass *(2**(- time / half_life))
print ("The amount of Radon-222 left after 5 days is:", new_mass, "grams.")

#This line of code uses Mohr-coulomb criterion to calculate the sheer stress 
#with a normal stress of 20 ibf/in^2 applied to a material that has a cohesion 
#of 2 ibf/in^2 and an internal friction of 35 degrees
#This code section creates useful varriables
normal_stress = 20
cohesion = 2
degrees = 35
radians = (degrees* math.pi) /180
#this area of code creates the equation and prints the solution
shear_stress = normal_stress * math.tan(radians) + cohesion
print ("The shear stress is:", shear_stress , "ibf/in^2.")