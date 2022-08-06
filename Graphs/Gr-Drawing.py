from tkinter import *
global e1

# Root window
gui = Tk()
gui.title('Drawing graphs')
gui.resizable(True, True)
gui.geometry("500x300")

# Making the widgets
Label(gui, text='Please enter your formula').grid(row=0, column=0)
Label(gui, text="Please use **2 instead of ²/, Also use B*x instead of Bx, don't put y= in front of it").grid(sticky="")
e1 = Entry(gui)
e1.grid(row=0, column=1)


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


Button(gui, text="Continue", command=graphs).grid(sticky="")

gui.mainloop()


# TODO MAKE THIS GUI PRETTY
