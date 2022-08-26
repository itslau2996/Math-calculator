# Global functions for graphs will be stored here!

def graphs(inp_expr):
    import sympy as sp
    from sympy.plotting import plot
    import matplotlib
    matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt

    x, y, z = sp.symbols('x, y, z')
    sp.init_printing(use_unicode=True)
    expr = sp.sympify(inp_expr)
    print(expr)
    p1 = plot(expr, show=False)
    p1.show()

