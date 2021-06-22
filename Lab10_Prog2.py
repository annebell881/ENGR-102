# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:52:45 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 10 2
# Date:         25 10 2020

import matplotlib.pyplot as plt

#useful hint: guess i need numpy instead of math as well
import numpy

####PLot 1#######
###plot 1-1########
xvals = numpy.linspace(-2.0,2.0,150)
yVals_f2 = (1/8)* xvals**2
yVals_f6 = (1/24)* xvals**2
plt.plot(xvals, yVals_f2, linewidth = 2.0, color='m')
plt.plot(xvals, yVals_f6, linewidth = 2.0, color='k')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Two parabolas focal length")
plt.legend(["focal length 2", "focal length 6"])
plt.show()
####Plot 2######
x = numpy.linspace(-2*numpy.pi, 2*numpy.pi,150)
y1 = numpy.sin(x)
y2 = numpy.cos(x)
plt.plot(x, y1, x, y2)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Sin(x) and Cos(x) plot")
plt.legend(["cos(x)", "sin(x)"])
plt.show()

