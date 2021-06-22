# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 19:26:32 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 4- act 2
# Date:         09/13/2020
#

#This program calculates the price of a parking garage with or without a ticket
print ("This program calculates the price in a parking garage.")
print("Please enter the hours as a decimal for the minutes, i.e. 30 minutes equals .5 hours")
print ("If there was a ticket and it was lost enter it as a negivite time")

#Takes user input
hours_parked = float(input("Please input the number of hours in the parking garage: "))
fee = 0

#creates conditions for if the ticket is lost
if hours_parked < 0 :
    time = - hours_parked
    fee += 36
else:
    time = hours_parked

#Creates time as the int above the decimal if a decimal appears    
if time == 0:
    fee = 0
elif time <  1:
    time = 1
elif time % int(time) != 0:
    time = int(time) + 1
else:
    time = int(time)
    
#creates the fee for parking per day
if time >= 24:
    days = time // 24
    time %= 24
    fee += (days * 24)

#creates the for hours
if time > 0 and time <= 2:
    fee += 4
elif time > 2 and time <= 4:
    fee += 7
elif time > 4 and time <= 21:
    fee += 7 + ((time - 4) * 1)
else:
    fee += 24
    
#prints the fee 
print("Parking for: ", ('%.1f' %hours_parked), "hours please pay $", fee)