import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("The input must be an integer.")
    sys.exit(1)


try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
    sys.exit(1)


print(f"{x} / {y} = {result}")
