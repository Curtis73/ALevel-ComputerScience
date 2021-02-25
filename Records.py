# Records/Database program
# 25/02/2021

players = []

add_players = True

while add_players:
    print("Enter a username: ")
    username = input()
    print("Enter a password: ")
    password = input()
    print("Enter a score: ")
    score = input()
    print("Enter their highest score: ")
    highscore = input()

    player = {
        "username" : username,
        "password" : password,
        "score" : score,
        "highscore" : highscore
    }

    players.append(player)

    print ("Would you like to add another player? Y/N")
    answer = input().upper()
    if answer == "N":
        add_players = False

print("Which record would you like to access: ")
record = int(input()) -1
print ("What attribute would you like to access:")
attribute = input()
if attribute.lower() == "username":
    print (players[record]["username"])
elif attribute.lower() == "password":
    print (players[record]["password"])
elif attribute.lower() == "score":
    print (players[record]["score"])
elif attribute.lower() == "highscore":
    print (players[record]["highscore"])
else:
    print ("Please specify either: Username, Password, Score, Highscore")