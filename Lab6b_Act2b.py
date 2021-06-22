# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 21:59:19 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 6b act 2
# Date:         27-09-2020

#Print statment 
print("This program calulates the stress on a curve using four segements")

#Variables for the points
strain0 = 0
stress0 = 0
strainA = 0.01
stressA = 44
strainC = .06
stressC = 44
strainD = .18
stressD = 60
strainE = .26
stressE = 51

#get strain from user
userStrain = float(input("Please enter a user strain: "))

#calculate
if(userStrain < 0):
    print ("Error strain is not defined")
elif(userStrain < strainA):
    fr = (userStrain - strain0) / (strainA - strain0)
    stress = stress0 + fr * (strainA - strain0)
    print("The stress is ", stress)
elif(userStrain < strainC):
    fr = (userStrain - strainA) / (strainC - strainA)
    stress = stressA + fr * (strainC - strainA)
    print("The stress is ", stress)
elif(userStrain < strainD):
    fr = (userStrain - strainC) / (strainD - strainC)
    stress = stressC + fr * (strainD - strainC)
    print("The stress is ", stress)
elif(userStrain < strainE):
    fr = (userStrain - strainD) / (strainE - strainD)
    stress = stressD + fr * (strainE - strainD)
    print("The stress is ", stress)
elif(userStrain < strainE):
    print ("Error strain is passed all points.")
    
                   