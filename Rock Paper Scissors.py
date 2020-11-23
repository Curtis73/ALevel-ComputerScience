import random

rps = ["rock", "paper", "scissors"]
computerScore = 0
playerScore = 0
won = False

def computer_choose():
    return random.choice(rps)
    
def checkInput(player_input):
    if (player_input.lower() not in rps):
        print ("Wrong input - please try again\n")
        return None
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
    print ("Player Score: " + str(playerScore))
    print ("Computer Score: " + str(computerScore) + "\n")    
    if (playerScore == 10):
        print ("Player wins the match! Congratulations!")
        won = True
        quit()
    if  (computerScore == 10):
        print ("Computer wins the match! Better luck next time!")
        won = True
        quit()        
        
def rockPaperScissors(computer, player):
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
    if (checkInput(playerInput) is None):
        continue
    playerInput = checkInput(playerInput)
    computer = computer_choose()
    rockPaperScissors(computer, playerInput)