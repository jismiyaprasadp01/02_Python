"""
Find the Difference Between the Largest and Smallest of Three Numbers (Using Only Expressions)
Write an expression to find the difference between the largest and the smallest of three numbers.
Sample Input: a = 8, b = 27, c = 14
"""
a, b, c = 8, 27, 14
largest = a if a >= b and a >= c else (b if b >= c else c)
smallest = a if a <= b and a <= c else (b if b <= c else c)
difference = largest - smallest
print("Difference:", difference)
