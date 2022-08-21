from tkinter import *
from functions import outputs, clear_output
global entry, res, outputs, clear_output

# Creating the window
gui = Tk()
gui.title('Calculator')
gui.resizable(True, True)
gui.geometry("500x300")

# Creating the widgets
entry = Entry(gui, bd=5)
entry.pack()
res = Label(gui)
res.pack()
l1 = Label(gui, text="Calculator")
l1.pack()


# Function for calculating
def calc(e):
    sum1 = entry.get()
    answer = eval(sum1)
    res.configure(text="Result: " + str(answer))
    outputs("*calc*" + str(sum1) + " = " + str(answer))


# Function for opening memory
def mem():
    exec(open("../Memory/outputs.py").read())


# Binding enter to above function and packing memory button
entry.bind("<Return>", calc)
Button(gui, text="Memory", command=mem).pack(side=BOTTOM)
Button(gui, text="Clear Memory", command=clear_output).pack(side=BOTTOM)

# Opening the app
gui.mainloop()
