# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 18:02:18 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 2 - 2
# Date:         08 28 2020
#


#This program focuses on showing the liner polation of the position of 
# a racecar on the racetrack at a given time for part 1

#Defines the inital position of the car
t_zero = 10
p_zero = 100

#Defines the final position of the car
t_one = 30
p_one = 800

#Defines the t at any given time 
t_obs = 21

#These lines evaluate the equation and show the position at the given time
p_obs = p_zero + (((p_one - p_zero) / (t_one - t_zero)) * ( t_obs - t_zero))
print ("For t =", t_obs, "seconds, the position p =", p_obs, "meters.")

#The position of the car at time zero creates a negative interger. 
#The postion  is -250 at time zero
#I interupt the position as 250 meters behind the placement at time zero
#The placemet at time zero should be where the car had initally started on the track 
#150 meters behind the inital point of 100 meters



#This program is going focus on giving the distance from the starting point 
#focused in part 2

import math

#This is going to initalize the radius of the track in meters
r_in_meters = 0.5 * 1000

#This is going to initalize the circumfrence of the track
cirum_of_track = 2 * math.pi * r_in_meters

#This initalizes the observed time in seconds for 25 minutes
t_obs = 25 * 60

#This evaluates the position past the starting line
distance = (p_zero + (((p_one - p_zero) / (t_one - t_zero)) * ( t_obs - t_zero))) % cirum_of_track
print("For t =", t_obs, "seconds, the position p =", distance, "meters.")

#Yes this is linear extrapolation, we are using it because we are going outside
#the limts of the equation in part one, and the veloctiy is constant. 
#Extrapolation can be used when the velocity is constant.

#The code will output the same soultion for part two as part one. 

