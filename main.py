import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from Functions import add, subtract, multiply, divide, pythagoras, strike
from easygui import *
i = 1
while i == 1:
    msg = 'Please enter choice: '
    title = 'Math-calc Window'
    choices = ['a. add', 'b. subtract', 'c. multiply', 'd. divide', 'e. pythagoras', 'f. Draw graphs', 'g. Find Y in Graphs', 'h. Find X in Graphs']

    ChoiceBoxOutput = choicebox(msg, title, choices)

    if ChoiceBoxOutput is None:
        msgbox(msg='An error occurred, Closing app..', title='Error')
        i = i + 1

    else:
        choice = ChoiceBoxOutput[0]
        sums = [choice != 'f',
                choice != 'g',
                choice != 'h']
        if all(sums):
            snum_1 = enterbox(msg='Please enter your first number:', title='Step1/2', strip=True)
            snum_2 = enterbox(msg='Please enter your second number:', title='Step2/2', strip=True)
            num_1 = float(snum_1)
            num_2 = float(snum_2)
            prnum1 = str(snum_1)
            prnum2 = str(snum_2)
            # prnum is used for the message, num is used for action, snum is input
            Title = 'Finished'
            ok = 'close'
            options = ['Close', 'Continue']

            if choice == 'a':
                msg = prnum1, " + ", prnum2, " = ", add(num_1, num_2)
                if boolbox(msg=msg, title=title, choices=options, cancel_choice='Close'):
                    i = i + 1
                    print('close?')
                else:
                    pass
            elif choice == 'b':
                msg = prnum1, " - ", prnum2, " = ", subtract(num_1, num_2)
                msgbox(msg=msg, title=title, ok_button=ok)
                i = i + 1
            elif choice == 'c':
                msg = prnum1, " * ", prnum2, " = ", multiply(num_1, num_2)
                msgbox(msg=msg, title=title, ok_button=ok)
                i = i + 1
            elif choice == 'd':
                msg = prnum1, " / ", prnum2, " = ", divide(num_1, num_2)
                msgbox(msg=msg, title=title, ok_button=ok)
                i = i + 1
            elif choice == 'e':
                msg = 'SQRT(', prnum1, '²+', prnum2, '²)= ', pythagoras(num_1, num_2)
                msgbox(msg=msg, title=title, ok_button=ok)
                i = i + 1
            else:
                print("You shouldn't be here \n  Neither should you")
                i = i + 1

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
                msgbox(msg="This isn't a equation", title='Error', ok_button='OK')

        elif choice == 'g':
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
                msgbox(msg="This isn't a equation", title='Error', ok_button='OK')

        elif choice == 'h':
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
                msgbox(msg="This isn't a equation", title='Error', ok_button='OK')

        else:
            msgbox(msg="You chose a non-existent option", title='Error', ok_button='OK')  # this cant be seen if I did everything right
