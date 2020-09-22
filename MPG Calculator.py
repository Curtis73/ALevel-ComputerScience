last_mileage = float(input("Please input your car's last mileage\n"))
current_mileage = float(input("Please input your car's current mileage\n"))
tank_capacity = int(input("Please input the size of your tank in litres\n"))

mpg = (current_mileage - last_mileage) / tank_capacity

print("Your MPG is " + str(mpg))
