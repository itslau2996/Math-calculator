from tkinter import *
from userinteract import inp

gui = Tk()
frame = Frame(gui)
frame.pack()
gui.title("math functions")


Button(gui, text="Calculator", width=15, relief=RAISED, command=lambda m="A": inp(m)).pack()
Button(gui, text='Pythagorean theorem', width=15, relief=RAISED, command=lambda m="B": inp(m)).pack()
Button(gui, text="Graphs", width=15, relief=RAISED, command=lambda m="C": inp(m)).pack()
Button(gui, text="Drawing Graphs", width=15, relief=RAISED, command=lambda m="D": inp(m)).pack()

gui.mainloop()
