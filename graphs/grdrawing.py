from tkinter import *
from graphs.grfunctions import graphs
global graphs, e1

# Root window
gui = Tk()
gui.title('Drawing graphs')
gui.resizable(True, True)
gui.geometry("370x100")
gui.columnconfigure(0, weight=1)
gui.columnconfigure(1, weight=3)

# Making the widgets
Label(gui, text='Please enter your formula:').grid(column=0, row=0, sticky=W, padx=5, pady=5)
wrn = Label(gui, text="Example: 3*X**2+5*x+4 (using a y=ax^2+bx+c equation")
wrn.grid(column=0, columnspan=3, row=2, sticky=S, padx=5, pady=5)
wrn.configure(font=('TkDefaultFont', 8))
e1 = Entry(gui, width=24)
e1.grid(column=1, row=0, sticky=E, padx=5, pady=5)

Button(gui, text="Continue", command= lambda: graphs(e1.get())).grid(column=1, row=3, sticky=E, padx=5, pady=5)

gui.mainloop()
