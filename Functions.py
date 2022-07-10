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
    # TODO Graphs = find X = 0
    # TODO graphs = find Y = 0


def add(p, q): return p + q


def subtract(p, q): return p - q


def multiply(p, q): return p * q


def divide(p, q): return p / q


def pythagoras(p, q): return math.sqrt(p ** 2 + q ** 2)
