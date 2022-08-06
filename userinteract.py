from tkinter import messagebox


def inp(m):
    if m == "A":
        exec(open("Calculator.py").read())
    elif m == "B":
        exec(open("pyth.py").read())
    elif m == "C":
        messagebox.showinfo("Warning", "This module is still in development, so its disabled.")
    elif m == "D":
        exec(open("./Graphs/Gr-Drawing.py").read())
    