"""
Take a number as input and calculate its factorial using loops (no recursion
"""
n = int(input("Enter a number: "))

fact = 1

if n < 0:
    print("Factorial does not exist for negative numbers")
else:
    for i in range(1, n + 1):
        fact *= i
    print("Factorial =", fact)
