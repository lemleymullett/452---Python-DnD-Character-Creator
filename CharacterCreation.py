#Lemley!
# Character Creator - D&D Fifth Edition
#Fall 2017
# D&D is Wizards of the Coast material. I'm just organizing it.

from random import randint

# I looked at Lindsay V. Clark on Github's code for help with this function
def abilityscores():
    abscores = []
    for j in range(6):
        thesedice = []
        # Roll 4 d6 and keep the best three
        for k in range(4):
            thesedice[k:k] = [random.randint(1,6)]
        abscores[j:j] = [sum(sorted(thesedice)[1:])]
        abscores.sort()

    abnames = ["Strength", "Dexterity", "Constitution",
               "Intelligence", "Wisdom", "Charisma"]
    playerabs = [] # score order same as other orders
    for j in range(6): # loop through the six specific abilities
        print("\nRemaining scores to choose from are:")
        print(abscores)
        thisscore = -99
        while thisscore not in abscores:
            try:
                thisscore = int(input("Choose score for " + abnames[j] + ": "))
                if thisscore in abscores:
                    break
            except:
                pass
            print("Incorrect input, try again")
        playerabs.append(thisscore) # assign score to ability
        thisind = abscores.index(thisscore)
        del abscores[thisind] # remove score from collection
    return playerabs

def modifierConverter(statnumber):
    #ability modifiers are based on stats
    #always rounds down
    mod = int((statnumber - 10)/2)
    return mod

# ******************DATA SECTION***********************************
#Skill Dictionary and the Skills they Depend On
#still being worked on. will match to ability table
skills = {'Acrobatics': 'dex', 'Animal Handling': 'wis',
             'Arcana': 'int', 'Athletics': 'str',
             'Deception': 'cha', 'History': 'int',
             'Insight': 'wis', 'Intimidation': 'cha',
             'Investigation': 'int', 'Medicine': 'wis',
             'Nature': 'int', 'Perception': 'wis',
             'Performance': 'cha', 'Persuasion': 'cha',
             'Religion': 'int', 'Sleight of Hand': 'dex',
             'Stealth': 'dex', 'Survival': 'wis'}

#Race Data
#this first races dictionary is used to match user input to Race
#will probably not be needed when i edit to be cleaner next go-round
races = {'dwarf':'dwarf', 'elf':'elf','human':'human', 'half orc':'halfOrc', 'half elf':'halfElf', 'gnome':'gnome', 'dwarf':'dwarf', 'halfling':'halfling', 'tiefling':'tiefling','dragonborn':'dragonborn'}

#race dictionaries
#most fiddly stuff is just shoved under the catchall 'features'. will separate out another time
dwarf = {'ability': [0,0,2,0,0,0],
         'speed': 25,
         'features': ['darkvision', 'advantage on saving throws for poison and resistance against poison damage'],
         'language':['common', 'dwarvish'],
         'proficiency': []}

elf = {'ability': [0,2,0,0,0,0],
         'speed': 30,
         'features': ['darkvision', 'advantage on saving throws against being Charmed',
                      'magic cannot put you to sleep', 'meditating for 4 hours = 8 hours of human sleep'],
         'language':['common', 'elvish'],
         'proficiency': ['perception']}

human = {'ability': [1,1,1,1,1,1],
         'speed': 30,
         'features': [],
         'language':['common','1 extra language'],
         'proficiency': []}

halfElf = {'ability': [0,0,0,0,0,2],
           #half elf can choose 2 abilities to give +1 to
         'speed': 30,
         'features': ['darkvision','advantage on saving throws against being charmed', 'magic cannot put you to sleep'],
         'language':['common','elvish', 'one extra language of your choice'],
         'proficiency': []}
           #prof in 2 skills of your choice

halfOrc = {'ability': [2,0,1,0,0,0],
         'speed': 30,
         'features': ['darkvision', 'if reduced to 0 hit points, once every Long Rest you can instead choose to drop to 1'
                      'when you score a critical hit (nat 20) on a melee weapon attack, you can roll one of the weapons damage dice and add it to the extra damage of the crit'],
         'language':['common', 'orc'],
         'proficiency': ['intimidation']}

halfling = {'ability': [0,2,0,0,0,0],
         'speed': 25,
         'features': ['when you roll 1 on an attack roll, ability check, or saving throw, you can reroll the die and must take the new number.'
                      'advantage on saving throws against being frightened',
                      'you can move through the spave of any creature that is a size larger than you'],
         'language':['common', 'halfling'],
         'proficiency': []}

