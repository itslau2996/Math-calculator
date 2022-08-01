import math


def pythagoras(p, q): return math.sqrt(p ** 2 + q ** 2)


def outputs(txt):
    with open("output.txt", "a") as file:
        file.write(txt + "\n")
        file.close()



