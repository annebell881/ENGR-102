# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 21:09:47 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 12 1
# Date:         08 11 2020

#Section defines the most used functions in this program
def f(x):
    '''defines one function'''
    f = x**3 - 1 
    return f

def g(x):
    '''defines one interval'''
    g = 2 * (x**3) + 2 * (x**2) - 5 * x + 3
    return g

def h(x):
    '''defines an interval'''
    h = 3 * (x**3) - x**2 + 2 * x - 1
    return h

#Menu
def menu():
    """This function shows the user three functions and asks them to pick one"""
    print("Please select a function: ")
    print("1: x^3 - 1")
    print("2: 2x^3 + 2x^2 - 5x + 3")
    print("3: 3x^3 - x^2 + 2x - 1")
    userChoice = int(input("Enter your choice (1,2,3): "))
    if userChoice == 1:
        funct = f
    elif userChoice == 2:
        funct = g
    elif userChoice == 3:
        funct = h
    return funct

def interval():
    """This function sets the upper and lower bounds for the interval"""
    lower = float(input("Please enter a lower bounds for the interval: "))
    upper = float(input("Please enter a upper bounds for the interval: "))
    return upper, lower

def leftsum(func, upper, lower):
    '''area under the curve at the starting interval'''
    intervals = 10
    error = 1e6
    area = 0
    prevArea = 0
    while abs(error) > 1e-6:
        width = (upper - lower) / intervals
        for i in range (intervals):
            area = width * func(lower + width *i)
        intervals += 1
        error = area - prevArea
        prevArea = area
    return area

def rightSum(func, upper, lower):
    '''returns the area of under the curve stating at the end'''
    intervals = 10
    error = 1e6
    area = 0
    prevArea = 0
    while abs(error) > 1e-6:
        width = (upper - lower) / intervals
        for i in range (intervals):
            area = width * func(upper + width *i)
        intervals += 1
        error = area - prevArea
        prevArea = area
        return area
    
def midPoint(func, lower, upper):
    '''returns the midpoint interval'''
    intervals = 10
    error =  1e6
    prevArea = 0
    area = 0
    while abs(error) > 1e-4:
        width = (upper-lower)/intervals
        for i in range(intervals):
            area += width * func(lower*width/2 +(width*i))
        intervals += 1
        error = area - prevArea
        prevArea = area
    return area

def trapizodial(func, lower, upper):
    '''Returns the trapizodial interval area'''
    intervals = 10
    error = 1e6
    prevArea = 0
    while abs(error) > 1e-4:
        width = (upper - lower) / intervals
        area = 0
        for i in range(intervals):
            area += width *(func(lower- (width*i))+ (func(lower+ (width*(i+1)))))/2
        intervals += 1
        error = area- prevArea
        prevArea = area
    return area

func = menu()
upper, lower = interval()
left = leftsum(func, upper, lower)
right = rightSum(func, upper, lower)
midpoint = midPoint(func, lower, upper)
trap = trapizodial(func, lower, upper)

print('Shape 1 area: ', '%.3f' %left)
print('Shape 2 area: ', '%.3f' %right)
print('Shape 3 area: ', '%.3f' %midpoint)
print('Shape 4 area: ', '%.3f' %trap)