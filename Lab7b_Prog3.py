# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 15:03:06 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 7b act 3
# Date:         04-10-2020

#######Part A##############
#get user input for the lists
user_input =input("Please enter the numbers seperated by a comma. ")
numbers = user_input.split(",")
list = []
#get user input for the size
size_num = input("Enter the size (ex: 4x3) : ")
size = size_num.split('x')



#put numbers into a list
multi_list = []
x= 0

for i in range (int(size[0])):
    temp = []
    for j in range (int(size[1])):
        temp.append(list[x])
        x += 1
    multi_list.append(temp)
    
print(multi_list)
#seperates the parts
print()

##############Part B################
#make a left justified table 
for i in range(len(multi_list)):
    for j in range(len(multi_list)):
        print (multi_list[i][j], end=' ')
        
 #seperates the parts       
print()

########Part C#######################
#diagonal
for i in range(len(multi_list)):
    for j in range(len(multi_list)):
        if i >= j: #ensures a stacked list by making 1 , 2 ,3 the numbers
            print(multi_list[i][j], end = ' ')

    
    