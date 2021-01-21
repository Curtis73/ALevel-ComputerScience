# RPG Inventory Program
# 21/01/2021

import random

inventory = []

def pick(item):
    inventory.append(item)
    print(item, "has been added to your inventory!")

def drop(item):
    if item in inventory:
        inventory.remove(item)
        print (item, "has been removed from your inventory!")
    else:
        print (item, "couldn't be found!")

def pull():
    print (random.choice(inventory), "has been pulled!")

def search():
    for item in inventory:
        print (item)

# Main Program
while True:
    command = input("Please select 'pick', 'drop', 'pull' or search")

    if command == "pick":
        item = input("Please enter an item to add to your inventory")
        pick(item)
    elif command == "drop":
        item = input("Please enter an item to remove from your inventory")
        drop(item)
    elif command == "pull":
        pull()
    elif command == "search":
        search()
    else:
        print ("Invalid command, please try again")