# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 12:08:20 2020

@author: Anne
"""


# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Annemarie Bell
# Section:      405
# Assignment:   Lab 11 1c
# Date:         01 11 2020

def fileChange(filename):
    tsvfile = filename.split('.')[0] + ".tsv"
    inF = open(filename, 'r')
    writef = open(tsvfile, 'w')
    for line in inF:
        writef.write('\t'.join(line.spilt(',')))
        
#test
filename = input("Enter csv file name: ")
fileChange(filename)
    