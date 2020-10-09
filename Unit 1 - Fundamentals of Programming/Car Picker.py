cars = ["Economy Car", "Saloon Car", "Sports Car"]

print("Please choose a car:")
print("1. Economy Car")
print("2. Saloon Car")
print("3. Sports Car")

car = input("\n")

if (car in cars):
    proceed = input("Are you sure you'd like to proceed?")
    if proceed == "yes" or proceed == "true":
        print("You have confirmed:", car, ",Have a nice day!")
    else:
        print("You have cancelled your order")
else:
    print ("Invalid choice")

