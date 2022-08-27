from tkinter import messagebox


def grint(m):
    if m == "A":        # finding Y
        exec(open("graphs/grfindy.py").read())
    elif m == "B":      # finding X
        exec(open("graphs/grfindx.py").read())

    elif m == "C":
        pass
        # TODO make a Find point in graph function

