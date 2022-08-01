from tkinter import *
from userinteract import inp

gui = Tk()
frame = Frame(gui)
frame.pack()

Button(gui, text="Calculator", relief=RAISED, command=lambda m="A": inp(m)).pack()
Button(gui, text='Pythagorean theorem', relief=RAISED, command=lambda m="B": inp(m)).pack()

gui.mainloop()
