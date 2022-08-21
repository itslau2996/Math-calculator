from functions import outputs, clear_output, pythagoras
from math import *
from tkinter import *
import re

global e1, e2, res, pythagoras, outputs, clear_output

# Window creating
gui = Tk()
gui.title('Pythagorean theorem')
gui.resizable(True, True)
gui.geometry("500x300")

# Widget Creation
e1 = Entry(gui, bd=5)
e1.pack()
e2 = Entry(gui, bd=5)
e2.pack()
l1 = Label(gui, text="Pythagorean theorem")
l1.pack()
res = Label(gui)
res.pack()


def calc(e):
    p = e1.get()
    q = e2.get()
    if p.islower() or p.isupper() or q.islower() or q.isupper():
        res.configure(text="Please make sure to only enter numbers!")
        pass
    else:
        ans = pythagoras(int(p), int(q))
        res.configure(text="Result: " + str(ans))
        outputs("*pyth* sqrt(" + str(p) + "**2 + " + str(q) + "**2) = " + str(ans))


def mem():
    exec(open("../Memory/outputs.py").read())


e2.bind("<Return>", calc)
Button(gui, text="Memory", command=mem).pack(side=BOTTOM)
Button(gui, text="Clear Memory", command=clear_output).pack(side=BOTTOM)
