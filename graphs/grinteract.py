from tkinter import messagebox


def grint(m):
    if m == "A":        # finding Y
        exec(open("graphs/grfindy.py").read())
    elif m == "B":      # finding X
        messagebox.showinfo("Error", "Still in development, thus disabled")
    elif m == "C":      # not anything yet?
        messagebox.showinfo("Error", "Still in development, thus disabled")