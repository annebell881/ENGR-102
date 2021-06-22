# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 08:25:40 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 9b 1
# Date:         19 10 2020

import math
#open file
myfile= open('WeatherData.csv', 'r')
#get lines
line= myfile.readline()

#create helper lists
all_data = []
temp_high = []
temp_low = []
precp = []

#set data to lists
for i in myfile:
    line = i.strip().spilt(',')
    all_data.append(line)

for j in range(len(all_data)):
    for k in range(1,len(all_data[i])):
        all_data[i][j] = float(all_data[i][j])
 
#calc min/max temp and precip
maxT = all_data[0][1]
maxP = 0

minT = all_data[0][1]
posMin = 0

precipitation = 0
for i in range(len(all_data)):
    if all_data[i][1] > maxT:
        maxT = all_data[i][1]
        maxP = i
    if all_data[i][3] < minT:
        minT = all_data[i][3]
        posMin = i
    precipitation += all_data[i][-1]
    
averageP = precipitation /len(all_data)

#print Outputs
print("3-year maximum temperature: ", minT, " F")
print("3-year minimum temperature: ", maxT, " F")
print("3-year average precipitation: ", '%.2f' %precipitation, "inches")

#input from user
month = input("Please enter a month: ")
year = int(input("Please enter a year: "))

#calc
monthYear = []
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

for i in range(len(months)):
    if month[i] == month.strip():
        monthVal = i + 1
for row in range(len(all_data)):
    firstcol = all_data[row][0].split('/')
    if int(firstcol[0]) == monthVal and int(firstcol[2]) == year:
        monthYear.append(all_data[row])

dev =0
lowTavg = 0
humAvg = 0
mean = 0
count = 0

for num in range(len(monthYear)):
    lowTavg += monthYear[num][3]
    mean += monthYear[num][-1]
    if monthYear[num][8] < 75:
        count += 1

lowTavg /= len(monthYear)
mean /= len(monthYear)
count /= len(monthYear)
count *= 100 

for i in range (len(monthYear)):
    dev += (monthYear[i][-1] -mean)**2
    dev /= len(monthYear)
    dev = math.sqrt(dev)
    
#print statments
print("For ", month, " ", year,":")
print("Average low temperature: ", '%.1f' %lowTavg, "f")
print("Percentage of days with average humidity below 75%:", '%.1f' %count, " %")
print("Mean daily precipitation: ", '%.4f' %mean, " inches")
print("Standard deviation of daily precipitation: ", '%.4f' %dev, " inches")

           