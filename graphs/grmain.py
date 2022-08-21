from tkinter import *
from graphs.grinteract import grint
global grint
gui = Tk()
frame = Frame(gui)
frame.pack()
gui.title("graphs")


Button(gui, text="Calculator", width=15, relief=RAISED, command=lambda m="A": grint(m)).pack()
Button(gui, text='Pythagorean theorem', width=15, relief=RAISED, command=lambda m="B": grint(m)).pack()
Button(gui, text="graphs", width=15, relief=RAISED, command=lambda m="C": grint(m)).pack()
Button(gui, text="Drawing graphs", width=15, relief=RAISED, command=lambda m="D": grint(m)).pack()

gui.mainloop()