gnome = {'ability': [0,0,0,2,0,0],
         'speed': 25,
         'features': ['darkvision', 'advantage on all Intelligence, Wisdom, and Charisma saving throws against magic'],
         'language':['common',],
         'proficiency': []}
dragonborn = {'ability': [2,0,0,0,0,1],
         'speed': 30,
         'features': ['breath weapon'],
         'language':['common','draconic'],
         'proficiency': []}

tiefling = {'ability': [0,0,0,1,0,2],
         'speed': 30,
         'features': ['darkvision','resistance to fire damage',
                      'you know the thaumaturgy cantrip',
                      'you learn hellish rebuke at level 3 and can use it at 2ndlevel once a day'
                      'you learn darkness at 5th level and can cast it once per day'],
         'language':['common','infernal'],
         'proficiency': []}

#Class Data. I only have the first 3 as proof of concept
barbarian = {'hp':(12),
             'proficiency':['light armor', 'medium armor', 'shields', 'simple weapons', 'martial weapons', 'str','con'],
             #choose 2 skills to add prof to
            'equipment':['greataxe','two handaxes', 'four javelins', 'explorers pack'],
             'features':[]}

bard = {'hp':(8),
        'proficiency':['light armor','simple weapons', 'hand crossbows', 'longswords','rapiers', 'shortswords',
                       'three insturments of choice', 'dex', 'cha'],
        'equipment':['simple weapon','entertainers pack','musical instrument of choice','leather armor', 'dagger'],
        'spells':['two bard cantrips of choice','four 1st level spells of choice'],
        'spell slots':2,
        'features':['bardic inspiration, xCharisma modifier times per day']}
        # choose any 3 skills
cleric = {'hp':(8),
          'proficiency':['light armor', 'medium armor', 'shields', 'simple weapons','wis','cha'],
          #two skills of choice from history/insight/med/persuasion/religion
           'equipment':['mace','scale mail','any simple weapon','priests pack','shield','holy symbol'],
          'spells':'three cleric cantrips of choice',
          'spell slots':2,
          'features':['divine domain']}

#*****************DATA ENDS HERE***********

name = input("Pick a name for your character!: ")
print()
print("Next is race! You can choose from:")
for i in races:
    print(i.capitalize())
print()
raceinput = input("Character race: ")
check = False
while check == False:
    if raceinput.lower() in races:
        print("Got it, you want to be a(n) ", raceinput, "!")
        check = True
    else:
        print("Sorry, could you type that again? Please match the spelling above!")
        raceinput = input("Character race: ")

classes = ["bard", "barbarian", "cleric"]
classCheck = False
classinput = input("And what Class would you like to be? Currently this code only handles Barbarian, Cleric and Bard.")
while classCheck == False:
    if classinput.lower() in classes:
        classCheck = True
    else:
        print("Sorry, you either misspelled or I haven't put that class in yet!")


print("What is your character's alignment? This will tell us about their general morals and behavior.")
print("These are the options: (pick one from the first row and one from any column")
algnheader= ":  Lawful  :  Neutral  :  Chaotic :"
algntable = ['Good','Neutral', 'Evil',]
print(algnheader)
for a in algntable:
    print(":",a," "*(7-len(a)), ":", a," "*(8-len(a)),":", a," "*(3-len(a)), ":")

alignment = input("Your character is: ")

print("Okay! Next is determining your ability scores.")
print("Think about the class you want to play. What stats will be mot useful?")
print("The stats are Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma.")
print()
print("This program rolls 4 dice and adds the top 3 choices, 6 times. You can decide where to put these numbers.")
print()

BasicScores = abilityscores()

#the form-filing parts
features = []
languages = []
proficiency = []

