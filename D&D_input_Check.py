# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 13:41:20 2020

@author: Anne
"""

class Character:
    def __init__(char, givenRace, givenClass, givenBackground):
        '''This function initalizes the character'''
        char.race = givenRace
        char.cclass = givenClass
        char.background = givenBackground

        
    def validate_class(char):
        """This function validates the character Class using a class"""

        possible_class = ["Barbarian", "Bard", "Cleic", "Druid", "Fighter", 
                          "Monk","Paladin", "Ranger", "Rouge", "Sorcerer",
                          "Warlock", "Wizard"]
        
        for i in possible_class:
            if(i == char.cclass):
                return True
            
        return False
        

    def Val_bg(char):
        '''This function checks for valid character background using a class'''
        possible_background =["Acolyte", "Criminal", "Spy", "Folk Hero",
                              "Haunted One", "Noble", "Sage", "Soldier"]
        for k in possible_background:
            if(k == char.background):
                return True
        return False
                
    def Val_race(char):
        '''Thus function valiates the character race using a class'''
        possible_race = ["Dragonborn", "Hill Dwarf", "Mountain Dwarf", 
                         "Eladrin Elf", "High Elf", "Wood Elf", "Rock Gnome",
                         "Half-Elf", "Half-Orc", "Lightfoot Halfling",
                         "Stout Halfling", "Human", "Tiefling"]
        for j in possible_race:
            if(j == char.race):
                return True
        
        
print("Capitalize the first character of each choice: ")
char_class = input("Please enter the character's class: ")
char_background = input("Please enter the charater's background: ")
char_race = input("Please enter the charater's race: ")

char = Character(char_race, char_class, char_background)


if(char.validate_class() and char.Val_bg() and char.Val_race()):
    print("Character Validated")
else:
    print("Invalid Charater. ")


        