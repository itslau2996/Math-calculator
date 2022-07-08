import math


def add(p, q): return p + q


def subtract(p, q): return p - q


def multiply(p, q): return p * q


def divide(p, q): return p / q


def pythagoras(p, q): return math.sqrt(p ** 2 + q ** 2)


# Now we will take inputs from the user
print("Please select the operation.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")
print("e. Pythagoras")

choice = input("Please enter choice (a/ b/ c/ d/ eyT): ")

num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))

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
