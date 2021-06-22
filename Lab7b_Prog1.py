# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 15:03:03 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 7b act 1
# Date:         04-10-2020

import math 
#Create two empty vectors
vect_A = []
vect_B = []

#Get input for the num of elements in both vectors
vect_elm = int(input("Enter the number of elements for the vectors: "))


#Loops through the vectors to get the elements added to their list
#Vector A
for i in range(0, vect_elm):
    element = int(input("Enter a element for Vector A: "))
    vect_A.append(element)
#vector B    
for i in range(0, vect_elm):
    element = int(input("Enter a element for Vector B: "))
    vect_B.append(element)

sum_A = 0
sum_B = 0
magA = 0
magB =0
    
#mag of A
for i in range(len(vect_A)):
    sum_A += (vect_A[i])**2

magA = math.sqrt(sum_A)

#Mag B
for i in range(len(vect_B)):
    sum_B += (vect_B[i])**2

magB = math.sqrt(sum_B)

#Adding A and B
sumAB_vect = []
sumAB = 0
for i in range (0, vect_elm):
    sumAB = vect_A[i] + vect_B[i]
    sumAB_vect.append(sumAB)
  
#Subtracting A and B
diffAB_vect = []
diffAB = 0
for i in range (0, vect_elm):
    diffAB = vect_A[i] - vect_B[i]
    diffAB_vect.append(sumAB)
    
#dot product
dot = 0
muli = 0
for i in range (len(vect_A)):
    for j in range (len(vect_B)):
        muli = vect_A[i] * vect_B[j]
        dot += muli
        
#Print outcomes
print("Magitude of Vector A is: ", magA)
print("Magitude of Vector B is: ", magB)
print("A + B is: ", sumAB_vect)
print("A - B is: ", diffAB_vect)
print("The dot product of A and B are: ", dot)