#ability scores: 0Str, 1Dex, 2Con, 3Int, 4Wis, 5Cha
scoretable = [["Strength",0,0],["Dexterity",0,0], ["Constitution",0,0], ["Intelligence",0,0], ["Wisdom",0,0], ["Charisma",0,0]]
headers = (": Ability        : Score : Modifier")
#ability-adding AND ALSO ALL THE OTHER STUFF SO I DONT GOTTA WRITE ANOTHER IF STATEMENT BASED ON RACE
if raceinput.lower() == "dwarf":
    scoretable[0][1] += dwarf["ability"][0]
    scoretable[0][1] += BasicScores[0]
    scoretable[0][2] = modifierConverter(scoretable[0][1])
    scoretable[1][1] += dwarf["ability"][1]
    scoretable[1][1] += BasicScores[1]
    scoretable[1][2] = modifierConverter(scoretable[1][1])
    scoretable[2][1] += dwarf["ability"][2]
    scoretable[2][1] += BasicScores[2]
    scoretable[2][2] = modifierConverter(scoretable[2][1])
    scoretable[3][1] += dwarf["ability"][3]
    scoretable[3][1] += BasicScores[3]
    scoretable[3][2] = modifierConverter(scoretable[3][1])
    scoretable[4][1] += dwarf["ability"][4]
    scoretable[4][1] += BasicScores[4]
    scoretable[4][2] = modifierConverter(scoretable[4][1])
    scoretable[5][1] += dwarf["ability"][5]
    scoretable[5][1] += BasicScores[5]
    scoretable[5][2] = modifierConverter(scoretable[5][1])

    features.append(dwarf["features"])
    speed = dwarf["speed"]
    languages.append(dwarf["language"])
    proficiency.append(dwarf["proficiency"])

elif raceinput.lower() == "elf":
    scoretable[0][1] += elf["ability"][0]
    scoretable[0][1] += BasicScores[0]
    scoretable[0][2] = modifierConverter(scoretable[0][1])
    scoretable[1][1] += elf["ability"][1]
    scoretable[1][1] += BasicScores[1]
    scoretable[1][2] = modifierConverter(scoretable[1][1])
    scoretable[2][1] += elf["ability"][2]
    scoretable[2][1] += BasicScores[2]
    scoretable[2][2] = modifierConverter(scoretable[2][1])
    scoretable[3][1] += elf["ability"][3]
    scoretable[3][1] += BasicScores[3]
    scoretable[3][2] = modifierConverter(scoretable[3][1])
    scoretable[4][1] += elf["ability"][4]
    scoretable[4][1] += BasicScores[4]
    scoretable[4][2] = modifierConverter(scoretable[4][1])
    scoretable[5][1] += elf["ability"][5]
    scoretable[5][1] += BasicScores[5]
    scoretable[5][2] = modifierConverter(scoretable[5][1])

    features.append(elf["features"])
    speed = elf["speed"]
    languages.append(elf["language"])
    proficiency.append(elf["proficiency"])

elif raceinput.lower() == "gnome":
    scoretable[0][1] += gnome["ability"][0]
    scoretable[0][1] += BasicScores[0]
    scoretable[0][2] = modifierConverter(scoretable[0][1])
    scoretable[1][1] += gnome["ability"][1]
    scoretable[1][1] += BasicScores[1]
    scoretable[1][2] = modifierConverter(scoretable[1][1])
    scoretable[2][1] += gnome["ability"][2]
    scoretable[2][1] += BasicScores[2]
    scoretable[2][2] = modifierConverter(scoretable[2][1])
    scoretable[3][1] += gnome["ability"][3]
    scoretable[3][1] += BasicScores[3]
    scoretable[3][2] = modifierConverter(scoretable[3][1])
    scoretable[4][1] += gnome["ability"][4]
    scoretable[4][1] += BasicScores[4]
    scoretable[4][2] = modifierConverter(scoretable[4][1])
    scoretable[5][1] += gnome["ability"][5]
    scoretable[5][1] += BasicScores[5]
    scoretable[5][2] = modifierConverter(scoretable[5][1])


    features.append(gnome["features"])
    speed = gnome["speed"]
    languages.append(gnome["language"])
    proficiency.append(gnome["proficiency"])

