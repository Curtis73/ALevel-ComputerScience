import time
lives = 5
attempts = 0
guessed_letters = []

word = input("Player 1: Please input your word\n")

time.sleep(1)
print("\n")

while lives > 0:
  print("You have " + str(lives) + " lives remaining.")
  guess = input("Player 2: Please guess a letter\n")
  guessed_letters.append(guess)
  output_word = ""
  for char in word:
    if char in guessed_letters:
      output_word += char
    else:
      output_word += "*"
  if (guess not in list(word)):
    lives -= 1
  print (output_word)

  if (output_word == word):
    print("\n")
    print("Player two wins!")
    print ("The word was: " + word)
    break

if (lives == 0):
  print("\n")
  print("Player one wins!")
  print("The word was: " + word)