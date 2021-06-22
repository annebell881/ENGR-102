# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 21:30:34 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 6 act 2
# Date:         26-09-2020


#get user input 

sex = input("Enter your sex (M/F): ")
age = int(input("Enter your age (years): "))
smoker = input("Do you smoke cigarettes (Y/N)? ")
total_chol = int(input("Enter your total cholesterol (mg/dL): "))
hDL = int(input("Enter your HDL cholesterol (mg/dL): "))
bP = int(input("Enter your systolic BP (mmHg): "))
medication = input("Are you taking blood pressure medication (Y/N)? ")
total_points = 0


#Male points determining their total points
#age
if (age >= 20 and age <= 34):
    total_points += -9
elif age >= 35 and age <= 39:
    total_points += -4
elif age >= 45 and age <= 49:
    total_points += 3
elif age >= 50 and age <= 54:
    total_points += 6
elif age >= 55 and age <= 59:
    total_points += 8
elif age >= 60 and age <= 64:
    total_points += 10
elif age >= 65 and age <= 69:
    total_points += 11
elif age >= 70 and age <= 74:
    total_points += 12
elif age >= 75 and age <= 79:
    total_points += 13
    
#total Cholesterol
if ((total_chol <= 160 and total_chol <=199) and (age >= 20 and age <= 39) ):
    total_points += 4
elif ((total_chol <= 160 and total_chol <=199) and (age >= 40 and age <= 49) ):
    total_points += 3
elif ((total_chol <= 160 and total_chol <=199) and (age >= 50 and age <= 59) ):
    total_points += 2
elif ((total_chol <= 160 and total_chol <=199) and (age >= 60 and age <= 69) ):
    total_points += 1
elif ((total_chol <= 200 and total_chol <=239) and (age >= 20 and age <= 39) ):
    total_points += 7
elif ((total_chol <= 200 and total_chol <=239) and (age >= 40 and age <= 49) ):
    total_points += 5
elif ((total_chol <= 200 and total_chol <=239) and (age >= 50 and age <= 59) ):
    total_points += 3
elif ((total_chol <= 200 and total_chol <=239) and (age >= 60 and age <= 69) ):
    total_points += 1
elif ((total_chol <= 240 and total_chol <=279) and (age >= 20 and age <= 39) ):
    total_points += 9
elif ((total_chol <= 240 and total_chol <=279) and (age >= 40 and age <= 49) ):
    total_points += 6
elif ((total_chol <= 240 and total_chol <=279) and (age >= 50 and age <= 59) ):
    total_points += 4
elif ((total_chol <= 240 and total_chol <=279) and (age >= 60 and age <= 69) ):
    total_points += 2
elif ((total_chol <= 240 and total_chol <=279) and (age >= 70 and age <= 79) ):
    total_points += 1   
elif ((total_chol >= 280 ) and (age >= 20 and age <= 39) ):
    total_points += 11
elif ((total_chol >= 280) and (age >= 40 and age <= 49) ):
    total_points += 8
elif ((total_chol >= 280) and (age >= 50 and age <= 59) ):
    total_points += 5
elif ((total_chol >= 280) and (age >= 60 and age <= 69) ):
    total_points += 3
elif ((total_chol >= 280) and (age >= 70 and age <= 79) ):
    total_points += 1  
#smoking   
if ( smoker == 'Y' and (age >= 20 and age <= 39) ):
    total_points += 8
elif ( smoker == 'Y' and (age >= 40 and age <= 49) ):
    total_points += 5
elif ( smoker == 'Y' and (age >= 50 and age <= 59) ):
    total_points += 3
elif ( smoker == 'Y' and (age >= 60 and age <= 69) ):
    total_points += 1
elif ( smoker == 'Y' and (age >= 60 and age <= 69) ):
    total_points += 1  
#HDL
if hDL >= 60:
    total_points += -1
elif hDL >= 40 and hDL <= 49:
    total_points += 1
elif hDL < 40:
    total_points += 2
    
#Bp
if (bP >= 120 and bP <= 129) and medication == 'Y':
    total_points += 1
elif (bP >= 130 and bP <= 139) and medication == 'N':
    total_points += 1
elif (bP >= 130 and bP <= 139) and medication == 'Y':
    total_points += 2
elif (bP >= 140 and bP <= 159) and medication == 'N':
    total_points += 1
