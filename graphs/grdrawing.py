from tkinter import *
global e1

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


# Using SymPy to solve it (at least that's what I hope to do)
def graphs():
    import sympy as sp
    from sympy.plotting import plot
    import matplotlib
    matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt

    x, y, z = sp.symbols('x, y, z')
    sp.init_printing(use_unicode=True)
    expr = sp.sympify(e1.get())
    print(expr)
    p1 = plot(expr, show=False)
    p1.show()


Button(gui, text="Continue", command=graphs).grid(column=1, row=3, sticky=E, padx=5, pady=5)

gui.mainloop()
