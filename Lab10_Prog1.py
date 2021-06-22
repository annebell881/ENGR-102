# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:52:44 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 10 1
# Date:         25 10 2020

import numpy


######Part A######
#create 4 randomized arrays
A = numpy.random.rand(3,4)
B = numpy.random.rand(4,2)
C = numpy.random.rand(2,3)
D = numpy.random.rand(3,1)
#print the arrays
print ("Now printing the 3x4 array:  A = ")
print (A)
print()
print ("Now printing the 4x2 array: B = ")
print (B)
print()
print ("Now printing the 2x3 array: C = ")
print (C)
print()
print ("Now printing the 3x1 array: D = ")
print (D)
print()

######Part B############
# computes the multiplication of A B and C and puts it into E
a_times_b = numpy.matmul(A,B)
E = numpy.matmul(a_times_b, C)
# outputs the resulting matrix
print ("Now printing the resulting output of A*B*C: E = ")
print(E)
print()

############Part C##########
#####prints the transpose of E
print("Now printing the transpose of E: ")
print(E.transpose())
print()

############Part D ############
#solves the equation for D? I think thats what it means
x = numpy.linalg.solve(E, D)
print("Now printing the solution to the linear equation for D: ")
print(x)
print()

##########Part E##############
# make a matrix for T and V
t = numpy.array([[25, 5, 1], [64, 8, 1], [144, 12, 1]])
v = numpy.array([106.8, 177.2, 279.2])

#ta = v as shown in the lab insturctions idk how to write that maxtrix in comments
# so i hope you understand what i mean
x = numpy.linalg.solve(t , v)

#find v for the times
v6 = x[0]*(6.0**2) + x[1] * 6.0 +x[2]
v7 = x[0]*(7.5**2) + x[1] * 7.5 +x[2]
v9 = x[0]*(9.0**2) + x[1] * 9.0 +x[2]
v11 = x[0]*(11.0**2) + x[1] * 11.0 +x[2]

#pretty print for t = 6, 7.5, 9, 11

print ("At t = 6.0 the velocity is ", '%.2f' %v6)
print ("At t = 6.0 the velocity is ", '%.2f' %v7)
print ("At t = 6.0 the velocity is ", '%.2f' %v9)
print ("At t = 6.0 the velocity is ", '%.2f' %v11)

