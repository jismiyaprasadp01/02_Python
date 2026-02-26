"""
Ask for two numbers and compute their Greatest Common Divisor (GCD) using repeated subtraction or division with loops
"""
a, b = map(int, input("Enter the numbers a b: ").split())

a = abs(a)
b = abs(b)

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print("GCD =", a)
