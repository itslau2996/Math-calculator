from tkinter import *
from Functions import outputs
global entry, res, outputs
gui = Tk()
text = Text(gui)

entry = Entry(gui, bd=5)
entry.pack()
res = Label(gui)
res.pack()
l1 = Label(gui, text="Calculator")
l1.pack()


def calc(e):
    sum1 = entry.get()
    answer = eval(sum1)
    print(answer)
    res.configure(text="Result: " + str(answer))
    outputs(str(sum1) + " = " + str(answer))


entry.bind("<Return>", calc)
# Button(gui, text="Calculate", relief=RAISED, command=calc).pack(side=BOTTOM)

gui.mainloop()
