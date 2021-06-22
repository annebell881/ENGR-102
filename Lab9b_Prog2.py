# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 08:13:19 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 9b 2
# Date:         19 10 2020

#open file
f_open = open('address_book.dat','r')

#create a list
addresses = []
#for loop for addresses to become a list
for i in f_open:
    addresses.append([i[:20], i[20:40], i[40:60], i[60]])
    
#counter
count = 0
#find how many addresses there are
for j in addresses: 
    if j[3][:2] == '77':
        count += 1
#print statement
print ("There are ", count, "addresses with the zip code starting with 77")

#closing reading file
f_open.close()

#open writing file
fW = open('address_book.csv', 'w')

#create a loop to write addresses to file
for row in range(len(addresses)):
    for column in addresses[row]:
        fW.write(column + ',')

#close writing file
fW.close()