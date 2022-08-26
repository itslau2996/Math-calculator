from tkinter import *
from graphs.grinteract import grint
global grint
gui = Tk()
frame = Frame(gui)
frame.pack()
gui.title("graphs")


Button(gui, text="Graphs finding Y", width=15, relief=RAISED, command=lambda: grint('A')).pack()
Button(gui, text="Graphs finding X", width=15, relief=RAISED, command=lambda: grint('B')).pack()
# template
# Button(gui, text="%", width=15, relief=RAISED, command=lambda m="%": grint(m)).pack()

gui.mainloop()
