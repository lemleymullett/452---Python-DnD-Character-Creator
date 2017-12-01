#Lemley!
# Character Creator - D&D Fifth Edition
# Welcome to my weird dummycode + actual code combo
# D&D is Wizards of the Coast material. I'm just organizing it.

from random import randint

#we're going to need to keep all of the information the below sections return so that it can be organized into a table somewhere. I haven't done this part yet.
#Also how the HECK am i gonna format this to look pretty at the end LOL... i guess i could have the program -
#-output an HTML-formatted chunk that can be pasted on a website somewhere??
#or just mess with print statements and white space until it looks decent

#the program will show the user the information on DnD classes(basically occupations)
#and then ask them to pick one
#*******Reminder to myself to put in try-except loop thingies so a bad input doesnt mess up the whole dealio
#technically, a class will add different attributes to the character's stats, so i need to know not just to slap flavor text in but to provide proper numbers
#I'll probably add class descriptions and stuff last once i get the actual code part worked out
#for now i gotta make a class-numbers file somewhere to reference.
def Class():

#Same format as Class. technically adds variables to stats
def Race():


#add some
def StatRandomizer():
    # This function is for ability scores.
    # To create an ability score, you roll 4 dice, and add the three highest rolls.
    stat = []
    stat.append[randint(1,6)]
    stat.append[randint(1,6)]
    stat.append[randint(1,6)]
    stat.append[randint(1,6)]
    #Figure out how to remove smallest number from list
    finalanswer = 0
    for item in stat:
        finalanswer += item

    return finalanswer

def modifierConverter(statnumber):
    #ability modifiers are based on stats
    #this is gonna be a big if/else statement
    if statnumber <= 1:
        mod = -5
    elif statnumber <=3:
        mod = -4
    elif statnumber <=5:
        mod = -3
    elif statnumber <=7:
        mod = -2
    elif statnumber <=9:
        mod = -1
    elif statnumber <= 11:
        mod = 0
    elif statnumber <=13:
        mod = 1
    elif statnumber <=15:
        mod = 2
    elif statnumber <=17:
        mod = 3
    elif statnumber <=19:
        mod = 4
    #my code is limited to level 1 character creation, so it's unlikely the numbers past this will be needed
    elif statnumber <=21:
        mod = 5
    elif statnumber <=23:
        mod = 6
    elif statnumber <=25:
        mod = 7
    elif statnumber <=27:
        mod = 8
    elif statnumber <=29:
        mod = 9
    elif statnumber >=30:
        mod = 10
    else:
        print("UHHHH NOPE DONT GET THIS")

    return mod

def armorClass(dex, armor??):
    #this will depend on the Dex ability and... the default armor that comes with a class, so
#I'll need to get that information out of the Class section
    return armor

def weaponChoice():
    #character sstart out with like, 2 weapons of their choice
    #i'll need to grab that information and let users pick from weapons they can use
    #this might depend on race and class details, so I'll have to hook that in too

def description():
    # uhhhhhhhhhhh tell me your characters personality and stuff so i can put it on the page
    #Or something


#code making all of these functions Go will be here

#oh heck i need the output function or something:
def output():
    #PRINT THAT GOOD GOOD SHEET
    #THIS COMES LAST
    #...PROBABLY
