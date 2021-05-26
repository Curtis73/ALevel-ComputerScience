# Classification Program
# 13/05/2021

yes = []
no = []

armour = ["Darth Vader", "Clone Trooper", "Mandalorian"]
robot = ["Darth Vader", "General Grievous", "Gonk Droid"]
legs_2 = ["Clone Trooper", "Yoda", "Darth Vader", "Kenobi", "Mandalorian"]
lightsaber = ["Darth Vader", "General Grievous", "Yoda", "Kenobi"]

dicts = {
    "armour": armour,
    "robot": robot,
    "legs_2": legs_2,
    "lightsaber": lightsaber
}

armour_check = input("Does your character wear armour? ")
if armour_check.lower() == "yes":
    yes.append("armour")
else:
    no.append("armour")

robot_check = input("Is your character a robot? ")
if robot_check.lower() == "yes":
    yes.append("robot")
else:
    no.append("robot")

legs_2_check = input("Does your character have 2 legs? ")
if legs_2_check.lower() == "yes":
    yes.append("legs_2")
else:
    no.append("legs_2")

lightsaber_check = input("Does your character wield a lightsaber? ")
if lightsaber_check.lower() == "yes":
    yes.append("lightsaber")
else:
    no.append("lightsaber")

no_list = []
for var in no:
    no_list += dicts.get(var)
no_list = list(dict.fromkeys(no_list))  # Merge lists & remove duplicates

yes_list = []
for var in yes:
    yes_list += dicts.get(var)
yes_list = list(dict.fromkeys(yes_list))  # Merge lists & remove duplicates

for value in no_list:
    if value in yes_list:
        # If there's a value in both no & yes lists, remove it from final list
        yes_list.remove(value)
for value in yes_list:
    if value in no_list:
        yes_list.remove(value)

if len(yes_list) == 1:
    print("Your character is: ", yes_list[0])
else:
    print("Your character is one of the following: ", yes_list)








