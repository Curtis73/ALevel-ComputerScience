# Tkinter Calculator Program
# 03/02/2021

from tkinter import *

window = Tk()

window.title("Curtis' Calculator")

window.geometry('250x100')

lbl1 = Label(window, text="Number 1")
lbl1.grid(column=0, row=0)

lbl2 = Label(window, text="Number 2")
lbl2.grid(column=0, row=1)

num1 = Entry(window,width=10)
num1.grid(column=1, row=0)

num2 = Entry(window,width=10)
num2.grid(column=1, row=1)

def clicked():
    answer = Label(window, text="Answer: " + str(int(num1.get()) + int(num2.get())))
    answer.grid(column=0, row=3)

btn = Button(window, text="Add Numbers", command=clicked)
btn.grid(column=2, row=0)

window.mainloop()