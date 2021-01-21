# Notebook Program
# 21/01/2021

notes = ["","","","","","","","","",""]

while True:
    for x in range (len(notes)):
        print(x,":",notes[x])
    num = int(input("Please enter a note to change: "))

    if (num >= 0 and num < 10):
        new_note = input("Please enter the new note: ")
        notes[num] = new_note
    else:
        print("Error: please specify a number between 0 and 9")