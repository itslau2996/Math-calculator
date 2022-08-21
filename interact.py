def inp(m):
    if m == "A":
        exec(open("Calcs/calculator.py").read())
    elif m == "B":
        exec(open("Calcs/pyth.py").read())
    elif m == "C":
        exec(open("graphs/grmain.py").read())
    elif m == "D":
        exec(open("graphs/grdrawing.py").read())
    