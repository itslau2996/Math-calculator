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
l2 = Label(gui, text='Please enter the Y-value you want to find the X-value of:')
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
    # Collecting Data
    from sympy import symbols, parse_expr, Eq, solve, lambdify
    import numpy as np
    import matplotlib.pyplot as plt
    x, y = symbols('x, y')
    # Getting the data from the entries
    raw_y = e2.get()
    raw_expr = e1.get()
    # Checking for unwanted symbols
    expr = raw_expr.replace(" ", "")
    inp_y = float(raw_y.replace(" ", ""))

    # SOLVING
    # Making it usable for SymPy
    sp_expr = parse_expr(expr)
    eq1 = Eq(sp_expr, inp_y)
    # Solving start
    x_ans = solve(eq1, x)
    xmark = x_ans
    ymark = inp_y
    if len(x_ans) == 2:
        ymark = ([inp_y, inp_y])
    else:
        pass

    # MAKING PLOT
    f = lambdify(x, sp_expr, 'numpy')
    xas = np.arange(-10, 11, 1)
    yas = f(xas)
    print('xmark:', xmark)
    print('ymark:', ymark)
    print('yas:', yas)
    print('xas:', xas)

    plt.plot(xmark, ymark, 'o')
    plt.plot(xas, yas)
    plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

    plt.show()
    print('Function finished!')


Button(gui, text="Continue", command=findx).grid(column=1, row=3, sticky=E, padx=5, pady=5)

gui.mainloop()