elif (bP >= 140 and bP <= 159) and medication == 'Y':
    total_points += 2
elif bP >= 160 and medication == 'N':
    total_points += 2
elif bP >= 160 and medication == 'Y':
    total_points += 3

#risk and total points
if (sex == 'M' and total_points < 0):
    print ("Your 10-year risk of a heart attack is <1%")
elif (sex == 'M' and total_points == 0):
    print ("Your 10-year risk of a heart attack is 1%")
elif (sex == 'M' and total_points == 1):
    print ("Your 10-year risk of a heart attack is 1%")
elif (sex == 'M' and total_points == 2):
    print ("Your 10-year risk of a heart attack is 1%")
elif (sex == 'M' and total_points == 3):
    print ("Your 10-year risk of a heart attack is 1%")
elif (sex == 'M' and total_points == 4):
    print ("Your 10-year risk of a heart attack is 1%")
elif (sex == 'M' and total_points == 5):
    print ("Your 10-year risk of a heart attack is 2%")
elif (sex == 'M' and total_points == 6):
    print ("Your 10-year risk of a heart attack is 2%")
elif (sex == 'M' and total_points == 7):
    print ("Your 10-year risk of a heart attack is 3%")
elif (sex == 'M' and total_points == 8):
    print ("Your 10-year risk of a heart attack is 4%")
elif (sex == 'M' and total_points == 9):
    print ("Your 10-year risk of a heart attack is 5%")
elif (sex == 'M' and total_points == 10):
    print ("Your 10-year risk of a heart attack is 6%")
elif (sex == 'M' and total_points == 11):
    print ("Your 10-year risk of a heart attack is 8%")
elif (sex == 'M' and total_points == 12):
    print ("Your 10-year risk of a heart attack is 10%")
elif (sex == 'M' and total_points == 13):
    print ("Your 10-year risk of a heart attack is 12%")
elif (sex == 'M' and total_points == 14):
    print ("Your 10-year risk of a heart attack is 16%")
elif (sex == 'M' and total_points == 15):
    print ("Your 10-year risk of a heart attack is 20%")
elif (sex == 'M' and total_points == 16):
    print ("Your 10-year risk of a heart attack is 25%")
elif (sex == 'M' and total_points >= 17):
    print ("Your 10-year risk of a heart attack is >=30%")

#Female points determining their total points
#age
if (age >= 20 and age <= 34):
    total_points += -7
elif age >= 35 and age <= 39:
    total_points += -3
elif age >= 45 and age <= 49:
    total_points += 3
elif age >= 50 and age <= 54:
    total_points += 6
elif age >= 55 and age <= 59:
    total_points += 8
elif age >= 60 and age <= 64:
    total_points += 10
elif age >= 65 and age <= 69:
    total_points += 12
elif age >= 70 and age <= 74:
    total_points += 14
elif age >= 75 and age <= 79:
    total_points += 16
    
#total Cholesterol
if ((total_chol <= 160 and total_chol <=199) and (age >= 20 and age <= 39) ):
    total_points += 4
elif ((total_chol <= 160 and total_chol <=199) and (age >= 40 and age <= 49) ):
    total_points += 3
elif ((total_chol <= 160 and total_chol <=199) and (age >= 50 and age <= 59) ):
    total_points += 2
elif ((total_chol <= 160 and total_chol <=199) and (age >= 60 and age <= 69) ):
    total_points += 1
elif ((total_chol <= 160 and total_chol <=199) and (age >= 70 and age <= 79) ):
    total_points += 1  
elif ((total_chol <= 200 and total_chol <=239) and (age >= 20 and age <= 39) ):
    total_points += 8
elif ((total_chol <= 200 and total_chol <=239) and (age >= 40 and age <= 49) ):
    total_points += 6
elif ((total_chol <= 200 and total_chol <=239) and (age >= 50 and age <= 59) ):
    total_points += 4
elif ((total_chol <= 200 and total_chol <=239) and (age >= 60 and age <= 69) ):
    total_points += 2
elif ((total_chol <= 200 and total_chol <=239) and (age >= 70 and age <= 79) ):
    total_points += 1  
elif ((total_chol <= 240 and total_chol <=279) and (age >= 20 and age <= 39) ):
    total_points += 11