elif raceinput.lower() == "half orc":
    scoretable[0][1] += halfOrc["ability"][0]
    scoretable[0][1] += BasicScores[0]
    scoretable[0][2] = modifierConverter(scoretable[0][1])
    scoretable[1][1] += halfOrc["ability"][1]
    scoretable[1][1] += BasicScores[1]
    scoretable[1][2] = modifierConverter(scoretable[1][1])
    scoretable[2][1] += halfOrc["ability"][2]
    scoretable[2][1] += BasicScores[2]
    scoretable[2][2] = modifierConverter(scoretable[2][1])
    scoretable[3][1] += halfOrc["ability"][3]
    scoretable[3][1] += BasicScores[3]
    scoretable[3][2] = modifierConverter(scoretable[3][1])
    scoretable[4][1] += halfOrc["ability"][4]
    scoretable[4][1] += BasicScores[4]
    scoretable[4][2] = modifierConverter(scoretable[4][1])
    scoretable[5][1] += halfOrc["ability"][5]
    scoretable[5][1] += BasicScores[5]
    scoretable[5][2] = modifierConverter(scoretable[5][1])

    features.append(halfOrc["features"])
    speed = halfOrc["speed"]
    languages.append(halfOrc["language"])
    proficiency.append(halfOrc["proficiency"])

elif raceinput.lower() == "half elf":
    scoretable[0][1] += halfElf["ability"][0]
    scoretable[0][1] += BasicScores[0]
    scoretable[0][2] = modifierConverter(scoretable[0][1])
    scoretable[1][1] += halfElf["ability"][1]
    scoretable[1][1] += BasicScores[1]
    scoretable[1][2] = modifierConverter(scoretable[1][1])
    scoretable[2][1] += halfElf["ability"][2]
    scoretable[2][1] += BasicScores[2]
    scoretable[2][2] = modifierConverter(scoretable[2][1])
    scoretable[3][1] += halfElf["ability"][3]
    scoretable[3][1] += BasicScores[3]
    scoretable[3][2] = modifierConverter(scoretable[3][1])
    scoretable[4][1] += halfElf["ability"][4]
    scoretable[4][1] += BasicScores[4]
    scoretable[4][2] = modifierConverter(scoretable[4][1])
    scoretable[5][1] += halfElf["ability"][5]
    scoretable[5][1] += BasicScores[5]
    scoretable[5][2] = modifierConverter(scoretable[5][1])

    features.append(halfElf["features"])
    speed = halfElf["speed"]
    languages.append(halfElf["language"])
    proficiency.append(halfElf["proficiency"])

elif raceinput.lower() == "tiefling":
    scoretable[0][1] += tiefling["ability"][0]
    scoretable[0][1] += BasicScores[0]
    scoretable[0][2] = modifierConverter(scoretable[0][1])
    scoretable[1][1] += tiefling["ability"][1]
    scoretable[1][1] += BasicScores[0]
    scoretable[1][2] = modifierConverter(scoretable[1][1])
    scoretable[2][1] += tiefling["ability"][2]
    scoretable[2][1] += BasicScores[0]
    scoretable[2][2] = modifierConverter(scoretable[2][1])
    scoretable[3][1] += tiefling["ability"][3]
    scoretable[3][1] += BasicScores[0]
    scoretable[3][2] = modifierConverter(scoretable[3][1])
    scoretable[4][1] += tiefling["ability"][4]
    scoretable[4][1] += BasicScores[0]
    scoretable[4][2] = modifierConverter(scoretable[4][1])
    scoretable[5][1] += tiefling["ability"][4]
    scoretable[5][1] += BasicScores[0]
    scoretable[5][2] = modifierConverter(scoretable[5][1])

    features.append(tiefling["features"])
    speed = tiefling["speed"]
    languages.append(tiefling["language"])
    proficiency.append(tiefling["proficiency"])

elif raceinput.lower() == "dragonborn":
    scoretable[0][1] += dragonborn["ability"][0]
    scoretable[0][1] += BasicScores[0]
    scoretable[0][2] = modifierConverter(scoretable[0][1])
    scoretable[1][1] += dragonborn["ability"][1]
    scoretable[1][1] += BasicScores[1]
    scoretable[1][2] = modifierConverter(scoretable[1][1])
    scoretable[2][1] += dragonborn["ability"][2]
    scoretable[2][1] += BasicScores[2]
    scoretable[2][2] = modifierConverter(scoretable[2][1])
    scoretable[3][1] += dragonborn["ability"][3]
    scoretable[3][1] += BasicScores[3]
    scoretable[3][2] = modifierConverter(scoretable[3][1])
    scoretable[4][1] += dragonborn["ability"][4]
    scoretable[4][1] += BasicScores[4]
    scoretable[4][2] = modifierConverter(scoretable[4][1])
    scoretable[5][1] += dragonborn["ability"][5]
    scoretable[5][1] += BasicScores[5]
    scoretable[5][2] = modifierConverter(scoretable[5][1])

    features.append(dragonborn["features"])
    speed = dragonborn["speed"]
    languages.append(dragonborn["language"])
    proficiency.append(dragonborn["proficiency"])

