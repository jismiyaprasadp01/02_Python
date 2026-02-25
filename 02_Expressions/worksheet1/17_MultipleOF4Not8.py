"""
Check If a Number is a Multiple of 4 but Not of 8
Write an expression that is True only if a number is divisible by 4 but not by 8.
Sample Input: n = 12
"""
num = int(input("Enter the num: "))

print("True" if (num % 4 == 0 and num % 8 != 0) else "False")
