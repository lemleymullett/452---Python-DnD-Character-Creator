#This section is for the ability scores
nestedList = [["i am a list", "within al ist"],["another list","whithin a list"], ["aaaa","a"]]
headers = (": Ability : Score : Modifier")
print(headers)
for item in nestedList:
    print(":",item[0]," "*(13-len(item[0])), ":", item[1]," "*(13-len(item[0])),":")

print()
# used this to type the thing lol
# list = []
# a = ""
# while a != "stop":
#     list.append(a)
#     a = input("what u want")
#
# for item in list:
#     print('print("',item,'")')

print("Name: ")
print("Class: ")
print("Race: ")
print("Alignment: ")
print("Languages: ")
print(" ")
print("Armor Class: ")
print("Initiative: ")
print("Speed: ")
print("HP: ")
print(" ")
print("Weapons: ")
print("Features: ")
