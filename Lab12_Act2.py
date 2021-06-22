# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 08:07:59 2020

@author: Anne
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 12 2
# Date:         06 11 2020

import turtle as t

#letters i, v, x, l, c, d, m
#for each function turtle will draw the letter
def drawI():
    '''Draws an I'''
    #draw I
    t.right(98)
    t.down()
    t.forward()
    t.up()
    #reset to start
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(70)
    t.right(90)
    
def drawV():
    '''Draws a V'''
    t.right(60)
    t.down()
    t.forward(55)
    t.right(60)
    t.backward(55)
    #reset to draw next
    t.up()
    t.right(240)
    t.forward(25)
    
def drawL():
    '''Draws a L'''
    t.right(90)
    t.down()
    t.forward(70)
    t.left(90)
    t.forward(50)
    
    #reset
    t.up()
    t.forward(35)
    t.left(90)
    t.forward(70)
    t.right(90)
    
def drawX():
    '''Draws a X'''
    t.right(60)
    t.down()
    t.forward(70)
    t.up()
    t.left(60)
    t.backwards(35)
    t.left(60)
    t.down()
    t.forward(70)

    #reset
    t.up()
    t.right(60)
    t.forward(30)

def drawC():
    '''Draws a C'''
    t.up()
    t.forward(40)
    t.down()
    t.left(180)
    t.circle(30,180)
    
    #reset
    t.up()
    t.foward(30)
    t.left(90)
    t.forward(50)
    t.right(90)

def drawD():
    '''draws a D'''
    t.circle(30,180)
    t.down()
    t.left(90)
    t.forward(60)
    
    #reset
    t.up()
    t.backward(60)
    t.left(90)
    t.forward(60)

def drawM():
    '''draws a M'''
    t.right(90)
    t.forward(40)
    t.down()
    t.backward(40)
    t.left(30)
    t.forward(45)
    t.left(120)
    t.forward(45)
    t.right(150)
    t.forward(40)
    
    #reset
    t.up()
    t.backward(40)
    t.left(90)
    t.forward(25)
    
def num_to_roman(user_input):
   '''Creates a roman numeral from user input'''
   stri = ""
   numM = user_input // 1000
   stri += (numM * 'M')
   user_input -= numM *1000
    
   numD = user_input // 500
   stri += (numD * 'D')
   user_input -= numD *500
    
   numC = user_input // 100
   stri +=(numC *'C')
   user_input -= numC * 100
    
   numL = user_input // 50
   stri += (numL * 'L')
   user_input -= numL * 50
    
   numx = user_input // 10
   stri += (numL * 'X')
   user_input -= numx * 10
    
   numV = user_input // 5
   stri += (numV * 'V')
   user_input -= numV * 5

   numI = user_input 
   stri += (numI * 'I')
   return stri()

def draw(stri):
    '''Tells the program what to draw'''
    for i in range(len(stri)):
        if (stri[i] == 'I'):
            drawI()
        elif (stri[i] == 'V'):
            drawV()
        elif (stri[i] == 'X'):
            drawX()
        elif (stri[i] == 'L'):
            drawL()
        elif (stri[i] == 'C'):
            drawC()
        elif (stri[i] == 'D'):
            drawD()
        elif(stri[i] == 'M'):
            drawM()
            
    
    
#main function: try/ except
user_input = input("Enter a value to convert: ")
while(True):
    try:
        int(user_input)
    except:
        user_input = input("Enter a value to convert: ")
        
string = num_to_roman(user_input)
draw(string)
    