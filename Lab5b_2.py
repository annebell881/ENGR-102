# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 08:19:35 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 5b - 2
# Date:         09 18 2020
#

#prints what the code does
print("This program creates a loop to get the cost of the tickets for a group.")

#gets user input for the amount of people in the group
number_of_people = int(input ("Please enter the number of people in the group:"))

#creates a cost variable
total_cost = 0

#creates a loop for the amounted amount of people and asking for the age of each person
#to determine the cost and adds to cost
for i in range(0, number_of_people +1):
    designator = input("Please enter the approprate designator of the person (senior, adult, teen,  child and tot): ")
    
    #determines the cost
    if designator == "senior":
        APR_card = input("Is a valid APR present (yes or no) :")
        if (APR_card == "yes"):
            total_cost += 6.25
        else:
            total_cost += 7.00
    elif designator == "adult":
        total_cost += 9.00
    elif designator == "teen":
        total_cost += 7.50
    elif designator == "child":
        total_cost += 5.00
    elif designator == "tot":
        total_cost += 0
        
#prints the total cost of the tickets
print("The total cost for this group of ", number_of_people, " is $", ('%.2f' %total_cost))
            