elif ((total_chol <= 240 and total_chol <=279) and (age >= 40 and age <= 49) ):
    total_points += 8
elif ((total_chol <= 240 and total_chol <=279) and (age >= 50 and age <= 59) ):
    total_points += 5
elif ((total_chol <= 240 and total_chol <=279) and (age >= 60 and age <= 69) ):
    total_points += 3
elif ((total_chol <= 240 and total_chol <=279) and (age >= 70 and age <= 79) ):
    total_points += 3   
elif ((total_chol >= 280 ) and (age >= 20 and age <= 39) ):
    total_points += 13
elif ((total_chol >= 280) and (age >= 40 and age <= 49) ):
    total_points += 10
elif ((total_chol >= 280) and (age >= 50 and age <= 59) ):
    total_points += 7
elif ((total_chol >= 280) and (age >= 60 and age <= 69) ):
    total_points += 4
elif ((total_chol >= 280) and (age >= 60 and age <= 69) ):
    total_points += 2  
#smoking   
if ( smoker == 'Y' and (age >= 20 and age <= 39) ):
    total_points += 9
elif ( smoker == 'Y' and (age >= 40 and age <= 49) ):
    total_points += 7
elif ( smoker == 'Y' and (age >= 50 and age <= 59) ):
    total_points += 4
elif ( smoker == 'Y' and (age >= 60 and age <= 69) ):
    total_points += 2
elif ( smoker == 'Y' and (age >= 60 and age <= 69) ):
    total_points += 1  
#HDL
if hDL >= 60:
    total_points += -1
elif hDL >= 40 and hDL <= 49:
    total_points += 1
elif hDL < 40:
    total_points += 2
    
#Bp
if (bP >= 160 and bP <= 129) and medication == 'N':
    total_points += 1
elif (bP >= 120 and bP <= 129) and medication == 'Y':
    total_points += 3
elif (bP >= 130 and bP <= 139) and medication == 'N':
    total_points += 2
elif (bP >= 130 and bP <= 139) and medication == 'Y':
    total_points += 4
elif (bP >= 140 and bP <= 159) and medication == 'N':
    total_points += 3
elif (bP >= 140 and bP <= 159) and medication == 'Y':
    total_points += 5
elif bP >= 160 and medication == 'N':
    total_points += 4
elif bP >= 160 and medication == 'Y':
    total_points += 6

#risk and total points
if (sex == 'F' and total_points < 9):
    print ("Your 10-year risk of a heart attack is <1%")
elif (sex == 'F' and total_points == 9):
    print ("Your 10-year risk of a heart attack is 1%")
elif (sex == 'F' and total_points == 10):
    print ("Your 10-year risk of a heart attack is 1%")
elif (sex == 'F' and total_points == 11):
    print ("Your 10-year risk of a heart attack is 1%")
elif (sex == 'F' and total_points == 12):
    print ("Your 10-year risk of a heart attack is 1%")
elif (sex == 'F' and total_points == 13):
    print ("Your 10-year risk of a heart attack is 2%")
elif (sex == 'F' and total_points == 14):
    print ("Your 10-year risk of a heart attack is 2%")
elif (sex == 'F' and total_points == 15):
    print ("Your 10-year risk of a heart attack is 3%")
elif (sex == 'F' and total_points == 16):
    print ("Your 10-year risk of a heart attack is 4%")
elif (sex == 'F' and total_points == 17):
    print ("Your 10-year risk of a heart attack is 5%")
elif (sex == 'F' and total_points == 18):
    print ("Your 10-year risk of a heart attack is 6%")
elif (sex == 'F' and total_points == 19):
    print ("Your 10-year risk of a heart attack is 8%")
elif (sex == 'F' and total_points == 20):
    print ("Your 10-year risk of a heart attack is 11%")
elif (sex == 'F' and total_points == 21):
    print ("Your 10-year risk of a heart attack is 14%")
elif (sex == 'F' and total_points == 22):
    print ("Your 10-year risk of a heart attack is 17%")
elif (sex == 'F' and total_points == 23):
    print ("Your 10-year risk of a heart attack is 22%")
elif (sex == 'F' and total_points == 24):
    print ("Your 10-year risk of a heart attack is 27%")
elif (sex == 'F' and total_points >= 25):
    print ("Your 10-year risk of a heart attack is >=30%")  