import time
lives = 5
attempts = 0
guessed_letters = []

word = input("Player 1: Please input your word\n")

time.sleep(1)

while lives > 0:
  guess = input("Player 2: Please type a letter\n")
  guessed_letters.append(guess)
  for char in word:
    if guess in guessed_letters:
      print (char)
    else:
      print ("*")

