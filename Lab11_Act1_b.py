# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:38:22 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 11 1b
# Date:         01 11 2020

def addressLabel(name, city, state, address, zipcode):
    print(name)
    print (address)
    print(city, ", ", state, " ", zipcode)
 
#Test    
name = input("Please enter your name: ")
address = input("Please enter the address: ")
city = input("Please enter the city: ")
state = input("PLease enter the state: ")
zipcode = input("Please enter the zipcode: ")

addressLabel(name, city, state, address, zipcode)
