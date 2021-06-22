# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 20:36:04 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 9 read
# Date:         18 10 2020

#user input
inFile = input("Please enter the name for the file: ")

#open file
openFile = open(inFile, "r")

#reading from file


#Print 5 mpa data
print("5 MPa Data")
print("Temp [C]".ljust(8),"v[m3/kg]".ljust(10)," u[kJ/kg]".ljust(15), "h[kJ/kg]".rjust(8),"s[kJ/kgK]".rjust(10))


line = openFile.readline()
i = 0

while line != ' ':
    list_of_line = list(line.split(","))
    if(list_of_line[0] == 0 and i!= 0):
        #Print 10 mpa data
        print("10 MPa Data")
        print("Temp [C]".ljust(8),"v[m3/kg]".ljust(10)," u[kJ/kg]".ljust(15), "h[kJ/kg]".rjust(8),"s[kJ/kgK]".rjust(10))
    print(list_of_line[0].ljust(8) + list_of_line[1].ljust(10) + list_of_line[2].ljust(15) + list_of_line[3].rjust(8) + list_of_line[4].rjust(10))
    line = openFile.readline()
    i += 1


#close file
openFile.close()