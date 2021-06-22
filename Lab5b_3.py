# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 08:19:34 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 5b - 3
# Date:         09 18 2020
#

#prints what the program does
print ("This progam prints if a number is prime or not between 2 and 100.")
print("This program will print how many numbers are prime.")
#creates a counter
count = 0
#creates a for loop to count / decide if a number is prime
for num in range (2,101):
    #creates a is prime bool
    is_prime = True
    for i in range (2, num):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print (num, "Is prime")
        count = count + 1
    else:
        print(num, "is not prime")


#prints the itterations
print ("There are ", count, " number of primes between 2 and 100.")

            
    
        
        
