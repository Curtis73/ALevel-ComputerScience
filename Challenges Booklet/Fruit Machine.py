# Fruit Machine
# 21/5/2021

import random

credit = 100
list = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]
keep_going = True

def roll():
    rolled = []
    global credit
    global keep_going
    credit = credit-20
    for x in range(3):
        rolled.append(random.choice(list))
    print("You rolled" + str(rolled))
    check_rewards(rolled)
    keep = input("Would you like to go again? y/n: ")
    if (keep != "y"):
        keep_going = False

def check_rewards(rolled):
    global credit
    cherry = bell = lemon = orange = star = skull = 0
    things = [cherry, bell, lemon, orange, star, skull]
    for val in rolled:
        val = val.lower()
        if val == "cherry":
            cherry += 1
        elif val == "bell":
            bell += 1
        elif val == "lemon":
            lemon += 1
        elif val == "orange":
            orange += 1
        elif val == "star":
            star += 1
        else:
            skull += 1

    counter = 0
    for value in things:
        if value == 2:
            credit += 50
        if value == 3:
            credit += 100
        if (value == "bell" and value == 3):
            credit += 500
        if value == "skull":
            if value == 2:
                credit -= 100
            if value == 3:
                credit = 0
    print("Your balance is now:", str(credit))

while keep_going is True and credit > 20:
    roll()