from tkinter import *
global e1, e2

# Making a new window
gui = Tk()
gui.title('Finding y in formula')
gui.resizable(True, True)
gui.geometry("560x200")
gui.columnconfigure(0, weight=1)
gui.columnconfigure(1, weight=3)

# Widgets
l1 = Label(gui, text='Please enter your formula:')
l2 = Label(gui, text='Please enter the X-value you want to find the Y-value of:')
wrn = Label(gui, text="Example: 3*X**2+5*x+4 (using a y=ax^2+bx+c equation")
e1 = Entry(gui, width=24)
e2 = Entry(gui, width=24)

# Widgets.grid
l1.grid(column=0, row=0, sticky=W, padx=5, pady=5)
l2.grid(column=0, row=1, sticky=W, padx=5, pady=5)
wrn.grid(column=0, columnspan=3, row=2, sticky=S, padx=5, pady=5)
wrn.configure(font=('TkDefaultFont', 8))
e1.grid(column=1, row=0, sticky=E, padx=5, pady=5)
e2.grid(column=1, row=1, sticky=E, padx=5, pady=5)


def findx():
    # TODO REDO THIS
    raw_expr = e1.get()
    raw_x = e2.get()


Button(gui, text="Continue", command=findx).grid(column=1, row=3, sticky=E, padx=5, pady=5)

gui.mainloop()
