# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:52:46 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 10 3
# Date:         25 10 2020

import numpy
import matplotlib.pyplot as plt
#input from user
xknot = float(input("Please input the intial x value: "))
omega = float(input("Please input an omega value: "))
beta = float(input("Please input a value for beta: "))
tFinal = float(input("PLease input a value for the final time: "))
#find gamma and phi
gamma = numpy.sqrt((omega**2)-(beta**2))
phi = numpy.arctan(beta/gamma)
xvals = numpy.linspace(0, tFinal, 150)
#find x of t
xT = ((xknot*omega)/gamma)*(numpy.exp(-1*xvals*beta))*(numpy.cos((xvals*gamma)-phi))
xNeg = xT[xT<0]
tNeg = xvals[xT<0]
#plot 
plt.plot(xvals, xT, color='b')
plt.plot(tNeg,xNeg,'*',color = 'r')
plt.xlabel("Time")
plt.ylabel("Displacement realitive to x0")
plt.title("Underdamped oscillations")
plt.show()

