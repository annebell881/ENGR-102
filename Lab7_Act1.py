# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 11:55:30 2020

@author: Anne
"""


# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 7 act 1
# Date:         04-10-2020

#############Part One###########

#takes user input and puts it into a string of three or more stock prices into a float
#list
stockPrices = input("Please enter stock prices followed by a space")
maxLen = 0

for i in range(len(stockPrices)):
    #gets the length of the max  decimal
    if len(stockPrices[i]) > maxLen:
        maxLen = len(stockPrices[i])
        
    #adds one to each element
    stockPrices[i] = float(stockPrices[i]) + 1
    
#prints the  list using the max length
form = "$ %" +str(maxLen + 2) +'.2f'
for i in range (len(stockPrices)):
    print(form%stockPrices[i])



############Part Two###############
#hard code the temp list
myTemps = [75, 87, 95, 102, 76]

#gets two charaters from input
symbol = input("Please input two charaters: ")

#loop that prints the two charters between the list
for i in range (len(myTemps)):
   
    if (i < (len(myTemps)-1)): 
        print(myTemps[i],symbol, end =" ")
    else:
        print(myTemps[i])
    