elif raceinput.lower() == "halfling":
    scoretable[0][1] += halfling["ability"][0]
    scoretable[0][1] += BasicScores[0]
    scoretable[0][2] = modifierConverter(scoretable[0][1])
    scoretable[1][1] += halfling["ability"][1]
    scoretable[1][1] += BasicScores[1]
    scoretable[1][2] = modifierConverter(scoretable[1][1])
    scoretable[2][1] += halfling["ability"][2]
    scoretable[2][1] += BasicScores[2]
    scoretable[2][2] = modifierConverter(scoretable[2][1])
    scoretable[3][1] += halfling["ability"][3]
    scoretable[3][1] += BasicScores[3]
    scoretable[3][2] = modifierConverter(scoretable[3][1])
    scoretable[4][1] += halfling["ability"][4]
    scoretable[4][1] += BasicScores[4]
    scoretable[4][2] = modifierConverter(scoretable[4][1])
    scoretable[5][1] += halfling["ability"][5]
    scoretable[5][1] += BasicScores[5]
    scoretable[5][2] = modifierConverter(scoretable[5][1])

    features.append(halfling["features"])
    speed = halfling["speed"]
    languages.append(halfling["language"])
    proficiency.append(halfling["proficiency"])

elif raceinput.lower() == "human":
    scoretable[0][1] += human["ability"][0]
    scoretable[0][1] += BasicScores[0]
    scoretable[0][2] = modifierConverter(scoretable[0][1])
    scoretable[1][1] += human["ability"][1]
    scoretable[1][1] += BasicScores[1]
    scoretable[1][2] = modifierConverter(scoretable[1][1])
    scoretable[2][1] += human["ability"][2]
    scoretable[2][1] += BasicScores[2]
    scoretable[2][2] = modifierConverter(scoretable[2][1])
    scoretable[3][1] += human["ability"][3]
    scoretable[3][1] += BasicScores[3]
    scoretable[3][2] = modifierConverter(scoretable[3][1])
    scoretable[4][1] += human["ability"][4]
    scoretable[4][1] += BasicScores[4]
    scoretable[4][2] = modifierConverter(scoretable[4][1])
    scoretable[5][1] += human["ability"][5]
    scoretable[5][1] += BasicScores[5]
    scoretable[5][2] = modifierConverter(scoretable[5][1])

    features.append(human["features"])
    speed = human["speed"]
    languages.append(human["language"])
    proficiency.append(human["proficiency"])


#CLASS ADDING SHENANIGANS
if classinput.lower() == "bard":
    classfeatures = (bard["features"])
    hp = bard["hp"] + scoretable[2][2]
    spells = bard["spells"]
    spellslots = bard["spell slots"]


if classinput.lower() == "barbarian":
    classfeatures = (barbarian["features"])
    hp = barbarian["hp"] + scoretable[2][2]
    spells = ""
    spellslots = ""


if classinput.lower() == "cleric":
    classfeatures = (cleric["features"])
    hp = cleric["hp"] + scoretable[2][2]
    spells = cleric["spells"]
    spellslots = cleric["spell slots"]



print()
print()
print("OKAY! Here we go:")
print()
#this is the final form!!!

print("Name: ", name)
print("Class: " , classinput)
print("Race: ", races[raceinput])
print("Alignment: ", alignment)
print("Languages: ", languages)
print(" ")
print("Armor Class: ", scoretable[1][2] + 11)
print("Initiative: ", scoretable[1][2])
print("Speed: ", speed)
print("HP: ", hp)
print(" ")
print("Spells:", spells)
print("Features: ")
for l in features:
    print(l)
print()
print("Saving Throws:")
print("Str", scoretable[0][2])
print("Dex",scoretable[1][2])
print("Con",scoretable[2][2])
print("Wis",scoretable[3][2])
print("Int",scoretable[4][2])
print("Cha",scoretable[5][2])

print(headers)
for item in scoretable:
    print(":",item[0]," "*(13-len(item[0])), ":", item[1]," "*(3),":", item[2])

print("There you go! Go forth and use this info for the greater DnD good.")
input("Press Enter to close the program once youve copied your data.")
