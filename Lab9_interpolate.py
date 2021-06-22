# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:41:10 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 9 interpolate
# Date:         19 10 2020
#declare an input file
inputFile = "Lab9_ThermoProperties.csv"

#input from user
temp = int(input("Enter a temperature between 0 and 260 C: "))
pressure = int(input ("Enter a pressure between 5 and 10 MPa: "))

#checks the input conditions
while (temp < 0 and temp > 260):
    temp = int(input("Enter a temperature between 0 and 260 C: "))
    
while(pressure < 5 and pressure > 10):
    pressure = int(input ("Enter a pressure between 5 and 10 MPa: "))

#open file
inFile = open(inputFile, "r")
#creates lists
listFile = inFile.readlines()
list5 = []
list10 = []
y = 0

#files the inputs into list
for i in range(len(listFile)):
    if listFile[i].strip() == "10 MPa data":
        y == 1
        continue
    if y == 0 and i == 1:
        list5[i] = (listFile[i].strip().split(","))
    else:
        list10[i] = (listFile[i].strip().split(","))
        
        
upper5 = 0
lower5 = 0
for i in range(len(list5)):
    if list5[0][i] < temp:
        lower5 = i
        i += 1
        upper5 = lower5 + 1
        
upper10 = 0
lower10 = 0
for i in range(len(list5)):
    if list10[0][i] < temp:
        lower10 = i
        i += 1
        upper10 = lower10 + 1

#V        
slope5 = ((list5[upper5][1] - list5[lower5][1])/(list5[upper5][0] - list5[lower5][0]))
v5 = slope5* (temp - (list5[lower5][0] + list5[lower5][1]))

slope10 = ((list10[upper10][1] - list10[lower10][1])/(list10[upper10][0] - list10[lower10][0]))
v10 = slope10* (temp - (list10[lower10][0] + list10[lower10][1]))

slopeV = (V10 - V5)/ 5
finalV = slopeV * (pressure - 5) + v5

print("Properties at 50.0 C and 8.0 MPa are:")
print("Specific volume (m^3/kg): ", '.7f%' %finalV)

#ie
slope5 = ((list5[upper5][2] - list5[lower5][2])/(list5[upper5][0] - list5[lower5][0]))
v5 = slope5* (temp - (list5[lower5][0] + list5[lower5][2]))

slope10 = ((list10[upper10][2] - list10[lower10]21])/(list10[upper10][0] - list10[lower10][0]))
v10 = slope10* (temp - (list10[lower10][0] + list10[lower10][2]))

slopeie = (V10 - V5)/ 5
finalie = slopeV * (pressure - 5) + v5

print("Specific internal energy (kJ/kg): ", '.2f%' %finalie)

#entha
slope5 = ((list5[upper5][3] - list5[lower5][3])/(list5[upper5][0] - list5[lower5][0]))
v5 = slope5* (temp - (list5[lower5][0] + list5[lower5][3]))

slope10 = ((list10[upper10][3] - list10[lower10][3])/(list10[upper10][0] - list10[lower10][0]))
v10 = slope10* (temp - (list10[lower10][0] + list10[lower10][3]))

slopeentha = (V10 - V5)/ 5
finalentha = slopeV * (pressure - 5) + v5

print("Specific enthalpy (kJ/kg): ", '.2f%' %finalentha)

#entro
slope5 = ((list5[upper5][4] - list5[lower5][4])/(list5[upper5][0] - list5[lower5][0]))
v5 = slope5* (temp - (list5[lower5][0] + list5[lower5][3]))

slope10 = ((list10[upper10][4] - list10[lower10][4])/(list10[upper10][0] - list10[lower10][0]))
v10 = slope10* (temp - (list10[lower10][0] + list10[lower10][4]))

slopeentro = (V10 - V5)/ 5
finalentro = slopeV * (pressure - 5) + v5

print("Specific entropy (kJ/kgK): ", '.4f%' %finalentro)