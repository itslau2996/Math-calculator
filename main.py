import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from Functions import add, subtract, multiply, divide, pythagoras, choices, strike

choices()

choice = input("Please enter choice: ")
sums = [choice != 'f',
        choice != 'g',
        choice != 'h']

if all(sums):
    num_1 = float(input("Please enter the first number: "))
    num_2 = float(input("Please enter the second number: "))

    if choice == 'a':
        print(num_1, " + ", num_2, " = ", add(num_1, num_2))
    elif choice == 'b':
        print(num_1, " - ", num_2, " = ", subtract(num_1, num_2))
    elif choice == 'c':
        print(num_1, " * ", num_2, " = ", multiply(num_1, num_2))
    elif choice == 'd':
        print(num_1, " / ", num_2, " = ", divide(num_1, num_2))
    elif choice == 'e':
        print('SQRT(', num_1, '²+', num_2, '²)= ', pythagoras(num_1, num_2))
    else:
        print('This is an invalid input')
elif choice == 'f':
    x = np.array([-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6])
    print('equation types')
    print('1) y=mx+b')
    print('2) y=ax^2 + c')
    print('3) y=ax^2 + bx + c')

    eq = int(input('equation type number: '))
    # X but squared for formulas 1 and 3
    num_x = x ** 2
    if eq == 1:
        m = float(input('m: '))
        b = float(input('b: '))
        print(m, b)
        y = m * x + b
        print(y)
        plt.plot(x, y)
        plt.grid(color='black', linewidth=1)
        plt.show()
    if eq == 2:
        a = float(input('a: '))
        c = float(input('c: '))
        print(a, c)
        y = a * num_x + c
        print(y)
        plt.plot(x, y)
        plt.grid(color='black', linewidth=1)
        plt.show()
    if eq == 3:
        a = float(input('a: '))
        b = float(input('b: '))
        c = float(input('c: '))
        print(a, b, c)
        y = a * num_x + b * x + c
        print(y)
        plt.plot(x, y)
        plt.grid(color='black', linewidth=1)
        plt.show()
    else:
        print('\n')

elif choice == 'g':
    print('equation types')
    print('1) y=mx+b')
    strike('2) y=ax^2 + c')
    strike('3) y=ax^2 + bx + c')

    eq = int(input('equation type number: '))

    xas = np.array([-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6])
    num_xas = xas ** 2
    if eq == 1:
        m = float(input('m: '))
        b = float(input('b: '))
        x = float(input('x: '))
        y = m * x + b
        yas = m * xas + b
        print('y = ', m, '*', x, '+', b)
        print('The Y is: ', y)
        plt.plot(xas, yas)
        plt.plot(x, y, 'o')
        plt.grid(color='black', linewidth=1)
        plt.show()

    if eq == 2:
        a = float(input('a: '))
        c = float(input('c: '))
        x = float(input('x: '))
        num_x = x ** 2
        y = a * num_x + c
        yas = a * num_xas + c
        print('y = ', a, '*', x, '^2', '+', c)
        print('The Y is: ', y)
        plt.plot(xas, yas)
        plt.plot(x, y, 'o')
        plt.grid(color='black', linewidth=1)
        plt.show()

    if eq == 3:
        a = float(input('a: '))
        b = float(input('b: '))
        c = float(input('c: '))
        x = float(input('x: '))
        num_x = x ** 2
        y = a * num_x + b * x + c
        yas = a * num_xas + b * xas + c
        print('y = ', a, '*', x, '^2', '+', b, '*', x, '+', c)
        print('The Y is: ', y)
        plt.plot(xas, yas)
        plt.plot(x, y, 'o')
        plt.grid(color='black', linewidth=1)
        plt.show()
    else:
        print("\n This isn't an valid equation ")

elif choice == 'h':
    print('equation types')
    print('1) y=mx+b')
    print('2) y=ax^2 + c')
    print('3) y=ax^2 + bx + c')

    eq = int(input('equation type number: '))

    xas = np.array([-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6])
    num_xas = xas ** 2
    if eq == 1:
        m = float(input('m: '))
        b = float(input('b: '))
        y = float(input('y: '))
        x = symbols('x')
        equ = Eq(m * x + b, y)
        xans = solve(equ, x)
        print(xans)
        xans.replace(',', '.')
        yas = m * xas + b
        plt.plot(xas, yas)
        plt.plot(xans, y, 'o')
        plt.grid(color='black', linewidth=1)
        plt.show()

    if eq == 2:
        print('Sorry, this function is disabled for the time being')

    if eq == 3:
        print('Sorry, this function is disabled for the time being')
    else:
        print("\n")
