import math
import tkinter.messagebox as tkmb


def pythagoras(p, q): return math.sqrt(p ** 2 + q ** 2)


def outputs(txt):
    with open("Memory/output.txt", "a") as file:
        file.write(txt + "\n")
        file.close()


def clear_output():
    with open("Memory/output.txt", "w"):
        tkmb.showinfo("Clear Memory", "Memory Cleared!")
