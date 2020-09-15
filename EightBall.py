import random
import time

answers = [
  "Yes",
  "No",
  "Maybe in the future",
  "This will never happen",
  "Unsure",
  "Unlikely",
  "Undecided",
  "Certain"
]

print ("Welcome to the Ephereal Eight Ball!!!")
time.sleep(1)
question = input(("What would you like to know?\n"))
while question != None:   
    print(random.choice(answers))
    break;
