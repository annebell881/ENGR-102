# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 12:08:07 2020

@author: Anne
"""


# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 11 1e
# Date:         01 11 2020

def avgVel(list1, list2):
    velList=[]
    for i in range(1,len(list1)):
        velList.append((2*list2[i])/list1[i])
    return velList
#Test
print(avgVel([2,7,19],[3,1,6]))