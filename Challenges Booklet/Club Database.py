# Club Database Program
# 03/04/2021

import csv

more = True
data = []

def printData(name, dob, address, gender):
    print("Name:", name)
    print("DoB:", dob)
    print("Address:", address)
    print("Gender:", gender)

def accessData():
    with open("data.csv", "r") as file:
        data = []
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
        return data
    
def retrieveData(name):
    data = accessData()
    for array in data:
        if array[0] == name:
            return array

while more == True:
    name = input("Please input the name: ")
    dob = input("Please input date of birth: ")
    address = input("Please input address: ")
    gender = input("Please input gender: ")
    correct = input("Is this correct? y/n: ")
    if (correct != "y"):
        continue
    cont = input("Would you like to add another? y/n: ")
    if (cont != "y"):
        more = False

    data.extend([([name,dob,address,gender])])

with open("data.csv", "w") as file:
    write = csv.writer(file, lineterminator="\n")
    write.writerows(data)

search = input("Would you like to searched for a stored user? y/n: ")

if search == "y":
    repeat = True
    while repeat == True:
        name = input("Please input the name of the user to search for: ")
        retrieved_data = retrieveData(name)
        try:
            printData(retrieved_data[0], retrieved_data[1], retrieved_data[2], retrieved_data[3])
        except TypeError:
            print("That user could not be found, try again!")
            
        more = input("Would you like to search for another user? y/n: ")
        if more != "y":
            repeat = False