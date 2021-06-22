# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 13:51:32 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 7 act 3
# Date:         04-10-2020

#creates lists
birth_list = []
birth_list_num = []
months = ["January", "February", "March"]

#for loop to get months and dates for list
for i in range(1,6):
    birth= input("Please enter a birthdate for person")
    birth_list += [birth]
    month_to_num = 0
#sets up the month for the birthdate   
    for m in range(len(months)):
        if birth[0] == months[m]:
            month_to_num = (m+1)*100
            break
    month_to_num += int(birth[1])
    birth_list_num += [month_to_num]
#puts birthdays in order
for i in range(4):
    for j in range(i+1, 5):
        if birth_list_num[j] < birth_list_num[i]:
            temp_var_num = birth_list_num[i]
            temp_var_months = birth_list[i]
            birth_list_num[i] = birth_list_num[j]
            birth_list[i] = birth_list[j]
            birth_list_num[j] = temp_var_num
            birth_list[j] = temp_var_months
#Prints birthlist
for i in range (len(birth_list)):
    print (birth_list[i]) 