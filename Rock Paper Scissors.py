import random

rps = ["rock", "paper", "scissors"]
computerScore = 0
playerScore = 0
won = False

def computer_choose():
    return random.choice(rps)
    
def checkInput(player_input):
    if (player_input.lower() not in rps):
        print ("Wrong input - please try again")
        
    else:
        return player_input.lower()
            
def win(winner):
    global computerScore
    global playerScore
    print (winner, "Wins!")
    if (winner == "Player"):
        playerScore += 1
    else:
        computerScore += 1
    print ("Player Score:" + str(playerScore))
    print ("Computer Score:" + str(computerScore))
    print ("\n")
    
    if (playerScore == 10):
        print ("PLAYER WINS!!")
        won = True
        quit()
    if  (computerScore == 10):
        print ("COMPUTER WINS!!")
        won = True
        quit()        
        
def rockPaperScissors(computer, player):
    print ("computer: " + computer)
    print ("player: " + player)
    if (computer == playerInput):
        print ("Draw!\n")
    elif (computer == "rock" and player == "paper"):
        win("Player")
    elif (computer == "rock" and player == "scissors"):
        win("Computer")
    elif (computer == "paper" and player == "rock"):
        win("Computer")
    elif (computer == "paper" and player == "scissors"):
        win("Player")
    elif (computer == "scissors" and player == "paper"):
        win("Computer")
    elif (computer == "scissors" and player == "rock"):
        win("Computer")

while won == False:
    playerInput = input("Please enter Rock, Paper or Scissors\n")
    playerInput = checkInput(playerInput)
    computer = computer_choose()
    rockPaperScissors(computer, playerInput)
    
    


