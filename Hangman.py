# By Curtis Hambleton

import time
lives = 5
attempts = 0
guessed_letters = []

word = input("Player 1: Please input your word\n") # Ask player one for their word

time.sleep(1)
print("\n")

while lives > 0: # While player has more than 0 lives
  print("You have " + str(lives) + " lives remaining.")
  guess = input("Player 2: Please guess a letter\n")
  guessed_letters.append(guess) # Add the player's guess to guessed_letters
  output_word = ""
  for char in word: # For each character in the word
    if char in guessed_letters: # If the character has been guessed
      output_word += char # Print the character
    else: # Otherwise
      output_word += "*" # Print an asterisk
  if (guess not in list(word)): # If the guessed character is not in the word
    lives -= 1 # Remove a life
  print (output_word) # Print the concatonated word

  if (output_word == word): # If the word output is equal to the initially input word, player two wins
    print("\n")
    print("Player two wins!")
    print ("The word was: " + word)
    break

if (lives == 0): # If player two runs out of lives, player one wins
  print("\n")
  print("Player one wins!")
  print("The word was: " + word)