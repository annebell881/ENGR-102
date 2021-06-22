# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 08:10:51 2020

@author: Anne
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 3 - 2
# Date:         09 04 2020
#


#These line of code is going to take in the name and birthday of user 1
user1_name = input("User one, please enter your name: ") 
user1_bday = input("User one, please enter your birthday (day, month, year): ")

#These line of code is going to take in the name and birthday of user 2
user2_name = input("User two, please enter your name: ") 
user2_bday = input("User two, please enter your birthday (day, month, year): ")

#These line of code is going to take in the name and birthday of user 3
user3_name = input("User three, please enter your name: ") 
user3_bday = input("User three, please enter your birthday (day, month, year): ")

#These line of code is going to take in the name and birthday of user 4
user4_name = input("User four, please enter your name: ") 
user4_bday = input("User four, please enter your birthday (day, month, year): ")

#these lines of code print the input in columns
print( "Name".ljust(10), "Birthday".rjust(10))
print(user1_name.ljust(10), user1_bday.rjust(10))
print(user2_name.ljust(10), user2_bday.rjust(10))
print(user3_name.ljust(10), user3_bday.rjust(10))
print(user4_name.ljust(10), user4_bday.rjust(10))
