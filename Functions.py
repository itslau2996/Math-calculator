import math


def choices():
    print("Please select the operation.")
    print("a. Add")
    print("b. Subtract")
    print("c. Multiply")
    print("d. Divide")
    print("e. Pythagoras")
    print("f. Graphs, drawing")
    print("g. Graphs, finding Y")
    print("h. Graphs, finding X")



def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result


def add(p, q): return p + q


def subtract(p, q): return p - q


def multiply(p, q): return p * q


def divide(p, q): return p / q


def pythagoras(p, q): return math.sqrt(p ** 2 + q ** 2)
